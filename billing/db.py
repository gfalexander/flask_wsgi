import sqlite3

import click
from flask import current_app, g


def init_app(app):
    # tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)

    # adds a new command that can be called with the flask command
    app.cli.add_command(init_db_command)


def init_db():
    # get_db() returns a database connection, which is used to execute the commands read from the file
    db = get_db()

    # open_resource() opens a file relative to the billing package
    with current_app.open_resource('schema.sql') as f:
        # executescript() executes the entire file as a single script
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    # clears the existing data and creates new tables
    init_db()
    click.echo('Initialized the database.')

def get_db():
    if 'db' not in g:
        # sqlite3.connect() connects to the file pointed at by the DATABASE configuration key
        # current_app is a special object that points to the Flask application handling the request
        # g is a special object that is unique for each request
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # sqlite3.Row tells the connection to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()