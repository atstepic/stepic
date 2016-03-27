from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^question/(?P<id>\d+)/$', 'qa.views.test'),
    url(r'^admin/', include(admin.site.urls)),
)
