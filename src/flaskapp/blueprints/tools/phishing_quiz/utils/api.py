from flask import Blueprint, Response, abort
from ..models import PhishingEmail

bp: Blueprint = Blueprint('api_phishing_quiz', __name__, url_prefix='/api/phishing_quiz',
                          static_folder='static', template_folder='templates')

@bp.route('/<int:id>')
def email_id(id: int) -> Response:
    
    phi = PhishingEmail.get_from_id(id)
    
    if phi is None:
        abort(404)
    
    return {
        'id': phi.id,
        'from_name': phi.from_name,
        'from_email': phi.from_email,
        'subject': phi.subject,
        'content': phi.content,
        'comment': phi.comment,
        'phishing_location': phi.phishing_location,
        'next': phi.next()
    }
