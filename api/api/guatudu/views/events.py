# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from api.guatudu.models import Event

# Serializers
from api.guatudu.serializers.events import EventModelSerializer
from api.sliders.serializers.sliders import SliderMassAssignSerializer

class EventViewSet(viewsets.ModelViewSet):
    """ Event Model ViewSet. """

    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    @action(methods=['post'], detail=False)
    def slider(self, request):
        """ Handles the creation of events with a new slider """

        slider_serializer = SliderMassAssignSerializer(data=request.data)
        if slider_serializer.is_valid(raise_exception=True):
            slider = slider_serializer.save()
            request.data['slider_id'] = slider['id']
            request.data.pop('images')
            print('*************************')
            print(request.data)
            print('*************************')
            event_serializer = EventModelSerializer(data=request.data)
            if(event_serializer.is_valid(raise_exception=True)):
                print('-----SERIALIZER------------')
                print(event_serializer.data)
                print('--------------------')
                print('-----CREANDO----------')
                event = event_serializer.save()
                print('///////////////CREADO////////////')
                print(event)
            data = {
                'event' : event.data
            }

            return Response(data, status=status.HTTP_200_OK)