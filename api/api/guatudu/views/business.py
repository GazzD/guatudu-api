# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from api.guatudu.models import Business, AdminProfile

# Serializers
from api.guatudu.serializers.business import BusinessModelSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    """ Business Model ViewSet. """

    queryset = Business.objects.all()
    serializer_class = BusinessModelSerializer

    @action(methods=['patch'], detail=True)
    def assign_admin(self, request, pk):
        """ Assign admin profiles to a business """

        business = get_object_or_404(Business, pk=pk)
        admin = get_object_or_404(AdminProfile, pk=request.data['admin_id'])
        business.admin_profiles.add(admin)
        business_serializer = BusinessModelSerializer(business)
        data = {
            'business' : business_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)