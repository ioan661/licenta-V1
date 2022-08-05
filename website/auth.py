from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username = username).first()
        if user: 
            if check_password_hash(user.password, password): 
                flash('Bun venit '+ user.prenume, category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.notes'))
            else:
                flash('Logare esuata! ', category='error')
        else: 
            flash('Nu exista utilizatorul!', category='error')


    return render_template("login.html", user=current_user)



@auth.route('/register/', methods=['GET', 'POST'])
@login_required
def register(): 
    if request.method == 'POST': 
        email = request.form.get('email')
        username = request.form.get('username')
        prenume = request.form.get('prenume')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        email_user = User.query.filter_by(email=email).first()
        username_user = User.query.filter_by(email=email, username=username).first()
        if email_user: 
            print(email_user.email)
            flash('Exista deja un utilizatorul cu aceasta adresa!', category='error')
        elif username_user: 
            flash('Exista deja un utilizatorul cu acest username!', category='error')

        elif(len(email) < 6):
            flash("Email is incorect!", category='error')
        elif len(username) < 4: 
            flash("Username is too short!", category='error')
        elif password != password2: 
            flash("Parolele nu corepund!", category='error') 
        elif len(password) < 5: 
            flash("Parola trebuie sa fie mai lunga!", category='error')
        else: 
            new_user = User(email= email,username=username, prenume= prenume, password = generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Cont creat! ', category='succes')
            return redirect(url_for('views.home'))
        
    return render_template("register.html", user = current_user)


@auth.route('/logout')
@login_required 
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))
