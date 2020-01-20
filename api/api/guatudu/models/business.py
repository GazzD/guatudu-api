"""Business model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class Business(BaseModel):
    """ Business model. """

    name = models.CharField(max_length = 150)
    admin_profiles = models.ManyToManyField('guatudu.AdminProfile')
    
    def __str__(self):
        """ Return business string representation"""
        return str(self.name)
    
    class Meta:
        db_table = 'business'

