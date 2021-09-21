from enum import unique
from operator import index
from . import db

class Pitch(db.Model):
    '''
    Create a class for users
    '''
    __tablename__ = 'pitches'

    id=db.Column(db.Integer,primary_key = True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref = 'pitch', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.Foreignkey('pitches.id'))

    def __repr__(self):
        return f'User {self.username}'

