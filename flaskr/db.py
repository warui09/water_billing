#!/usr/bin/python3
"""Create a connection to SQLite"""

import click
import sqlite3
from flask import current_app, g


def get_db():
    """Returns a connection to sqlite database"""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
def init_db_command():
    """Clear existing data and create new tables"""
    init_db()
    click.echo('Initialized the database')
