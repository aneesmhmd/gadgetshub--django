from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Address
from django.contrib import messages
import razorpay
from django.conf import settings
# Create your views here.


@login_required
def cart(request):
    cart=None
    cart_items=None
    try:
        cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)
    except Exception as e:
        print(e)

    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        coupon_obj = Coupon.objects.filter(coupon_code__icontains=coupon)
        print(coupon_obj)
        if not coupon_obj.exists():
            messages.error(request, 'Invalid Coupon')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if cart.coupon:
            messages.warning(request, 'Coupon Already applied')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if cart.get_cart_total() < coupon_obj[0].min_amount:
            messages.warning(
                request, f'Total amount should be greater than ₹{coupon_obj[0].min_amount} excluding tax')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if coupon_obj[0].is_expired:
            messages.warning(request, 'This coupon has expired')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        cart.coupon = coupon_obj[0]
        cart.save()
        messages.success(request, 'Coupon Applied')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'cart_items': cart_items, 'cart': cart}
    return render(request, 'store/cart.html', context)




@login_required
def add_cart(request, product_id):
    product_variant = None
    try:
        variation = request.GET.get('variant')
        product = Product.objects.get(id=product_id)
        user = request.user

        if variation:
            product_variant = Variation.objects.get(
                product=product, variation=variation)

        cart, _ = Cart.objects.get_or_create(user=user, is_active=True)
        is_cart_item = CartItem.objects.filter(
            cart=cart, product=product, variant=product_variant).exists()

        if is_cart_item:
            cart_item = CartItem.objects.get(
                cart=cart, product=product, variant=product_variant)
            cart_item.quantity += 1
            cart_item.save()

        else:
            cart_item = CartItem.objects.create(
                product=product, quantity=1, cart=cart, variant=product_variant)
            cart_item.save()

    except:
        pass
    return redirect('cart')




@login_required
def remove_cart(request, product_id, cart_item_id):

    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user, is_active=True)
        cart_item = CartItem.objects.get(
            product=product, id=cart_item_id, cart=cart)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass

    return redirect('cart')



@login_required
def remove_cart_item(request, product_id, cart_item_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user, is_active=True)
    cart_item = CartItem.objects.filter(
        product=product, id=cart_item_id, cart=cart)
    cart_item.delete()
    return redirect('cart')



@login_required
def remove_coupon(request):
    try:
        cart = Cart.objects.get(user=request.user, is_active=True)
        cart.coupon = None
        cart.save()
        messages.success(request, 'Coupon removed successfully')
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required
def checkout(request):
    current_user = request.user
    addresses = Address.objects.filter(user=current_user).order_by('id')

    try:
        cart = Cart.objects.get(user=current_user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)
        client = razorpay.Client(auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.order.create({'amount' : int(cart.get_grand_total()) * 100, 'currency' : 'INR', 'payment_capture': 1})
    except:
        pass #Just Ignore 
        
    cart.razorpay_order_id=payment['id']
    cart.save()
    context = {'cart': cart,
               'cart_items': cart_items,
               'addresses': addresses,
               'payment' : payment
               }

    return render(request, 'store/checkout.html', context)
