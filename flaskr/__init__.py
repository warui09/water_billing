#!/usr/bin/python3
"""Defines the application factory"""

from flask import Flask
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #if not testing, load the test_config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load test config if passed
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # test page
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    return app
