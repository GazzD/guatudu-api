"""Users Urls"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from api.users.views import users as user_views
from api.users.views import roles as role_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'roles', role_views.RoleViewSet, basename='roles')

urlpatterns = router.urls
