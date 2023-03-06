import csv
import io
from django.shortcuts import render
from rest_framework.decorators import api_view
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


# Create your views here.
# @api_view(['GET'])
# def upload_patient_file_view(request):
#     return render(request, "upload_patient_file.html")

def upload_patient_file_view(request):
    if request.method == 'POST' and request.FILES['patient_file']:
        patient_file = request.FILES['patient_file']

        # Read csv file InMemoryUploadedFile
        file = patient_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))

        # Generate a list comprehension
        data = [line for line in reader]

        # for line in reader:
        #     if creat
        #
        #     print(line)



        return render(request, 'upload_patient_file.html', {
            'file_uploaded': True
        })
    return render(request, 'upload_patient_file.html')
