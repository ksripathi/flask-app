from flask import Flask, jsonify, make_response, render_template, request, session, redirect
import json
from flask_sqlalchemy import SQLAlchemy
from dblayer import *
from utils import jsonify_list
app = Flask(__name__)
app.secret_key = 'djfjsdkjXXS7979dfdfd'
#SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:vlead123@localhost/demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:vlead123@localhost/demo'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if ('email' in session):
            return render_template('success.html')
        else:
            return redirect('/')
        
    else:
        get_name = request.form['text']
        name = str(get_name)
        get_pswd = request.form['pswd']
        pswd = str(get_pswd)
        user = User.query.filter_by(username=name).first_or_404()
        if user.username:
            session['email'] = user.email
            return render_template('success.html', name=session['email'], paswd=pswd)

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('email', None)
    return redirect("/")
#    return render_template('index.html')
'''
@app.route("/users")
def users():
    users = User.query.all()
    return jsonify_list([i.to_client() for i in users])
'''
if __name__ == "__main__":
    app.run(debug=True)
