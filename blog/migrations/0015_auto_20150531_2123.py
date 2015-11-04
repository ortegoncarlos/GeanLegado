# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_hero_directo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='directo',
            field=models.CharField(max_length=100, verbose_name=b'codigo hangout', blank=True),
            preserve_default=True,
        ),
    ]
