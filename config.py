# encoding: utf-8
from datetime import timedelta

LOG_FILE = '/home/log/test_nginx_access.log'  # 日志文件路径
EVENT_NAME = 'response'  # socketio 事件名称
NAMESPACE = '/shell'  # socketio 名称空间


class Config(object):
    SECRET_KEY = 'this is a secret string'
    CELERY_BROKER_URL = 'redis://localhost:6379/0',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_IMPORTS = (
        'celeryTask.test'
    )
    TIMEZONE = 'UTC'
    CELERYBEAT_SCHEDULE = {
        'save2Mongo': {
            'task': "save2Mongo",
            'schedule': timedelta(minutes=1),
            'args': ''
        },
        'correctWifiSave2Mongo': {
            'task': "correctWifiSave2Mongo",
            'schedule': timedelta(minutes=1),
            'args': ''
        },
        'saveFenShen2Mongo': {
            'task': "saveFenShen2Mongo",
            'schedule': timedelta(minutes=1),
            'args': ''
        }
    }
    MONGODB_SETTINGS = {
        'db': 'wifi',
        'host': 'localhost',
        'port': 27017,
        # 'password': '123456',
        # 'username': 'test',
    }


class DevelopmentConfig(Config):
    DEBUG = False

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6370
    REDIS_DB = 4
    REDIS_PASSWORD = ''

    MONGODB_INFO = ''


class ProductionConfig(Config):
    DEBUG = True

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6370
    REDIS_DB = 4
    REDIS_PASSWORD = ''

    MONGODB_INFO = ''


Conf = ProductionConfig
