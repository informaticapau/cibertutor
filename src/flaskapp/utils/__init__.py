import click
from flask.cli import AppGroup
from .db import db

db_cli = AppGroup('db', short_help="Data Base options.")

@db_cli.command('init')
def db_init_command():
    """Creates new tables."""
    db.create_all()
    click.echo('Initialized the database.')


@db_cli.command('drop')
def db_drop_command():
    """Clears the existing data."""
    db.drop_all()
    click.echo('Dropped the database.')


@db_cli.command('restart')
def db_drop_command():
    """Same as running 'drop' and 'init'."""
    db.drop_all()
    db.create_all()
    click.echo('Restarted the database.')