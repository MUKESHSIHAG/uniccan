from app import db
from app import login_manager
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    college = db.Column(db.String(200))
    gender = db.Column(db.String(10))
    dob = db.Column(db.DateTime)
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Circle(db.Model):
    code = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))