from armoire.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.eyetive.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('ARMOIRE_DB_NAME'),
        'USER': os.getenv('ARMOIRE_USER_NAME'),
        'PASSWORD': os.getenv('ARMOIRE_DB_PASSWORD'),
        'HOST': os.getenv('ARMOIRE_DB_HOST'),
        'PORT': os.getenv('ARMOIRE_DB_PORT'),
    }
}