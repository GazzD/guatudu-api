"""Profile model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from api.utils.models import GuatuduModel

class Profile(GuatuduModel):
    """ Profile model. """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures', 
        blank=True,
        null=True
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone nubmer must be entered in the formar: +999999999. Up to 15 digits allowed.'
    )
    
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        """ Return user string representation"""
        return str(self.user)
    