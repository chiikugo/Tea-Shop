from flask import Flask, render_template, redirect, url_for

#from flask_sqlalchemy import SQLAlchemy
#i want to use python, genja and an api for this project

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/tea')
def tea():
    return render_template("tea.html")

@app.route('/poem1')
def poem1():
    return render_template("poem1.html")

