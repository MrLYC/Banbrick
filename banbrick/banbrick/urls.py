from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'banbrick.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^panel/', include('xpanel.urls')),
)
