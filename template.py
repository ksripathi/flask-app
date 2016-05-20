from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:vlead123@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):

        self.username = username
        self.email = email

        def to_client(self):
            return {
                'id': self.id,
                'email': self.username
            }

        def __repr__(self):
            return "Name = %s, user = %s, path = %s" % \
                (self.username, self.id, self.email)


def insert_user():
    admin = Users('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    insert_user()
