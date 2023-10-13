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
from .module import ModuleRep


class TopicRep(db.Model):

    # Metadata
    __tablename__ = "topic"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    module = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)

    # Relationships
    theory = db.relationship('TheoryRep', lazy=True)
    practice = db.relationship('PracticeRep', lazy=True)

    def __repr__(self) -> str:
        return f"Topic{{'{self.id}' {self.title}'}}"


class Topic:

    def __init__(self, id: int, title: str, description: str, module: int,
                 ordinal: int) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.module = module
        self.ordinal = ordinal

    @classmethod
    def __from_TopicRep(cls, t: TopicRep):
        return cls(
            t.id,
            t.title,
            t.description,
            t.module,
            t.ordinal
        )

    @classmethod
    def get_from_module(cls, module_id: int) -> list:
        m: ModuleRep = ModuleRep.query.get(module_id)
        t: list[TopicRep] = m.topics
        return [cls.__from_TopicRep(i) for i in t]

    @classmethod
    def get_from_id(cls, id: int):
        t: TopicRep = TopicRep.query.get(id)
        return None if t is None else cls.__from_TopicRep(t)

    @staticmethod
    def exists(id: int) -> bool:
        t: TopicRep = TopicRep.query.get(id)
        return t is not None

    def belongs_to_module(self, module_id: int) -> bool:
        return self.module == module_id

    def next(self) -> int | None:
        t: TopicRep = TopicRep.query\
            .filter(TopicRep.module == self.module,
                    TopicRep.ordinal > self.ordinal)\
            .order_by(TopicRep.ordinal)\
            .first()
        return None if t is None else t.id

    def previous(self) -> int | None:
        t: TopicRep = TopicRep.query\
            .filter(TopicRep.module == self.module,
                    TopicRep.ordinal < self.ordinal)\
            .order_by(TopicRep.ordinal.desc())\
            .first()
        return None if t is None else t.id
