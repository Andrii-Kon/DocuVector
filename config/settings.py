# config/settings.py

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists.
# This is useful for local development.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Production-ready Secret Key and Debug settings ---
# The SECRET_KEY is read from an environment variable for security.
# A default value is provided for convenience, but it should be set in production.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-local-dev')

# DEBUG is set to False by default. It will only be True if the DEBUG
# environment variable is explicitly set to 'True'.
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'


# --- Allowed Hosts ---
# In production, this must be set to the domain of your site.
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
else:
    # For local development
    ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost'])


# --- Application definition ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'converter',
]

# --- Middleware Configuration ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise middleware should be placed directly after SecurityMiddleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# --- Database Configuration ---
# Uses dj-database-url to parse the DATABASE_URL environment variable.
# Defaults to SQLite for easy local development.
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Static files (CSS, JavaScript, Images) ---
STATIC_URL = 'static/'
# This is the directory where `collectstatic` will gather all static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This setting is for WhiteNoise to find and serve static files efficiently.
STORAGES = {
    # Default storage for user-uploaded media files.
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # Storage for static files, handled by WhiteNoise.
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# --- Media files (User-uploaded content) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Celery Configuration ---
# Reads the Redis URL from an environment variable for flexibility.
# Defaults to localhost for local development.
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'