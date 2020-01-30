# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from api.users.models import Role

class RoleModelSerializer(serializers.ModelSerializer):
    """Role Model Serializer """
    name = serializers.CharField(
        max_length=140,
        validators = [
            UniqueValidator(queryset=Role.objects.all())
        ]
    )
    class Meta:
        """Meta class"""
        model = Role
        fields = (
            'id',
            'name',
        )
    