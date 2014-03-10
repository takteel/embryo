#!/usr/bin/env python

import os
import sys
from os.path import abspath, dirname, join

if __name__ == "__main__":
    PROJECT_ROOT = dirname(dirname(abspath(__file__)))
    APPLICATIONS_ROOT = join(PROJECT_ROOT, "apps")
    LIBRARIES_ROOT = join(PROJECT_ROOT, "libs")

    if not PROJECT_ROOT in sys.path:
        sys.path.insert(1, PROJECT_ROOT)
    if not APPLICATIONS_ROOT in sys.path:
        sys.path.insert(1, APPLICATIONS_ROOT)
    if not LIBRARIES_ROOT in sys.path:
        sys.path.insert(1, LIBRARIES_ROOT)

    os.environ.setdefault("PROJECT_ENVIRONMENT", "development")
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings.%s" % (os.environ["PROJECT_ENVIRONMENT"],)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
