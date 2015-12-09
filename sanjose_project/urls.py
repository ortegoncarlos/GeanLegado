from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from rest_framework import routers
from legado.views import PerfilViewSet , FotosPerfilViewSet

router = routers.DefaultRouter()
router.register(r'perfil',PerfilViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GranLegado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('legado.urls')),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html'),name="account_profile"),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

