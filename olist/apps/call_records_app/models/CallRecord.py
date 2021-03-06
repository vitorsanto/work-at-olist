from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _
from apps.call_records_app import utils
from apps.call_records_app.models.choices import BOOLEAN_CHOICES, CALL_TYPE


class CallRecord(models.Model):
    """
    Call record model
    """

    timestamp = models.DateTimeField(
        verbose_name=_('call timestamp'),
        null=True, blank=True,
        help_text=_('The timestamp of when the event occurred')
    )

    call_type = models.PositiveSmallIntegerField(
        verbose_name=_('call type'), choices=CALL_TYPE,
        help_text=_('Indicate if it is a call start or end record.'),
    )

    call_id = models.PositiveIntegerField(
        verbose_name=_('call ID'),
        help_text=_('Unique ID for each call record pair.'),
    )

    source = models.CharField(
        max_length=20,
        verbose_name=_('origin phone number'),
        null=True, blank=True,
        validators=[utils.phone_number_validator],
        help_text=_('The subscriber phone number that originated the call.')
    )

    destination = models.CharField(
        max_length=20,
        verbose_name=_('destination phone number'),
        blank=True, null=True,
        help_text=_('The phone number receiving the call.')
    )

    compromised = models.BooleanField(
        default=False,
        verbose_name=_('compromised'),
        choices=BOOLEAN_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    reference_month = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('reference month')
    )
    reference_year = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('reference year')
    )

    processed_call = models.BooleanField(default=False, verbose_name=_('processed call'))

    def __str__(self):
        return _(
            'call_id: %(call_id)s, type: %(call_type)s, timestamp: %(timestamp)s.') % {
                   'call_id': self.call_id or '',
                   'call_type': self.call_type or '',
                   'timestamp': self.timestamp or ''}

    def save(self, *args, **kwargs):
        if self.call_type == 1:
            if self.destination in ['', ' ', None]:
                self.compromised = True

        if self.call_type == 2:
            if self.timestamp:
                self.reference_month = self.timestamp.month
                self.reference_year = self.timestamp.year
            else:
                now = datetime.now()
                self.reference_month = now.month
                self.reference_year = now.year

        if not self.timestamp:
            self.compromised = True

        super().save(*args, **kwargs)

    class Meta:
        app_label = 'call_records_app'
        ordering = ['timestamp', ]
        verbose_name_plural = _('call records')
        verbose_name = _('call record')
