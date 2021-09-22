from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
    '''
    Create a class for users
    '''
    __tablename__ = 'pitches'

    id=db.Column(db.Integer,primary_key = True)
    title=db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.Text)
    slug = db.Column(db.String(64), unique=True)
    picture_path = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    like = db.relationship('Like', backref='post', lazy='dynamic')
    dislike = db.relationship('Dislike', backref='post', lazy='dynamic')
    comment = db.relationship('Comment', backref='post', lazy='dynamic') 

    def __repr__(self):
        return f'User {self.title}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch=db.relationship('Pitch', backref='user', lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    # get all the comments related to a single post
    @classmethod
    def get_comments(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

    # get comment author details from the author id
    @classmethod
    def get_comment_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        return author

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def save_like(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls, post_id):
        likes = Like.query.filter_by(post_id=post_id).all()
        return likes

    @classmethod
    def get_like_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        
class Dislike(db.Model):
    __tablename__ = 'dislikes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def save_dislike(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls, post_id):
        dislikes = Dislike.query.filter_by(post_id=post_id).all()
        return dislikes

    @classmethod
    def get_dislike_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        return author
