"""City view"""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.locations.serializers import CityModelSerializer

# Models
from api.locations.models import City

class CityViewSet(viewsets.ModelViewSet):
    """City viewset"""

    queryset = City.objects.all()
    serializer_class = CityModelSerializer