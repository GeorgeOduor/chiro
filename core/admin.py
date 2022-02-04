from django.contrib import admin
from .models import *


# Register your models here.
class tbl_TrxAccounts_Admin(admin.ModelAdmin):
    list_display = ('AccountID', 'TransactionType', 'TrxDate', 'TrxNarration', 'Amount', 'TrxTypeID', 'ClientType')
    list_display_links = ('AccountID',)
    search_fields = ('AccountID', 'TransactionType', 'TrxDate')
    # list_filter = ('Call_Agent', 'source')


admin.site.register(tbl_Transactions, tbl_TrxAccounts_Admin)
