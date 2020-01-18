"""Country model."""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

# Models
from api.locations.models.cities import City

class Country(BaseModel):
    """ Country model. """
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='cities/images', max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        """ Return country string representation"""
        return str(self.name)
   