# MIT License

# Copyright (c) 2023 Daniel Feito Pin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click
import yaml
from flask.cli import AppGroup
from os import environ
from flaskapp.utils import db
from ..models.phishingemail import PhishingEmailRep

db_cli = AppGroup('db', short_help="Phishing Emails' Data Base options.")

@db_cli.command('load')
def load_data():
    """Loads data from YAML files."""

    def read_file(file: str) -> dict:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
        
    try:
        file: str = environ['PHISHING_QUIZ_EMAILS']
        print(f'Extracting data from: {file}')
        
        data: dict = read_file(file)
        print(data)
        
        for email in data:
            db.session.add(PhishingEmailRep(
                from_name = email['from_name'],
                from_email = email['from_email'],
                subject = email['subject'],
                content = email['content'],
                comment = email['comment'],
                phishing_location = email['phishing_location']
            ))

        db.session.commit()
        click.echo(f"Emails loaded.")
            
    except Exception as e:
        click.echo('Error while loading data:')
        click.echo(e)
        db.session.rollback()
        
@db_cli.command('clear')
def clear_data():
    """Purges data from the Data Base without deleting the tables."""
    db.session.query(PhishingEmailRep).delete()
    db.session.commit()
    click.echo('The data base was cleared.')