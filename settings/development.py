"""
Django development settings for embryo project.
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
		'NAME': normpath(join(PROJECT_ROOT, 'embryo', 'development.sqlite3'))
	}
}
# END DATABASE CONFIGURATION

# CACHE CONFIGURATION
CACHES = {
	'default': {
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': normpath(join(PROJECT_ROOT, 'embryo', 'cache'))
		'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
	}
}
# END CACHE CONFIGURATION

# # APPS CONFIGURATION
# INSTALLED_APPS += (
#     'debug_toolbar',
# )
# # END APPS CONFIGURATION

# # MIDDLEWARE CONFIGURATION
# MIDDLEWARE_CLASSES = (
#     'django.middleware.gzip.GZipMiddleware',
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )
# # END MIDDLEWARE CONFIGURATION

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]
