from django.conf.urls import patterns, include, url

import apps.game.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^game/', include(apps.game.urls, namespace='game')),
	# url(r'^api/', include(apps.api.urls, namespace='api')),

	# url(r'^$', 'embryo.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls))
)
