from django.urls import path,include
from . import views

urlpatterns = [
    # Category
    path('', views.admin_category,name="admin_category"),
    path('edit-category/<int:id>/', views.edit_category,name="edit_category"),
    path('delete-category/<int:id>/', views.delete_category,name="delete_category"),
    path('add-category/', views.add_category,name="add_category"),

    # Brand
    path('brands/', views.admin_brand, name="admin_brand"),
    path('add-brand/', views.add_brand,name="add_brand"),
    path('edit-brand/<int:id>/', views.edit_brand,name="edit_brand"),
    path('remove-brand/<int:id>/', views.remove_brand,name="remove_brand"),
]