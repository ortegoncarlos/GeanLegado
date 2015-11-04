from django.shortcuts import render, render_to_response
from django.template import RequestContext
from legado.models import *
from django.http import HttpResponse
from haystack.query import SearchQuerySet
import json

def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')

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

def PerfilPersona(request, slug, id):
    perfil_persona = Perfil.objects.get(id=id)
    fotos = FotosPerfil.objects.filter(perfil=id)
    return render_to_response('perfil-persona.html',locals(), context_instance=RequestContext(request))

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


def ContactoIndex(request):
    direc = Direccion.objects.first()
    return render_to_response('contacto.html',locals(), context_instance=RequestContext(request))