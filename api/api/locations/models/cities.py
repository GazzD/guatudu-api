"""City model."""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

# Models
from api.locations.models.countries import Country

class City(BaseModel):
    """ City model. """
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/cities/images', max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        """ Return city string representation"""
        return str(self.name)
    
    class Meta:
        db_table = 'cities'