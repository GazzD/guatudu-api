""" User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

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

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone nubmer must be entered in the formar: +999999999. Up to 15 digits allowed.'
    )
    
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Hlelp easily distinguish uysers and perform queries.'
            'Clients are the main type user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text= 'Set to true when the user have verified its email address.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """ Return username"""
        return self.username
    
    def get_short_name(self):
        """ Return username"""
        return self.username