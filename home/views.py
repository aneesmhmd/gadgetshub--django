from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product 

# Create your views here.
def home(request):
    context = {'products' : Product.objects.all()[:4] }
    return render(request, 'user/index.html',context)