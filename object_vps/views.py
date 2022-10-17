from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from object_vps.models import VPS
from object_vps.serializers import VPSSerializer, CreateVPSSerializer, UpdateVPSSerializer


class VPSDetailView(generics.RetrieveAPIView):
    """
    Получить VPS по uid (GET)
    """
    lookup_field = 'id'
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer


class CreateVPSView(generics.CreateAPIView):
    """
    Создать VPS (POST)
    """
    serializer_class = CreateVPSSerializer


class UpdateVPSView(generics.UpdateAPIView):
    """
    Перевести VPS в другой статус (UPDATE)
    """
    serializer_class = UpdateVPSSerializer
    queryset = VPS.objects.all()
    lookup_field = 'id'


class VPSListView(generics.ListAPIView):
    """
    Получить список VPS с возможностью фильтрации по параметрам (GET)
    """
    serializer_class = VPSSerializer
    queryset = VPS.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram']
