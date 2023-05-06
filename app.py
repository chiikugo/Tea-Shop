from flask import Flask, render_template, redirect, url_for

#from flask_sqlalchemy import SQLAlchemy
#i want to use python, genja and an api for this project

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/tea')
def tea():
    return "<h2> This is a tea page, made by us! .. <h2>"

if __name__ == '__main__':
    app.run()

@app.route('/button')
def button():
    return render_template("button.html")