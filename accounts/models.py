from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class myuser(AbstractBaseUser):
    """
        This is a User model to create come extra fields
    """
    email_address = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email_address'
