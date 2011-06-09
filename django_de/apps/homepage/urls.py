from django.conf.urls.defaults import *

from django_de.apps.homepage.views import HomepageView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
)
