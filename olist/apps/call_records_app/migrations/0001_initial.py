# Generated by Django 2.1.1 on 2018-09-22 19:48

from django.db import migrations, models

import apps.call_records_app.utils.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='call timestamp')),
                ('call_type',
                 models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Start'), (2, 'End')], null=True,
                                                  verbose_name='call type')),
                ('call_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='call ID')),
                ('source', models.CharField(max_length=20,
                                            validators=[apps.call_records_app.utils.validators.phone_number_validator],
                                            verbose_name='origin phone number')),
                ('destination',
                 models.CharField(blank=True, max_length=20, null=True, verbose_name='destination phone number')),
                ('compromised', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False,
                                                    verbose_name='compromised')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'call record',
                'verbose_name_plural': 'call records',
                'ordering': ['timestamp'],
            },
        ),
    ]
