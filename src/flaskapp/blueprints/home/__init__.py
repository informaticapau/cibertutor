from flask import Blueprint, render_template 

bp: Blueprint = Blueprint('home', __name__, url_prefix='/home', 
                          static_folder='static', template_folder='templates')

@bp.route("/")
def index() -> str:
    return render_template('home/index.html')