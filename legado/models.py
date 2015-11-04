from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from ckeditor.fields import RichTextField
from django.conf import settings
from audiofield.fields import AudioField
import os.path
from django.core import urlresolvers

class Perfil(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    fecha_nacimiento = models.DateField(max_length=100,verbose_name='Fecha de nacimiento',blank=True,null=True)
    lugar_nacimiento = models.CharField(max_length=100,verbose_name='Lugar de Nacimiento',blank=True,null=True)
    imagen = ProcessedImageField(upload_to='perfiles/img',processors=[ResizeToFit(1200, 500)],format='JPEG',options={'quality': 50}, blank=True,null=True)
    profesion = models.CharField(max_length=100,verbose_name='Profesion',blank=True,null=True)
    biografia = RichTextField(verbose_name='Biografia',blank=True,null=True)
    origen_apellido = models.CharField(max_length=100,verbose_name='Origen del apellido',blank=True,null=True)
    qrcode = models.CharField(max_length=100,verbose_name='url del codigo QR',blank=True,null=True)
    slug = models.SlugField()

    audio_file = AudioField(upload_to='perfiles/audio', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))


    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<audio controls="controls"><source src="%s" /></audio> <p>%s</p>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')
    
    def save(self, *args, **kwargs):
        import requests
        urldata = "http://159.203.132.60/perfil/"+str(self.slug)+"/"+str(self.pk)
        url = "http://api.qrcode.unitag.fr/api?t_pwd=degraded&setting={%22EYES%22:{%22EYE_TYPE%22:%22LLLeft%22,%22COLOR_EHD%22:%228a9935%22,%22COLOR_IHD%22:%228a9935%22,%22COLOR_EBG%22:%2271801f%22,%22COLOR_IBG%22:%2271801f%22},%22BODY_TYPE%22:2,%22LAYOUT%22:{%22COLORBG%22:%22ffffff%22,%22GRADIENT_TYPE%22:%22HORI%22,%22COLOR1%22:%22afc928%22,%22COLOR2%22:%22d7eb67%22,%22FORCE_SHADOW%22:%22L%22,%22COLOR_SHADOW%22:%22b6b8a7%22}}&data={%22DATA%22:{%22URL%22:%22"+urldata+"%22},%22TYPE%22:%22URL%22}"
        r = requests.get(url)
        response = requests.get(url)
        if response.status_code == 200:
            furl = os.path.join(settings.MEDIA_ROOT, 'img/'+str(self.slug)+"-"+str(self.pk)+'.jpeg')
            f = open( furl , 'wb')
            f.write(response.content)
            f.close()
            self.qrcode = settings.MEDIA_URL+'img/'+str(self.slug)+"-"+str(self.pk)+'.jpeg'
            super(Perfil, self).save(*args, **kwargs)
    
    def qr_tag(self):
        """audio player tag for admin"""
        if self.qrcode:
            file_url =  str(self.qrcode)
            url_string = '<img width="200px" src="'+file_url+'">'
            return url_string

    qr_tag.allow_tags = True
    qr_tag.short_description = ('Qr tag')
    
    def get_absolute_url(self):
        return urlresolvers.reverse('perfil', args=[self.slug,self.pk])
    def __unicode__(self):
        return self.nombre


class FotosPerfil(models.Model):
    imagen = ProcessedImageField(upload_to='img/perfiles/otras',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion')
    perfil =  models.ForeignKey(Perfil)
    def __unicode__(self):
        return self.descripcion

class FotosReconocimiento(models.Model):
    imagen = ProcessedImageField(upload_to='img/perfiles/reconocimiento',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion')
    perfil =  models.ForeignKey(Perfil)


class Servicio(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/servicios',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    resumen = RichTextField(verbose_name='Resumen')
    plan_amarillo = RichTextField(verbose_name='Plan Amarillo')
    plan_azul = RichTextField(verbose_name='Plan Azul')
    plan_rojo = RichTextField(verbose_name='Plan Rojo')

    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)

    def __unicode__(self):
        return self.nombre

class Homenajes(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/homenajes',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    resumen = RichTextField(verbose_name='Resumen')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')

    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)


class Somos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')
    parrafo_cuatro = RichTextField(verbose_name='Parrafo Cuatro')
    imagen = ProcessedImageField(upload_to='img/somos',processors=[ResizeToFill(1200, 551)],format='JPEG',options={'quality': 100})

class FuerzaMilitar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/fuerzamilitar',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    body = RichTextField(verbose_name='Cuerpo')


class Legajados(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen = RichTextField(verbose_name='Resumen')
    imagen = ProcessedImageField(upload_to='img/legajados',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)


class Funciona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')
    imagen = ProcessedImageField(upload_to='img/somos',processors=[ResizeToFill(1200, 551)],format='JPEG',options={'quality': 100})


class PreguntasFrecuentes(models.Model):
    pregunta = models.CharField(max_length=100, verbose_name='Pregunta')
    respuesta = RichTextField( verbose_name='Respuesta')

    def __unicode__(self):
        return self.pregunta

class Biografia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    texto = RichTextField(verbose_name='Texto')

    def __unicode__(self):
        return self.nombre

class BiografiaCronologica(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    texto = RichTextField(verbose_name='Texto')

    def __unicode__(self):
        return self.nombre

class BiografiaNarrativa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    texto = RichTextField(verbose_name='Texto')

    def __unicode__(self):
        return self.nombre

class Direccion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    calle = RichTextField(verbose_name='Calle')
    telefono = RichTextField(verbose_name='Telefono')
    movil = models.CharField(max_length=100, verbose_name='Movil')
    ubicacion = models.CharField(max_length=100, verbose_name='Ubicacion')

    def __unicode__(self):
        return self.nombre


class Matrimonio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre

class Quince(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre


class Graduacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre

class Angelitos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/angelitos',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre


class Familia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/familia',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre

class FuerzaPublica(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/fuerzapublica',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre

class EjercitoMilitar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/ejercitomilitar',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})

    def __unicode__(self):
        return self.nombre