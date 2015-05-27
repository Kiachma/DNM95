ADMINS = (

    ('Emil Aura', 'aura.emil@gmail.com'),

)

MANAGERS = ADMINS




# Local time zone for this installation. Choices can be found here:

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name

# although not all choices may be available on all operating systems.

# In a Windows environment this must be set to your system time zone.

TIME_ZONE = 'Europe/Helsinki'



# Language code for this installation. All choices can be found here:

# http://www.i18nguy.com/unicode/languageidentifiers.html

LANGUAGE_CODE = 'sv_FI'

SITE_ID = 1



# If you set this to False, Django will make some optimizations so as not

# to load the internationalization machinery.

USE_I18N = True



# If you set this to False, Django will not format dates, numbers and

# calendars according to the current locale.

USE_L10N = True



# If you set this to False, Django will not use timezoneaware datetimes.

USE_TZ = True



# Make this unique, and don't share it with anybody.

SECRET_KEY = 'w5p3l#^z&amp;7j($&amp;4%qn&amp;uu7n$0vdfo6w9d(smsq*x264t2*wp0s'



# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',

    'django.template.loaders.app_directories.Loader',

    #     'django.template.loaders.eggs.Loader',

)

MIDDLEWARE_CLASSES = (

    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'DNM.Middleware.middleware.RequireLoginMiddleware',

    # Uncomment the next line for simple clickjacking protection:

    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'DNM.urls'



# Python dotted path to the WSGI application used by Django's runserver.

WSGI_APPLICATION = 'DNM.wsgi.application'

import os

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '../../', 'DNM/templates').replace('\\', '/'),)

INSTALLED_APPS = (

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.sites',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:

    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:

    # 'django.contrib.admindocs',

    'DNM.apps.members',
    'DNM.apps.news',
    'DNM.apps.news.events',
    'DNM.apps.signup',
    'DNM.apps.gallery',
    'DNM.apps.klotter',
    'DNM.apps.overrides',
    'DNM.apps.static_pages',
    'DNM.apps.templatetags',

        'taggit',

    'sortedm2m',
    'django_summernote',

    'chart_tools',

    'widget_tweaks',

    'mptt',

    'endless_pagination',
    'sorl.thumbnail'

)



# A sample logging configuration. The only tangible logging

# performed by this configuration is to send an email to

# the site admins on every HTTP 500 error when DEBUG=False.

# See http://docs.djangoproject.com/en/dev/topics/logging for

# more details on how to customize your logging configuration.

LOGGING = {

    'version': 1,

    'disable_existing_loggers': False,

    'filters': {

        'require_debug_false': {

            '()': 'django.utils.log.RequireDebugFalse'

        }

    },

    'handlers': {

        'mail_admins': {

            'level': 'ERROR',

            'filters': ['require_debug_false'],

            'class': 'django.utils.log.AdminEmailHandler'

        }

    },

    'loggers': {

        'django.request': {

            'handlers': ['mail_admins'],

            'level': 'ERROR',

            'propagate': True,

        },

    }


}

AUTH_USER_MODEL = 'members.Member'

TEMPLATE_CONTEXT_PROCESSORS = (

    "django.contrib.auth.context_processors.auth",

    "django.core.context_processors.debug",

    "django.core.context_processors.i18n",

    "django.core.context_processors.media",

    "django.core.context_processors.static",

    "django.contrib.messages.context_processors.messages",

    "django.core.context_processors.request",



)

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {

    messages.ERROR: 'danger',

}
INSTALLED_APPS += ('django_pjaxr', )

TEMPLATE_CONTEXT_PROCESSORS += ('django_pjaxr.context_processors.pjaxr_information',)

DEFAULT_PJAXR_TEMPLATE = "django_pjaxr/pjaxr.html"


LOGIN_REQUIRED_URLS = (
    r'/(.*)$',
)
LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/event/export/',
    r'/user/password(.*)$',
)
THUMBNAIL_DUMMY =True


SUMMERNOTE_CONFIG = {
    # Usage of iframe
    'iframe': False,

    # Change editor size
    'width': '100%',

    # Set editor language/locale
    'lang': 'en-US',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style','fontname']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['font', ['strikethrough']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'height']],
        ['insert', ['picture','video','table']],
    ],


}

DATE_INPUT_FORMATS=['%d.%m.%Y',]