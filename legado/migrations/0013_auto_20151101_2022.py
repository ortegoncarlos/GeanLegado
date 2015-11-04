# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0012_auto_20151101_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='biografia',
            field=ckeditor.fields.RichTextField(null=True, verbose_name=b'Biografia', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(max_length=100, null=True, verbose_name=b'Fecha de nacimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='lugar_nacimiento',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Lugar de Nacimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='origen_apellido',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Origen del apellido', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='profesion',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Profesion', blank=True),
            preserve_default=True,
        ),
    ]
