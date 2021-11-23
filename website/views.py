from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')   # displays 'home.html' whenever the '/' route is accessed
def home():
    return render_template("home.html")




