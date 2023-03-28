from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Account
from admin_products.views import superadmin_check
from orders.models import OrderItem
from django.db.models import Count
# Create your views here.

@user_passes_test(superadmin_check)
def admin_panel(request):
    sales = OrderItem.objects.all().count()
    users = Account.objects.all().count()
    
    context = {
        'sales' : sales,
        'users' : users,
    }
    return render(request, 'admin_home/index.html',context)



def admin_login(request):
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superadmin:
                auth.login(request,user)
                return redirect(admin_panel)
            else:
                messages.error(request, "You're not an admin")
                return redirect('admin_login')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect(admin_login)
        
    return render(request, 'admin_home/login.html')



@login_required
def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')



@login_required
@user_passes_test(superadmin_check)
def users_list(request):
    users = Account.objects.all().order_by('id')
    return render(request, 'admin_home/users_list.html', {'users': users})



@login_required
@user_passes_test(superadmin_check)
def block_unblock(request, id):
    try:
        user = Account.objects.get(id=id)
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
    except Account.DoesNotExist:
        pass
    return redirect(users_list)




    
