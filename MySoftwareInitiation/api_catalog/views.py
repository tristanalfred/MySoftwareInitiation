from rest_framework.response import Response
from rest_framework import viewsets, status


class CheckApi(viewsets.ViewSet):
    """
    View returning 200 to check if an API works correctly
    """

    def list(self, _request):
        """
        Return a list of all users.
        """
        return Response(status=status.HTTP_200_OK)

