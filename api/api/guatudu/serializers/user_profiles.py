""" Business Serializers. """

# Django Rest Framework
from rest_framework import serializers

# Models
from api.guatudu.models import UserProfile

# Serializers
from api.guatudu.serializers.profiles.admins import AdminProfileModelSerializer

class BusinessModelSerializer(serializers.ModelSerializer):
    """ Business Model Serializer. """

    user_profiles = UserProfileModelSerializer(many=True, read_only=True)

    class Meta():
        model = UserProfile
        fields = (
            'id',
            'user',
            'picture',
            'phone_number',
            'birth_date',
        )
    