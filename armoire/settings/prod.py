from armoire.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.pythonanywhere.com']

SECRET_KEY = os.getenv('ARMOIRE_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('desarrolloeyetiv$armoire'),
        'USER': os.getenv('desarrolloeyetiv'),
        'PASSWORD': os.getenv('armoire2017'),
        'HOST': os.getenv('desarrolloeyetive.mysql.pythonanywhere-services.com'),
        'PORT': os.getenv(''),
    }
}
