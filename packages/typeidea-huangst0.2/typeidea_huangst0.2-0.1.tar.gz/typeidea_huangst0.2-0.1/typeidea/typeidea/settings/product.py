from .base import  *
DEBUG = False
REDIS_URL = '127.0.0.1:6379:1'
ALLOWED_HOSTS = ['192.168.179.128']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'OPTIONS' : {'charset': 'utf8mb4'},
        'NAME' : 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '200307191q',
        'HOST': '<正式数据库IP>',
        'PORT': 3306,
        'CONT_MAX_AGE' : 5 * 60,

    },
}

CACHE = {
    'default':{
        "BACKEND": 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT' : 300,
        'OPTIONS': {
            #'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis_client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',


    }
}