"""SliderImage Serializers"""

# Django Rest Framework
from rest_framework import serializers

# Model
from api.sliders.models import SliderImage, Slider

# Serializers

class SliderImageModelSerializer(serializers.ModelSerializer):
    """ Slider Image Model Serializer. """
    slider_id = serializers.IntegerField()

    class Meta:
        """ Meta class """
        model = SliderImage
        fields = (
            'id',
            'url',
            'link',
            'slider_id',
            'position',
        )


