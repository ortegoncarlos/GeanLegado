# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150512_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='newslettter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'T\xc3\xadtulo')),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('message', models.TextField(max_length=1000, verbose_name=b'Mensaje')),
                ('solucionado', models.BooleanField(default=False, verbose_name=b'Se solucion\xc3\xb3')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Pregunta carrera',
                'verbose_name_plural': 'Preguntas carreras',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='faculty',
        ),
        migrations.AddField(
            model_name='post',
            name='carrera',
            field=models.ForeignKey(default='1', verbose_name=b'Carrera', to='blog.Careers'),
            preserve_default=False,
        ),
    ]
