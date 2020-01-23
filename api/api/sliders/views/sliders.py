"""Slider view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.sliders.serializers import SliderModelSerializer

# Models
from api.sliders.models import Slider

class SliderViewSet(viewsets.ModelViewSet):
    """Slider viewset"""

    queryset = Slider.objects.all()
    serializer_class = SliderModelSerializer
