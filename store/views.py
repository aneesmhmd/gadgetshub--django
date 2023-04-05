from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Product, Variation
from category.models import *
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from wishlist.models import WishlistItem, Wishlist
from orders.models import ReviewRating
from orders.models import OrderItem

# Create your views here.



# All/Brandwise/Categorywise products
def all_products(request, category_slug=None, brand_slug=None):

    page_obj = None
    try:
        if category_slug != None:
            categories = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(
                category=categories, is_available=True).order_by('id')

        elif brand_slug != None:
            brands = Brand.objects.get(slug=brand_slug)
            products = Product.objects.filter(
                brand=brands, is_available=True).order_by('id')
            
        elif request.GET.get('min'):
            min = request.GET.get('min')
            max = request.GET.get('max')
            products = Product.objects.filter(price__range=(min, max))

        elif request.GET.get('sortby'):
            sort = request.GET.get('sortby')
            if sort == 'newest':
                products = Product.objects.all().order_by('-created_date')
            elif sort == 'low-to-high':
                products = Product.objects.all().order_by('price')
            elif sort == 'high-to-low':
                products = Product.objects.all().order_by('-price')

        else:
            products = Product.objects.all().filter(is_available=True).order_by('id')

        paginator = Paginator(products, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Exception as e:
        pass  # custom 404 page
    
    context = {'products': page_obj}
    return render(request, 'store/all_products.html', context)




# Single product view
def product_detail(request, category_slug, product_slug):
    in_wishlist = False
    single_product = None
    count = 0
    ordered = None

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        variants = Variation.objects.filter(product=single_product)
        reviews = ReviewRating.objects.filter(product=single_product)
        count = reviews.count()

        if request.user.is_authenticated:
            ordered = OrderItem.objects.filter(product=single_product, user=request.user).exists()
        
        context = {'single_product': single_product,
                   'variants': variants,
                   'reviews':reviews, 
                   'ordered' : ordered,
                   'count' : count,
                   }

        if reviews:
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            context['avg_rating'] = avg_rating
        
        if request.GET.get('variant'):
            variant = request.GET.get('variant')
            ram, storage = variant.split(",")
            variant_price = single_product.get_product_price(variant)

            context.update({
                'selected_variant': variant,
                'variant_price': variant_price,
                'ram': ram,
                'storage': storage,
            })

        if request.user.is_authenticated:
            try:
                wishlist = Wishlist.objects.get(user=request.user)
                in_wishlist = WishlistItem.objects.filter(wishlist=wishlist, product__product_name=single_product)
                context['in_wishlist'] = in_wishlist
            except:
                pass

        return render(request, 'store/product_detail.html', context)

    except:
        return render(request, 'store/product_detail.html', {'single_product' : single_product})




# Search
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count = products.count()

    context = {
        'products': products,
        'products_count': products_count,
    }

    return render(request, 'store/all_products.html', context)
