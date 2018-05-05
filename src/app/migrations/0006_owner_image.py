# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180327_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='image',
            field=models.ImageField(upload_to='product_images', blank=True),
        ),
    ]
