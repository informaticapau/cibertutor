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

from flaskapp.utils.db import db
from .practice import PracticeRep


class AnswersRep(db.Model):

    # Metadata
    __tablename__ = "answers"

    # Columns
    practice = db.Column(db.Integer, db.ForeignKey(
        'practice.id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False)
    is_solution = db.Column(db.Boolean, nullable=False,
                            default=False)  # 'True' or 'False'

    def __repr__(self) -> str:
        return f"Answers{{{self.practice} {self.id} '{self.content}' {self.is_solution}}}"


class Answer:

    def __init__(self, practice: int, id: int, content: str,
                 is_solution: bool) -> None:
        self.practice = practice
        self.id = id
        self.content = content
        self.is_solution = is_solution

    @classmethod
    def __from_AnswerRep(cls, a: AnswersRep):
        return cls(
            a.practice,
            a.id,
            a.content,
            a.is_solution
        )

    @classmethod
    def get_from_practice(cls, practice_id: int) -> list:
        p: PracticeRep = PracticeRep.query.get(practice_id)
        a: list[AnswersRep] = p.answers
        return [cls.__from_AnswerRep(i) for i in a]
