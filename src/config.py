import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_name = 'monit'

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_top_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI= "mysql://monit:password@192.168.33.253:3306/" + database_name


class DockerConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI= "sqlite:////tmp/monit.db"

