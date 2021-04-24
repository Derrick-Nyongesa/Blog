import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:daniel@localhost/blog'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    pass

class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:daniel@localhost/blog_test'
    pass

class DevConfig(Config):
    
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}