# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20150531_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'images', blank=True)),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria de imagenes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['evento'], 'verbose_name': 'Programacion', 'verbose_name_plural': 'Programacion'},
        ),
    ]
