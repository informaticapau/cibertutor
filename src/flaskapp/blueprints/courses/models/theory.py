from flaskapp.utils.db import db
from .topic import TopicRep


class TheoryRep(db.Model):

    # Metadata
    __tablename__ = "theory"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    topic = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Theory{{'{self.id}' {self.title}'}}"


class Theory:

    def __init__(self, id: int, title: str, content: str, topic: int,
                 ordinal: int) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.topic = topic
        self.ordinal = ordinal

    @classmethod
    def __from_TheoryRep(cls, th: TheoryRep):
        return cls(
            th.id,
            th.title,
            th.content,
            th.topic,
            th.ordinal
        )

    @classmethod
    def get_from_topic(cls, topic_id: int) -> list:
        t: TopicRep = TopicRep.query.get(topic_id)
        th: list[TheoryRep] = t.theory
        return [cls.__from_TheoryRep(i) for i in th]

    @classmethod
    def get_from_id(cls, id: int):
        th: TheoryRep = TheoryRep.query.get(id)
        return None if th is None else cls.__from_TheoryRep(th)

    def belongs_to_module(self, module_id: int) -> bool:
        t: TopicRep = TopicRep.query.get(self.topic)
        return t.module == module_id

    def belongs_to_topic(self, topic_id: int) -> bool:
        return self.topic == topic_id
