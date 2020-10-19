from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import marshmallow
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

class ConfigDB:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@dbpostgres:5432/backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(ConfigDB):
    SQLALCHEMY_ECHO = True

class ProductionConfig(ConfigDB):
    SQLALCHEMY_ECHO = False



def config_Blueprint(app):
  from Project.Users.endpoints import user_blueprint
  app.register_blueprint(user_blueprint)

def error_handler(app):
  @app.errorhandler(marshmallow.exceptions.ValidationError)
  def validationErrorHandler(ex):
      return ex.messages, 400

def create_app():

 app = Flask(__name__)
 app.config.from_object(ConfigDB)

 db.init_app(app)
 ma.init_app(app)
 migrate.init_app(app, db)

 config_Blueprint(app)
 error_handler(app)

 return app
