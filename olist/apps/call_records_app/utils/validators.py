from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re


def phone_number_validator(number):
    """
    Validator for phone number
    """
    number = re.sub("[^0-9]", "", number)
    if not number.isnumeric():
        raise ValidationError(_("Phone number must have only numeric characters."))
    elif not len(number) in [10, 11]:
        raise ValidationError(_("Phone number must have 10 or 11 characters."))

    return number
