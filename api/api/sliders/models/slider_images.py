"""SliderImage model."""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

# Models
from api.sliders.models.sliders import Slider

class SliderImage(BaseModel):
    """ SliderImage model. """
    url = models.ImageField(upload_to='uploads/sliders/images', max_length=100)
    link = models.CharField(max_length=255, blank=True, null=True)
    slider = models.ForeignKey(Slider,related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        """ Return SliderImage string representation"""
        return str(self.url)
    
    class Meta:
        """ Meta class. """
        db_table = 'slider_images'