from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from WebGit import app, db, lm, db_service
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]   
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        flash('Login="' + form.email.data + '", password=' + str(form.password.data) + '", remember_me=' + str(form.remember_me.data))
        return db_service.try_login(form.email.data, form.password.data)
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        )

@app.route('/logout')
@login_required
def logout():    
    logout_user()
    return redirect(url_for('index'))