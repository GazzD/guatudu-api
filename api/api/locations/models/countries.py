"""Country model."""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class Country(BaseModel):
    """ Country model. """
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='uploads/countries/images', max_length=100, blank=True, null = True)
    
    def __str__(self):
        """ Return country string representation"""
        return str(self.name)

    class Meta:
        db_table = 'countries'