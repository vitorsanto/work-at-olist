from django.test import TestCase
from django.utils.timezone import datetime

from apps.telephone_bill_app import utils


class BillCalculator(TestCase):
    pass

    def test_calculations(self):
        """
        Tests the bill calculator
        """
        self.call_id_70_s = datetime(year=2016, month=2, day=29, hour=12)
        self.call_id_70_f = datetime(year=2016, month=2, day=29, hour=14)
        self.assertTrue(utils.billing_calculator(self.call_id_70_s, self.call_id_70_f), 11.16)

        self.call_id_71_s = datetime(year=2017, month=12, day=12, hour=15, minute=7, second=13)
        self.call_id_71_f = datetime(year=2017, month=12, day=12, hour=15, minute=14, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_71_s, self.call_id_71_f), 0.99)

        self.call_id_72_s = datetime(year=2017, month=12, day=12, hour=22, minute=47, second=56)
        self.call_id_72_f = datetime(year=2017, month=12, day=12, hour=22, minute=50, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_72_s, self.call_id_72_f), 0.36)

        self.call_id_73_s = datetime(year=2017, month=12, day=12, hour=21, minute=57, second=13)
        self.call_id_73_f = datetime(year=2017, month=12, day=12, hour=22, minute=10, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_73_s, self.call_id_73_f), 0.54)

        self.call_id_74_s = datetime(year=2017, month=12, day=12, hour=4, minute=57, second=13)
        self.call_id_74_f = datetime(year=2017, month=12, day=12, hour=6, minute=10, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_74_s, self.call_id_74_f), 1.26)

        self.call_id_75_s = datetime(year=2017, month=12, day=12, hour=21, minute=57, second=13)
        self.call_id_75_f = datetime(year=2017, month=12, day=13, hour=22, minute=10, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_75_s, self.call_id_75_f), 86.94)

        self.call_id_76_s = datetime(year=2017, month=12, day=12, hour=15, minute=7, second=58)
        self.call_id_76_f = datetime(year=2017, month=12, day=12, hour=15, minute=12, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_76_s, self.call_id_76_f), 11.52)

        self.call_id_77_s = datetime(year=2018, month=2, day=28, hour=21, minute=57, second=13)
        self.call_id_77_f = datetime(year=2018, month=3, day=1, hour=22, minute=10, second=56)
        self.assertTrue(utils.billing_calculator(self.call_id_77_s, self.call_id_77_f), 86.94)
