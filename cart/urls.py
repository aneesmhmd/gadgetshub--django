from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name="cart"),
    path('add-cart/<int:product_id>/', views.add_cart, name="add_cart"),
    path('remove-cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name="remove_cart"),
    path('remove-cart-item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name="remove_cart_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('apply-coupon/', views.cart, name="apply_coupon"),
    path('remove-coupon/', views.remove_coupon, name="remove_coupon"),
]