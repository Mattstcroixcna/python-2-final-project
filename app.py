from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/library")
def ibrary():
    return render_template('library.html')

app.run()