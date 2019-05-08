#-*-coding:utf-8-*-
"""
Django  for Django project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics//

For the full list of  and their values, see
https://docs.djangoproject.com/en/2.1/ref//
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development  - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vfi0e2g3n-*$&=okst0f#l#^!e93g!^5vo&ne&xvf33d+ouq%7'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True  # 改

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'Temage',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'Temage.middleware.auth.TokenMiddleware'
]

ROOT_URLCONF = 'Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Django.wsgi.application'

#改
# Database
# https://docs.djangoproject.com/en/2.1/ref//#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'temage',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES',foreign_key_checks = 0;",
            'charset': 'utf8mb4',
        },
        'TEST_CHARSET': 'utf-8',
    }
}
#product env
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'temage',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'mysql',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES',foreign_key_checks = 0;",
#             'charset': 'utf8mb4',
#         },
#         'TEST_CHARSET': 'utf-8',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref//#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'



CORS_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     'localhost:8081',
#     '192.168.1.226:8082'
# )
CORS_ALLOW_CREDENTIALS = True





# Media
PRE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MEDIA_ROOT = os.path.join(PRE_ROOT,'media')
MEDIA_URL = '../media/'

# sentry 
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://01a7e750f90f44ec9a0fd2c4d608c4c9@sentry.io/1395787",
    integrations=[DjangoIntegration()]
)

# 改
# ES 
ES_CREATE_URL = 'http://101.132.73.215:9200/temage/product/'
ES_DELETE_URL = 'http://101.132.73.215:9200/temage/product/_delete_by_query/'
ES_SEARCH_URL = 'http://101.132.73.215:9200/temage/product/_search'
# pruduction env
# ES_CREATE_URL = 'http://elastic-elasticsearch-coordinating-only:9200/temage/product/'
# ES_DELETE_URL = 'http://elastic-elasticsearch-coordinating-only:9200/temage/product/_delete_by_query/'
# ES_SEARCH_URL = 'http://elastic-elasticsearch-coordinating-only:9200/temage/product/_search'

#改
# ServerB URL 
SERVERB_HISTORIES_URL = 'http://127.0.0.1:8000/history_predict'
SERVERB_TEXT_IMAGE_MATCH_URL = 'http://127.0.0.1:8000/image_match'
# pruduction env
# SERVERB_HISTORIES_URL = 'http://serverb:8000/history_predict'
# SERVERB_TEXT_IMAGE_MATCH_URL = 'http://serverb:8000/image_match'

# SECRET_KEY = os.getenv('SECRET_KEY')
