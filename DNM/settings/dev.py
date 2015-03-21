try:
   from common import *
except ImportError:
   pass

try:
   from DNM.settings.priv import *
except ImportError:
   pass



DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.'+DATABASE_ENGINE, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.

        'NAME': DATABASE_NAME, # Or path to database file if using sqlite3.

        'USER': DATABASE_USER, # Not used with sqlite3.

        'PASSWORD': DATABASE_PASSWORD, # Not used with sqlite3.

        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.

        'PORT': '', # Set to empty string for default. Not used with sqlite3.

    }

}



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
