from rest_framework import serializers
from django.utils.translation import ugettext as _
from apps.call_records_app.models.models import CallRecord


class CallRecordSerializer(serializers.ModelSerializer):
    """
    Call record model serializer
    """

    class Meta:
        model = CallRecord
        exclude = ('compromised', 'created_at')

    def validate(self, data):
        """
        Validates the fields necessary to maintain the consistency between the call tuples
        """

        if data['call_type'] in ["", " ", None]:
            """
            Evaluates the call type according to its fields.
            By doing this the application becomes more tolerant to inconsistency.
            """
            if data['source'] not in ["", " ", None]:
                data['call_type'] = 1
            else:
                data['call_type'] = 2

        if data['call_type'] == 1 and data['source'] in ["", " ", None]:
            raise serializers.ValidationError(_('Call start records must have a source number.'))

        if data['call_type'] == 2 and data['call_id'] in ["", " ", None]:
            raise serializers.ValidationError(_('Call end records must have a call id.'))

        return data
