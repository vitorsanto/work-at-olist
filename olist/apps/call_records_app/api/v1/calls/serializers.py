from rest_framework import serializers

from apps.call_records_app import models


class CallRecordSerializer(serializers.ModelSerializer):
    """
    Call record model serializer
    """
    class Meta:
        model = models.CallRecord
        exclude = ('compromised', 'created_at')
