# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_owner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='image',
        ),
    ]
