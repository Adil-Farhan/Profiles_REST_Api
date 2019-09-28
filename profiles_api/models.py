from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models her_e.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for UserProfile in system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = model.BooleanField(default = True)
    is_staff = model.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'name'

    def get_full_name(self):
        """Get full name of user """
        return self.name

    def get_short_name(self):
        """Get short name of user """
        return self.name


    def __str__(self):
        """GEt String representation of user"""
        return self.email
