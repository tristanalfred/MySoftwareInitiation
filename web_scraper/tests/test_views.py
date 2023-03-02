from django.http import QueryDict
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# class WebscraperViewsTests(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.client_admin = APIClient()
#         # cls.client_admin.login(username='admin', password='admin')
#
#     def test_retrieve_archetypes(self):
#         # url = reverse('archetypes?api') + "?api/"
#         query_dictionary = QueryDict('', mutable=True)
#         query_dictionary.update(
#             {
#                 'api': 'food'
#             }
#         )
#         url = f'{reverse("archetypes")}?{query_dictionary.urlencode()}'
#         # url = reverse("archetypes")
#
#         response = self.client_admin.get(url, format='json')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(1, 1)
