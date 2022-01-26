from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models as m
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = m.EmailField(unique=True)
    user_name = m.CharField(max_length=150, unique=True)
    first_name = m.CharField(max_length=150, blank=True)
    about = m.TextField(max_length=500, blank=True)
    # Delivery details
    country = CountryField()
    phone_number = m.CharField(max_length=15, blank=True)
    postcode = m.CharField(max_length=12, blank=True)
    address_line_1 = m.CharField(max_length=150, blank=True)
    address_line_2 = m.CharField(max_length=150, blank=True)
    town_city = m.CharField(max_length=150, blank=True)
    # User Status
    is_active = m.BooleanField(default=False)
    is_staff = m.BooleanField(default=False)

    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    """For the create superuser"""
    REQUIRED_FIELDS = ['user_name']

    objects = CustomAccountManager()

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.user_name


