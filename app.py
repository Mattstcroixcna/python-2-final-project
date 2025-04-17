from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta
import os
import uuid
app = Flask(__name__)
app.secret_key = "gaming"
allowed_types = [".png", ",jpg"]
save_location = "static/images"

@app.route("/")
def home():
    return render_template('index.html')

app.route("/remove")
def remove_game():
    return render_template('remove.html')
    
@app.route("/library", methods=["GET"])
def index():
    if "videoGames" not in session:
        print("clearing games")
        session["videoGames"] = []

    print(session.get("videoGames"))
    return render_template("library.html",games=session.get("videoGames"), file_location=save_location)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        if "videoGames" not in session:
            print("Clearing session data")
            session["videoGames"] = []
        name = request.form.get("name", "invalid")
        rate = request.form.get("rate", "invalid")
        year = request.form.get("year", "invalid")
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            extension = os.path.splitext(uploaded_file.filename)[1]
            if extension in allowed_types:
                unique_name = f"{uuid.uuid4().hex}{extension}"
                filename = os.path.join(save_location, unique_name)
                uploaded_file.save(filename)
                session["videoGames"].append({"name": name, "rate": rate, "year": year, "image": unique_name})
            else:
                flash("The file is of the wrong type", "error")
                return redirect("./add")


        print(session.get("videoGames"))
        session.modified = True
        return redirect("/library")


app.run()