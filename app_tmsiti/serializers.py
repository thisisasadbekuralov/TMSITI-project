from .models import News, Announcement, Management, StructuralDivision, Standard, ElectronicFunds, BuildingRegulation

from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        write_only_fields = ('created_at', 'updated_at')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class StructuralDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructuralDivision
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ContactSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=50)


class ElectronicFundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicFunds
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class BuildingRegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingRegulation
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

