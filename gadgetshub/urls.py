from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400
from home.views import error_page

urlpatterns = [
    path('admindj/', admin.site.urls),
    path('', include('home.urls')),
    path('store/', include('store.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('order/', include('orders.urls')),

    # Admin Side
    path('adm/', include('admin_accounts.urls')),
    path('adm/store/', include('admin_products.urls')),
    path('adm/category/', include('admin_categories.urls')),
    path('adm/orders/', include('admin_orders.urls')),
    path('adm/banners/', include('banner.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, settings.STATIC_ROOT)


handler400 = error_page
