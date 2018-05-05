# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='image',
        ),
        migrations.AddField(
            model_name='owner',
            name='image',
            field=models.ManyToManyField(to='app.Photo'),
        ),
    ]
