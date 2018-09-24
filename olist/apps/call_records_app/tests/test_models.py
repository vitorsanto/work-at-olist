from django.test import TestCase
from model_mommy import mommy
from apps.call_records_app.models.models import CallRecord
from django.core.exceptions import ValidationError
from apps.call_records_app import utils


class TestCallRecord(TestCase):

    def test_callrecord_creation(self):
        """
        Tests the creation of a new call record
        """
        self.callrecord = mommy.make(CallRecord)
        self.assertTrue(isinstance(self.callrecord, CallRecord))

        expected_output = \
            'call_id: %(call_id)s, type: %(call_type)s, timestamp: %(timestamp)s.' % {
                'call_id': self.callrecord.call_id or '',
                'call_type': self.callrecord.call_id or '',
                'timestamp': self.callrecord.call_id or ''}

        self.assertEquals(self.callrecord.__str__(), expected_output)

    def test_callrecord_type_validator(self):
        """
        Tests the source number type validation of a call record
        """

        number = utils.random_alphanumeric_generator(11)
        print(number)
        self.callrecord_type = mommy.make(CallRecord, source=number)
        with self.assertRaises(ValidationError) as cm:
            self.callrecord_type.full_clean()
        e = cm.exception
        self.assertTrue('source' in e.message_dict.keys())
        self.assertTrue('Phone number must have only numeric digits.' in e.messages)

    def test_callrecord_length_validator(self):
        """
        Tests the source number length validation of a call record
        """
        number = utils.random_numeric_generator(13)
        print(number)
        self.callrecord_len = mommy.make(CallRecord, source=number)
        with self.assertRaises(ValidationError) as cm:
            self.callrecord_len.full_clean()
        e = cm.exception
        self.assertTrue('source' in e.message_dict.keys())
        self.assertTrue('Phone number must have 10 or 11 digits.' in e.messages)

    def test_callrecord_compromised_flag(self):
        """
        Tests the compromised validation of a call record
        *Registers are considered 'compromised' in these cases:
            - don't have a call_id
            - don't have a destination number
            - don't have a timestamp
        """
        self.callrecord_1 = mommy.make(CallRecord, call_id=None)
        self.assertTrue(self.callrecord_1.compromised)

        self.callrecord_2 = mommy.make(CallRecord, destination=None)
        self.assertTrue(self.callrecord_2.compromised)

        self.callrecord_3 = mommy.make(CallRecord, timestamp=None)
        self.assertTrue(self.callrecord_3.compromised)
