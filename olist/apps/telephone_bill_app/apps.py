from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TelephoneBillAppConfig(AppConfig):
    name = 'apps.telephone_bill_app'
    verbose_name = _('telephone bill app')
