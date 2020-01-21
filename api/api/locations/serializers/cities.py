"""City Serializers"""

#Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Model
from api.locations.models import City

class CityModelSerializer(serializers.ModelSerializer):
    """City Model Serializer"""

    class Meta:
        """Meta class"""
        model = City
        fields = (
            'id',
            'name',
            'image',
            'country',
        )