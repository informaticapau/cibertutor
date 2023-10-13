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


class ModuleRep(db.Model):

    # Metadata
    __tablename__ = "module"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)
    icon = db.Column(db.String(20), nullable=True)

    # Relationships
    topics = db.relationship('TopicRep', lazy=True)

    def __repr__(self) -> str:
        return f"Module{{'{self.id}' {self.title}'}}"


class Module:
    def __init__(self, id: int, title: str, description: str,
                 ordinal: int, icon: str) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.ordinal = ordinal
        self.icon = icon

    @classmethod
    def __from_ModuleRep(cls, m: ModuleRep):
        return cls(
            m.id,
            m.title,
            m.description,
            m.ordinal,
            m.icon
        )

    @classmethod
    def get_all(cls) -> list:
        m: list[ModuleRep] = ModuleRep.query.order_by(ModuleRep.ordinal).all()
        return [cls.__from_ModuleRep(i) for i in m]

    @classmethod
    def get_from_id(cls, id: int):
        m: ModuleRep = ModuleRep.query.get(id)
        return None if m is None else cls.__from_ModuleRep(m)

    @staticmethod
    def exists(id: int) -> bool:
        m: ModuleRep = ModuleRep.query.get(id)
        return m is not None

    def next(self) -> int | None:
        m: ModuleRep = ModuleRep.query\
            .filter(ModuleRep.ordinal > self.ordinal)\
            .order_by(ModuleRep.ordinal)\
            .first()
        return None if m is None else m.id

    def previous(self) -> int | None:
        m: ModuleRep = ModuleRep.query\
            .filter(ModuleRep.ordinal < self.ordinal)\
            .order_by(ModuleRep.ordinal.desc())\
            .first()
        return None if m is None else m.id
