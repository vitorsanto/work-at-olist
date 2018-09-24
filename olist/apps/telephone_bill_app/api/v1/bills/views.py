from rest_framework import generics
from apps.call_records_app.models.models import CallRecord
from apps.call_records_app.api.v1.calls.serializers import CallRecordSerializer


class GetTelephoneBillView(generics.RetrieveAPIView):
    """
    get:
     Returns a telephone bill of a given number at a give reference period.
    """
    serializer_class = CallRecordSerializer
    queryset = CallRecord.objects.all()

