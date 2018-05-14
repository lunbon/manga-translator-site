from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class Title(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title_name  = db.Column(db.String(128), index=True, unique=True)
	description = db.Column(db.String(2048), default=' ')
	chapters = db.relationship('Chapter', backref='title', lazy='dynamic')
	def __repr__(self):
		return self.title_name

class Chapter(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	chapter_name = db.Column(db.String(128), index=True, unique=True)
	chapter_number = db.Column(db.Integer(), default=0)
	title_id = db.Column(db.Integer, db.ForeignKey('title.id'))
	poster_url = db.Column(db.String(1024), default = '/')
	read_url = db.Column(db.String(1024), default = '/')
	added_time = db.Column(db.DateTime, default=datetime.utcnow)
	def __repr__(self):
		return self.title_name

class User(UserMixin,db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def set_password_hash(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))