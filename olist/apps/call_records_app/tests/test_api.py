from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.call_records_app import utils


class CreateRoomTest(APITestCase):

    def setUp(self):
        self.obj = utils.json_generator()

    def test_create_callrecord(self):
        """
        Tests a POST call to the callrecord API V1
        """
        response = self.client.post(reverse('v1_create_call'), self.obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)





