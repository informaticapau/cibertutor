from flaskapp.utils.db import db
from .topic import TopicRep


class PracticeRep(db.Model):

    # Metadata
    __tablename__ = "practice"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    style = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    topic = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)

    # Relationships
    answers = db.relationship('AnswersRep', lazy=True)

    def __repr__(self) -> str:
        return f"Practice{{'{self.id}' {self.title}'}}"


class Practice:

    def __init__(self, id: int, title: str, content: str, style: str,
                 topic: int, ordinal: int) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.style = style
        self.topic = topic
        self.ordinal = ordinal

    @classmethod
    def __from_PracticeRep(cls, p: PracticeRep):
        return cls(
            p.id,
            p.title,
            p.content,
            p.style,
            p.topic,
            p.ordinal
        )

    @classmethod
    def get_from_topic(cls, topic_id: int) -> list:
        t: TopicRep = TopicRep.query.get(topic_id)
        p: list[PracticeRep] = t.practice
        return [cls.__from_PracticeRep(i) for i in p]

    @classmethod
    def get_from_id(cls, id: int):
        p: PracticeRep = PracticeRep.query.get(id)
        return None if p is None else cls.__from_PracticeRep(p)

    def belongs_to_module(self, module_id: int) -> bool:
        t: TopicRep = TopicRep.query.get(self.topic)
        return t.module == module_id

    def belongs_to_topic(self, topic_id: int) -> bool:
        return self.topic == topic_id
