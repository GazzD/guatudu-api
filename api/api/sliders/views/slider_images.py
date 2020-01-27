"""Slider Images view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializers
from api.sliders.serializers import SliderImageModelSerializer

# Models
from api.sliders.models import SliderImage

class SliderImageViewSet(viewsets.ModelViewSet):
    """Slider Image viewset"""

    queryset = SliderImage.objects.all()
    serializer_class = SliderImageModelSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)