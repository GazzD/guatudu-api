"""Locations Urls"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from api.locations.views import countries as country_views
from api.locations.views import cities as city_views

router = DefaultRouter()
router.register(r'countries', country_views.CountryViewSet, basename='country')
router.register(r'cities', city_views.CityViewSet, basename='city')

urlpatterns = router.urls