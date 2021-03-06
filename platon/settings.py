"""Django settings for platon project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import logging
import os
import sys


################################################################################
#                              Django's Settings                               #
################################################################################

# Directories
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
APPS_DIR = os.path.realpath(os.path.join(BASE_DIR, "apps"))

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-90k)h+jqn8^82(om*zr(1dl^39kr4g&0_84bsdaueo7u6+)s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Set to true when 'python3 manage.py test' is used
TESTING = sys.argv[1:2] == ['test']

# Allowed Hosts
ALLOWED_HOSTS = []

# Application definition
PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'channels',
    'django_celery_beat',
    'django_extensions',
]
PROJECT_APPS = [
    'django_sandbox',
]
INSTALLED_APPS = PREREQ_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# Middleware Definition
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# URL
ROOT_URLCONF = 'platon.urls'

# Template definition
TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'shared/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS':  {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Logging definition
LOGGING = {
    'version':                  1,
    'disable_existing_loggers': False,
    'filters':                  {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true':  {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters':               {
        'verbose': {
            'format':  '[%(asctime)-15s] %(levelname)s -- '
                       'File: %(pathname)s line n°%(lineno)d -- %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
        'simple':  {
            'format':  '[%(asctime)-15s] %(levelname)s -- %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
    },
    'handlers':                 {
        'console':     {
            'level':     'DEBUG',
            'filters':   ['require_debug_true'],
            'class':     'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level':        'ERROR',
            'class':        'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter':    'verbose'
        }
    },
    'loggers':                  {
        '': {
            'handlers': ['console'],
            'level':    'INFO',
        },
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level':    'ERROR',
        },
    },
}


WSGI_APPLICATION = 'platon.wsgi.application'
ASGI_APPLICATION = 'platon.routing.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'django_platon',
        'USER':     'django',
        'PASSWORD': 'django_password',
        'HOST':     '127.0.0.1',
        'PORT':     '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "shared/static"),
]

################################################################################
#                             Third-Party's Settings                           #
################################################################################

# Channel layer
# https://channels.readthedocs.io/en/latest/topics/channel_layers.html
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG':  {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Paris'

################################################################################
#                            Project's Settings                                #
################################################################################

# Sandbox's settings
####################
# Seconds between polls of sandboxes usage. Must not be less than 30.
SANDBOX_POLL_USAGE_EVERY = 15
# Seconds between polls of sandboxes specifications. Must not be less than 300.
SANDBOX_POLL_SPECS_EVERY = 60 * 10
# Default sandbox url
SANDBOX_URL = 'http://localhost:7000/'
################################################################################

if APPS_DIR not in sys.path:  # pragma: no cover
    sys.path.append(APPS_DIR)

# Allow a config file to be created in the same directory as settings.
# It will override keys in settings
try:
    from .config import *
except Exception:
    logger = logging.getLogger(__name__)
    logger.exception("No config file found.")
    pass
