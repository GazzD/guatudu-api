"""Roles model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class Role(BaseModel):
    """ Role model XD"""

    name = models.CharField(max_length = 150)
    permissions = models.ManyToManyField('users.Permission')
    

    def __str__(self):
        """ Return user string representation"""
        return str(self.name)
    