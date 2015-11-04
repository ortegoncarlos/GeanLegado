#encoding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from sanjose_project.settings import FACULTY_CHOICES
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import *
from paintstore.fields import ColorPickerField
from django.template.defaultfilters import slugify

class Hero(models.Model):
    """
    Description: Aqui va to do lo que muestra el home
    """
    #Hero
    title = models.CharField(max_length=100,verbose_name='Titulo',default="Titulo")
    hero = ProcessedImageField(upload_to='images',processors=[ResizeToFill(2000, 1200)],format='JPEG',options={'quality': 30})
    copy = models.CharField(max_length=250,verbose_name='Sub Titulo',default="Resumen")
    btn = models.CharField(max_length=20,verbose_name='Titulo del Boton',default="boton")
    link_btn = models.CharField(max_length=200,verbose_name='Link del boton',default="#")
    created = models.DateTimeField(auto_now_add=True)
    directo = models.CharField(max_length=100,verbose_name='codigo hangout',blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='Unidad Heroe'
        verbose_name_plural='Home - Unidades Heroe'
 
class Circles(models.Model):
   #Circulos
    title = models.CharField(max_length=100,verbose_name='Titulo',default="Titulo")
    icono = models.CharField(max_length=20,verbose_name='icono de awsomefont 1',default="fa")
    link =models.CharField(max_length=200,verbose_name='link de icono 1')
    order =models.IntegerField(max_length=3,verbose_name='orden')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.icono
    class Meta:
        verbose_name='Circulo'
        verbose_name_plural='Home - Circulos'

class Featured(models.Model):
    #Rectangulos
    title = models.CharField(max_length=100,verbose_name='Titulo de la imagen 1',default="Titulo")
    copy = models.CharField(max_length=250,verbose_name='Copy de la imagen',default="Resumen")
    img = ProcessedImageField(upload_to='images',processors=[ResizeToFill(700, 400)],format='JPEG',options={'quality': 50}) 
    link = models.CharField(max_length=200,verbose_name='Link del Rectangulo 1',default="#")
    order =models.IntegerField(max_length=3,verbose_name='orden')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='Link de interes'
        verbose_name_plural='Links de interes'

#sedes

class Sedes(models.Model):
    """
    Description: url sedes directorio con mapa
    """
    title = models.CharField(max_length=100,verbose_name='Titulo de la imagen 1',default="Titulo")
    img = ProcessedImageField(upload_to='images',processors=[ResizeToFill(700, 400)],format='JPEG',options={'quality': 50}) 
    telephone = models.BigIntegerField(max_length=10,verbose_name='Telfono')
    address =  models.CharField(max_length=100,verbose_name='Dirección')
    latlang = models.CharField(max_length=100,verbose_name='Coordenadas')
    order =models.IntegerField(max_length=3,verbose_name='orden')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='sede'
        verbose_name_plural='Direcotrio de sedes'

class Speakers(models.Model):
    person = models.CharField(max_length=200,verbose_name='Nombre del conferencista')
    awards = models.CharField(max_length=200,verbose_name='Titulos biografia')

    class Meta:
        verbose_name = "Speakers"
        verbose_name_plural = "Speakerss"

    def __unicode__(self):
        return self.person
    
class Schedule(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    evento = models.DateTimeField(verbose_name='Fecha del evento')
    guests = models.ManyToManyField(Speakers, blank=True)    

    class Meta:
        verbose_name = "Programacion"
        verbose_name_plural = "Programacion"
        ordering = ['evento']


    def __unicode__(self):
        return self.title
    

class Slide(models.Model):
    title = models.CharField(max_length=100,verbose_name='Titulo')
    copy = models.CharField(max_length=200,verbose_name='Texto de apoyo')
    image = ProcessedImageField(upload_to='images',processors=[ResizeToFill(1900, 700)],format='JPEG',options={'quality': 50}) 
    boton = models.CharField(max_length=200,verbose_name='Link')
    orden = models.PositiveIntegerField(max_length=3,verbose_name='orden')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='Slide'
        verbose_name_plural='Slides'

class Video(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    resumen = models.CharField(max_length=100,verbose_name='Resumen')
    youtube = models.CharField(max_length=30,verbose_name='video de youtube',blank=True)
    publish = models.BooleanField(default=False,verbose_name='Publicado')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    evento = models.DateTimeField(verbose_name='Fecha del evento')
    modified = models.DateTimeField(auto_now=True,verbose_name='Modificado')
   
    def __unicode__(self): 
        return self.title 
    class Meta: 
        verbose_name = 'video'
        verbose_name_plural = 'Videos'
        ordering = ['-created']



class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    resumen = models.CharField(max_length=100,verbose_name='Resumen')
    imagen = ProcessedImageField(upload_to='images',blank=True,processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    youtube = models.CharField(max_length=30,verbose_name='video de youtube',blank=True)
    body = RichTextField(verbose_name='Cuerpo')
    slug = models.SlugField(max_length=50, unique=True,verbose_name='Slug')
    publish = models.BooleanField(default=False,verbose_name='Publicado')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    writer = models.ForeignKey(User)
    modified = models.DateTimeField(auto_now=True,verbose_name='Modificado')
   
    def __unicode__(self): 
        return self.title 
    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']


class newslettter(models.Model):
    """
    Description: Base de datos news letter
    """
    nombre = models.CharField(max_length=100,verbose_name='Título')
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField(max_length=1000,verbose_name='Mensaje')
    solucionado = models.BooleanField(default=False,blank=True,verbose_name='Se solucionó')
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Pregunta carrera'
        verbose_name_plural = 'Preguntas carreras'
        ordering = ['id']

class Galeria(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    imagen = ProcessedImageField(upload_to='images',processors=[ResizeToFit(1900, 900)],blank=True,format='JPEG',options={'quality': 50})
    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria de imagenes"

    def __unicode__(self):
        return self.title
     

import sys

from django.db.models.signals import post_syncdb
from django.contrib.sites.models import Site

from allauth.socialaccount.providers import registry
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.oauth.provider import OAuthProvider
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

def setup_dummy_social_apps(sender, **kwargs):
    """
    `allauth` needs tokens for OAuth based providers. So let's
    setup some dummy tokens
    """
    site = Site.objects.get_current()
    for provider in registry.get_list():
        if (isinstance(provider, OAuth2Provider)
            or isinstance(provider, OAuthProvider)):
            try:
                SocialApp.objects.get(provider=provider.id,
                                      sites=site)
            except SocialApp.DoesNotExist:
                print ("Installing dummy application credentials for %s."
                       " Authentication via this provider will not work"
                       " until you configure proper credentials via the"
                       " Django admin (`SocialApp` models)" % provider.id)
                app = SocialApp.objects.create(provider=provider.id,
                                               secret='secret',
                                               client_id='client-id',
                                               name='Dummy %s app' % provider.id)
                app.sites.add(site)


# We don't want to interfere with unittests et al
if 'syncdb' in sys.argv:
    post_syncdb.connect(setup_dummy_social_apps, sender=sys.modules[__name__])