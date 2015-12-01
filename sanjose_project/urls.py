from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from legado.views import PerfilViewSet 

router = routers.DefaultRouter()
router.register(r'pefil',PerfilViewSet)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GranLegado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('legado.urls')),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

