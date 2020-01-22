"""City Serializers"""

#Django Rest Framework
from rest_framework import serializers

# Serializers
from api.locations.serializers import CountryModelSerializer

#Model
from api.locations.models import City

class CityModelSerializer(serializers.ModelSerializer):
    """City Model Serializer"""
    country = CountryModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = City
        fields = (
            'id',
            'name',
            'image',
            'country',
        )