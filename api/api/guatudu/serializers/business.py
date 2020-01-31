""" Business Serializers. """

# Django Rest Framework
from rest_framework import serializers

# Models
from api.guatudu.models import Business

# Serializers
from api.guatudu.serializers.profiles.admins import AdminProfileModelSerializer

class BusinessModelSerializer(serializers.ModelSerializer):
    """ Business Model Serializer. """

    admin_profiles = AdminProfileModelSerializer(many=True, read_only=True)

    class Meta():
        model = Business
        fields = (
            'id',
            'name',
            'image',
            'phone',
            'email',
            'rating',
            'admin_profiles',
        )
    