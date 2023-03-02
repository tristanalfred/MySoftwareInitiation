from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status


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
