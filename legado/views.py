from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import UpdateView
from .forms import PerfilSearchForm, PerfilForm
from haystack.query import SearchQuerySet
from django.db.models import Q
from legado.models import *
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from django.core import serializers

def autocomplete(request):
    #sqs = SearchQuerySet().autocomplete(nombre=request.GET.get('q', ''))[:5]
    sqs1 = SearchQuerySet().models(Perfil).load_all().autocomplete(nombre=request.GET.get('q','')) 
    sqs2 = SearchQuerySet().models(Perfil).load_all().autocomplete(profesion=request.GET.get('q','')) 
    sqs3 = SearchQuerySet().models(Perfil).load_all().autocomplete(fecha_nacimiento=request.GET.get('q','')) 
    sqs4 = SearchQuerySet().models(Perfil).load_all().autocomplete(lugar_nacimiento=request.GET.get('q','')) 
    sqs5 = SearchQuerySet().models(Perfil).load_all().autocomplete(biografia=request.GET.get('q','')) 
    sqs = sqs1 | sqs2 | sqs3 | sqs4 | sqs5
    suggestions = serializers.serialize("json",[q.object for q in sqs])
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
 
    # the_data = json.dumps({
    #     'results': suggestions
    # })
    return HttpResponse(suggestions, content_type='application/json')

def Inicio(request):
    perfiles = Perfil.objects.all()
    servicio = Servicio.objects.first()
    homenaje = Homenajes.objects.first()
    legaj = Legajados.objects.first()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def SomosIndex(request):
    team = Somos.objects.first()
    return render_to_response('somos.html', locals(), context_instance=RequestContext(request))

def FuncionaIndex(request):
    func = Funciona.objects.first()
    return render_to_response('funciona.html', locals(), context_instance=RequestContext(request))

def BiografiaIndex(request):
    bio = Biografia.objects.first()
    return render_to_response('biografia.html', locals(), context_instance=RequestContext(request))

def BiografiaCronologicaIndex(request):
    bio_crono = BiografiaCronologica.objects.first()
    return render_to_response('bio_cronologica.html', locals(), context_instance=RequestContext(request))

def BiografiaNarrativaIndex(request):
    bio_narra = BiografiaNarrativa.objects.first()
    return render_to_response('bio_narrativa.html', locals(), context_instance=RequestContext(request))


def PreguntasIndex(request):
    preguntas = PreguntasFrecuentes.objects.all()
    return render_to_response('preguntas-frecuentes.html', locals(), context_instance=RequestContext(request))

def Servicios(request):
    servicio = Servicio.objects.first()
    return render_to_response('servicios.html', locals(), context_instance=RequestContext(request))

def HomenajesIndex(request):
    homenaj = Homenajes.objects.first()

    return render_to_response('homenajes.html', locals(), context_instance=RequestContext(request))

def SearchIndex(request):
    perfiles = SearchQuerySet().filter(nombre__exact=request.GET['q'])
    perfiles2 = SearchQuerySet().filter(profesion__exact=request.GET['q'])
    return render_to_response('search.html', locals(), context_instance=RequestContext(request))

def LegajadosIndex(request):
    legaja = Legajados.objects.first()
    matrimonio = Matrimonio.objects.first()
    quince = Quince.objects.first()
    gradua = Graduacion.objects.first()
    angelito = Angelitos.objects.first()
    familia = Familia.objects.first()
    fuerza = FuerzaPublica.objects.first()
    return render_to_response('legajados.html', locals(),context_instance=RequestContext(request))

def MatrimonioIndex(request):
    matrimonio = Matrimonio.objects.first()
    return render_to_response('matrimonios.html',locals(), context_instance=RequestContext(request))

def QuinceIndex(request):
    quince = Quince.objects.first()
    return render_to_response('quince.html',locals(), context_instance=RequestContext(request))

def GraduacionIndex(request):
    graduacion = Graduacion.objects.first()
    return render_to_response('graduacion.html',locals(), context_instance=RequestContext(request))

def FuerzaPublicaIndex(request):
    fuerza = FuerzaPublica.objects.first()
    ejercitos = EjercitoMilitar.objects.all()
    return render_to_response('fuerza_publica.html',locals(), context_instance=RequestContext(request))

def PerfilPersona(request, slug):
    perfil_persona = get_object_or_404(Perfil,slug=slug)
    fotos = FotosPerfil.objects.filter(perfil_id=perfil_persona.id)
    return render_to_response('perfil-persona.html',locals(), context_instance=RequestContext(request))

class EditarHomenaje(UpdateView):
    model = Perfil
    fields = ['nombre','fecha_nacimiento','lugar_nacimiento','imagen','profesion','biografia','origen_apellido','audio_file','listo']
    template_name = 'crear_homenaje.html'
    success_url = '/mishomenajes/'


def OrigenApell(request, id):
    perfil_persona = Perfil.objects.get(id=id)
    return render_to_response('origen_apellido.html', locals(), context_instance=RequestContext(request))

def Fotos(request, id):
    perfil_persona = Perfil.objects.get(id=id)
    fotos = FotosPerfil.objects.filter(perfil=id)
    return render_to_response('fotos.html', locals(), context_instance=RequestContext(request))

def EjercitoIndex(request, id):
    ejer = EjercitoMilitar.objects.get(id=id)
    return render_to_response('ejercito.html', locals(), context_instance=RequestContext(request))

def Reconocimientos(request, id):
    perfil_persona = Perfil.objects.get(id=id)
    reconocimientos = FotosReconocimiento.objects.filter(perfil=id)
    return render_to_response('reconocimientos.html', locals(), context_instance=RequestContext(request))


def Mishomenajes(request):
    # send_mail('Subject here', 'Here is the message.', 'rmazahares@uci.cu',
    # ['rmazahares@uci.cu'], fail_silently=False)
    homenajes = Perfil.objects.filter(usuario=request.user)
    return render_to_response('mishomenajes.html', locals(), context_instance=RequestContext(request))

def CrearHomenaje(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            new_homenaje = form.save(commit=False)
            new_homenaje.usuario = request.user
            new_homenaje.save()
            form.save()
            return HttpResponseRedirect('mishomenajes')
    else:
        form = PerfilForm()
    return render_to_response("crear_homenaje.html", {"form": form}, context_instance=RequestContext(request))



def ContactoIndex(request):
    direc = Direccion.objects.first()
    return render_to_response('contacto.html',locals(), context_instance=RequestContext(request))

from .serializers import PerfilSerializer
from rest_framework import viewsets

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

