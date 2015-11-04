from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from django.conf import settings
from audiofield.fields import AudioField
import os.path
from  GranLegado.settings import STATIC_URL





class Perfil(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    fecha_nacimiento = models.DateField(max_length=100,verbose_name='Fecha de nacimiento')
    lugar_nacimiento = models.CharField(max_length=100,verbose_name='Lugar de Nacimiento')
    imagen = ProcessedImageField(upload_to='img/perfiles',processors=[ResizeToFill(400, 250)],format='JPEG',options={'quality': 100})
    profesion = models.CharField(max_length=100,verbose_name='Profesion')
    biografia = RichTextField(verbose_name='Biografia')
    origen_apellido = models.CharField(max_length=100,verbose_name='Origen del apellido')
    slug = models.SlugField()

    audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))


    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')

    def __unicode__(self):
        return self.nombre


class FotosPerfil(models.Model):
    imagen = ProcessedImageField(upload_to='img/perfiles/otras',processors=[ResizeToFill(427, 285)],format='JPEG',options={'quality': 100})
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion')
    perfil =  models.ForeignKey(Perfil)


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
        return STATIC_URL+str(self.imagen)

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
        return STATIC_URL+str(self.imagen)


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
        return STATIC_URL+str(self.imagen)


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