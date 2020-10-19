


class ConfigDB:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@dbpostgres:5432/backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(ConfigDB):
    SQLALCHEMY_ECHO = True

class ProductionConfig(ConfigDB):
    SQLALCHEMY_ECHO = False

class TestingConfig(ConfigDB):
    SQLALCHEMY_ECHO = False