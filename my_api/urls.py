from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'university', UniversityViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'kafedras', KafedraViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
