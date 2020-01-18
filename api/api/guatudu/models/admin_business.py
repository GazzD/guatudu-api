"""Business model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class AdminBusiness(BaseModel):
    """ Role model. """

    name = models.CharField(max_length = 150)
    admin = models.ForeignKey('guatudu.AdminProfile', on_delete=models.CASCADE)
    business = models.ForeignKey('guatudu.Business', on_delete=models.CASCADE)
    

    def __str__(self):
        """ Return user string representation"""
        return str(self.user)
    