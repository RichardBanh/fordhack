from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



def hex_uuid():
    return uuid.uuid4().hex

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, uuid, phone_number, registration_date, is_staff, password,  **other_fields):
        user = self.model(email=email, username=username, uuid=uuid, phone_number=phone_number, registration_date=registration_date, is_staff=is_staff)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password):
                user = self.model(username=username, password=password)
                user.is_superuser = True
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

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return (
                f'uuid: {self.uuid}.'
                f'username: {self.username}.'
            )