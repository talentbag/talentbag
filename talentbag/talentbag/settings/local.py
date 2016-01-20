
from talentbag.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
STATIC_ROOT = "/Users/vish/Desktop/talentbag/static/"

STATICFILES_DIRS = ('/Users/vish/Desktop/talentbag/talentbag/home/static/',   )


SECRET_KEY = '@+s)c6qw5pany&z-qs_=tgcv6xj86%)$441g7pu!!mon_01ts='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '54.191.223.12', 'talentbag.com']





# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talentbag',
        'USER': 'root',
        'PASSWORD': 'hello',
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',   
        'PORT': '',
    }
}



