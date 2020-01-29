"""Country Serializers"""

#Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Serializers
from api.locations.serializers.cities import CityModelSerializer

#Model
from api.locations.models import Country

class CountryModelSerializer(serializers.ModelSerializer):
    """Country Model Serializer"""
    cities = CityModelSerializer(many=True, read_only=True)
    class Meta:
        """Meta class"""
        model = Country
        fields = (
            'id',
            'name',
            'image',
            'cities'
        )

# class CountrySerializer(serializers.Serializer):
#     """Country Serializer"""

#     name = serializers.CharField()
#     image = serializers.FilePathField()

# class CreateCountrySerializer(serializers.Serializer):
#     """Create Country Serializer """

#     name = serializers.CharField(
#         max_length=140,
#         validators = [
#             UniqueValidator(queryset=Country.objects.all())
#         ]
#     )
#     image = serializers.FilePathField(required = False)

#     def create(self, data):
#         return Country.objects.create(**data)
