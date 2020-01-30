"""Profile model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from api.utils.models import BaseModel

class AdminProfile(BaseModel):
    """ Admin Profile model. """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    role = models.ForeignKey('users.Role', on_delete=models.CASCADE)

    def __str__(self):
        """ Return Admin Profile string representation"""
        return str(self.user)

    class Meta:
        db_table = 'admin_profiles'
    
    def signup(data):
        print('---------------------------------------------------')
        print(data)
        print('---------------------------------------------------')
        profile = AdminProfile()
        profile.user_id = data['user_id']
        profile.role_id = data['role_id']
        profile.save()
        return profile