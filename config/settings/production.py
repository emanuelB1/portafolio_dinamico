import os
from config.logging import *
from config.settings.base import *
from dotenv import load_dotenv

load_dotenv(Path.joinpath(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [ '*' ]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Esto varia dependiendo de donde alojaras tu aplicación
CSRF_TRUSTED_ORIGINS = ['https://esto_es_el_link_de_tu_pagina_en_produccion.com']

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['https://esto_es_el_link_de_tu_pagina_en_produccion.com']


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Si usaras servicio de mail en tu aplicación, debes configurar esto
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # No usar SSL, ya que estás usando TLS
EMAIL_TIMEOUT = None
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


