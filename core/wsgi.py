"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.wsgi import get_wsgi_application
dirs = BASE_DIR / "core.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", dirs)

application = get_wsgi_application()


