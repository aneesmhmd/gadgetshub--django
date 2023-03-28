from django.urls import path
from . import views

urlpatterns = [
    # Category
    path('', views.banner_managemet,name="banner"),
    path('add-banner/', views.add_banner,name="add_banner"),
    path('edit-banner/<int:id>/', views.edit_banner,name="edit_banner"),
    path('remove-banner/<int:id>/', views.remove_banner,name="remove_banner"),
    
]