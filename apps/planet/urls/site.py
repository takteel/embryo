from django.conf.urls import patterns, url

urlpatterns = patterns('embryo.apps.planet.views.site',
	url(r'^(?P<name>\d{4})/$', 'planet', name='planet-site-planet')
)
