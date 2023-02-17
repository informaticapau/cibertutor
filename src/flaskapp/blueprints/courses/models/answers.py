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
