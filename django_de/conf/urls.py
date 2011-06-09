from django.conf.urls.defaults import *
from django.contrib import admin

from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('django_de.apps.homepage.urls')),
    
    (r'^admin/', include(admin.site.urls)),
    
    url('^accounts/login/$', login, name='auth_login'),
    url('^accounts/logout/$', logout, name='auth_logout'),
    
    (r'^', include('django_de.apps.wakawaka.urls')),
)
