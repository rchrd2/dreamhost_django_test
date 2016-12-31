import sys
import os

sys.path.insert(0, os.path.abspath('python_packages'))

from dreamhost_django_test import wsgi
application = wsgi.application
