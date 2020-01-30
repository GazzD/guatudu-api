"""Role view"""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.users.serializers import RoleModelSerializer

# Models
from api.users.models import Role


class RoleViewSet(viewsets.ModelViewSet):
    """User viewset"""

    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer