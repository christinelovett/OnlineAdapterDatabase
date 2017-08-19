# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oadb', '0013_auto_20170819_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdapterKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universal_sequence', models.CharField(max_length=100)),
                ('index_sequence', models.CharField(max_length=100)),
                ('full_sequence', models.CharField(max_length=100)),
                ('index_type', models.CharField(choices=[('i5', 'i5'), ('i7', 'i7')], max_length=5)),
                ('barcode', models.CharField(default='', max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('kit', models.CharField(max_length=100)),
                ('subkit', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('kit', 'subkit', 'version', 'barcode'),
                'db_table': 'oadb_adapterkit',
                'managed': False,
            },
        ),
        migrations.RunSQL(
            '''
            DROP VIEW IF EXISTS "oadb_adapterkit";
            CREATE VIEW "oadb_adapterkit" AS SELECT
                a.id, a.barcode, a.index_type, a.index_sequence,
                a.universal_sequence, a.full_sequence,
                k.vendor, k.kit, k.subkit, k.version, k.status
            FROM oadb_adaptor a, oadb_kit k
            WHERE a.kit_id = k.id;
            '''
        ),
    ]