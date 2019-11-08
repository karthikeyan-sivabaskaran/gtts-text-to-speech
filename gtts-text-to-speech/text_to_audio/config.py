class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = '12345'
    SERVER_ADDRESS = "0.0.0.0"
    SERVER_PORT = 5777


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True