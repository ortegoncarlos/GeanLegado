# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0017_perfil_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatoEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asunto', models.CharField(max_length=200, verbose_name=b'Asunto del correo')),
                ('cuerpo', models.TextField(verbose_name=b'Cuerpo del correo')),
            ],
            options={
                'verbose_name': 'Dato de Correo',
                'verbose_name_plural': 'Datos del Correo ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FloresRegalo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.FileField(upload_to=b'img/floresregalo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrasesRegalo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField(verbose_name=b'Texto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegaloEnvio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user_re', models.IntegerField(verbose_name=b'Usuario que Recibe')),
                ('id_perfil_re', models.IntegerField(verbose_name=b'Perfil que Recibe')),
                ('frase', models.TextField(null=True, verbose_name=b'Frase', blank=True)),
                ('imagen', models.FileField(upload_to=b'img/floresenvio')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de Regalo')),
                ('opacity', models.DecimalField(default=0.9, verbose_name=b'Opaca la Flor', max_digits=3, decimal_places=2)),
                ('dias', models.IntegerField(default=0, verbose_name=b'Dias de enviado')),
                ('id_user_en', models.IntegerField(verbose_name=b'Usuario que Envia')),
                ('user', models.CharField(max_length=100, verbose_name=b'Nombre del Usuario que Envia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100, verbose_name=b'Tipo de correo')),
            ],
            options={
                'verbose_name': 'Tipo de Correo',
                'verbose_name_plural': 'Tipos de Correo',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datoemail',
            name='tipo',
            field=models.ForeignKey(verbose_name=b'Tipo de correo', to='legado.TipoEmail'),
            preserve_default=True,
        ),
    ]
