from flask import Flask, jsonify, make_response
import json
from flask_sqlalchemy import SQLAlchemy
from dblayer import *
from utils import jsonify_list
app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:vlead123@localhost/demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:vlead123@localhost/demo'


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
    return jsonify_list([i.to_client() for i in users])
#    return make_response(json.dumps(users), 200,
 #                        {'content-type': 'application/json'})

    

if __name__ == "__main__":
    app.run(debug=True)
