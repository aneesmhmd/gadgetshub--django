from django.shortcuts import render, redirect
from store.models import Product, ProductImage
from category.models import Category, Brand
from django.contrib import messages
from store.models import Variation, Ram, Storage
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def superadmin_check(user):
    if user.is_authenticated:
        return user.is_superadmin


@user_passes_test(superadmin_check)
def products_list(request):
    products = Product.objects.all().order_by('id')
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'brands': brands
    }
    return render(request, 'admin_home/products.html', context)


@user_passes_test(superadmin_check)
def add_product(request):

    if request.method == 'POST':
        product_name = request.POST['name']
        brand_name = request.POST['brand']
        cat_name = request.POST['category']
        images = request.FILES.getlist('images')
        description = request.POST['description']
        stock = int(request.POST['stock'])
        price = int(request.POST['price'])

        try:
            category = Category.objects.get(category_name=cat_name)
            brand = Brand.objects.get(brand_name=brand_name)
        except:
            pass

        if Product.objects.filter(product_name=product_name).exists():
            messages.warning(request, 'Product already exists')
            return redirect(products_list)

        elif stock < 0 or stock > 50:
            messages.warning(request, 'Enter valid stock')
            return redirect(products_list)

        elif price <= 0:
            messages.warning(request, 'Enter valid price')
            return redirect(products_list)

        product = Product.objects.create(product_name=product_name, category=category,
                                         brand=brand, price=price, stock=stock, description=description)

        for image in images:
            ProductImage.objects.create(product=product, image=image)
            
        messages.success(request, 'Product addedd successfully')
        return redirect(products_list)


