# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funciona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('parrafo_uno', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Primero')),
                ('parrafo_dos', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Segundo')),
                ('parrafo_tres', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Tercero')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/somos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
