"""Permissions model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class Permission(BaseModel):
    """ Permission model"""

    name = models.CharField(max_length=150)

    def __str__(self):
        """ Return permission string representation"""
        return str(self.name)
    
    class Meta:
        db_table = 'permissions'