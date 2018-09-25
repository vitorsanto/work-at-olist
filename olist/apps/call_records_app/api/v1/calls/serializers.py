from django.utils.translation import ugettext as _
from rest_framework import serializers

from apps.call_records_app.models.CallRecord import CallRecord


class CallRecordSerializer(serializers.ModelSerializer):
    """
    Call record model serializer
    """

    class Meta:
        model = CallRecord
        exclude = (
            'compromised',
            'created_at',
            'processed_call',
            'reference_month',
            'reference_year'
        )

    def validate(self, data):
        if data['call_type'] == 1 and data['source'] in ["", " ", None]:
            raise serializers.ValidationError(
                _("A start call must have a source number.")
            )

        return data
