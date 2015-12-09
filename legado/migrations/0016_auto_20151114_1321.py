# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0015_perfil_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='listo',
            field=models.BooleanField(default=True, verbose_name=b'Listo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='publico',
            field=models.BooleanField(default=False, verbose_name=b'Publico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 14, 18, 21, 46, 997261, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fotosperfil',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Descripcion', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
