from .base import * # NOQA
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER' : 'root',
        'PASSWORD': '200307191q',
        'HOST': '127.0.0.1',
        'PORT' : 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}

    },
}
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',

]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
INTERNAL_IPS = ['127.0.0.1']


