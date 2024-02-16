"""
Django settings for hmc project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from environ import Env
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
Env.read_env(os.path.join(BASE_DIR, 'hmc/.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(env("DEBUG")) == "1"

ALLOWED_HOSTS = [env("ALLOWED_HOST"), env("LOCAL_HOST"), env("RAILWAY_DOMAIN")]

CSRF_TRUSTED_ORIGINS = [env("CSRF_TRUSTED_ORIGINS")]

INTERNAL_IPS = (
    env("ALLOWED_HOST"),
    env("LOCAL_HOST"),
)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps
    "core",
    # "invoice", #removed
    # AWS
    # "storages",
    # installed libraries
    # "django_browser_reload", #removed
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # installed libraries
    # "django_browser_reload.middleware.BrowserReloadMiddleware", #removed
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # installed libraries end
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hmc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hmc.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Original SQLite3 database setup:


DATABASES = {}
DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"))


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": env("ENGINE"),
            "NAME": env("NAME"),
            "USER": env("USER"),
            "PASSWORD": env("PASSWORD"),
            "HOST": env("HOST"),
            "PORT": env("PORT"),  # default PostgreSQL port
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

LANGUAGE_CODE = env("LANGUAGE_CODE")
TIME_ZONE = env("TIME_ZONE")
USE_I18N = env("USE_I18N")
USE_TZ = env("USE_TZ")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "hmc/hmc/static"),)
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ===================================================================
# This is to send emails from django project
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_COMPANY = env("EMAIL_HOST_COMPANY")
COMPANY_WEBSITE = env("COMPANY_WEBSITE")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
# ===================================================================
