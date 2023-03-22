from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    category_image = models.ImageField(upload_to='categories')


    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)


    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name
    

# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True)
    brand_image = models.ImageField(upload_to='brands', blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)


    def get_url(self):
        return reverse('products_by_brand', args=[self.slug])


    def __str__(self):
        return self.brand_name