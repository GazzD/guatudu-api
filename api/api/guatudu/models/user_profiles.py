"""Profile model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from api.utils.models import BaseModel

class UserProfile(BaseModel):
    """ User Profile model. """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='uploads/users/pictures', 
        blank=True,
        null=True
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone nubmer must be entered in the format : +999999999. Up to 15 digits allowed.'
    )

    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )

    birth_date = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        blank=True,
        null=True
    )

    city = models.ForeignKey('locations.City', on_delete=models.CASCADE)

    def __str__(self):
        """ Return user string representation"""
        return str(self.user)
    
    class Meta:
        db_table = 'user_profiles'