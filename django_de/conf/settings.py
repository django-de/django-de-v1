# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Berlin'
SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
SESSION_CACHE_BACKEND = CACHE_BACKEND

EMAIL_BACKEND = 'django_de.conf.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[django-de.org] '

#==============================================================================
# I18N
#==============================================================================

USE_I18N = True
USE_L10N = False

LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', 'Deutsch'),
    #('en', 'English'),
)

#==============================================================================
# Calculation of directories relative to the module location
#==============================================================================
import os
import sys
import django_de

PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(django_de.__file__))
)

PYTHON_BIN = os.path.dirname(sys.executable)
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # Assume that the presence of 'activate_this.py' in the python bin/
    # directory means that we're running in a virtual environment. Set the
    # variable root to $VIRTUALENV/var.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
    if not os.path.exists(VAR_ROOT):
        os.mkdir(VAR_ROOT)
else:
    # Set the variable root to the local configuration location (which is
    # ignored by the repository).
    VAR_ROOT = os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'conf', 'local')

#==============================================================================
# Static files and media settings
#==============================================================================

MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'static'),
)

COMPRESS = True
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]

#==============================================================================
# Project URLS
#==============================================================================

ROOT_URLCONF = 'django_de.conf.urls'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

#==============================================================================
# Templates and Apps
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES += (
    'django.middleware.locale.LocaleMiddleware',
)

INSTALLED_APPS = (
    # Django Batteries
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    # 3rd Party
    'south',
    'gunicorn',
    'compressor',

    # Apps
    'django_de.apps.homepage',
)

#==============================================================================
# 3rd party apps
#==============================================================================

THUMBNAIL_BASEDIR = '_thumbs'
