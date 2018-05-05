# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_owner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='image',
            field=models.ImageField(upload_to='product_images', blank=True),
        ),
    ]
