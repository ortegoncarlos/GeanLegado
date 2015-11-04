# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150531_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('evento', models.DateTimeField(verbose_name=b'Fecha del evento')),
            ],
            options={
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programacion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.CharField(max_length=200, verbose_name=b'Nombre del conferencista')),
                ('awards', models.CharField(max_length=200, verbose_name=b'Titulos biografia')),
            ],
            options={
                'verbose_name': 'Speakers',
                'verbose_name_plural': 'Speakerss',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='schedule',
            name='guests',
            field=models.ManyToManyField(to='blog.Speakers'),
            preserve_default=True,
        ),
    ]
