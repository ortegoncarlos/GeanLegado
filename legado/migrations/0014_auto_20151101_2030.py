# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0013_auto_20151101_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'perfiles/img', blank=True),
            preserve_default=True,
        ),
    ]
