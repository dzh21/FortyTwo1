from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortytwotask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('tasks42.urls')),
    url(r'^requests/', 'tasks42.views.requests'),
    url(r'^edit_contacts/', 'tasks42.views.edit_contacts'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
    }),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {
        'next_page': 'tasks42.views.index'
    }),
)
