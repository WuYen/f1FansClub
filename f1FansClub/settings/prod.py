import django_on_heroku
from decouple import config

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# heroku
django_on_heroku.settings(locals(), staticfiles == False)
del DATABASES['default']['OPETIONS']['sslmode']
