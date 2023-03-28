from django.shortcuts import render, redirect
from category.models import Category, Brand
from .forms import CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from admin_products.views import superadmin_check


# Create your views here.
@user_passes_test(superadmin_check)
def admin_category(request):
    return render(request, 'admin_home/category.html')


@user_passes_test(superadmin_check)
def add_category(request):
    if request.method == 'POST':
        try:
            cat_name = request.POST['cat_name']
            description = request.POST['cat_description']
            cat_image = request.FILES['cat_image']

            if Category.objects.filter(category_name=cat_name).exists():
                messages.warning(request, "Category already exists!")
                return redirect(add_category)

            Category.objects.create(category_name=cat_name, description=description, category_image=cat_image)
            messages.success(request, 'Category addedd succesfully')
            return redirect(admin_category)
        except:
            pass

    return redirect(admin_category)


@user_passes_test(superadmin_check)
def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == 'POST':
            cat_name = request.POST['cat_name']
            description = request.POST['cat_description']

            
            if Category.objects.filter(category_name=cat_name).exclude(id=id).exists():
                messages.warning(request, 'Category already exists!')
                return redirect(admin_category)
            else:
                category.category_name = cat_name
                category.description = description
                category.save()

            if request.FILES['cat_image']:
                cat_image = request.FILES['cat_image']
                category.category_image = cat_image
                category.save()

            messages.success(request, f'Category {category.category_name} updated successfully')
            return redirect(admin_category)
    except:
        pass
    return redirect(admin_category)


@user_passes_test(superadmin_check)
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
    except:
        pass
    return redirect(admin_category)

# ============================ End Category ============================


# ============================ Brand ============================

@user_passes_test(superadmin_check)
def admin_brand(request):
    return render(request, 'admin_home/brand.html')


@user_passes_test(superadmin_check)
def add_brand(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']

        if Brand.objects.filter(brand_name=brand_name).exists():
            messages.warning(request, 'Brand already exists')
            return redirect(admin_brand)

        brand = Brand.objects.create(brand_name=brand_name)
        brand.save()
        messages.success(request, 'Brand addedd succesfully')
        return redirect(admin_brand)

    return redirect(admin_brand)


@user_passes_test(superadmin_check)
def edit_brand(request, id):
    try:
        brand = Brand.objects.get(id=id)
        
        if request.method == 'POST':
            brand_name = request.POST['brand_name']

            if Brand.objects.filter(brand_name=brand_name).exclude(id=id).exists():
                messages.warning(request, 'Brand already exists!')
                return redirect(admin_brand)
            
            brand.brand_name = brand_name
            brand.save()
            messages.success(request, 'Brand edited successfully')
            return redirect(admin_brand)

    except Brand.DoesNotExist:
        messages.warning(request, 'Brand doesnot exist')
        return redirect(admin_brand)


@user_passes_test(superadmin_check)
def remove_brand(request, id):
    try:
        brand = Brand.objects.get(id=id)
        brand.delete()
        messages.success(request, 'Brand deleted successfully')
        return redirect(admin_brand)

    except Brand.DoesNotExist:
        messages.warning(request, 'Brand doesnot exist')
        return redirect(admin_brand)
