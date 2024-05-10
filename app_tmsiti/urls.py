from django.urls import path
from rest_framework import routers

from .views import NewsViewSet, AnnouncementViewSet, ManagementViewSet, StructuralDivisionViewSet, StandardViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'management', ManagementViewSet)
router.register(r'structural-division', StructuralDivisionViewSet)
router.register(r'standard', StandardViewSet)

urlpatterns = router.urls
