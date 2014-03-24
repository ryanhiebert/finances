import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if os.environ.get('ADMINS', None):
    ADMINS = tuple(
        tuple(x.split(',')) for x in os.environ.get('ADMINS').split(';'))
else:
    ADMINS = None
DEBUG = TEMPLATE_DEBUG = not ADMINS
MANAGERS = ADMINS

if os.environ.get('SECURE_PROXY_SSL_HEADER', None):
    SECURE_PROXY_SSL_HEADER = tuple(
        os.environ.get('SECURE_PROXY_SSL_HEADER').split(',')) or None

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SECRET_KEY = os.environ.get('SECRET_KEY', 'not-a-secret')
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'finances',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'finances.urls'
WSGI_APPLICATION = 'finances.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(),
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
