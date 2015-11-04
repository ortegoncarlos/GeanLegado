from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GranLegado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('legado.urls')),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

