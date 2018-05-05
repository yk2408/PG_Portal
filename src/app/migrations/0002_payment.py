# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ac_no', models.BigIntegerField(default=0, verbose_name='A/C No')),
                ('ini_balance', models.IntegerField(default=0, verbose_name='Initial Balance')),
                ('rem_balance', models.IntegerField(default=0, verbose_name='Remaining Balance')),
            ],
        ),
    ]
