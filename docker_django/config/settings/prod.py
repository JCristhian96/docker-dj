from .base import *
from . import db


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = db.SQLITE3


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child('static'),
]
STATIC_ROOT = BASE_DIR.child('staticfiles')
# STATIC_ROOT = '/code/staticfiles/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
# MEDIA_ROOT = '/code/media/'


# BASE_DIR2 = Path(__file__).ancestor(4)
# print("*******************************")
# print(BASE_DIR)
# print("*******************************")
# print("*******************************")
# print(BASE_DIR2)
# print("*******************************")