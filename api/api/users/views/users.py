"""Slider view"""

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from api.users.serializers import UserModelSerializer, UserSignUpSerializer

# Models
from api.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """User viewset"""

    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Sign Up users without profile. """
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data = {
                'user' : user,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
