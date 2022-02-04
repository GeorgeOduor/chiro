from django.contrib import admin

# Register your models here.
from .models import *


class tbl_Clients_Admin(admin.ModelAdmin):
    list_display = ('AccountNumber','CreatedOn','date_of_birth','first_name','last_name','gender','mobile_no','national_id')
    list_display_links = ('AccountNumber',)
    search_fields = ('AccountNumber', 'CreatedOn', 'first_name')
    # list_filter = ('Call_Agent', 'source')


admin.site.register(tbl_Clients,tbl_Clients_Admin)
