# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0006_biografianarrativa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('calle', ckeditor.fields.RichTextField(verbose_name=b'Calle')),
                ('telefono', ckeditor.fields.RichTextField(verbose_name=b'Telefono')),
                ('movil', models.CharField(max_length=100, verbose_name=b'Movil')),
                ('ubicacion', models.CharField(max_length=100, verbose_name=b'Ubicacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
