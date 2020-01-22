import os

class Config:
    """Base config vars."""
    BASE_URL = os.path.dirname(__file__)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIJAX_STATIC_PATH = '/static/js/sijax/json2.js'
    RECORDS_PER_PAGE = 10

class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://your_db_username:your_db_pass@localhost/your_db_name''
    SECRET_KEY = 'app-sample-secret-key'
    WTF_CSRF_SECRET_KEY = 'wtform-sample-secret-key'

class HerokuProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = 'app-sample-secret-key'
    WTF_CSRF_SECRET_KEY = 'wtform-sample-secret-key'