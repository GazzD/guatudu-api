""" Admin User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from api.utils.models import BaseModel

class Admin(BaseModel, AbstractUser):
    """ Admin model. """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A admin with that email already exists.'
        }
    )

    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'admin_users'

    def __str__(self):
        """ Return email"""
        return self.email
    
    def get_short_name(self):
        """ Return email"""
        return self.email