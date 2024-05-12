from django.urls import path
from rest_framework import routers

from .views import NewsViewSet, AnnouncementViewSet, ManagementViewSet, StructuralDivisionViewSet, StandardViewSet, get_user_info, ElectronicFundsViewSet, BuildingRegulationViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'management', ManagementViewSet)
router.register(r'structural-division', StructuralDivisionViewSet)
router.register(r'standard', StandardViewSet)
router.register(r'funds', ElectronicFundsViewSet)
router.register(r'building-regulation', BuildingRegulationViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('contact/', get_user_info, name='user_info'),
]
