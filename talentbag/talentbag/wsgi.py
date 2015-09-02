"""
WSGI config for talentbag project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/talentbag/talentbag')
sys.path.append('home/ubuntu/talentbag')


os.environ['LD_LIBRARY_PATH']= '/home/ubuntu/.virtualenvs/talentbag/local/lib/ython2.7/site-packages'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talentbag.settings.production")

application = get_wsgi_application()


