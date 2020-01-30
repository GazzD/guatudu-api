""" Admin Profile serializers """

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from api.users.models import User, Role
from api.guatudu.models import AdminProfile

# Serializers
from api.users.serializers.users import UserSignUpSerializer

class AdminProfileModelSerializer(serializers.ModelSerializer):
    """ Admin Profile model serializer """

    user = serializers.ModelField(User, read_only=False)
    role = serializers.ModelField(Role, read_only=False)

    class Meta():
        """ Meta class. """
        model = AdminProfile
        fields = (
            'user',
            'role'
        )

class AdminProfileSignUpSerializer(serializers.Serializer):

    """This handles the creation of users with an admin profile """
    user_id = serializers.CharField(read_only=False)
    role_id = serializers.CharField(read_only=False)

    def create(self, validated_data):
        profile = AdminProfile.signup(validated_data)
        serializer = AdminProfileModelSerializer(instance=profile)
        return serializer.data
 
    def update(self, instance, validated_data):
        """Update user email or password """
        User.update(instance, **validated_data)
        validated_data.pop('password')
        return validated_data
