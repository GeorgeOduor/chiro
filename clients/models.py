from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

# Create your models here.
class tbl_Clients(models.Model):
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    user = models.OneToOneField(Account, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    mobile_no = models.CharField(max_length=15, null=True)
    national_id = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6, null=True, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    date_of_birth = models.DateField(null=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    AccountNumber = models.CharField(max_length=13, null=False, unique=True)
    Address = models.CharField(max_length=13, null=True)
    AmountEligible = models.DecimalField(max_digits=12, max_length=12, null=True, decimal_places=2)
    ClientType = models.CharField(max_length=2, choices=[('C', 'Client'), ('L', 'Lender'), ('S', 'Service provider'), ],
                                  null=True)
    BusinessName = models.CharField(max_length=13, null=True)

    class Meta:
        verbose_name = 'tbl_Client'
        verbose_name_plural = 'tbl_Clients'
