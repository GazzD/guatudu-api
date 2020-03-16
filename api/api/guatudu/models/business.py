"""Business model"""

# Django
from django.db import models

# Models
from api.guatudu.models import AdminBusiness, UserBusiness

# Utilities
from api.utils.models import BaseModel

class Business(BaseModel):
    """ Business model. """

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/business')
    phone = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    admin_profiles = models.ManyToManyField('guatudu.AdminProfile', through=AdminBusiness)
    user_profiles = models.ManyToManyField("guatudu.UserProfile", through=UserBusiness)
    def __str__(self):
        """ Return business string representation"""
        return str(self.name)

    class Meta:
        db_table = 'business'