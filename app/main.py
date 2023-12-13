#!/usr/bin/python3
"""Entry for a water billing app"""

from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.forms import LoginForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object(Config)

@app.route('/')
def index():
    """Render the home page of the app"""
    return render_template('./index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        #login code
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

@app.route('/user/<name>')
def user_home():
    """Render the user's home page on login"""
    return render_template('user_home.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle the page not found error"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server error"""
    return render_template('500.html'), 500
