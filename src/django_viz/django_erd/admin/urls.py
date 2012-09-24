from django.conf.urls.defaults import patterns, url

from django_erd.admin.views import erd

urlpatterns = patterns('',
    url(r'erd/$',
          erd,
          name="erd"),
)
