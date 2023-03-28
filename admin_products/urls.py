from django.urls import path,include
from . import views, views_1

urlpatterns = [
    path('', views.products_list,name="products_list"),
    path('add-products/', views.add_product,name="add_product"),
    path('remove-products/<int:id>/', views.remove_product,name="remove_product"),
    path('edit-products/<int:id>/', views.edit_product,name="edit_product"),

    # Variations
    path('variations/', views.variations, name='variations'),
    path('add-variation/', views.add_variation, name='add_variation'),
    path('edit-variation/<int:id>/', views.edit_variation, name='edit_variation'),
    path('remove-variation/<int:id>/', views.remove_variation, name='remove_variation'),

    # RAM
    path('add-ram/',views.add_ram,name="add_ram"),
    path('edit-ram/<int:id>/',views.edit_ram, name="edit_ram"),
    path('remove-ram/<int:id>/',views.remove_ram,name="remove_ram"),

    #Storage
    path('add-storage/', views.add_storage, name="add_storage"),
    path('edit-storage/<int:id>/', views.edit_storage, name="edit_storage"),
    path('remove-storage/<int:id>/', views.remove_storage, name="remove_storage"),

    #coupon
    path('coupon/', views_1.coupons, name="coupons"),
    path('add-coupon/', views_1.add_coupon, name="add_coupon"),
    path('edit-coupon/<int:id>/', views_1.edit_coupon, name="edit_coupon"),
    path('remove-coupon/<int:id>/', views_1.remove_coupon, name="remove_coupon"),
    path('coupon-status/<int:id>/', views_1.coupon_status, name="coupon_status"),
]