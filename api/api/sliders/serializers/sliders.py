"""Slider Serializers"""

# Django
from django.core.files.storage import FileSystemStorage

# Django Rest Framework
from rest_framework import serializers

# Serializers
from api.sliders.serializers.slider_images import SliderImageModelSerializer

# Model
from api.sliders.models import Slider, SliderImage

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

class SliderMassAssignSerializer(serializers.Serializer):
    """ Serializer to mass assign images to a slider """
    images = serializers.ListField(child=serializers.ImageField())

    def validate(self, attrs):
        if len(attrs['images']) > 5:
            raise serializers.ValidationError("A Slider can only contain 5 images")
        return attrs

    def create(self, data):
        """Create a slider and asociate up to 5 SliderImages """
        slider = Slider()
        slider.save()
        for image in data['images']:
            slider_image = SliderImage()
            file_system = FileSystemStorage()
            name = 'uploads/sliders/images/'+image.name
            filename = file_system.save(name, image)
            slider_image.url = file_system.url(filename)
            slider_image.slider = slider
            slider_image.save()

        serializer = SliderModelSerializer(slider)
        return serializer.data