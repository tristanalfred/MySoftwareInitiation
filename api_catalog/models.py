from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name.capitalize()


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
