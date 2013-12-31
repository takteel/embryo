from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', 'embryo.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls))
)
