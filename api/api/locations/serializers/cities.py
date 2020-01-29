"""City Serializers"""

# Django Rest Framework
from rest_framework import serializers

# Model
from api.locations.models import City

class CityModelSerializer(serializers.ModelSerializer):
    """ City Model Serializer. """
    name = serializers.CharField(max_length=150)
    class Meta:
        """Meta class"""
        model = City
        fields = (
            'id',
            'name',
            'image',
            'country'
        )
