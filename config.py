import os

class Config:
    """Base config vars."""
    BASE_URL = os.path.dirname(__file__)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIJAX_STATIC_PATH = '/static/js/sijax/json2.js'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/coop_app_db'
    SECRET_KEY = 'usethisatyourownrisk'
    WTF_CSRF_SECRET_KEY = 'anothersecret'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'set this up depend on your host'
    SECRET_KEY = 'app-sample-secret-key'
    WTF_CSRF_SECRET_KEY = 'wtform-sample-secret-key'

class HerokuProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'set this up depend on your host'
    SECRET_KEY = 'app-sample-secret-key'
    WTF_CSRF_SECRET_KEY = 'wtform-sample-secret-key'