from wishlist.models import Wishlist, WishlistItem
from cart.models import Cart,CartItem

def counter(request):
    pass
    wishlist_count = 0
    cart_count = 0

    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)

        cart = Cart.objects.get(user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)

        for item in wishlist_items:
            wishlist_count += 1
        
        for item in cart_items:
            cart_count += 1
    except:
        # wishlist_count = 0
        pass
    
    return dict(wishlist_count=wishlist_count,cart_count=cart_count)