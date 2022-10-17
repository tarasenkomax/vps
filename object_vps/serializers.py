from rest_framework import serializers

from object_vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ["id", "cpu", "ram", "hdd", "status"]


class CreateVPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ["cpu", "ram", "hdd"]


class UpdateVPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ["status"]