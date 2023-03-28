from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from orders.models import Order, OrderItem, ReviewRating
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from admin_products.views import superadmin_check

# Create your views here.

@user_passes_test(superadmin_check)
def order_management(request):
    context = {
    'orders' : Order.objects.all().order_by('-id'),
    'order_items' : OrderItem.objects.all()
    }
    return render(request, 'admin_home/orders.html', context)



@user_passes_test(superadmin_check)
def order_items(request, id):
    try:
        order = Order.objects.get(id=id)
        order_items = OrderItem.objects.filter(order=order).order_by('id')
        return render(request, 'admin_home/order_items.html', {'order_items' : order_items})
    
    except:
        messages.error(request, 'Oops!Something gone wrong')
        return redirect(order_management)
    


@user_passes_test(superadmin_check)
def status_update(request, id):
    try:
        order_item = OrderItem.objects.get(id=id)
        if request.method == 'POST':
            status = request.POST['status']
            order_item.order_status = status
            order_item.save()
            messages.success(request, 'Status updated successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    except OrderItem.DoesNotExist:
        messages.error(request, 'Oops!Something gone wrong')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




# ----------------------- Review management -------------------

@user_passes_test(superadmin_check)
def review_management(request):
    reviews = ReviewRating.objects.all()
    return render(request, 'admin_home/reviews.html', {'reviews' : reviews})


@user_passes_test(superadmin_check)
def remove_review(request, id):
    try:
        review = ReviewRating.objects.get(id=id)
        review.delete()
        messages.success(request, 'Review removed succesfully')
        return redirect(review_management)
    
    except ReviewRating.DoesNotExist:
        messages.warning(request, 'Oops!Something went wrong')
        return redirect(review_management)