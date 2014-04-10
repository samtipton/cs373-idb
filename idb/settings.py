"""
Django settings for idb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTING_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTING_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
DATABASE_PATH = os.path.join(PROJECT_PATH, 'db.sqlite3')




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h#tb420ho@#ob%u&a=rc&t2e6*m!4s-e-m538zzywi9k^8xcz@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'idb'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'idb.urls'

WSGI_APPLICATION = 'idb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if('test' in sys.argv):
    DATABASES = {
        'default' : dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))

    }
else:
    DATABASES = {
#        'default': {
#            "ENGINE": 'django.db.backends.postgresql_psycopg2',
#            'NAME': 'd32vi54g8ai6jj',
#            'USER': 'ixxtrtkrutggss',
#            'PASSWORD': '9-pxBrjhH81zuzhpBvc_XDeC47',
#            'HOST': 'ec2-54-204-36-244.compute-1.amazonaws.com',
#            'PORT': '5432',
#        }
        'default' : dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
    }



TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)
