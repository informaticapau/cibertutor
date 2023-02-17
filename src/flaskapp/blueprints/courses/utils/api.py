from flask import Blueprint, url_for, abort
from flaskapp.blueprints.courses.models import Module, Topic, Theory, \
    Practice, Answer

bp: Blueprint = Blueprint('api_courses', __name__, url_prefix='/api/courses')


@bp.route('/')
def api_courses() -> list[dict]:

    # Get data
    module_list: list[Module] = Module.get_all()

    # Make DTO
    dto: list[dict] = [] if module_list == [] else [
        {
            'id': m.id,
            'icon': url_for('courses.static', filename=f'img/{m.icon}') \
                if m.icon \
                else url_for('courses.static', filename='img/default.png'),
            'link': url_for(f'api_courses.api_course', id1=m.id),
            'ordinal': m.ordinal,
            'title': m.title,
        } for m in module_list
    ]

    return dto


@bp.route('/<int:id1>')
def api_course(id1: int) -> dict:

    # Get data
    m: Module = Module.get_from_id(id1)

    if m is None:
        abort(404)

    # Make DTO
    dto: dict = {
        'id': m.id,
        'title': m.title,
        'description': m.description,
        'ordinal': m.ordinal,
    }

    # Pagination
    pagination: dict[str, int | None] = {
        'previous': m.previous(),
        'next': m.next(),
    }
    dto['pagination'] = pagination

    return dto


@bp.route('/<int:id1>/topics/')
def api_topics(id1: int) -> list[dict]:

    # Get data
    if not Module.exists(id1):
        abort(404)

    topics_list: list[Topic] = Topic.get_from_module(id1)

    # Make DTO
    dto: list[dict] = []

    if topics_list != []:
        dto = [
            {
                'id': t.id,
                'link': url_for(f'api_courses.api_topic', id1=id1, id2=t.id),
                'ordinal': t.ordinal,
                'title': t.title,
            } for t in topics_list
        ]
        dto.sort(key=lambda x: x['ordinal'])

    return dto


@bp.route('/<int:id1>/topics/<int:id2>')
def api_topic(id1: int, id2: int) -> dict:

    # Get data
    if not Module.exists(id1):
        abort(404)

    t: Topic = Topic.get_from_id(id2)

    if t is None or not t.belongs_to_module(id1):
        abort(404)

    # Make DTO
    dto: dict = {
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'module': t.module,
        'ordinal': t.ordinal,
    }

    # Pagination
    pagination: dict[str, int | None] = {
        'previous': t.previous(),
        'next': t.next(),
    }
    dto['pagination'] = pagination

    return dto


@bp.route('/<int:id1>/topics/<int:id2>/lessons/')
def api_lessons(id1: int, id2: int) -> list[dict]:

    # Get data
    if not Module.exists(id1) or not Topic.exists(id2):
        abort(404)

    theory_list: list[Theory] = Theory.get_from_topic(id2)

    # Make DTO
    dto: list[dict] = [] if theory_list == [] else [
        {
            'id': th.id,
            'link': url_for(f'api_courses.api_lesson', id1=id1, id2=id2, \
                id3=th.id),
            'ordinal': th.ordinal,
            'title': th.title,
            'topic': th.topic,
        } for th in theory_list
    ]

    return dto


@bp.route('/<int:id1>/topics/<int:id2>/exercises/')
def api_exercises(id1: int, id2: int) -> list[dict]:

    # Get data
    if not Module.exists(id1) or not Topic.exists(id2):
        abort(404)

    practice_list: list[Practice] = Practice.get_from_topic(id2)

    # Make DTO
    dto: list[dict] = [] if practice_list == [] else [
        {
            'id': p.id,
            'link': url_for(f'api_courses.api_exercise', id1=id1, id2=id2, \
                id3=p.id),
            'ordinal': p.ordinal,
            'title': p.title,
            'topic': p.topic,
        } for p in practice_list
    ]

    return dto


@bp.route('/<int:id1>/topics/<int:id2>/subtopics/')
def api_subtopics(id1: int, id2: int) -> list[dict]:

    dto: list[dict] = []

    for i in api_lessons(id1, id2):
        i['type'] = 'lesson'
        dto.append(i)

    for i in api_exercises(id1, id2):
        i['type'] = 'exercise'
        dto.append(i)

    dto.sort(key=lambda x: x['ordinal'])

    return dto


@bp.route('/<int:id1>/topics/<int:id2>/lessons/<int:id3>')
def api_lesson(id1: int, id2: int, id3: int) -> dict:

    # Get data
    th: Theory = None
    previous: int = None
    next: int = None
    s = api_subtopics(id1, id2)
    for i in range(len(s)):
        if s[i]['id'] == id3 and s[i]['type'] == 'lesson':
            th = Theory.get_from_id(id3)
            break

    if th is None:
        abort(404)

    # Pagination
    if i > 0:
        previous = (s[i-1]['type'], s[i-1]['id'])
    if i < len(s)-1:
        next = (s[i+1]['type'], s[i+1]['id'])

    # Make DTO
    dto: dict = {
        'content': th.content,
        'id': th.id,
        'ordinal': th.ordinal,
        'title': th.title,
        'topic': th.topic,
        'pagination': {
            'previous': previous,
            'next': next
        }
    }

    return dto


@bp.route('/<int:id1>/topics/<int:id2>/exercises/<int:id3>')
def api_exercise(id1: int, id2: int, id3: int) -> dict:

    # Get data
    p: Practice = None
    previous: int = None
    next: int = None
    s = api_subtopics(id1, id2)
    for i in range(len(s)):
        if s[i]['id'] == id3 and s[i]['type'] == 'exercise':
            p = Practice.get_from_id(id3)
            break

    if p is None:
        abort(404)

    # Pagination
    if i > 0:
        previous = (s[i-1]['type'], s[i-1]['id'])
    if i < len(s)-1:
        next = (s[i+1]['type'], s[i+1]['id'])

    # Make DTO
    dto: dict = {
        'answers': [{
            'id': a.id,
            'content': a.content,
            'is_solution': a.is_solution
        } for a in Answer.get_from_practice(p.id)],
        'content': p.content,
        'id': p.id,
        'ordinal': p.ordinal,
        'style': p.style,
        'title': p.title,
        'topic': p.topic,
        'pagination': {
            'previous': previous,
            'next': next
        }
    }

    return dto
