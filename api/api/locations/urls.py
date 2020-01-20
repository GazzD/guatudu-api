"""Locations Urls"""

#Django
from django.urls import path

# Views
from api.locations.views import CountryAPIView

urlpatterns = [
    path('locations',CountryAPIView.as_view(), name='countries')

]