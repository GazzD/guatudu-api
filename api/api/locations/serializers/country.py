"""Country Serializer"""

#Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Model
from api.locations.models import Country

class CountrySerializer(serializers.Serializer):
    """Country Serializer"""

    name = serializers.CharField()
    image = serializers.FilePathField()

class CreateCountrySerializer(serializers.Serializer):
    """Create Country Serializer """

    name = serializers.CharField(
        max_length=140,
        validators = [
            UniqueValidator(queryset=Country.objects.all())
        ]
    )
    image = serializers.FilePathField()

    def create(self, data):
        return Country.objects.create(**data)
