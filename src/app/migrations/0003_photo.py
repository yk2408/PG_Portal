# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='product_images', blank=True)),
                ('pg_type', models.CharField(max_length=5, verbose_name='PG Type', choices=[('1*', '1*'), ('2*', '2*'), ('3*', '3*'), ('4*', '4*')])),
            ],
        ),
    ]
