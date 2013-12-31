"""
WSGI config for embryo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("EMBRYO_ENVIRONMENT", "production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "embryo.settings.%s" % (os.environ["EMBRYO_ENVIRONMENT"],))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
