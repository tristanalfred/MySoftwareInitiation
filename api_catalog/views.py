import csv
import io
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status

from api_catalog.models import Patient, Service


def homepage_view(request):
    """
    Homepage displaying the README file content
    """
    with open("./README.md") as f:
        content = f.readlines()

    context = {
        "readme": content
    }
    return render(request, "home.html", context)


class CheckApi(viewsets.ViewSet):
    """
    View returning 200 to check if an API works correctly
    """

    def list(self, _request):
        return Response(status=status.HTTP_200_OK)


def upload_patient_file_view(request):
    if request.method == 'POST' and request.FILES['patient_file']:
        patient_file = request.FILES['patient_file']

        # Read csv file InMemoryUploadedFile
        file = patient_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))

        for line in reader:
            if not Patient.objects.filter(first_name=line["first_name"], last_name=line["last_name"]):
                patient = Patient(first_name=line["first_name"], last_name=line["last_name"])
                patient.save()
            else:
                patient = Patient.objects.filter(first_name=line["first_name"], last_name=line["last_name"]).first()

            if not Service.objects.filter(name=line["service"]):
                service = Service(name=line["service"])
                service.save()
            else:
                service = Service.objects.filter(name=line["service"]).first()

            if patient.service != service:
                patient.service = service
                patient.save()

        return render(request, 'upload_patient_file.html', {
            'file_uploaded': True
        })
    return render(request, 'upload_patient_file.html')
