from django.contrib import admin
from api_catalog.models import Patient, Service


class PatientAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)
admin.site.register(Service, ServiceAdmin)
