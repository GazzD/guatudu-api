"""Slider view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from api.sliders.serializers import SliderModelSerializer, SliderImageModelSerializer

# Models
from api.sliders.models import Slider


class SliderViewSet(viewsets.ModelViewSet):
    """Slider viewset"""

    queryset = Slider.objects.all()
    serializer_class = SliderModelSerializer
