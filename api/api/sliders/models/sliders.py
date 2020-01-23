"""Slider model."""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel


class Slider(BaseModel):
    """ Slider model. """
    STATUS = (
    ('ENABLED', 'ENABLED'),
    ('DISABLED', 'DISABLED')
)
    status = models.CharField(max_length=8, choices=STATUS, default='ENABLED')
   

    def __str__(self):
        """ Return Slider string representation"""
        return str(self.status)
    
    class Meta:
        db_table = 'sliders'