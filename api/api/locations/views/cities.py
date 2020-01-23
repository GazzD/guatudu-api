"""City view"""
#Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.locations.serializers import CityModelSerializer
from api.locations.serializers import CountryModelSerializer

# Models
from api.locations.models import City
from api.locations.models import Country

class CityViewSet(viewsets.ModelViewSet):
    """City viewset"""

    queryset = City.objects.all()
    serializer_class = CityModelSerializer