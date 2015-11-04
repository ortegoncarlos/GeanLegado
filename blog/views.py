#encoding:utf-8
from django.shortcuts import render_to_response , get_object_or_404
from django.template import RequestContext
from blog.models import Post, Hero, Circles, Featured,Sedes,Slide,Video,Schedule, Speakers,Galeria




def Home(request):
    post = Post.objects.all().order_by('-created')[:4]
    hero = Hero.objects.all().order_by('-created')[:1]
    circles = Circles.objects.all().order_by('-order')[:4]  
    featrured = Featured.objects.all().order_by('-order')[:4]
    slide = Slide.objects.all().order_by('-orden')
    videos = Video.objects.all().order_by('-evento')
    progra = Schedule.objects.all().order_by('evento')
    speak = Speakers.objects.all()
    gallery = Galeria.objects.all()
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


# def Career(request,slug):
#     career = get_object_or_404(Careers,slug=slug)
#     titulacion = Titulacion.objects.filter(Carrera_id=career.id ).order_by('duracion')[:3]
#     return render_to_response('Modelo_Carrera.html', locals(), context_instance=RequestContext(request))


# def Admissions(request):

#     admission = get_object_or_404(Admission,pk=1)
#     featrured = Featured.objects.all().order_by('-order')[:3]    
#     return render_to_response('Admisiones.html', locals(), context_instance=RequestContext(request))


# def Institution(request):
#     return render_to_response('Modelo_InfoInstit.html', locals(), context_instance=RequestContext(request))

# def Estudiantes(request):
#     return render_to_response('Modelo_PortalEstudiante.html', locals(), context_instance=RequestContext(request))

# def Docentes(request):
#     return render_to_response('Modelo_PortalDocentes.html', locals(), context_instance=RequestContext(request))

# def Finan(request):
#     return render_to_response('financiacion.html', locals(), context_instance=RequestContext(request))

# def Proces(request):
#     return render_to_response('proceso-de-inscripcion.html', locals(), context_instance=RequestContext(request))



# def Directorio(request):
#     listsedes = Sedes.objects.all().order_by('order')    
#     return render_to_response('Sedes.html', locals(), context_instance=RequestContext(request))


# def OnePost(request,slug):
#     post = get_object_or_404(Post,slug=slug)
#     slug = post.slug
#     post_facultad = Post.objects.filter(facultad_id=post.id).published()
#     return render_to_response('Post_all.html', locals(), context_instance=RequestContext(request))


# def Facultadslg(request,slug):
#     facultad = get_object_or_404(Facultad,slug=slug)
#     carreras = Careers.objects.filter(facultad_id=facultad.id)
#     post_facultad = Post.objects.filter(facultad_id=facultad.id).exclude(publish=False)
#     fac_fid = Facultad.objects.all().exclude(id=facultad.id)
#     featrured = Featured.objects.all().order_by('-order')[:3]    
#     return render_to_response('Blog.html', locals(), context_instance=RequestContext(request))

# def News(request):
#     facultad = Facultad.objects.get(title="San Jose")
#     post_facultad = Post.objects.all().order_by('created').published()
#     featrured = Featured.objects.all().order_by('-order')[:3]    
#     return render_to_response('noticias.html', locals(), context_instance=RequestContext(request))

# def Offer(request):
#     post_facultad = Post.objects.all().order_by('created').published()
#     titulacion = Titulacion.objects.all().order_by('duracion')
#     return render_to_response('offer.html', locals(), context_instance=RequestContext(request))

# """def Fafaculty(request):
#     list_fapost = Post.objects.fafaculty()
#     return render_to_response('Blog_FacultadArte.html', locals(), context_instance=RequestContext(request))

# def Fcfaculty(request):
#     list_fcpost = Post.objects.fcfaculty()
#     return render_to_response('Blog_FacultadCiencias.html', locals(), context_instance=RequestContext(request))

# def Fifaculty(request):
#     list_fipost = Post.objects.fifaculty()
#     return render_to_response('Blog_FacultadIngenieria.html', locals(), context_instance=RequestContext(request))

# def Fhfaculty(request):
#     list_fhpost = Post.objects.fdfaculty()
#     return render_to_response('Blog_FacultadDeportes.html', locals(), context_instance=RequestContext(request))"""

# #ESTO HASTA AHORA ES INNECESARIO.
# # def ListPost(request):
# #     posts = Post.objects.order_by('-created')
# #     return render_to_response('blog/list.html', {'posts': posts})
# #
# #
# # def PostsbyCategory(request, idcategory):
# #     category = Category.objects.get(id=idcategory)
# #     posts = category.post_set.order_by('-created')
# #     return render_to_response('blog/list.html', {'posts':posts})
# #
# #
# # def PostsbyUser(request, iduser):
# #     category = Category.objects.get(id=iduser)
# #     posts = category.post_set.order_by('-created')
# #     return render_to_response('blog/list.html', {'posts':posts})