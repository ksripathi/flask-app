from apilayer import *

def insert_user():
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    insert_user()
