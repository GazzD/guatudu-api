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

    city = CityModelSerializer(read_only=True)
    city_id = serializers.IntegerField()
    slider = SliderModelSerializer(read_only=True)
    slider_id = serializers.IntegerField()
    business = BusinessModelSerializer(read_only=True)
    business_id = serializers.IntegerField()
    
    class Meta():
        """Meta class"""
        model = Event
        fields = (
            'id',
            'name',
            'description',
            'status',
            'start_date',
            'end_date',
            'price',
            'main_image',
            'city',
            'business',
            'slider',
            'business_id',
            'city_id',
            'slider_id',
        )