"""Locations Urls"""

#Django
from django.urls import path

# Views
from api.locations.views import LocationAPIView

urlpatterns = [
    path('locations',LocationsAPIView.as_view(). namespace = "locations")

]