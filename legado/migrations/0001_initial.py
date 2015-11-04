# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import audiofield.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FotosPerfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/perfiles/otras')),
                ('descripcion', models.CharField(max_length=100, verbose_name=b'Descripcion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FotosReconocimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/perfiles/reconocimiento')),
                ('descripcion', models.CharField(max_length=100, verbose_name=b'Descripcion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuerzaMilitar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/fuerzamilitar')),
                ('body', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Homenajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/homenajes')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name=b'Resumen')),
                ('parrafo_uno', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Primero')),
                ('parrafo_dos', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Segundo')),
                ('parrafo_tres', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Tercero')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legajados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name=b'Resumen')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/legajados')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('fecha_nacimiento', models.DateField(max_length=100, verbose_name=b'Fecha de nacimiento')),
                ('lugar_nacimiento', models.CharField(max_length=100, verbose_name=b'Lugar de Nacimiento')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/perfiles')),
                ('profesion', models.CharField(max_length=100, verbose_name=b'Profesion')),
                ('biografia', ckeditor.fields.RichTextField(verbose_name=b'Biografia')),
                ('origen_apellido', models.CharField(max_length=100, verbose_name=b'Origen del apellido')),
                ('slug', models.SlugField()),
                ('audio_file', audiofield.fields.AudioField(help_text=b'Allowed type - .mp3, .wav, .ogg', upload_to=b'your/upload/dir', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/servicios')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name=b'Resumen')),
                ('plan_amarillo', ckeditor.fields.RichTextField(verbose_name=b'Plan Amarillo')),
                ('plan_azul', ckeditor.fields.RichTextField(verbose_name=b'Plan Azul')),
                ('plan_rojo', ckeditor.fields.RichTextField(verbose_name=b'Plan Rojo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Somos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('parrafo_uno', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Primero')),
                ('parrafo_dos', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Segundo')),
                ('parrafo_tres', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Tercero')),
                ('parrafo_cuatro', ckeditor.fields.RichTextField(verbose_name=b'Parrafo Cuatro')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'img/somos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fotosreconocimiento',
            name='perfil',
            field=models.ForeignKey(to='legado.Perfil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fotosperfil',
            name='perfil',
            field=models.ForeignKey(to='legado.Perfil'),
            preserve_default=True,
        ),
    ]
