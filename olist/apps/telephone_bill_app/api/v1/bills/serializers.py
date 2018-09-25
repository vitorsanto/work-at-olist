from rest_framework import serializers

from apps.telephone_bill_app.models.TelephoneBill import TelephoneBill


class TelephoneBillSerializer(serializers.ModelSerializer):
    """
    Telephone bill serializer
    """
    start_date = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()

    class Meta:
        model = TelephoneBill
        fields = (
            'id',
            'destination',
            'start_date',
            'start_time',
            'call_duration',
            'call_cost',
        )

    def get_start_date(self, obj):
        return obj.started_at.date()

    def get_start_time(self, obj):
        return obj.started_at.time()
