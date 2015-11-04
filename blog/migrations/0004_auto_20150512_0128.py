# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150512_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulacion',
            name='resolucion',
            field=models.CharField(max_length=200, verbose_name=b'resolucion'),
            preserve_default=True,
        ),
    ]
