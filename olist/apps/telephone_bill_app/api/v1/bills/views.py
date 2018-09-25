from datetime import datetime

from django.db.models import Q
from rest_framework import generics

from apps.telephone_bill_app import utils
from apps.telephone_bill_app.api.v1.bills.serializers import TelephoneBillSerializer
from apps.telephone_bill_app.models.TelephoneBill import TelephoneBill


class GetTelephoneBillListView(generics.ListAPIView):
    """
    get:
     Returns a telephone bill of a given number at a give reference period.
     - To pass a reference month and a reference year, user this pattern: month={month}&year={year}
    """
    queryset = TelephoneBill.objects.all()
    serializer_class = TelephoneBillSerializer

    def get_queryset(self):
        source_number = self.kwargs['source_number']

        params = self.request.query_params
        today = datetime.now()

        month = params.get('month', u"-")
        month = month if month.isnumeric() else today.month

        year = params.get('year', u"-")
        year = year if year.isnumeric() else today.year

        utils.telephone_bill_creator(source_number, month, year)

        query = Q(source=source_number)
        query &= Q(reference_month=month)
        query &= Q(reference_year=year)

        queryset = TelephoneBill.objects.filter(query)
        return queryset
