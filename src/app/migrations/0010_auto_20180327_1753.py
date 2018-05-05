# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180327_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
