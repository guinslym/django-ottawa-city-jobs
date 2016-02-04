import os
#import dj_database_url

from settings import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.testsqlite3'),
    }
}
SECRET_KEY = 'THISISSECRET!'
