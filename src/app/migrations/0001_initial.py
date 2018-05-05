# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('pg_type', models.CharField(max_length=5, choices=[('1*', '1*'), ('2*', '2*'), ('3*', '3*'), ('4*', '4*')])),
                ('no_of_person', models.CharField(default='One', max_length=5, choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')])),
                ('wifi', models.BooleanField(default=False)),
                ('loundry', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('maid', models.BooleanField(default=False)),
                ('arrival_date', models.DateField(default=django.utils.timezone.now)),
                ('departure_date', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(max_length=10)),
                ('sharing', models.CharField(max_length=20)),
                ('price', models.DecimalField(null=True, max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='CheckAvailibility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('pg_type', models.CharField(max_length=5, verbose_name='PG Type', choices=[('1*', '1*'), ('2*', '2*'), ('3*', '3*'), ('4*', '4*')])),
                ('available_from', models.DateField(default=django.utils.timezone.now)),
                ('available_to', models.DateField(default=django.utils.timezone.now)),
                ('no_of_person', models.CharField(default='One', max_length=5, choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')])),
                ('email', models.EmailField(max_length=254, null=True)),
                ('area', models.CharField(max_length=10, choices=[('vadaj', 'Vadaj'), ('ranip', 'Ranip'), ('cg road', 'CG Road'), ('naranpura', 'Naranpura'), ('navarangpura', 'Navarangpura')])),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('contact', models.BigIntegerField(default=0)),
                ('message', models.TextField(max_length=200, blank=True)),
                ('user', models.ForeignKey(to='app.Booking', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilitiesPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.BigIntegerField(default=0)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('pg_type', models.CharField(max_length=5, verbose_name='PG Type', choices=[('1*', '1*'), ('2*', '2*'), ('3*', '3*'), ('4*', '4*')])),
                ('description', models.TextField(max_length=200, blank=True)),
                ('price', models.DecimalField(null=True, max_digits=20, decimal_places=2)),
                ('sharing', models.CharField(max_length=20)),
                ('wifi', models.BooleanField(default=False)),
                ('loundry', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('maid', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to='product_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('pg_type', models.CharField(max_length=5, verbose_name='PG Type', choices=[('1*', '1*'), ('2*', '2*'), ('3*', '3*'), ('4*', '4*')])),
                ('comfort', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=20)),
                ('quality', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to='app.Booking', null=True)),
            ],
        ),
    ]
