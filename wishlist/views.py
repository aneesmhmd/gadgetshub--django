from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def wishlist(request,wishlist_items=None):
    
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    except:
        pass

    context = { 'wishlist_items' : wishlist_items }


    return render(request,'store/wishlist.html',context)

@login_required
def add_wishlist(request,product_id):

    product = Product.objects.get(id=product_id)
    user = request.user
    wishlist, _ = Wishlist.objects.get_or_create(user=user)

    wishlist_item= WishlistItem.objects.create(wishlist=wishlist, product=product, quantity=1)
    wishlist_item.save()

    return redirect('wishlist')


def remove_wishlist(request,product_id):
    product = Product.objects.get(id=product_id)
    user = request.user

    wishlist = Wishlist.objects.get(user=user)
    wishlist_item = WishlistItem.objects.get(wishlist=wishlist, product=product)
    wishlist_item.delete()

    return redirect('wishlist')
