import os

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'emplois',
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.testsqlite3'),
    }
}
SECRET_KEY = 'THISISSECRET!'
