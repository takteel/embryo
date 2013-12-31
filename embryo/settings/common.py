"""
Django common settings for embryo project.
"""

import sys
from os.path import abspath, basename, dirname, join, normpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's@3@s18q_4c+b^y^@i6iczzvy(o#ya)cy*i0+u_@mq2us_(qw^'

sys.path.append(SITE_ROOT)

ALLOWED_HOSTS = []

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []
# END DEBUG CONFIGURATION

# ADMIN CONFIGURATION
ADMINS = (
	('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
# END ADMIN CONFIGURATION

# INTERNATIONALIZATION CONFIGURATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# END INTERNATIONALIZATION CONFIGURATION

# MEDIA CONFIGURATION
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'assets')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# TEMPLATE CONFIGURATION
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
# END TEMPLATE CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# APPS CONFIGURATION
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'libs.defer'
)
# END APPS CONFIGURATION

ROOT_URLCONF = 'embryo.urls'

WSGI_APPLICATION = 'embryo.wsgi.application'
