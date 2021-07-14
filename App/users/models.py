from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



def hex_uuid():
    return uuid.uuid4().hex

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, uuid, phone_number, registration_date, password,  **other_fields):
        user = self.model(email=email, username=username, uuid=uuid, phone_number=phone_number, registration_date=registration_date)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password):
                user = self.create_user(username=username, password=password, uuid="null", phone_number="null", registration_date="null", is_staff=True, email="null")
                user.is_superuser = True
                user.is_admin = True
                user.is_staff = True
                user.is_active = True
                user.save(using=self._db)

                return user

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True
    )
    username = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'uuid: {self.uuid}.', f'username: {self.username}.'
            


# need to clean this up