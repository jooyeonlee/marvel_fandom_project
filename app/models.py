from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from secrets import token_hex
import uuid

# login manager
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# db
db = SQLAlchemy()

#FavoriteTable = db.Table('favorite',
#    db.Column('user_id', db.String, db.ForeignKey('user.id')),
#    db.Column('character_id', db.Integer, db.ForeignKey('character.id'))
#)

class User(db.Model, UserMixin):
    __tablename__ ='user'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default='')
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default='')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    token = db.Column(db.String(32), nullable=False, default=None)
    charactors = db.relationship('Charactor', secondary='favorite', backref=db.backref('user'))

    def __init__(self, email, password, name=''):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.token = token_hex(16)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'datecreated': self.date_created,
            'apitoken': self.token
        }

class Charactor(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='')
    description = db.Column(db.String(250), nullable=True)
    comics_appeared_in = db.Column(db.String(250), nullable=True)
    super_power = db.Column(db.String(100), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'comic': self.comics_appeared_in,
            'superpower': self.super_power,
            'datecreated': self.date_created
        }

    def from_dict(self, new):
        if new.get('id'):
            self.id = new.get('id')
        if new.get('name'):
            self.name = new.get('name')
        if new.get('description'):
            self.description = new.get('description')
        if new.get('comic'):
            self.comics_appeared_in = new.get('comic')
        if new.get('superpower'):
            self.super_power = new.get('superpower')

#Association Table
class FavoriteCharactor(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id', ondelete='CASCADE'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id', ondelete='CASCADE'))