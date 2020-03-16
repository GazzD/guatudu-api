"""User Business model"""

# Django
from django.db import models

# Utilities
from api.utils.models import BaseModel

class UserBusiness(BaseModel):
    """ UserBusiness model. """

    user = models.ForeignKey('guatudu.UserProfile', on_delete=models.CASCADE)
    business = models.ForeignKey('guatudu.Business', on_delete=models.CASCADE)
    
    def __str__(self):
        """ Return admin bussiness string representation"""
        return str(self.admin) + ' ' + str(self.business)

    class Meta:
        db_table = 'admin_business'
    