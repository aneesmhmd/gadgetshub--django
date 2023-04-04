from django.urls import path
from . import views


urlpatterns = [
    # auth
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),

    # forgot password
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name="reset_password_validate"),
    path('reset_password/', views.reset_password, name="reset_password"),

    # user dashboard
    path('dashboard/', views.dashboard, name="dashboard"),
    path('edit_profile/<int:user_id>/', views.edit_profile, name="edit_profile"),
    path('change_password/<int:user_id>/', views.change_password, name="change_password"),
    path('change_dp/', views.change_dp, name="change_dp"),

    # addresses
    path('add_address/<int:num>/', views.add_address, name="add_address"),
    path('addresses/edit_address/<int:id>/', views.edit_address, name='edit_address'),   
    path('addresses/delete_address/<int:id>/<int:num>/', views.delete_address, name='delete_address'),   
    path('addresses/default_address/<int:id>/<int:num>/', views.default_address, name='default_address'),
]