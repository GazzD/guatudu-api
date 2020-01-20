""" User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from api.utils.models import BaseModel

class User(BaseModel, AbstractUser):
    """ User model. """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    facebook_id = models.CharField(blank=True, max_length=255)
    password = models.CharField(blank=True, max_length=255)
    google_id = models.CharField(blank=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        """ Return email"""
        return self.email
    
    def get_short_name(self):
        """ Return email"""
        return self.email