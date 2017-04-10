class Config(object):

    # MongoDB settings
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017

    @staticmethod
    def init_app(app):
        pass

# Configuration for test - Windows OS
class TestingConfig(Config):
    DEBUG = True

# Configuration for development - Linux OS
class DevelopmentConfig(Config):
    pass

# Configuration for production - Extranet server
class ProductionConfig(Config):
    pass

config = {
    'testing': TestingConfig,           # Windows PC
    'development': DevelopmentConfig,   # Linux PC
    'product': ProductionConfig         # Production Server
}

RUN_LEVEL = 'testing'