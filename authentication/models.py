from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        """ Create and saves a new User """
        if not username:
            raise ValueError("User mas have a username")
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """ Create a new Super User """
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=250, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    isProvinceSpecialist = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
