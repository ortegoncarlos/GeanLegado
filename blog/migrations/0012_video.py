# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150531_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('resumen', models.CharField(max_length=100, verbose_name=b'Resumen')),
                ('youtube', models.CharField(max_length=30, verbose_name=b'video de youtube', blank=True)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publicado')),
                ('created', models.DateTimeField(verbose_name=b'Fecha del evento')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Modificado')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'video',
                'verbose_name_plural': 'Videos',
            },
            bases=(models.Model,),
        ),
    ]
