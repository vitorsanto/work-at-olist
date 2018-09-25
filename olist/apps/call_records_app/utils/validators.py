from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def phone_number_validator(value):
    """
    Validator for phone number
    """
    if not value.isnumeric():
        raise ValidationError(_('Phone number must have only numeric digits.'), code='is not a phone number')
    elif not len(value) in [10, 11]:
        raise ValidationError(_('Phone number must have 10 or 11 digits.'), code='invalid phone number')
