from django.utils import timezone
import random
import string


def json_generator():
    return {
        "timestamp": timezone.datetime.now().isoformat(),
        "call_type": 1,
        "call_id": 20,
        "source": "11999997598",
        "destination": "31995877485"
    }


def random_alphanumeric_generator(length=11):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))


def random_numeric_generator(length=13):
    return int(''.join(random.choice(string.digits) for _ in range(length)))
