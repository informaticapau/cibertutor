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

from flask import Blueprint, Response, render_template, url_for

bp: Blueprint = Blueprint('tools', __name__, url_prefix='/tools',
                          static_folder='static', template_folder='templates')


__tool_list: list[dict] = [
    ('Phishing Quiz - Emails', 'phishing_quiz', 'email', 'img/icon.png'),
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
