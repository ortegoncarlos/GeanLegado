# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150512_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(verbose_name=b'Categor\xc3\xada', to='blog.Careers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=False, verbose_name=b'Publicado'),
            preserve_default=True,
        ),
    ]
