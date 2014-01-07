from django.conf.urls import patterns, url

urlpatterns = patterns('embryo.apps.planet.views.api',
	url(r'^(?P<name>\d{4})/$', 'planet', name='planet-api-planet')
)
