import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework','rest_framework.authtoken','drf_yasg','django_filters',
    'departments','employees','analytics'
]

DATABASES = {'default': env.db()}  # django-environ  [oai_citation_attribution:9‡django-environ.readthedocs.io](https://django-environ.readthedocs.io/en/latest/quickstart.html?utm_source=chatgpt.com)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.UserRateThrottle'],
    'DEFAULT_THROTTLE_RATES': {'user': '100/day','anon': '10/day'},  # DRF throttle  [oai_citation_attribution:10‡drf-yasg.readthedocs.io](https://drf-yasg.readthedocs.io/en/stable/readme.html?utm_source=chatgpt.com)
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

STATIC_URL = '/static/'
