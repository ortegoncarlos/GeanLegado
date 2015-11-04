# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150512_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='name_first_link',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='name_second_link',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='resumen_first_link',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='resumen_second_link',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='second_image',
        ),
    ]
