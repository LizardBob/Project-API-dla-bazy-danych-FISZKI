# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-13 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20180513_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApisSlowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'apis_slowa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id_dislike', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'dislikes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id_like', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'likes',
                'managed': False,
            },
        ),
    ]