import datetime
import hashlib
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager

# Create your models here.


class BaseModel(models.Model):
    """
        This is for storing commonly used fields.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class MyUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
        This is a User model to create some extra fields.
    """
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255)
    email_token_created_on = models.DateTimeField(default=datetime.datetime.now())

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def generate_token(self):
        """
            This method will generate the token and save it to the database.
        """
        random_string = hashlib.sha1(os.urandom(128)).hexdigest()
        while True:
            if MyUser.objects.filter(email_token=random_string).first():
                random_string = hashlib.sha1(os.urandom(128)).hexdigest()
            else:
                self.email_token = random_string
                self.email_token_created_on = datetime.datetime.now()
                self.save()
                break
