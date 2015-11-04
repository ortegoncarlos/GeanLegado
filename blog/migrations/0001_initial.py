# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import paintstore.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'T\xc3\xadtulo')),
                ('message', models.CharField(max_length=100, verbose_name=b'Mensaje')),
                ('admission_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Perfil', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo')),
                ('homologations_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen de Homologaciones', blank=True)),
                ('homologations_body', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo de Homologaciones')),
                ('refunds_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen de Reintegros', blank=True)),
                ('refunds_body', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo de Reintegros')),
                ('name_first_link', models.CharField(max_length=100, verbose_name=b'Nombre del primer Link de Inter\xc3\xa9s')),
                ('resumen_first_link', models.CharField(max_length=200, verbose_name=b'Resumen del primer Link de Inter\xc3\xa9s')),
                ('name_second_link', models.CharField(max_length=100, verbose_name=b'Nombre del segundo Link de Inter\xc3\xa9s')),
                ('second_image', models.ImageField(upload_to=b'images', verbose_name=b'Imagen del segundo link de Inter\xc3\xa9s', blank=True)),
                ('resumen_second_link', models.CharField(max_length=200, verbose_name=b'Resumen del segundo Link de Inter\xc3\xa9s')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Admisi\xf3n',
                'verbose_name_plural': 'Admisiones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('color', paintstore.fields.ColorPickerField(default=b'#000000', max_length=7)),
                ('profile', models.TextField(verbose_name=b'Perfil')),
                ('profile_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Perfil')),
                ('objective', models.TextField(verbose_name=b'Objetivo de la Carrera')),
                ('objective_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Objetivo')),
                ('study_plan', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Plan de Estudios ')),
                ('why_careers', models.TextField(verbose_name=b'Raz\xc3\xb3n de Estudio')),
                ('why_careers_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen de la Raz\xc3\xb3n de Estudio')),
                ('dir_image', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Perfil')),
                ('dir_nombre', models.CharField(max_length=200, verbose_name=b'Nombre del director')),
                ('dir_telefono', models.CharField(max_length=200, verbose_name=b'Telfono del director')),
                ('dir_email', models.EmailField(max_length=200, verbose_name=b'Email del director')),
                ('dir_hours', models.CharField(max_length=200, verbose_name=b'Horario de atencion del director', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name=b'Slug', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categor\xeda',
                'verbose_name_plural': 'Categor\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Circles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Titulo', max_length=100, verbose_name=b'Titulo')),
                ('icono', models.CharField(default=b'fa', max_length=20, verbose_name=b'icono de awsomefont 1')),
                ('link', models.CharField(max_length=200, verbose_name=b'link de icono 1')),
                ('order', models.IntegerField(max_length=3, verbose_name=b'orden')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Circulo',
                'verbose_name_plural': 'Circulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('color', paintstore.fields.ColorPickerField(default=b'#000000', max_length=7)),
                ('text1', models.TextField(verbose_name=b'Perfil')),
                ('img1', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Perfil')),
                ('text2', models.TextField(verbose_name=b'Objetivo de la Carrera')),
                ('img2', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen del Objetivo')),
                ('text3', models.TextField(verbose_name=b'Raz\xc3\xb3n de Estudio')),
                ('img3', imagekit.models.fields.ProcessedImageField(upload_to=b'images', verbose_name=b'Imagen de la Raz\xc3\xb3n de Estudio')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Slug')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Titulo', max_length=100, verbose_name=b'Titulo de la imagen 1')),
                ('copy', models.CharField(default=b'Resumen', max_length=250, verbose_name=b'Copy de la imagen')),
                ('img', imagekit.models.fields.ProcessedImageField(upload_to=b'images')),
                ('link', models.CharField(default=b'#', max_length=200, verbose_name=b'Link del Rectangulo 1')),
                ('order', models.IntegerField(max_length=3, verbose_name=b'orden')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Link de interes',
                'verbose_name_plural': 'Links de interes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Titulo', max_length=100, verbose_name=b'Titulo')),
                ('hero', imagekit.models.fields.ProcessedImageField(upload_to=b'images')),
                ('copy', models.CharField(default=b'Resumen', max_length=250, verbose_name=b'Sub Titulo')),
                ('btn', models.CharField(default=b'boton', max_length=20, verbose_name=b'Titulo del Boton')),
                ('link_btn', models.CharField(default=b'#', max_length=200, verbose_name=b'Link del boton')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Unidad Heroe',
                'verbose_name_plural': 'Unidades Heroe',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('resumen', models.CharField(max_length=100, verbose_name=b'Resumen')),
                ('faculty', models.CharField(max_length=30, verbose_name=b'Facultad', choices=[(b'FA', b'Facultad de Artes'), (b'FC', b'Facultad de Ciencias Administrativas'), (b'FI', b'Facultad de Ingenier\xc3\xada'), (b'FH', b'Facultad de Humanidades')])),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to=b'images')),
                ('body', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Slug')),
                ('publish', models.BooleanField(default=True, verbose_name=b'Publicado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Modificado')),
                ('category', models.ForeignKey(verbose_name=b'Categor\xc3\xada', to='blog.Category')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Titulo', max_length=100, verbose_name=b'Titulo de la imagen 1')),
                ('img', imagekit.models.fields.ProcessedImageField(upload_to=b'images')),
                ('telephone', models.BigIntegerField(max_length=10, verbose_name=b'Telfono')),
                ('address', models.CharField(max_length=100, verbose_name=b'Direcci\xc3\xb3n')),
                ('latlang', models.CharField(max_length=100, verbose_name=b'Coordenadas')),
                ('order', models.IntegerField(max_length=3, verbose_name=b'orden')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'sedes',
                'verbose_name_plural': 'Direcotrio de sedes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Titulacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('diploma', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('snies', models.CharField(max_length=10, verbose_name=b'SNIES')),
                ('academic_credits', models.IntegerField(max_length=3, verbose_name=b'Cr\xc3\xa9ditos acad\xc3\xa9micos')),
                ('duracion', models.IntegerField(max_length=2, verbose_name=b'duracion en semestres')),
                ('credit_value', models.FloatField(verbose_name=b'Valor por cr\xc3\xa9dito')),
                ('tuition_value', models.FloatField(verbose_name=b'Valor de matr\xc3\xadcula')),
                ('resolucion', models.CharField(unique=True, max_length=200, verbose_name=b'resolucion')),
                ('Carrera', models.ForeignKey(to='blog.Careers')),
            ],
            options={
                'verbose_name': 'Titulacion',
                'verbose_name_plural': 'Titulaciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='careers',
            name='facultad',
            field=models.ForeignKey(to='blog.Facultad'),
            preserve_default=True,
        ),
    ]
