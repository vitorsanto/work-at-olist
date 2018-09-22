from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CallDetailRecordsConfig(AppConfig):
    name = 'apps.call_records_app'
    verbose_name = _('call records app')
