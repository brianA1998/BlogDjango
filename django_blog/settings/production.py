from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogdevelopers.herokuapp.com']



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dc5fmedlso6k1u',
        'USER':'kndarqtgjufmsn',
        'PASSWORD':'f13f29c05aa3a033f83e98cd75f0d98479ef742b0e06384bf22abe9c5b354349',
        'HOST':'ec2-3-211-48-92.compute-1.amazonaws.com',
        'PORT':5432,

    }
}

STATICFILES_DIRS = (BASE_DIR,'static')


