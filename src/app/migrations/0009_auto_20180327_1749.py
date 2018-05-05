# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_owner_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='pg_type',
            new_name='photo',
        ),
    ]
