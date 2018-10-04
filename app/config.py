import os

class Config(object):
    '''This class stores the configurations for this app'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MYSQL_DATABASE_HOST = "localhost"
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = "ece1779pass"
    MYSQL_DATABASE_DB = "ECE1779A1"
    MYSQL_CURSORCLASS = "DictCursor"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ece1779pass@localhost/ECE1779A1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False