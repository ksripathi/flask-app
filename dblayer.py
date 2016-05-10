from apilayer import *
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_client(self):
        return {
            'id': self.id,
            'email': self.username,
            'name': self.email,

        }
    
    def __repr__(self):
        return "Name = %s, user = %s, path = %s" % \
            (self.username, self.id, self.email)
#    return '<User %r>' % self.username
 
