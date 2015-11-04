# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0009_auto_20151028_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Angelitos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name=b'Resumen')),
                ('texto', ckeditor.fields.RichTextField(verbose_name=b'Texto')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/angelitos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name=b'Resumen')),
                ('texto', ckeditor.fields.RichTextField(verbose_name=b'Texto')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/familia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
