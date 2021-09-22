
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:moringa@localhost/project'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    @staticmethod
    def init_app(app):
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

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}