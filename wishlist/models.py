from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.user.first_name


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.product.product_name
    

    