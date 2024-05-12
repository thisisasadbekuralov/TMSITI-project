# views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer, AnnouncementSerializer, ManagementSerializer, StructuralDivisionSerializer, StandardSerializer, ContactSerializer, ElectronicFundsSerializer, BuildingRegulationSerializer
from .models import News, Announcement, Management, StructuralDivision, Standard, Contact, ElectronicFunds, \
    BuildingRegulation
from .permissions import Permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view




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


@api_view(['POST'])
def get_user_info(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data['phone_number']
            email = serializer.data['email']
            name = serializer.data['name']
            contact = Contact.objects.create(phone_number=phone_number, email=email, name=name)
            return Response({'success': True})
        return Response({'success': False, 'error': serializer.errors})


class ElectronicFundsViewSet(ModelViewSet):
    queryset = ElectronicFunds.objects.all()
    serializer_class = ElectronicFundsSerializer
    permission_classes = [Permissions]


class BuildingRegulationViewSet(ModelViewSet):
    queryset = BuildingRegulation.objects.all()
    serializer_class = BuildingRegulationSerializer
    permission_classes = [Permissions]


