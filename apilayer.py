from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dblayer import *
app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:vlead123@localhost/demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:paswd@localhost/dbname'


@app.route("/users/<username>")
def hello(username):
    try:
        user = User.query.filter_by(username=username).first_or_404()
        if user.username:
            return jsonify({'Found the result for the name': user.username})
    except:
        return "failure"

@app.route("/users")
def users():
    users = User.query.all()
    return jsonify_list([i.to_client() for i in User.get_all()])
    

if __name__ == "__main__":
    app.run(debug=True)
