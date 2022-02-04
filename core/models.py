from django.db import models

from clients.models import tbl_Clients
from django.db.models import Sum


# Create your models here.
class tbl_Transactions(models.Model):
    ClientID = models.ForeignKey(tbl_Clients, on_delete=models.CASCADE, null=True)
    AccountID = models.CharField(max_length=13, blank=False, unique=False, null=False)
    TransactionType = models.CharField(max_length=10, choices=[
        ('Credit', 'Credit'),
        ('Debit', 'Debit')
    ])
    TrxDate = models.DateTimeField(auto_now_add=True, null=False)
    TrxNarration = models.TextField(max_length=5000, null=False)
    Amount = models.DecimalField(decimal_places=2, default=0, null=False, max_digits=20)
    TrxTypeID = models.CharField(max_length=2, choices=[('TC', 'TC'), ('TD', 'TD'), ('CC', 'CC'), ], null=False)
    ClientType = models.CharField(max_length=2, choices=[('C', 'Client'), ('L', 'Lender'), ('S', 'Service provider'), ],
                                  null=False)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class tbl_LoanAccounts(models.Model):
    ClientID = models.OneToOneField(tbl_Clients, on_delete=models.CASCADE, null=True,unique=True)
    AccountID = models.CharField(max_length=13, blank=False, unique=True, null=False)
    CreateDate = models.DateTimeField(auto_now_add=True, null=False)

    def CheckAccountID(self):
        print(self.AccountID)


