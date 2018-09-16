from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.call_records_app import utils
from apps.call_records_app.choices import BOOLEAN_CHOICES, CALL_TYPE


class CallRecord(models.Model):
    """
    Call record model
    """

    timestamp = models.DateTimeField(verbose_name=_('call timestamp'), null=True, blank=True)
    call_type = models.PositiveSmallIntegerField(verbose_name=_('call type'), choices=CALL_TYPE, null=True, blank=True)
    call_id = models.PositiveIntegerField(verbose_name=_('call ID'), null=True, blank=True)

    source = models.CharField(max_length=20,
                              verbose_name=_('origin phone number'),
                              validators=[utils.phone_number_validator, ])

    destination = models.CharField(max_length=20,
                                   verbose_name=_('destination phone number'),
                                   blank=True, null=True)

    compromised = models.BooleanField(default=False, verbose_name=_('compromised'),
                                      choices=BOOLEAN_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return str(self.source)

    def save(self, *args, **kwargs):
        if not self.call_id or self.destination or self.timestamp:
            self.compromised = True
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'call_records_app'
        ordering = ['timestamp', ]
        verbose_name_plural = _('call records')
        verbose_name = _('call record')
