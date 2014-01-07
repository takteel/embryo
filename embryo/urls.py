from django.conf.urls import patterns, include, url

import apps.planet.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^game/planets/', include(apps.planet.urls.site)),
	url(r'^api/planets/', include(apps.planet.urls.api)),

	# url(r'^$', 'embryo.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls))
)
