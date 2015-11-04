# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='facultad',
            field=models.ForeignKey(default='1', verbose_name=b'Facultad', to='blog.Facultad'),
            preserve_default=False,
        ),
    ]
