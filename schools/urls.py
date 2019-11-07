from django.urls import path, include
from .views import StudentViewSet, CourseViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
urlpatterns = router.urls