from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^iluminare/', include('iluminare.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # a primeira pagina do site e a primeira pagina no madulo 'entrada'
    (r'^$', 'iluminare.entrada.views.index'),

    # o app entrada tera as urls administradas em entrada/urls.py
    (r'^entrada/', include('iluminare.entrada.urls'))    
    #(r'^entrada/', 'iluminare.entrada.views.index') 
)