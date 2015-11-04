# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20150531_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='guests',
            field=models.ManyToManyField(to='blog.Speakers', blank=True),
            preserve_default=True,
        ),
    ]
