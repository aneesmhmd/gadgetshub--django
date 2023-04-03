from django.shortcuts import render,redirect
from .models import Banner
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from admin_products.views import superadmin_check

# Create your views here.

@user_passes_test(superadmin_check)
def banner_managemet(request):
    banners = Banner.objects.all().order_by('-id')
    return render(request, 'admin_home/banner.html', {'banners' : banners})



@user_passes_test(superadmin_check)
def add_banner(request):
    if request.method == 'POST':
        image = request.FILES['banner_image']
        text_one = request.POST['text_one']
        text_two = request.POST['text_two']
        
        Banner.objects.create(image=image, text_one=text_one, text_two=text_two)
        messages.success(request, 'Banner added succesfully')
        return redirect(banner_managemet)
    


@user_passes_test(superadmin_check)
def edit_banner(request, id):
    if request.method == 'POST':
        text_one = request.POST['text_one']
        text_two = request.POST['text_two']
        
    try:
        banner = Banner.objects.get(id=id)
        banner.text_one = text_one
        banner.text_two = text_two

        try:
            if request.FILES['banner_image']:
                image = request.FILES['banner_image']
                banner.image = image
        except:
            pass

        banner.save()
        return redirect(banner_managemet)
    
    except Banner.DoesNotExist:
        messages.warning(request, 'Oops!Something gone wrong')
        return redirect(banner_managemet)
    


@user_passes_test(superadmin_check)
def remove_banner(request, id):
    try:
        banner = Banner.objects.get(id=id)
        banner.delete()
        messages.success(request, 'Banner removed succesfully')
        return redirect(banner_managemet)
    except Banner.DoesNotExist:
        messages.error(request, 'Oops!Something gone wrong')
        return redirect(banner_managemet)
    
