from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=50)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)

    class Meta:
        db_table = 'country'
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self) -> str: return self.name


class Nationalities(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Countries, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = 'nationalities'
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'

    def __str__(self) -> str: return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, mobile, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name,
                          mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, mobile, password=None, **extra_fields):
        """
        Create and return a superuser with an email, password, and admin privileges.
        """
        extra_fields.setdefault('role', 3)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, full_name, mobile, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class RoleChoices(models.IntegerChoices):
        STUDENT = 1, 'Student'
        STAFF = 2, 'Staff'
        ADMIN = 3, 'Admin'
        EDITOR = 4, 'Editor'

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=RoleChoices.choices, default=1)
    country = models.ForeignKey(
        Countries, on_delete=models.SET_NULL, null=True
    )
    nationality = models.ForeignKey(
        Nationalities, on_delete=models.SET_NULL, null=True
    )
    other_country = models.CharField(null=True, max_length=50)
    other_nationality = models.CharField(null=True, max_length=50)
    mobile = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'mobile']

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
