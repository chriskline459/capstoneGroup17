from flask import Blueprint, render_template
auth = Blueprint('auth', __name__)

@auth.route('/rewards', methods = ['GET', 'POST'])
def rewards():
    return render_template("rewards.html")

@auth.route('/progress', methods = ['GET', 'POST'])
def progress():
    return render_template("progress.html")

@auth.route('/arcade', methods = ['GET', 'POST'])
def arcade():
    return render_template("arcade.html")