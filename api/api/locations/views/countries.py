"""Countries view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.locations.serializers import CountryModelSerializer

# Models
from api.locations.models import Country

class CountryViewSet(viewsets.ModelViewSet):
    """Country viewset"""

    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
