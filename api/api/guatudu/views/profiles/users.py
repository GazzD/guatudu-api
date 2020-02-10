# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from api.guatudu.models import UserProfile

# Serializers
from api.guatudu.serializers.profiles.users import UserProfileModelSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """ User Model ViewSet. """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer

    @action(methods=['get'], detail=False)
    def hello(self, request):
        """ Assign admin profiles to a business """

        return Response('Hello', status=status.HTTP_200_OK)