"""Slider Images view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.sliders.serializers import SliderImageModelSerializer

# Models
from api.sliders.models import SliderImage

class SliderImageViewSet(viewsets.ModelViewSet):
    """Slider Image viewset"""

    queryset = SliderImage.objects.all()
    serializer_class = SliderImageModelSerializer
