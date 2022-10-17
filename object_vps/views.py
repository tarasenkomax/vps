from rest_framework import generics

from object_vps.models import VPS
from object_vps.serializers import VPSSerializer, CreateVPSSerializer


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
