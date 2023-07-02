from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("dashboard.html")

@views.route("/users")
def users():
    return render_template("users.html")