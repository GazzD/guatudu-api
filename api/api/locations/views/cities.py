"""City view"""
#Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.locations.serializers import CityModelSerializer
from api.locations.serializers import CountryModelSerializer

# Models
from api.locations.models import City
from api.locations.models import Country

class CityViewSet(viewsets.ModelViewSet):
    """City viewset"""

    queryset = City.objects.all()
    serializer_class = CityModelSerializer

    def get_object(self):
            """
            Returns the object the view is displaying.

            You may want to override this if you need to provide non-standard
            queryset lookups.  Eg if objects are referenced using multiple
            keyword arguments in the url conf.
            """
            queryset = self.filter_queryset(self.get_queryset())

            # Perform the lookup filtering.
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

            assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
            )

            filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
            obj = get_object_or_404(queryset, **filter_kwargs)

            # May raise a permission denied
            self.check_object_permissions(self.request, obj)
            
            return CityModelSerializer(obj)

    def create(self, request, *args, **kwargs):
        print('*************************')
        print(request.data)
        print('*************************')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)