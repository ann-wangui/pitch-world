from mimetypes import init
from pickle import TRUE
from pyexpat import model
import string
from turtle import title
from flask_script import Manager
from sqlalchemy import column
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch (db.Model):
    __tablename__= 'pitches'
    id = db.Column(db.Interger,primary_key = TRUE)
    title = db.Column(db.String(255))
    post = db.Column(db.String(), nullable = False)
    comment = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    upvote = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvote = db.relationship('Downvote',backref = 'pitch', lazy = 'dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # time = db.Column(db.datetime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True, nullable = False)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.post}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id = id).all()
        return upvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id = id).all()
        return Downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Comment(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text(), nullable = False )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id = pitch_id).all()
        return comments

    def __repr__(self):
        return f'comment:{self.comment}'