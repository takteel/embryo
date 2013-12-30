"""
Django development settings for embryo project.
"""

from common import *

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [ '.carbon-game.com' ]
# END DEBUG CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': normpath(join(DJANGO_ROOT, 'db.sqlite3'))
	}
}
# END DATABASE CONFIGURATION

# CACHE CONFIGURATION
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
		'LOCATION': normpath(join(DJANGO_ROOT, 'cache'))
	}
}
# END CACHE CONFIGURATION
