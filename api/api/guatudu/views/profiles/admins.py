""" Admin Profile Views """

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from api.guatudu.serializers.profiles.admins import AdminProfileModelSerializer, AdminProfileSignUpSerializer
from api.users.serializers.users import UserSignUpSerializer

# Models
from api.guatudu.models import AdminProfile
from api.users.models import User


class AdminProfileViewSet(viewsets.ModelViewSet):
    """ AdminProfile viewset """

    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileModelSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """ Sign Up AdminProfiles without profile. """
        user_serializer = UserSignUpSerializer(data=request.data)
        # Create user
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            request.data['user_id'] = user['id']
            request.data.pop('password_confirmation')
            request.data.pop('password')
            request.data.pop('email')

            # Create profile
            admin_profile_serializer = AdminProfileSignUpSerializer(data=request.data)
            if admin_profile_serializer.is_valid(raise_exception=True):
                profile = admin_profile_serializer.save()
                data = {
                    'profile' : profile,
                }
            return Response(data, status=status.HTTP_201_CREATED)
        
