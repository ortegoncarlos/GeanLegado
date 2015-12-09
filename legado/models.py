from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from ckeditor.fields import RichTextField
from django.conf import settings
from audiofield.fields import AudioField
from django.template.defaultfilters import slugify
import os.path
from django.core import urlresolvers

class Perfil(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    usuario = models.ForeignKey(User)
    fecha_nacimiento = models.DateField(max_length=100,verbose_name='Fecha de nacimiento',blank=True,null=True)
    lugar_nacimiento = models.CharField(max_length=100,verbose_name='Lugar de Nacimiento',blank=True,null=True)
    imagen = ProcessedImageField(upload_to='perfiles/img',processors=[ResizeToFit(1200, 500)],format='JPEG',options={'quality': 50}, blank=True,null=True)
    profesion = models.CharField(max_length=100,verbose_name='Profesion',blank=True,null=True)
    biografia = RichTextField(verbose_name='Biografia',blank=True,null=True)
    origen_apellido = models.CharField(max_length=100,verbose_name='Origen del apellido',blank=True,null=True)
    qrcode = models.CharField(max_length=100,verbose_name='url del codigo QR',blank=True,null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    listo = models.BooleanField(default=True, verbose_name="Listo")
    publico = models.BooleanField(default=False, verbose_name="Publico")

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
        self.slug = slugify(str(self.nombre)+"-"+str(self.fecha_nacimiento))
        super(Perfil, self).save(*args, **kwargs)

        import requests
        urldata = "http://159.203.132.60/perfil/"+str(self.slug)
        url = "http://api.qrcode.unitag.fr/api?t_pwd=degraded&setting={%22EYES%22:{%22EYE_TYPE%22:%22LLLeft%22,%22COLOR_EHD%22:%228a9935%22,%22COLOR_IHD%22:%228a9935%22,%22COLOR_EBG%22:%2271801f%22,%22COLOR_IBG%22:%2271801f%22},%22BODY_TYPE%22:2,%22LAYOUT%22:{%22COLORBG%22:%22ffffff%22,%22GRADIENT_TYPE%22:%22HORI%22,%22COLOR1%22:%22afc928%22,%22COLOR2%22:%22d7eb67%22,%22FORCE_SHADOW%22:%22L%22,%22COLOR_SHADOW%22:%22b6b8a7%22}}&data={%22DATA%22:{%22URL%22:%22"+urldata+"%22},%22TYPE%22:%22URL%22}"
        r = requests.get(url)
        response = requests.get(url)
        if response.status_code == 200:
            furl = os.path.join(settings.MEDIA_ROOT, 'img/'+str(self.slug)+'.jpeg')
            f = open( furl , 'wb')
            f.write(response.content)
            f.close()
            self.qrcode = settings.MEDIA_URL+'img/'+str(self.slug)+'.jpeg'
            super(Perfil, self).save(*args, **kwargs)
    
    def qr_tag(self):
        """qr tag for admin"""
        if self.qrcode:
            file_url =  str(self.qrcode)
            url_string = '<img width="200px" src="'+file_url+'">'
            return url_string

    qr_tag.allow_tags = True
    qr_tag.short_description = ('Qr tag')
 
    def foto_perfil(self):
        if self.imagen:
            file_url =  settings.MEDIA_URL+str(self.imagen)
            url_string = '<img width="200px" src="'+file_url+'">'
            return url_string

    foto_perfil.allow_tags = True
    foto_perfil.short_description = ('Foto')

    def get_absolute_url(self):
        return urlresolvers.reverse('perfil', args=[self.slug,self.pk])
    def __unicode__(self):
        return str(self.nombre)


class FotosPerfil(models.Model):
    imagen = ProcessedImageField(upload_to='img/perfiles/otras',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion',blank=True,null=True)
    perfil =  models.ForeignKey(Perfil)
    def __unicode__(self):
        return self.descripcion

class FotosReconocimiento(models.Model):
    imagen = ProcessedImageField(upload_to='img/perfiles/reconocimiento',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion')
    perfil =  models.ForeignKey(Perfil)


class Servicio(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/servicios',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})
    resumen = RichTextField(verbose_name='Resumen')
    plan_amarillo = RichTextField(verbose_name='Plan Amarillo')
    plan_azul = RichTextField(verbose_name='Plan Azul')
    plan_rojo = RichTextField(verbose_name='Plan Rojo')
    """Los planes debe ser un Many to many a un Planes"""
    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)

    def __unicode__(self):
        return self.nombre

class Homenajes(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/homenajes',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})
    resumen = RichTextField(verbose_name='Resumen')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')
    """Los PARRAFOS debe ser un Many to many a un MODEL"""
    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)


class Somos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')
    parrafo_cuatro = RichTextField(verbose_name='Parrafo Cuatro')
    """Los PARRAFOS debe ser un Many to many a un MODEL"""
    imagen = ProcessedImageField(upload_to='img/somos',processors=[ResizeToFit(1200, 551)],format='JPEG',options={'quality': 60})

class FuerzaMilitar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = ProcessedImageField(upload_to='img/fuerzamilitar',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})
    body = RichTextField(verbose_name='Cuerpo')


class Legajados(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen = RichTextField(verbose_name='Resumen')
    imagen = ProcessedImageField(upload_to='img/legajados',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def miimagen(self):
        return settings.STATIC_URL+str(self.imagen)


class Funciona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    parrafo_uno = RichTextField(verbose_name='Parrafo Primero')
    parrafo_dos = RichTextField(verbose_name='Parrafo Segundo')
    parrafo_tres = RichTextField(verbose_name='Parrafo Tercero')
    """Los PARRAFOS debe ser un Many to many a un MODEL"""
    imagen = ProcessedImageField(upload_to='img/somos',processors=[ResizeToFit(1200, 551)],format='JPEG',options={'quality': 60})


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
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre

class Quince(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre


class Graduacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/matrimonio',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre

class Angelitos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/angelitos',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre


class Familia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/familia',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre

class FuerzaPublica(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/fuerzapublica',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre

class EjercitoMilitar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    resumen =RichTextField(verbose_name='Resumen')
    texto = RichTextField(verbose_name='Texto')
    imagen = ProcessedImageField(upload_to='img/ejercitomilitar',processors=[ResizeToFit(427, 285)],format='JPEG',options={'quality': 60})

    def __unicode__(self):
        return self.nombre
        
class FloresRegalo(models.Model):
    imagen = models.FileField(upload_to='img/floresregalo')

class FrasesRegalo(models.Model):
    texto = models.TextField(verbose_name='Texto')


class RegaloEnvio(models.Model):
    id_user_re = models.IntegerField(verbose_name='Usuario que Recibe')
    id_perfil_re = models.IntegerField(verbose_name='Perfil que Recibe')
    frase = models.TextField(verbose_name='Frase',null=True,blank=True)
    imagen = models.FileField(upload_to='img/floresenvio')
    date = models.DateTimeField(verbose_name="Fecha de Regalo",auto_now_add=True)
    opacity = models.DecimalField(verbose_name="Opaca la Flor",default=0.9,max_digits=3,decimal_places=2)
    dias = models.IntegerField(verbose_name="Dias de enviado",default=0)
    id_user_en = models.IntegerField(verbose_name='Usuario que Envia')
    user = models.CharField(max_length=100, verbose_name='Nombre del Usuario que Envia')

class TipoEmail(models.Model):
    tipo = models.CharField(verbose_name='Tipo de correo',max_length=100)

    class Meta:
        verbose_name = 'Tipo de Correo'
        verbose_name_plural='Tipos de Correo'
    def __unicode__(self):
        return self.tipo


class DatoEmail(models.Model):
    asunto = models.CharField(verbose_name='Asunto del correo',max_length=200)
    cuerpo = models.TextField(verbose_name='Cuerpo del correo')
    tipo = models.ForeignKey(TipoEmail,verbose_name='Tipo de correo')

    class Meta:
        verbose_name = 'Dato de Correo'
        verbose_name_plural='Datos del Correo '
    def __unicode__(self):
        return self.asunto