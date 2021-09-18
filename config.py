from logging import DEBUG
from flask.config import Config


class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config:The parent configuratiion class with General config settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config:The parent configuratiion class with General config settings
    '''
    DEBUG = True