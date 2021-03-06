from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy import desc


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).order_by(desc('posted')).all()          
        return comments


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.Integer)
    title = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).all()
        return pitch

    @classmethod
    def get_pitches_by_category(cls,category):
        pitches = Pitch.query.filter_by(category = category).order_by(desc('posted')).all()
        return pitches