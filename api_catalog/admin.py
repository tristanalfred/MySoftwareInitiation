from django.contrib import admin
from api_catalog.models import Patient, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "get_service",)

    def get_service(self, obj):
        return obj.service.name


admin.site.register(Patient, PatientAdmin)
admin.site.register(Service, ServiceAdmin)
