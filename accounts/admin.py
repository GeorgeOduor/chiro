from django.contrib import admin
from .models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _



# Register your models here.

class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_no', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_admin', 'is_superadmin')}),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_no', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_no', 'email')
    list_filter = ('is_staff', 'is_superadmin', 'is_active', 'is_admin')
    search_fields = ('phone_no', 'email')
    ordering = ('phone_no',)

admin.site.register(Account, AccountAdmin)