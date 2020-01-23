"""Sliders Urls"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from api.sliders.views import sliders as slider_views
from api.sliders.views import slider_images as slider_images_views

router = DefaultRouter()
router.register(r'sliders', slider_views.SliderViewSet, basename='sliders')
router.register(r'slider/images', slider_images_views.SliderImageViewSet, basename='slider/images')

urlpatterns = router.urls