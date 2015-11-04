# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0014_auto_20151101_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='qrcode',
            field=models.CharField(max_length=100, null=True, verbose_name=b'url del codigo QR', blank=True),
            preserve_default=True,
        ),
    ]