@user_passes_test(superadmin_check)
def edit_product(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == 'POST':
            product_name = request.POST['name']
            brand_name = request.POST['brand']
            cat_name = request.POST['category']
            description = request.POST['description']
            stock = int(request.POST['stock'])
            price = int(request.POST['price'])

            try:
                category = Category.objects.get(category_name=cat_name)
                brand = Brand.objects.get(brand_name=brand_name)
            except:
                pass

            if stock < 0 or stock > 50:
                messages.warning(request, 'Enter valid stock')
                return redirect(products_list)

            elif price <= 0:
                messages.warning(request, 'Enter valid price')
                return redirect(products_list)
            
            elif Product.objects.filter(product_name=product_name).exclude(id=id).exists():
                messages.warning(request, 'Product already exists')
                return redirect(products_list)
            
            product.product_name = product_name
            product.brand = brand
            product.category = category
            product.description = description
            product.stock = stock
            product.price = price
            product.save()
            messages.success(
                request, f'{product_name} updated successfully')
            return redirect(products_list)

    except Product.DoesNotExist:
        messages.error(request, 'Oops!Something gone wrong')


@user_passes_test(superadmin_check)
def remove_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect(products_list)

    except Product.DoesNotExist:
        messages.error(request, 'Oops!Something gone wrong')
        return redirect(products_list)

# ---------------------------------------------



# ---------------- Variations -----------------


@user_passes_test(superadmin_check)
def variations(request):
    context = {
        'variations': Variation.objects.all().order_by('id'),
        'products': Product.objects.all().order_by('id'),
        'rams': Ram.objects.all().order_by('id'),
        'storages': Storage.objects.all().order_by('id')
    }
    return render(request, 'admin_home/variations.html', context)


@user_passes_test(superadmin_check)
def add_variation(request):
    if request.method == 'POST':
        pro_name = request.POST['product']
        pro_ram = request.POST['ram']
        pro_storage = request.POST['storage']
        price = int(request.POST['price'])

        try:
            product = Product.objects.get(product_name=pro_name)
            ram = Ram.objects.get(ram=pro_ram)
            storage = Storage.objects.get(storage=pro_storage)
        except:
            messages.warning(request, 'Oops!Something gone wrong.')
            return redirect(variations)

        if price < 0:
            messages.error(request, 'Enter a valid price')
            return redirect(variations)

        elif Variation.objects.filter(product=product, ram=ram, storage=storage).exists():
            messages.warning(
                request, f'Variation for {product} already exists')
            return redirect(variations)

        Variation.objects.create(
            product=product, ram=ram, storage=storage, price=price)
        messages.success(request, f'Variation addedd for the {product} succesfully')
        return redirect(variations)


@user_passes_test(superadmin_check)
def edit_variation(request, id):
    try:
        variation = Variation.objects.get(id=id)
    except Variation.DoesNotExist:
        messages.warning(request, 'Variation doesnot exist')
        return redirect(variations)

    if request.method == 'POST':
        pro_name = request.POST['product']
        pro_ram = request.POST['ram']
        pro_storage = request.POST['storage']
        price = int(request.POST['price'])

        try:
            product = Product.objects.get(product_name=pro_name)
            ram = Ram.objects.get(ram=pro_ram)
            storage = Storage.objects.get(storage=pro_storage)
        except:
            messages.warning(request, 'Oops!Something gone wrong.')
            return redirect(variations)

        if price < 0:
            messages.error(request, 'Enter a valid price')
            return redirect(variations)

        elif Variation.objects.filter(product=product, ram=ram, storage=storage).exclude(id=id).exists():
            messages.warning(request, f'Variation for {product} already exists')
            return redirect(variations)

        else:
            variation.product = product
            variation.ram = ram
            variation.storage = storage
            variation.price = price
            variation.save()
            messages.success(
                request, f'Variation updated for the {product} succesfully')
            return redirect(variations)


@user_passes_test(superadmin_check)
def remove_variation(request, id):
    try:
        variation = Variation.objects.get(id=id)
        variation.delete()
        messages.success(request, 'Variation deleted successfully')
        return redirect(variations)
    except Variation.DoesNotExist:
        messages.warning(request, 'Oops!Something went wrong.')
        return redirect(variations)

# -----------------------------------------------------


# --------------------- RAM and storage --------------------

@user_passes_test(superadmin_check)
def add_ram(request):
    if request.method == 'POST':
        ram = request.POST['ram']
        
        if Ram.objects.filter(ram=ram).exists():
            messages.warning(request, 'RAM already exists')
            return redirect(variations)
        
        Ram.objects.create(ram=ram)
        messages.success(request, 'RAM addedd succesfully')
        return redirect(variations)


@user_passes_test(superadmin_check)
def edit_ram(request,id):
    if request.method == 'POST':

        try:
            ram = Ram.objects.get(id=id)
        except Ram.DoesNotExist:

            messages.warning(request, 'Oops!Something gone wrong')
            return redirect(variations)
        
        edited_ram =request.POST['ram']
        ram.ram = edited_ram
        ram.save()
        messages.success(request, 'RAM updated succesfully')
        return redirect(variations)
    

@user_passes_test(superadmin_check)
def remove_ram(request,id):
    try:
        ram = Ram.objects.get(id=id)
        ram.delete()
        messages.success(request, 'RAM deleted succesfully')
        return redirect(variations)
    except Ram.DoesNotExist:
        messages.error(request, 'Oops!Something gone wrong')
        return redirect(variations)
    
# -----------------------------------------

# --------------- STORAGE ------------------


@user_passes_test(superadmin_check)
def add_storage(request):
    if request.method == 'POST':
        storage = request.POST['storage']

        if Storage.objects.filter(storage=storage).exists():
            messages.warning(request, 'Storage already exists')
            return redirect(variations)
        
        Storage.objects.create(storage=storage)
        messages.success(request, 'Storage addedd successfully')
        return redirect(variations)


@user_passes_test(superadmin_check)
def edit_storage(request,id):
    if request.method == 'POST':
        edited_storage = request.POST['storage']

        try:
            storage = Storage.objects.get(id=id)
        except Storage.DoesNotExist:
            messages.warning(request, 'Oops!Something gone wrong')
            return redirect(variations)
        
        if Storage.objects.filter(storage=edited_storage).exclude(id=id).exists():
            messages.warning(request, 'Storage already exists')
            return redirect(variations)
        
        storage.storage = edited_storage
        storage.save()
        messages.success(request, 'Storage added succesfully')
        return redirect(variations)


@user_passes_test(superadmin_check)
def remove_storage(request,id):
    try:
        storage = Storage.objects.get(id=id)
        storage.delete()
        messages.success(request, 'Storage deleted succesfully')
        return redirect(variations)
    except Storage.DoesNotExist:
         messages.warning(request, 'Oops!Something gone wrong')
         return redirect(variations)