# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("promgen", "0001_squashed_0044_common-rules"),
    ]

    operations = [
        migrations.AddField(
            model_name="shard",
            name="enabled",
            field=models.BooleanField(
                default=True, help_text="Able to register new Services and Projects"
            ),
        ),
        migrations.AlterField(
            model_name="shard",
            name="proxy",
            field=models.BooleanField(
                default=False, help_text="Queries can be proxied to these shards"
            ),
        ),
    ]
