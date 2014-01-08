from django.conf.urls import patterns, url

urlpatterns = patterns('apps.game.views',
	url(r'^/$', 'index', name='index'),
	url(r'^map/$', 'map', name='map'),
	url(r'^colony/(?P<name>\w+)/$', 'colony', name='colony')
)
