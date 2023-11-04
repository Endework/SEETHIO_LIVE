"""
Django settings for seethio_live project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-prs+%oud^uy1)kv5c6yqm4eg(2n#6ujtdor91k(d1^w)z*0$!q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "userauthentication",
    'social_django', #ogo added configuration
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware', # ogo add this    

]

ROOT_URLCONF = "seethio_live.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.login_redirect', # ogo added this
                'social_django.context_processors.backends', # ogo added this
            ],
        },
    },
]

WSGI_APPLICATION = "seethio_live.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "userauthentication.User"
# STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]
MEDIA_URL = "images/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static/images")

# SMTP configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = "TestSite Team <noreply@example.com>"

#social app custom settings added by ogo
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',  #add this
    'social_core.backends.google.GoogleOAuth2',       #add this
    'django.contrib.auth.backends.ModelBackend',
]
#social app URLS custom settings added by ogo
LOGIN_URL = 'login'   #add this
LOGIN_REDIRECT_URL = '/' #'home'   #add this
LOGOUT_URL = 'logout'   #add this
LOGOUT_REDIRECT_URL = 'login'   #add this
#LOGIN_ERROR_URL = 'login'

#APIS keys and ID settings added by ogo
SOCIAL_AUTH_FACEBOOK_KEY = '863786055075073'   #add this
SOCIAL_AUTH_FACEBOOK_SECRET = 'e026b8ff13c7d3ca71e5acb6eab264e4'    #add this
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1088080566509-7l4qpm8us2os6tf1ud0tpe39cdakjtl9.apps.googleusercontent.com'   #add this
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'    #add this

# Add the following name by ogo
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# external information by ogo
SOCIAL_AUTH_FACEBOOK_SCOPE = [    #add this
    'email',    
]
SOCIAL_AUTH_GOOGLE_SCOPE = [   #add this
    'email',    
]
# django_project/settings.py
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
