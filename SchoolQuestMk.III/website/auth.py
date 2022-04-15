from flask import Blueprint, request, flash, render_template, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # 'methods' contains the types of accepted HTTP requests
def login():
    if request.method == 'POST':
        email = request.form.get('email') # Retrieves the 'email' tag from the database 
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))  # command used to go to another page
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user) # displays 'Login' on page via html

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login')) # redirects user to login page

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
            
            
    return render_template("sign_up.html", user=current_user)

@auth.route('/rewards', methods = ['GET', 'POST'])
def rewards():
    return render_template("rewards.html", user=current_user)
    
@auth.route('/quiz', methods = ['GET', 'POST'])
def quiz():
    return render_template("student-take-quiz.html", user=current_user)

@auth.route('/quizResults', methods = ['GET', 'POST'])
def quizResults():
    return render_template("student-quiz-results.html", user=current_user)

@auth.route('/arcade', methods = ['GET', 'POST'])
def arcade():
    if request.method == 'POST':
        pts = request.form.get('note')
        new_points = Note(data=pts, user_id=current_user.id)
        db.session.add(new_points)
        db.session.commit()
        flash('Points added!', category='success')
    return render_template("arcade.html", user=current_user)

@auth.route('/progress', methods = ['GET', 'POST'])
def progress():
    return render_template("progress.html", user=current_user)

@auth.route('/profile', methods = ['GET', 'POST'])
def profile():
    return render_template("profile.html", user=current_user)
