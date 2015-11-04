# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150531_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='directo',
            field=models.CharField(default=b'codigo hangout', max_length=100, verbose_name=b'Titulo'),
            preserve_default=True,
        ),
    ]
