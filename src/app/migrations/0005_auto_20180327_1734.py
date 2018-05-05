# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180327_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='pg_type',
            field=models.ForeignKey(to='app.Owner'),
        ),
    ]
