from collections import defaultdict

from django.db.models import Q

from apps.call_records_app.models.CallRecord import CallRecord
from apps.telephone_bill_app.models.TelephoneBill import TelephoneBill


def telephone_bill_creator(src_number, reference_month, reference_year):
    """
    Creates a telephone bill for a given source number and a reference time
    """

    # filters the calls that haven't been processed
    query = Q(processed_call=False)

    if reference_month:
        query &= Q(reference_month=reference_month)

    if reference_year:
        query &= Q(reference_year=reference_year)

    call_ids = CallRecord.objects.filter(query).values('call_id')

    call_records = CallRecord.objects \
                       .filter(call_id__in=call_ids) \
                       .filter(source=src_number) \
                       .filter(processed_call=False) | CallRecord.objects.filter(query)

    call_dict = defaultdict(list)

    # Creates a dict to group the call record tuples by its call ids
    for call_record in call_records:
        key = call_record.call_id
        call_dict[key].append(call_record)

    # for each tuple, create a telephone bill record
    for key in call_dict:
        create_telephone_bill(call_dict[key])


# Creates the telephone bill record
def create_telephone_bill(call_records):
    mark_as_processed = []
    telephone_bill = TelephoneBill()
    for call_record in call_records:
        if call_record.call_type == 1:
            telephone_bill.started_at = call_record.timestamp
            telephone_bill.source = call_record.source
            telephone_bill.destination = call_record.destination
            telephone_bill.call_id = call_record.call_id
        else:
            telephone_bill.finished_at = call_record.timestamp
        mark_as_processed.append(call_record.id)

    telephone_bill.save()

    # Marks the calls as processed
    CallRecord.objects.filter(pk__in=mark_as_processed).update(processed_call=True)