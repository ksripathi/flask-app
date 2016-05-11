from apilayer import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    mobile = db.Column(db.String(120))

    def __init__(self, username, email, password, mobile):
        self.username = username
        self.email = email
        self.password = password
        self.mobile = mobile

    def to_client(self):
        return {
            'id': self.id,
            'email': self.username,
            'name': self.email,
            'password': self.password,
            'mobile': self.mobile

        }
    
    def __repr__(self):
        return "Name = %s, user = %s, path = %s" % \
            (self.username, self.id, self.email)

     
