from flask import render_template, request
from app.models.sys import SysUsers
from . import auth
from app.utils.crud import create

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    data = request.form.to_dict(flat=True)
    print(data)
    if request.method == "POST" and data:
        create(data, SysUsers)

    return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

