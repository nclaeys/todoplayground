from app import db
from app.utils import to_date
from datetime import date
import time

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    title = db.Column(db.String(80))
    user = db.Column(db.String(80))
    deadline = db.Column(db.Integer)

    def __init__(self, user: str, day: str, title: str, deadline: str = "01-01-2999"):
        self.day = to_date(day).toordinal()
        self.title = title
        self.deadline = deadline
        self.user = user

    def json(self):
        res = {'day': date.fromordinal(self.day), 'user': self.user, 'title': self.title}
        return res

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

    @classmethod
    def query_by_user(cls, user: str, bore_deadline = True):
        seconds = time.time()
        builder = cls.query.filter_by(user=user)
        if bore_deadline:
            builder.filter(Todo.deadline >= seconds)
        return builder.all()
