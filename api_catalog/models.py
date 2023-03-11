from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
