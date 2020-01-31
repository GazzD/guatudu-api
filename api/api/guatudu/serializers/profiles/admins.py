""" Admin Profile serializers """

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from api.users.models import User, Role
from api.guatudu.models import AdminProfile

# Serializers
from api.users.serializers.users import UserSignUpSerializer, UserModelSerializer
from api.users.serializers.roles import RoleModelSerializer

class AdminProfileModelSerializer(serializers.ModelSerializer):
    """ Admin Profile model serializer """

    user = UserModelSerializer(read_only=False)
    role = RoleModelSerializer(read_only=False)

    class Meta():
        """ Meta class. """
        model = AdminProfile
        fields = (
            'id',
            'user',
            'role' 
        )

class AdminProfileSignUpSerializer(serializers.Serializer):
    """This handles the creation of users with an admin profile """

    user_id = serializers.CharField(read_only=False)
    role_id = serializers.CharField(read_only=False)

    def create(self, validated_data):
        """Hanadle the creation of admin profiles """
        profile = AdminProfile.signup(validated_data)
        serializer = UserModelSerializer(profile.user)
        validated_data['user'] = serializer.data
        validated_data['user'].pop('password')
        return validated_data
 
    def update(self, instance, validated_data):
        """Update user email or password """
        User.update(instance, **validated_data)
        validated_data.pop('password')
        return validated_data
