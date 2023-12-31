#!/usr/bin/python3
"""Entry for a water billing app"""

from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from flask_login import UserMixin

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object(Config)


@app.route("/")
def index():
    """Render the home page of the app"""
    return render_template("./index.html")


@login_manager.user_loader
def load_user(user_id):
    """Return a registered user"""
    return User.query.get(int(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login a registered user"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("user_home", name=user.username))
    return render_template("login.html", title="Sign in", form=form)


@app.route("/logout")
@login_required
def logout():
    """Logout user"""
    logout_user()
    return redirect(url_for("index"))


@app.route("/user/<name>")
@login_required
def user_home(name):
    """Render user's home page"""
    return render_template("user_home.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    """Handle the page not found error"""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server error"""
    return render_template("500.html"), 500
