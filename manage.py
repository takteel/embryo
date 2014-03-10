#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	os.environ.setdefault("EMBRYO_ENVIRONMENT", "development")
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "embryo.settings.%s" % (os.environ["EMBRYO_ENVIRONMENT"],))

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
