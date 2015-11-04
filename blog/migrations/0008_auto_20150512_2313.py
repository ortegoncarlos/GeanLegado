# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150512_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='careers',
            name='titulo_image',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to=b'images', verbose_name=b'Imagen del titulo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='careers',
            name='dir_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del director'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='careers',
            name='profile',
            field=models.TextField(verbose_name=b'Perfil del estudiante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='careers',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del titulo'),
            preserve_default=True,
        ),
    ]
