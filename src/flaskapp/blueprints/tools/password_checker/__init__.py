from flask import Blueprint, Response, render_template

bp: Blueprint = Blueprint('password_checker', __name__, url_prefix='/password_checker',
                          static_folder='static', template_folder='templates')


@bp.route('/')
def password_checker() -> Response:
    return render_template('password_checker/password_checker.html')