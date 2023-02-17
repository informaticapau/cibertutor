from flask import Blueprint, Response, render_template, url_for

bp: Blueprint = Blueprint('tools', __name__, url_prefix='/tools',
                          static_folder='static', template_folder='templates')


__tool_list: list[dict] = [
    ('Phishing Quiz - Emails', 'phishing_quiz', 'email'),
    ('Password Checker', 'password_checker', 'password_checker', 'img/icon.png'),
]

@bp.route('/')
def index() -> Response:
    
    def tool_info(name: str, blueprint, endpoint: str, img_name: str = None):
        return {
            'name': name,
            'url': url_for(f'{blueprint}.{endpoint}'),
            'img_url': url_for(f'{blueprint}.static', filename=img_name) 
                    if img_name 
                    else url_for('static', filename='img/logo_redondo.png')
        }
    
    context: dict = {
        'tools': [tool_info(*t) for t in __tool_list]
    }
    return render_template('tools/index.html', **context)
