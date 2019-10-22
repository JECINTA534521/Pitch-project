import os

class Config:
    '''
    General configuration parent class
    '''
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jecinta:twinkle@localhost/pitch'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jecinta:twinkle@localhost/pitch'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jecinta:twinkle@localhost/pitch'


    DEBUG = True
    ENV = 'development'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
