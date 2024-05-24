from flask import render_template, redirect
from app import create_app
from models import init_db

app = create_app()

db = init_db()

@app.route("/")
def landing():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")
