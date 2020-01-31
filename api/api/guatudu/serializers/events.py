""" Event Serializers. """

# Django Rest Framework
from rest_framework import serializers

# Models
from api.guatudu.models import Event

# Serializers
from api.locations.serializers import CityModelSerializer
from api.guatudu.serializers.business import BusinessModelSerializer
from api.sliders.serializers.sliders import SliderModelSerializer

class EventModelSerializer(serializers.ModelSerializer):
    """ Event Model serializer. """

  
    
    class Meta():
        """Meta class"""
        model = Event
        fields = (
            'id',
            'name',
            'description',
            'main_image',
            'start_date',
            'end_date',
            'city',
            'business',
            'status',
            'slider',
            'price',
        )