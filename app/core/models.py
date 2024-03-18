"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users."""

    # **extra_fields can provide keyword arguments, e.g. a name
    def create_user(self, email, password=None, **extra_fields):
        """create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address')
        # vor "normalisieren der Mail Adresse"
        # user = self.model(email=email, **extra_fields)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # staff is allowed to open Django Admin!
    is_staff = models.BooleanField(default=False)

    # Assign UserManager to the User...
    objects = UserManager()

    # modify that email is the Username!
    USERNAME_FIELD = 'email'
