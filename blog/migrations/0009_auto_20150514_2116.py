# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20150512_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(default='', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='youtube',
            field=models.CharField(max_length=30, verbose_name=b'video de youtube', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='careers',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del perfil estudiante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='careers',
            name='why_careers',
            field=models.TextField(verbose_name=b'Perfil del egresado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='careers',
            name='why_careers_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Egresado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'images', blank=True),
            preserve_default=True,
        ),
    ]
