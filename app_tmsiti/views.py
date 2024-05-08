# views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer, AnnouncementSerializer
from .models import News, Announcement
from .permissions import Permissions


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = Permissions


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = Permissions
