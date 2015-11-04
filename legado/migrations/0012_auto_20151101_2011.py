# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audiofield.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0011_ejercitomilitar_fuerzapublica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='audio_file',
            field=audiofield.fields.AudioField(help_text=b'Allowed type - .mp3, .wav, .ogg', upload_to=b'perfiles/audio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'perfiles/img'),
            preserve_default=True,
        ),
    ]
