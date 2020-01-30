"""User Serializer"""

# Django
from django.contrib.auth import password_validation, authenticate

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Model
from api.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """ User Model Serializer. """

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'id',
            'email',
            'password',
            'facebook_id',
            'google_id'
        )

class UserSignUpSerializer(serializers.Serializer):
    """Create user with email and password. """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, attrs):
        """Verify passwords match."""
        passwd = attrs['password']
        passwd_conf = attrs['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return attrs

    def create(self, validated_data):
        """Handle user creation."""
        validated_data.pop('password_confirmation')
        user = User.create(self, **validated_data)
        validated_data['id'] = user.id
        validated_data.pop('password')
        return validated_data

    def update(self, instance, validated_data):
        """Update user email or password """
        User.update(instance, **validated_data)
        validated_data.pop('password')
        return validated_data