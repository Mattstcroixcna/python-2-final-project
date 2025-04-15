from flask import Flask, render_template 
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/library")
def ibrary():
    return render_template('library.html')

@app.route("/add")
def add():
    return render_template('add.html')


app.run()