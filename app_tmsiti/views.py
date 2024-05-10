# views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer, AnnouncementSerializer, ManagementSerializer, StructuralDivisionSerializer, StandardSerializer
from .models import News, Announcement, Management, StructuralDivision, Standard
from .permissions import Permissions


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [Permissions]


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [Permissions]


class ManagementViewSet(ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    permission_classes = [Permissions]


class StructuralDivisionViewSet(ModelViewSet):
    queryset = StructuralDivision.objects.all()
    serializer_class = StructuralDivisionSerializer
    permission_classes = [Permissions]


class StandardViewSet(ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer
    permission_classes = [Permissions]


