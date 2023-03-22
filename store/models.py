from django.db import models
from category.models import *
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products_brand')
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    description = models.TextField(max_length=500, blank=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def get_product_price(self, variation):
        return self.price + Variation.objects.get(product=self.id ,variation=variation).price

    def __str__(self):
        return self.product_name


# Multiple images
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f'{self.product.product_name}'
    

#------------------ Variations -----------------------

# RAM model
class Ram(models.Model):
    ram = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.ram


# Storage model
class Storage(models.Model):
    storage = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.storage

    
# Varation model
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    ram = models.ForeignKey(Ram, on_delete=models.SET_NULL, null=True)
    variation = models.CharField(max_length=100, null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.variation = f"{self.ram},{self.storage}"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.variation
    
#----------------- Variations end----------------------

    