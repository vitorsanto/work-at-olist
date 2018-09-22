from django.test import TestCase
from model_mommy import mommy
from apps.call_records_app.models import CallRecord
from django.core.exceptions import ValidationError


class TestCallRecord(TestCase):

    def setUp(self):
        self.callrecord = mommy.make(CallRecord)

    """
    Tests the creation of a new call record
    """

    def test_callrecord_creation(self):
        self.assertTrue(isinstance(self.callrecord, CallRecord))
        self.assertTrue(self.callrecord.__str__(), self.callrecord.source)

    """
    Tests the source number type validation of a call record
    """

    def test_callrecord_type_validator(self):
        self.callrecord.source = 'a1_5T231+['
        self.assertRaises(ValidationError, self.callrecord.full_clean)

    """
    Tests the source number length validation of a call record
    """

    def test_callrecord_length_validator(self):
        self.callrecord.source = 123456789101112
        self.assertRaises(ValidationError, self.callrecord.full_clean)
