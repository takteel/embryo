"""
Django development settings for embryo project.
"""

from common import *

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = False
# END DEBUG CONFIGURATION

ALLOWED_HOSTS = [ '.embryo-game.com' ]

SESSION_COOKIE_DOMAIN = 'www.embryo-game.com'
CRSF_COOKIE_DOMAIN = 'www.embryo-game.com'

# MEDIA FILES CONFIGURATION
MEDIA_URL = 'media.embryo-game.com/'
# END MEDIA FILES CONFIGURATION

# STATIC FILES CONFIGURATION
STATIC_URL = 'static.embryo-game.com/'
# END STATIC FILES CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(PROJECT_ROOT, 'embryo', 'production.sqlite3'))
	}
}
# END DATABASE CONFIGURATION

# CACHE CONFIGURATION
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
		'LOCATION': normpath(join(PROJECT_ROOT, 'embryo', 'cache'))
	}
}
# END CACHE CONFIGURATION
