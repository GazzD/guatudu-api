"""Slider Serializers"""

# Django Rest Framework
from rest_framework import serializers

# Serializers
from api.sliders.serializers import SliderImageModelSerializer

# Model
from api.sliders.models import Slider

class SliderModelSerializer(serializers.ModelSerializer):
    """ Slider Model Serializer. """
    images = SliderImageModelSerializer(many=True, read_only=True)

    class Meta:
        """Meta class"""
        model = Slider
        fields = (
            'id',
            'status',
            'images',
        )