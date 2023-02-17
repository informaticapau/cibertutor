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
