from django.urls import path

from object_vps.views import VPSDetailView, CreateVPSView, UpdateVPSView, VPSListView

urlpatterns = [
    path("vps/<str:id>", VPSDetailView.as_view(), name='vps_detail'),
    path("update_vps/<str:id>", UpdateVPSView.as_view(), name='vps_update'),
    path("create_vps/", CreateVPSView.as_view(), name='vps_create'),
    path("list_vps/", VPSListView.as_view(), name='vps_list'),
]
