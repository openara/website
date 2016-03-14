'''
Created on 12 janv. 2014

@author: rux
'''
import os
from apetizer.settings import *

INSTALLED_APPS.append('openara')
WSGI_APPLICATION = 'openara.wsgi.application'

# Just a pointer to the main config module
SECRET_KEY = "KHFUBYFGJHGILU?MHLGHKUH8KJGBUF5 466778"

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getcwd()+'/database.db',
     },
}