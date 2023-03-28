from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product 
from banner.models import Banner

# Create your views here.
def home(request):
    context = {
        'products' : Product.objects.all()[:4],
        'banners' : Banner.objects.all()
         }
    return render(request, 'user/index.html',context)