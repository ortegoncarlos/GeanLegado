from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('blog.views',
                    url(r'^$', 'Home', name='home'),
                    )