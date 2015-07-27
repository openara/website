from __future__ import unicode_literals
#-*- coding: utf-8 -*-

from openara.conf.base import *

ALLOWED_HOSTS = ['openara.biodigitals.com',
                 'openara.com',
                 '*.openara.com']

ALLOWED_HOSTS = ['*']

DOMAIN_NAME = ".openara.com"
SITE_NAME = "openara"

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openara',
        'USER': 'openara',
        'PASSWORD': 'openara',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 900,
        'KEY_PREFIX':'openara',
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        },
    },
    "locmem": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
    "dummy": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

CACHES['items'] = {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
    'TIMEOUT': 900,
    'OPTIONS': {
        'MAX_ENTRIES': 10000
    },    
}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

CRISPY_FAIL_SILENTLY = False

from settings_prod import *