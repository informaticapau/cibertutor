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
from .utils.api import api_courses, api_course, api_exercise, api_exercises, api_lesson, \
    api_lessons, api_subtopics, api_topic, api_topics
from .utils import db_cli

bp: Blueprint = Blueprint('courses', __name__, url_prefix='/courses',
                          static_folder='static', template_folder='templates')


bp.cli.help = "Options to manage the courses."
bp.cli.add_command(db_cli)


@bp.route('/')
def courses() -> Response:

    context: dict = {
        'title': 'Courses',
        'courses': api_courses(),
    }

    return render_template('courses/courses.html', **context)


@bp.route('/<int:id1>')
def course(id1: int) -> Response:

    topic_list: list[dict] = api_topics(id1)

    for t in topic_list:
        id2: int = t['id']

        topic: dict = api_topic(id1, id2)
        t['description'] = topic['description']

        t['subtopics'] = api_subtopics(id1, id2)

    context: dict = {
        'title': 'Courses',
        'course_info': api_course(id1),
        'topics': topic_list
    }
    
    # Pagination
    pagination: dict = context['course_info']['pagination']

    previous: int | None = pagination['previous']
    if previous is not None:
        previous: str = url_for('courses.course', id1=previous)

    next: int | None = pagination['next']
    if next is not None:
        next: str = url_for('courses.course', id1=next)

    context['pagination'] = {
        'previous': previous,
        'back': url_for('courses.courses'),
        'next': next
    }

    return render_template('course/course.html', **context)


@bp.route('/<int:id1>/topics/<int:id2>/lessons/<int:id3>')
def lesson(id1: int, id2: int, id3: int) -> Response:

    context: dict = {
        'dto': api_lesson(id1, id2, id3),
    }
    
    # Pagination
    pagination: dict = context['dto']['pagination']

    previous: list | None = pagination['previous']
    if previous is not None:
        previous: str = url_for(f'courses.{previous[0]}', id1=id1, id2=id2,
                                id3=previous[1])

    next: int | None = pagination['next']
    if next is not None:
        next: str = url_for(f'courses.{next[0]}', id1=id1, id2=id2, id3=next[1])

    context['pagination'] = {
        'previous': previous,
        'back': url_for('courses.course', id1=id1),
        'next': next
    }

    return render_template('subtopic/lesson.html', **context)


@bp.route('/<int:id1>/topics/<int:id2>/exercises/<int:id3>')
def exercise(id1: int, id2: int, id3: int) -> Response:

    context: dict = {
        'dto': api_exercise(id1, id2, id3),
    }
    
    # Pagination
    pagination: dict = context['dto']['pagination']

    previous: list | None = pagination['previous']
    if previous is not None:
        previous: str = url_for(f'courses.{previous[0]}', id1=id1, id2=id2,
                                id3=previous[1])

    next: int | None = pagination['next']
    if next is not None:
        next: str = url_for(f'courses.{next[0]}', id1=id1, id2=id2, id3=next[1])

    context['pagination'] = {
        'previous': previous,
        'back': url_for('courses.course', id1=id1),
        'next': next
    }

    return render_template('subtopic/exercise.html', **context)
