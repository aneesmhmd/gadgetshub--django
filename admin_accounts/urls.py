from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.admin_panel,name="admin_panel"),
    path('login/', views.admin_login,name="admin_login"),
    path('logout/', views.admin_logout,name="admin_logout"),

    # User management
    path('users/', views.users_list,name="users_list"),
    path('block-unblock/<int:id>', views.block_unblock,name="block_unblock"),
]