# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duanzi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duanzi',
            name='num',
        ),
        migrations.AlterField(
            model_name='duanzi',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]
