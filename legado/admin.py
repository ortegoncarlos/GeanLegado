from django.contrib import admin
from legado.models import *
from django import forms


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','resumen','mostrarimagen')
    list_editable = ('nombre', 'resumen',)
    def mostrarimagen(self,obj):
        url = obj.miimagen()
        tag = '<img src="%s">'%url
        return tag
    mostrarimagen.allow_tags = True


class HomenajesAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','resumen','mostrarimagen')
    list_editable = ('nombre', 'resumen',)
    def mostrarimagen(self,obj):
        url = obj.miimagen()
        tag = '<img src="%s">'%url
        return tag
    mostrarimagen.allow_tags = True


class LegajadosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','resumen','mostrarimagen')
    list_editable = ('nombre', 'resumen',)
    def mostrarimagen(self,obj):
        url = obj.miimagen()
        tag = '<img src="%s">'%url
        return tag
    mostrarimagen.allow_tags = True


class AdminPerfil(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['nombre'] }

from legado.models import Perfil

# add 'audio_file_player' tag to your admin view
list_display = ( 'audio_file_player')
actions = ['custom_delete_selected']

def custom_delete_selected(self, request, queryset):
    #custom delete code
    n = queryset.count()
    for i in queryset:
        if i.audio_file:
            if os.path.exists(i.audio_file.path):
                os.remove(i.audio_file.path)
        i.delete()
    self.message_user(request, ("Successfully deleted %d audio files.") % n)
custom_delete_selected.short_description = "Delete selected items"



admin.site.register(Perfil, AdminPerfil)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Homenajes, HomenajesAdmin)
admin.site.register(Somos)
admin.site.register(FotosPerfil)
admin.site.register(FuerzaMilitar)
admin.site.register(FotosReconocimiento)
admin.site.register(Legajados,LegajadosAdmin)
admin.site.register(Funciona)
admin.site.register(PreguntasFrecuentes)
admin.site.register(Biografia)
admin.site.register(BiografiaCronologica)
admin.site.register(BiografiaNarrativa)
admin.site.register(Direccion)
admin.site.register(Matrimonio)
admin.site.register(Quince)
admin.site.register(Graduacion)
admin.site.register(Angelitos)
admin.site.register(Familia)
admin.site.register(FuerzaPublica)
admin.site.register(EjercitoMilitar)
