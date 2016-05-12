from flask import Flask, jsonify, make_response, render_template, request, session, redirect, flash
import json
from flask_sqlalchemy import SQLAlchemy
from dblayer import *
from utils import jsonify_list

app = Flask(__name__)
app.secret_key = 'djfjsdkjXXS7979dfdfd'
#SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:vlead123@localhost/demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:vlead123@localhost/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = str(request.form['user'])
        password = str(request.form['pswd'])
        email = str(request.form['mobile'])
        mobile = str(request.form['email'])
        db.session.flush()
        newuser = Users(username, email, password, mobile)
        db.session.add(newuser)
        db.session.commit()
        return render_template('index.html', status="Successfully register please login")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if ('email' in session):
            return render_template('success.html')
        else:
            return redirect('/')
        
    else:
        name = str(request.form['name'])
        print name, type(name)
        pswd = str(request.form['pswd'])
        try:
            #user = Users.query.filter(username == name, email == pswd)
            user = Users.query.filter_by(username=name, password=pswd).first_or_404()
            #print user.email
            if user.username and user.email:
                session['email'] = user.email
                #return render_template('success.html', name=user.username, email=user.email)
                return redirect('/users')
        except:
            return render_template('index.html', user_exist_message="User or Password is wrong")

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('email', None)
    return redirect("/")
#    return render_template('index.html')

@app.route("/users")
def users():
    if request.method == 'GET':
        if ('email' in session):
            users = Users.query.all()
            return render_template('success.html', users=users)
        else:
            return redirect('/')
    

    

    #return jsonify_list([i.to_client() for i in users])


if __name__ == "__main__":
    app.run(debug=True)
