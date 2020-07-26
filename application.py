import os
#import render_template
import requests
from flask import Flask, session,request, render_template,jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database

@app.route("/login")
def index():
    return render_template("index1.html")

@app.route('/response',methods=["POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]   
    #return render_template("index4.html", value=password,password1=password1)
    #password2=password1[0]
    flag1=0
    if len(password)<6:
    	flag1=1
    flag2=1
    flag22=0
    flag23=0
    x=len(password)
    for i in range(x):
        if password[i]>='0' and password[i]<='9':
            flag22=1
        if password[i]>='a' and password[i]<='z':
            flag23=1
    if flag22==1 and flag23==1:
        flag2=0   
    flag3=0           
    x2=len(username)         
    for i1 in range(x2):
    	if username[i1]<'a' or username[i1]>'z':
            flag3=1

    if username=='vaibhav' and password=='abcd12':
    	return jsonify({"status":200,"msg":"Success"}),200
    elif flag1==1:
        return jsonify({"status":201,"msg":"Failure: password should be of length 6"}),201
    elif flag2==1:
        return jsonify({"status": 202,"msg": "Failure: password to have 1 chracter and 1 number"}),202
    elif flag3==1:	
        return jsonify({"status": 203,"msg": "Failure: only characters allowed in username"}),203
            #return render_template('index5.html')


