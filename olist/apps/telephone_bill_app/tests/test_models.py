from django.core.exceptions import ValidationError
from django.test import TestCase
from model_mommy import mommy

from apps.call_records_app import utils
from apps.telephone_bill_app.models import TelephoneBill


class TestTelephoneBill(TestCase):

    def test_callrecord_creation(self):
        """
        Tests the creation of a new Telephone bill record
        """
        self.bill = mommy.make(TelephoneBill)
        self.assertTrue(isinstance(self.bill, TelephoneBill))

        expected_output = 'call_id: %(call_id)s, cost: %(call_cost)s, duration: %(call_duration)s.' % {
            'call_id': self.bill.call_id or '',
            'call_cost': self.bill.call_cost or '',
            'call_duration': self.bill.call_duration or ''}

        self.assertEquals(self.bill.__str__(), expected_output)

    def test_bill_type_validator(self):
        """
        Tests the source number type validation of a call record
        """

        number = utils.random_alphanumeric_generator(11)
        self.bill_type = mommy.make(TelephoneBill, source=number)
        with self.assertRaises(ValidationError) as cm:
            self.bill_type.full_clean()
        e = cm.exception
        self.assertTrue('source' in e.message_dict.keys())
        self.assertTrue('Phone number must have only numeric digits.' in e.messages)

    def test_bill_length_validator(self):
        """
        Tests the source number length validation of a call record
        """
        number = utils.random_numeric_generator(15)
        self.bill_len = mommy.make(TelephoneBill, source=number)
        with self.assertRaises(ValidationError) as cm:
            self.bill_len.full_clean()
        e = cm.exception
        self.assertTrue('source' in e.message_dict.keys())
        self.assertTrue('Phone number must have 10 or 11 digits.' in e.messages)

    def test_bill_compromised_flag(self):
        """
        Tests the compromised validation of a bill record
        *Registers are considered 'compromised' in these cases:
            - don't have a finished_at datetime
            - don't have a started_at datetime
        """

        self.bill_1 = mommy.make(TelephoneBill, started_at=None)
        self.assertTrue(self.callrecord_2.compromised)

        self.bill_1 = mommy.make(TelephoneBill, finished_at=None)
        self.assertTrue(self.callrecord_3.compromised)
