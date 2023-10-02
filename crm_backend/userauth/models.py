from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.mixins import BaseModel, Timestamps, SoftDelete
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password
        """
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class User(AbstractUser, BaseModel, Timestamps, SoftDelete):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
