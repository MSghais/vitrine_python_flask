import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig(Config):
    debug= True
    # SQLALCHEMY_DATABASE_URLI = "postgresql+psycopg2://user:password@ip:port/db_name"
    SQLALCHEMY_DATABASE_URLI = "postgresql+psycopg2://user:password@ip:port/db_name"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True