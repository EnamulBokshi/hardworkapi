"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
from django.conf.urls.static import static

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6!%r$z(d4j4dqx6&fks78!ca_bj8kxp52pv09d!k5g==3&%doj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "hardworkapi-2.onrender.com",
    "hardworkapi-1.onrender.com",
    "127.0.0.1",
    "localhost",
    "184.168.113.249"
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://184.168.113.249',
    'http://abc.ancientsbuilders.com',
    'http://ancientsbuilders.com',
    'https://abc.ancientsbuilders.com',
    'https://ancientsbuilders.com',
    'http://localhost:5173'


]
CSRF_TRUSTED_ORIGINS = [
       'http://abc.ancientsbuilders.com',
       'https://abc.ancientsbuilders.com',
       'http://localhost:5173'

    ]
# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'api',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'anymail',
    'shortuuid',
    'django_ckeditor_5',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR,'dist')
STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'dist/assets')
# ]

STORAGES = {
    # ...
     "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',

    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_ALL_ORIGINS = False


AUTH_USER_MODEL = 'api.User'

# Custom Admin Settings
# JAZZMIN_SETTINGS = {
#     "site_title": "Hardwoking",
#     "site_header": "Hardwoking",
#     "site_brand": "HardWorking",
#     "site_icon": "logos/logo.jpg",
#     "site_logo": "logos/logo.jpg",
#     "welcome_sign": "Welcome To Hardwoking",
#     "copyright": "Hardwoking",
#     "user_avatar": "images/photos/logo.jpg",
#     "topmenu_links": [
#         {"name": "Dashboard", "url": "home", "permissions": ["auth.view_user"]},
#         {"model": "auth.User"},
#     ],
#     "show_sidebar": True,
#     "navigation_expanded": True,
#     "order_with_respect_to": [
#         "api",
#         "api.Post",
#         "api.Category",
#         "api.Comment",
#         "api.Bookmark",
#         "api.Notification",
#     ],
#     "icons": {
#         "admin.LogEntry": "fas fa-file",

#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",

#         "api.User": "fas fa-user",
#         "api.Profile":"fas fa-address-card",
#         "api.Post":"fas fa-th",
#         "api.Category":"fas fa-tag",
#         "api.Comment":"fas fa-envelope",
#         "api.Notification":"fas fa-bell",
#         "api.Bookmark":"fas fa-heart",

        
#     },
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-arrow-circle-right",
#     "related_modal_active": False,
    
#     "custom_js": None,
#     "show_ui_builder": True,
    
#     "changeform_format": "horizontal_tabs",
#     "changeform_format_overrides": {
#         "auth.user": "collapsible",
#         "auth.group": "vertical_tabs",
#     },
# }

# Jazzmin Tweaks

# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": True,
#     "brand_small_text": False,
#     "brand_colour": "navbar-indigo",
#     "accent": "accent-olive",
#     "navbar": "navbar-indigo navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": False,
#     "sidebar": "sidebar-dark-indigo",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": False,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "default",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-outline-primary",
#         "secondary": "btn-outline-secondary",
#         "info": "btn-info",
#         "warning": "btn-warning",
#         "danger": "btn-danger",
#         "success": "btn-success"
#     }
# }

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR/'static'