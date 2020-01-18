"""Permissions model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class Role(BaseModel):
    """ Permission model XD"""

    name = models.CharField(max_length = 150)

    def __str__(self):
        """ Return permission string representation"""
        return str(self.name)
    