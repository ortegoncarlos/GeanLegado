# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150527_1908'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admission',
        ),
        migrations.RemoveField(
            model_name='careers',
            name='facultad',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='titulacion',
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Titulacion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='carrera',
        ),
        migrations.DeleteModel(
            name='Careers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='facultad',
        ),
        migrations.DeleteModel(
            name='Facultad',
        ),
    ]
