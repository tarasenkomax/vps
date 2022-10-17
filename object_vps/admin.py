from django.contrib import admin
from object_vps.models import VPS


class VPSAdmin(admin.ModelAdmin):
    """ VPS """
    list_display = ("id", "cpu", "ram", "hdd", "status")
    list_display_links = ("id", "cpu", "ram", "hdd", "status")
    list_filter = ("status",)


admin.site.register(VPS, VPSAdmin)
