from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account,Address

# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('full_name' , 'house_name' ,'city' ,'district', 'state')
    list_display_links = ('full_name', 'house_name')
