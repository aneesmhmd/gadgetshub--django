from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishlist, name="wishlist"),
    path('add-to-wishlist/<int:product_id>', views.add_wishlist, name="add_wishlist"),
    path('remove-wishlist-item/<int:product_id>', views.remove_wishlist, name="remove_wishlist"),
]