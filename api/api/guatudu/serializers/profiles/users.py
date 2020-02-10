""" User Profile serializers """

# Django Rest Framework
from rest_framework import serializers

# Models
from api.users.models import User, Role
from api.guatudu.models import UserProfile
from api.locations.models import City

class UserProfileModelSerializer(serializers.ModelSerializer):
    """ User Profile model serializer """

    user = serializers.ModelField(User, read_only=False)
    city = serializers.ModelField(City, read_only=False)
    # name = serializers.CharField(required=False)
    # birth_date = serializers.DateField(required=False)
    # phone_number = serializers.CharField(required=False)
    # picture = serializers.ImageField(required=False)

    class Meta():
        """ Meta class. """
        model = UserProfile
        fields = (
            'id',
            'city',
            'user',
        )
