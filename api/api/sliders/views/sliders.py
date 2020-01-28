"""Slider view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from api.sliders.serializers import SliderModelSerializer, SliderImageModelSerializer, SliderMassAssignSerializer

# Models
from api.sliders.models import Slider


class SliderViewSet(viewsets.ModelViewSet):
    """Slider viewset"""

    queryset = Slider.objects.all()
    serializer_class = SliderModelSerializer

    @action(detail=False, methods=['post'])
    def mass_assign(self, request):
        """ Create a slider with several sliders in one request """

        serializer = SliderMassAssignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        slider = serializer.save()
        data = {
            'slider' : slider,
        }
        return Response(data, status=status.HTTP_201_CREATED)
