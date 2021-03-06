from builtins import dict, Exception, int

from werkzeug.security import *
from app_worker import *
from flask_login import UserMixin


class User(UserMixin, db.Model):
    ''' User class. This is the representation of UserInfo in the MySQL database
        This object will store information of the User.
        Including id (primary key), user's name, user's email address, user's password (added salt and hashed)
    '''
    __tablename__ = "UserInfo"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        '''set the password for the user. Password will be combined with salt and hashed'''
        self.password = generate_password_hash(password)

    def check_password(self, password):
        '''check the password for the user.
            :returns true if the password is valid
        '''
        return check_password_hash(self.password, password)


class ImageContents(db.Model):
    ''' Image content class. This is the representation of ImageInfo table in the MySQL database
        This object will store information of the image.
        Including image id (primary key), user's id (foreign key referencing UserInfo table), image's path in the
        project folder, image's thumbnail's path in the project folder
    '''
    __tablename__ = "ImageInfo"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(256), unique=True)
    path = db.Column(db.String(256), unique=True)
    thumbnail_path = db.Column(db.String(256), unique=True)

    def __init__(self, user_id, name, path, thumbnail_path):
        self.user_id = user_id
        self.name = name
        self.path = path
        self.thumbnail_path = thumbnail_path


class InvalidUsage(Exception):
    '''Exception class for error handling'''
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@login.user_loader
def load_user(id):
    '''method to load user'''
    return User.query.get(int(id))
