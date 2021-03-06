# Generated by Django 2.1.1 on 2018-09-27 04:53

import apps.call_records_app.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_records_app', '0003_auto_20180925_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrecord',
            name='source',
            field=models.CharField(blank=True, help_text='The subscriber phone number that originated the call.', max_length=20, null=True, validators=[apps.call_records_app.utils.validators.phone_number_validator], verbose_name='origin phone number'),
        ),
    ]
