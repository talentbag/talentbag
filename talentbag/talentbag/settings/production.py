from talentbag.settings.base import *
from os import environ
from django.core.exceptions import ImproperlyConfigured



STATIC_ROOT = "/home/ubuntu/talentbag/static/"

STATICFILES_DIRS = ('/home/ubuntu/talentbag/home/static/',   )

#def get_env_setting(setting):
 #   """ Get the environment setting or return exception """
  #  try:
   #     return environ[setting]
   # except KeyError:
    #    error_msg = "Set the %s env variable" % setting
    #    raise ImproperlyConfigured(error_msg)

#SECRET_KEY = get_env_setting('SECRET_KEY')

SECRET_KEY = '@+s)c6qw5pany&z-qs_=tgcv6xj86%)$441g7pu!!mon_01ts='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '54.191.223.12', 'talentbag.com']



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talentbag',
        'USER': 'root',
        'PASSWORD': 'monalisa',
        'HOST': '',   
        'PORT': '',
    }
}


