from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.call_records_app import utils


class CreateCallRecord(APITestCase):

    def test_create_callrecord(self):
        """
        Tests a POST call to the callrecord API V1
        """
        self.obj = utils.json_generator()
        response = self.client.post(reverse('v1_create_call'), self.obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_callrecord_with_null_fileds(self):
        """
        Tests a POST call to the callrecord API V1 using a json with null fields
        Should allow the creation in all cases except for
            - the case without call_id
            - the case without call_type
            - the case with no data
            - the case with no source and call_type = 1 (start)
        """

        self.obj_tstamp = utils.json_generator(timestamp=False)
        response = self.client.post(reverse('v1_create_call'), self.obj_tstamp)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.obj_dest = utils.json_generator(dest=False)
        response = self.client.post(reverse('v1_create_call'), self.obj_dest)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.obj_src = utils.json_generator(src=False)
        self.obj_src['call_type'] = 1
        response = self.client.post(reverse('v1_create_call'), self.obj_src)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.obj_ctype = utils.json_generator(calltype=False)
        response = self.client.post(reverse('v1_create_call'), self.obj_ctype)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.obj_cid = utils.json_generator(callid=False)
        response = self.client.post(reverse('v1_create_call'), self.obj_cid)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.obj_no_data = utils.json_generator(
            timestamp=False,
            calltype=False,
            callid=False,
            src=False,
            dest=False
        )
        response = self.client.post(reverse('v1_create_call'), self.obj_no_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
