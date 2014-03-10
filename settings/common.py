"""
Django common settings for embryo project.
"""

import sys
from os.path import abspath, basename, dirname, join, normpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = dirname(dirname(abspath(__file__)))
APPLICATIONS_ROOT = join(PROJECT_ROOT, "apps")
LIBRARIES_ROOT = join(PROJECT_ROOT, "libs")
PUBLIC_ROOT = join(PROJECT_ROOT, "public")

SITE_ID=1

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's@3@s18q_4c+b^y^@i6iczzvy(o#ya)cy*i0+u_@mq2us_(qw^'

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION

ALLOWED_HOSTS = []

# ADMIN CONFIGURATION
ADMINS = (
	('takteel', 'takteel@embryo-game.com'),
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
MEDIA_ROOT = normpath(join(PUBLIC_ROOT, 'media'))
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(PUBLIC_ROOT, 'static'))
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'static')),
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
    normpath(join(PROJECT_ROOT, 'templates')),
)
# END TEMPLATE CONFIGURATION

# APPS CONFIGURATION
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
	'django.contrib.admin',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'libs.defer',
	'apps.game'
)
# END APPS CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

ROOT_URLCONF = 'embryo.urls'

WSGI_APPLICATION = 'public.wsgi.application'
