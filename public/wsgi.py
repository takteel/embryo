import os
import sys

from os.path import abspath, dirname, join

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
APPLICATIONS_ROOT = join(PROJECT_ROOT, "apps")
LIBRARIES_ROOT = join(PROJECT_ROOT, "libs")

if not PROJECT_ROOT in sys.path:
    sys.path.insert(1, PROJECT_ROOT)
if not APPLICATIONS_ROOT in sys.path:
    sys.path.insert(1, APPLICATIONS_ROOT)
if not LIBRARIES_ROOT in sys.path:
    sys.path.insert(1, LIBRARIES_ROOT)

os.environ.setdefault("PROJECT_ENVIRONMENT", "production")
os.environ["DJANGO_SETTINGS_MODULE"] = "settings.%s" % (os.environ["PROJECT_ENVIRONMENT"],)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
