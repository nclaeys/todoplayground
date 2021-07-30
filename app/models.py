from app import db
from app.utils import to_date
from datetime import date

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    title = db.Column(db.String(80))

    def __init__(self, day: str, title: str):
        self.day = to_date(day).toordinal()
        self.title = title

    def json(self):
        return {'day': date.fromordinal(self.day), 'title': self.title}

    @classmethod
    def get_all(cls):
        return [res.json() for res in cls.query.all()]

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def query_by_day(cls, day: str):
        todos_by_day = cls.query.filter_by(day=to_date(day).toordinal()).all()
        return todos_by_day
