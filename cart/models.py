from django.db import models
from accounts.models import Account
from store.models import Product
from store.models import Variation

# Create your models here.
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=20)
    discount_price = models.PositiveIntegerField(default=799)
    min_amount = models.PositiveIntegerField(default=17999)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.coupon_code

# ---------------------------------------------


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cart_items')
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    # Payment details
    razorpay_order_id = models.CharField(max_length=100 ,null=True, blank=True,unique=True)

    def __str__(self) -> str:
        return self.user.email

    # Cart total
    def get_cart_total(self):
        cart_items = CartItem.objects.filter(cart=self.id)
        price = []
        for cart_item in cart_items:
            quantity = cart_item.quantity
            price.append(cart_item.product.price * quantity)
            if cart_item.variant:
                price.append(cart_item.variant.price * quantity)
            
        return sum(price)

    # Tax of cart_total
    def get_tax(self):
        return round(0.025 * self.get_cart_total(), 2)

    # tax + cart_total
    def get_grand_total(self):
        total = self.get_cart_total() + self.get_tax()

        if self.coupon:
            if self.coupon.min_amount < total:
                return total - self.coupon.discount_price
    
        return self.get_cart_total() + self.get_tax()

# ----------------------------------------------



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    variant = models.ForeignKey(Variation, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.product_name

    # Product price
    def get_product_price(self):
        product_price = [self.product.price]
        if self.variant:
            product_price.append(self.variant.price)

        return sum(product_price)

    # Cart item price
    def get_sub_total(self):
        price = [self.product.price]
        if self.variant:
            price.append(self.variant.price)
        sub_total = sum(price) * self.quantity
        return sub_total
