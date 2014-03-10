"""
Django tests settings for embryo project.
"""

from common import *

# DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = True
# END DEBUG CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
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
		'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
	}
}
# END CACHE CONFIGURATION
