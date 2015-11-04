# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150514_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titulo')),
                ('copy', models.CharField(max_length=200, verbose_name=b'Texto de apoyo')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'images')),
                ('boton', models.CharField(max_length=200, verbose_name=b'Link')),
                ('orden', models.PositiveIntegerField(max_length=3, verbose_name=b'orden')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
