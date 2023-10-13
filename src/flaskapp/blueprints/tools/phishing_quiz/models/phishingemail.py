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


class PhishingEmailRep(db.Model):

    # Metadata
    __tablename__ = "phishing_email"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    from_name = db.Column(db.String(20), nullable=False)
    from_email = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    phishing_location = db.Column(db.String(20), nullable=True)


class PhishingEmail:

    def __init__(self, id: int, from_name: str, from_email: str, subject: str,
                 content: str, comment: str, phishing_location: str) -> None:
        self.id: int = id
        self.from_name: str = from_name
        self.from_email: str = from_email
        self.subject: str = subject
        self.content: str = content
        self.comment: str = comment
        self.phishing_location: str = phishing_location

    @classmethod
    def __from_PhishingEmailRep(cls, phi: PhishingEmailRep):
        return cls(
            phi.id,
            phi.from_name,
            phi.from_email,
            phi.subject,
            phi.content,
            phi.comment,
            phi.phishing_location
        )

    @classmethod
    def get_from_id(cls, id: int):
        phi: PhishingEmailRep = PhishingEmailRep.query.get(id)
        return cls.__from_PhishingEmailRep(phi) if phi else None
    
    def next(self) -> int | None:
        e: PhishingEmailRep = PhishingEmailRep.query\
            .filter(PhishingEmailRep.id > self.id)\
            .order_by(PhishingEmailRep.id)\
            .first()
        return None if e is None else e.id