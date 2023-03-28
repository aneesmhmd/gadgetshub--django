from django.urls import path
from . import views

urlpatterns = [
    # Orders
    path('', views.order_management,name="order_management"),
    path('ordered-items/<int:id>/', views.order_items,name="order_items"),
    path('status-update/<int:id>/', views.status_update,name="status_update"),

    # Review
    path('review-managemet/', views.review_management, name="review_management"),
    path('remove-review/<int:id>/', views.remove_review, name="remove_review"),
]