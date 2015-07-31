from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from content.views.content import ContentView
from content.views.front import FrontView

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    
    # homepage
    url(r'^$',
        FrontView.as_view(),
        name='home',
        kwargs={'action': FrontView.default_action}),

    # profile pages
    url(FrontView.get_url_regexp(),
        FrontView.as_view(),
        name=FrontView.view_name),
    
    # some dashboard stuff ...
    url(r'^dashboard/todo/', include('content.todo.urls')),
    # catching up dashboard urls
    url(r'^dashboard/', include('content.dashboard.urls')),
    
    # cms pages
    url(ContentView.get_url_regexp('.*?'),
        ContentView.as_view(),
        name=ContentView.view_name),
)
