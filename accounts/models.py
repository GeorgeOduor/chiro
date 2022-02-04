from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.utils.translation import ugettext_lazy as _

from django.utils.translation import gettext_lazy as _



# Create your models here.

class MyAccountManager(BaseUserManager):
    """
    model for User model with no username field
    """
    def create_user(self, phone_no,email, password=None, **extra_fields):
        """ Create and save a user with the given email and password. """
        if not email:
            raise ValueError('Email address is mandatory')
        # if not username:
        #     raise ValueError('Username is mandatory')
        if not phone_no:
            raise ValueError('Phone number is mandatory')
        user = self.model(
            # email=self.normalize_email(email),
            # username=username,
            phone_no=phone_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            # username=username,
            password=password,
            phone_no=phone_no,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser,PermissionsMixin):
    username = None
    phone_no = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    # requires
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.phone_no

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return self.is_superadmin
