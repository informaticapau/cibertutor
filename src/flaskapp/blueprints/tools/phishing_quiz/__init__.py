from flask import Blueprint, Response, render_template
from .utils import db_cli

bp: Blueprint = Blueprint('phishing_quiz', __name__, url_prefix='/phishing_quiz',
                          static_folder='static', template_folder='templates')

bp.cli.help = "Options to manage the phishing email tool."
bp.cli.add_command(db_cli)


@bp.route('/emails')
def email() -> Response:
    return render_template('phishing_quiz/email.html')
