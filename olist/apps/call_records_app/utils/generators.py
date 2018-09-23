from django.utils import timezone
from random import randint, choice
import string


def json_generator(timestamp=True, calltype=True, callid=True, src=True, dest=True):
    """
    Generates a modularized random json
    :return:
        A random-generated json
    """

    if timestamp:
        r_year = randint(2000, 2018)
        r_month = randint(1, 12)
        r_day = randint(1, 28)

        r_hour = randint(0, 23)
        r_min = randint(0, 59)
        r_sec = randint(0, 59)

        r_datetime = timezone.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec).isoformat()
    else:
        r_datetime = None

    if calltype:
        r_call_type = randint(1, 2)
    else:
        r_call_type = None

    if callid:
        r_call_id = randint(1, 99999)
    else:
        r_call_id = None

    if src:
        r_source = random_numeric_generator(11)
    else:
        r_source = None

    if dest:
        r_destination = random_numeric_generator(11)
    else:
        r_destination = None

    return {
        "timestamp": r_datetime,
        "call_type": r_call_type,
        "call_id": r_call_id,
        "source": r_source,
        "destination": r_destination
    }


def random_alphanumeric_generator(length=11):
    """
    Generates a random alphanumeric string
    :return:
        A random-generated alphanumeric string
    """
    r_alphanumeric_string = ''.join(choice(string.printable) for _ in range(length))
    return r_alphanumeric_string


def random_numeric_generator(length=13):
    """
    Generates a random numeric
    :return:
        A random-generated numeric
    """
    r_numeric = int(''.join(choice(string.digits) for _ in range(length)))
    return r_numeric
