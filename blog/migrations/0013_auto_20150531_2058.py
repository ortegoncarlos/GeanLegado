# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='evento',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 31, 20, 58, 45, 299187, tzinfo=utc), verbose_name=b'Fecha del evento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Creado'),
            preserve_default=True,
        ),
    ]
