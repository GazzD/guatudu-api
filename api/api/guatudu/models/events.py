""" Event Model. """

#Django
from django.db import models

#Utils
from api.utils.models import BaseModel

class Event(BaseModel):
    """ Event Model """
    STATUS = (
        ('PENDING', 'PENDING'),
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE')
    )

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=999)
    main_image = models.ImageField(upload_to='uploads/events')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city = models.ForeignKey('locations.City', on_delete=models.CASCADE)
    business = models.ForeignKey('guatudu.Business', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')
    slider = models.ForeignKey('sliders.Slider', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        """Meta class"""
        db_table = 'events'
