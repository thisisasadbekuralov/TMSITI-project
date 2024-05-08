from django.urls import path
from rest_framework import routers

from .views import NewsViewSet, AnnouncementViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = router.urls
