# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0003_preguntasfrecuentes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biografia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('texto', ckeditor.fields.RichTextField(verbose_name=b'Texto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='preguntasfrecuentes',
            name='respuesta',
            field=ckeditor.fields.RichTextField(verbose_name=b'Respuesta'),
            preserve_default=True,
        ),
    ]
