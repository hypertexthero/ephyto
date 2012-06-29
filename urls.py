from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ephyto.views.home', name='home'),
    # url(r'^ephyto/', include('ephyto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'home.html'}), # for custom homepage template?
    # (r'^/$', 'direct_to_template', {'template': 'base.html'}), # / as url in flatpages shows homepage, which is editable :)
    # (r'^/()', 'direct_to_template', {'template': 'base.html'}) # matches any page created?
    # (r'^archive/(?P<url>[-\w]+)/$', 'direct_to_template', {'template': 'base.html'}),
)

# Serving static/media files could be better with Django. Here's how to do it in the development server (and use href="{{ STATIC_URL }}css/mysite.css" in mysite/myproject/templates/base.html). In production I believe it will be controlled by a the server's configuration, in this case (nginx), in the file mysite/myproject/etc/nginx.conf
# http://ecarmi.org/writing/django-on-joyent/
# http://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development
from django.conf import settings

if settings.DEBUG :
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )