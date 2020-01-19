"""Country views"""

#Django REST Framework
from rest_framework import APIView
from rest_framework import status

#Serializers
from api.locations.serializers import CreateCountrySerializer


class CountryAPIView(APIView):
    """Country API view"""
    def post(self, request, *args, **kwargs):
        """Create a new country"""
        serializer = CreateCountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        country = serializer.save()
        data = {
            'status': 'OK',
            'country': country
        }
        return Response(data, status= status.HTTP_201_CREATED)
