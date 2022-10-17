from django.urls import path

from object_vps.views import VPSDetailView, CreateVPSView

urlpatterns = [
    path("vps/<str:id>", VPSDetailView.as_view(), name='vps_detail'),
    path("create_vps/", CreateVPSView.as_view(), name='vps_create'),
]
