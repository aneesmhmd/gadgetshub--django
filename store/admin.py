from django.contrib import admin
from .models import *

# Register your models here.

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'is_available']
    inlines = [ProductImageAdmin]


@admin.register(Variation)
class VariationsAdmin(admin.ModelAdmin):
    list_display = ['product' ,'ram', 'storage','variation', 'price']
    model = Variation



admin.site.register(ProductImage)
admin.site.register(Ram)
admin.site.register(Storage)
