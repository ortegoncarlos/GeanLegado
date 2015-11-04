# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0002_funciona'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasFrecuentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=100, verbose_name=b'Pregunta')),
                ('respuesta', models.CharField(max_length=100, verbose_name=b'Respuesta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
