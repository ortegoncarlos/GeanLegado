from django.conf.urls import patterns,include,url
from django.contrib import admin
from legado import views

admin.autodiscover()
urlpatterns = patterns('legado.views',
                       (r'^ckeditor/', include('ckeditor_uploader.urls')),
                       (r'^search/', include('haystack.urls')),
                   url(r'^$', 'Inicio', name='inicio'),
                   url(r'^search/autocomplete/', 'autocomplete', name='autocomplete'),
                   url(r'^somos/', 'SomosIndex', name='somos'),
                   url(r'^funciona/', 'FuncionaIndex', name='funciona'),
                   url(r'^preguntas/', 'PreguntasIndex', name='preguntas'),
                   url(r'^biografia/', 'BiografiaIndex', name='biografia'),
                   url(r'^contacto/', 'ContactoIndex', name='contacto'),
                   url(r'^biografia-cronologica/', 'BiografiaCronologicaIndex', name='biografia-cronologica'),
                   url(r'^biografia-narrativa/', 'BiografiaNarrativaIndex', name='biografia-narrativa'),
                   url(r'^servicios/', 'Servicios', name='servicios'),
                   url(r'^homenajes/', 'HomenajesIndex', name='homenajes'),
                   url(r'^legajados/', 'LegajadosIndex', name='legajados'),
                   url(r'^matrimonios/', 'MatrimonioIndex', name='matrimonios'),
                   url(r'^quince/', 'QuinceIndex', name='quince'),
                   url(r'^graduacion/', 'GraduacionIndex', name='graduacion'),
                   url(r'^fuerza-publica/', 'FuerzaPublicaIndex', name='fuerza-publica'),
                   url(r'^perfil/(?P<slug>[-\w\d]+)/$', 'PerfilPersona', name='perfil'),
                   url(r'^origen_apellido/(?P<id>\d+)$', 'OrigenApell', name='origen_apellido'),
                   url(r'^fotos/(?P<id>\d+)$','Fotos', name='fotos'),
                   url(r'^ejercito/(?P<id>\d+)$','EjercitoIndex', name='ejercito'),
                   url(r'^reconocimientos/(?P<id>\d+)$','Reconocimientos', name='reconocimientos'),

                       )