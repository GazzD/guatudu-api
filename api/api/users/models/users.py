""" User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from api.utils.models import GuatuduModel

class User(GuatuduModel, AbstractUser):
    """ User model. """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text= 'Set to true when the user have verified its email address.'
    )

    facebook_id = models.CharField(blank=True, max_length=255)

    google_id = models.CharField(blank=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """ Return username"""
        return self.username
    
    def get_short_name(self):
        """ Return username"""
        return self.username