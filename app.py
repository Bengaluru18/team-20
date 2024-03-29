import os
from flask import Flask
from flask import request
import json
from flask import render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route('/signUpUser')
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})
    
if __name__ == "__main__":
    app.run()

 