from django.db import models
from django.utils.timezone import datetime, timedelta
from django.utils.translation import ugettext_lazy as _

from apps.call_records_app import utils as cr_utils
from apps.call_records_app.models.choices import BOOLEAN_CHOICES
from apps.telephone_bill_app import utils as tb_utils


class TelephoneBill(models.Model):
    """
    Telephone bill model
    """

    started_at = models.DateTimeField(
        verbose_name=_('started at'),
        null=True, blank=True,
        help_text=_('The timestamp of when the call has started')
    )

    finished_at = models.DateTimeField(
        verbose_name=_('finished at'),
        null=True, blank=True,
        help_text=_('The timestamp of when the call has finished')
    )

    call_id = models.PositiveIntegerField(
        verbose_name=_('call ID'),
        null=True, blank=True,
        help_text=_('Unique ID for each call record pair.')
    )

    source = models.CharField(
        max_length=20,
        verbose_name=_('origin phone number'),
        validators=[cr_utils.phone_number_validator, ],
        help_text=_('The subscriber phone number that originated the call.')
    )

    destination = models.CharField(
        max_length=20,
        verbose_name=_('destination phone number'),
        blank=True, null=True,
        help_text=_('The phone number that received the call.')
    )

    compromised = models.BooleanField(
        default=False,
        verbose_name=_('compromised'),
        choices=BOOLEAN_CHOICES
    )

    call_duration = models.DurationField(
        null=True, blank=True,
        verbose_name=_("call duration")
    )

    call_cost = models.DecimalField(
        max_digits=10,
        default=0.00,
        decimal_places=2,
        verbose_name=_('call cost')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    processed_call = models.BooleanField(default=False, verbose_name=_('processed'))

    reference_month = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('reference month')
    )
    reference_year = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('reference year')
    )

    def __str__(self):
        return _(
            'call_id: %(call_id)s, cost: %(call_cost)s, duration: %(call_duration)s.') % {
                   'call_id': self.call_id or '',
                   'call_cost': self.call_cost or '',
                   'call_duration': self.call_duration or ''}

    def save(self, *args, **kwargs):
        if not self.started_at or not self.finished_at:
            self.compromised = True

        if self.started_at and self.finished_at:
            self.call_duration = self.finished_at - self.started_at
            self.reference_month = self.finished_at.month
            self.reference_year = self.finished_at.year
        else:
            self.call_duration = timedelta()
            today = datetime.now()
            self.reference_month = today.month
            self.reference_year = today.year

        self.call_cost = tb_utils.billing_calculator(self.started_at, self.finished_at)

        super().save(*args, **kwargs)

    class Meta:
        app_label = 'telephone_bill_app'
        ordering = ['-started_at', ]
        verbose_name_plural = _('telephone bills')
        verbose_name = _('telephone bill')
