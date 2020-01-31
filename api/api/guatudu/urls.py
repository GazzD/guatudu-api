"""Guatudu Urls"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from api.guatudu.views.profiles import admins as admin_profile_views
from api.guatudu.views import business as business_views
from api.guatudu.views import events as event_views

router = DefaultRouter()
router.register(r'profiles/admin', admin_profile_views.AdminProfileViewSet, basename='profiles/admin')
router.register(r'business', business_views.BusinessViewSet, basename='business')
router.register(r'events', event_views.EventViewSet, basename='events')

urlpatterns = router.urls
