from .base import os, BASE_DIR


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child(os.getenv("DB_LOCAL")),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': (os.getenv('DB_PROD')),
        'USER': (os.getenv('DB_PROD_USER')),
        #'PASSWORD': (os.getenv('DB_PROD_PASS')),
        'HOST': 'db_postgres',
        'PORT': 5432
    }
}

