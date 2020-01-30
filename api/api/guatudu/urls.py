"""Guatudu Urls"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from api.guatudu.views.profiles import admins as admin_profile_views

router = DefaultRouter()
router.register(r'profiles/admin', admin_profile_views.AdminProfileViewSet, basename='profiles/admin')

urlpatterns = router.urls
