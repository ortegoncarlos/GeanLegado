# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_facultad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circles',
            options={'verbose_name': 'Circulo', 'verbose_name_plural': 'Home - Circulos'},
        ),
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name': 'Unidad Heroe', 'verbose_name_plural': 'Home - Unidades Heroe'},
        ),
        migrations.AlterModelOptions(
            name='sedes',
            options={'verbose_name': 'sede', 'verbose_name_plural': 'Direcotrio de sedes'},
        ),
        migrations.AlterModelOptions(
            name='titulacion',
            options={'verbose_name': 'Titulacion', 'verbose_name_plural': 'Carreras - Titulaciones'},
        ),
    ]
