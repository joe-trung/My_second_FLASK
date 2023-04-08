from datetime import datetime

from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'


# db.create_all()
def init_db():
    db.create_all()
    # create a test title
    t = Task(title="First Title", date=datetime.utcnow())
    db.session.add(t)
    db.session.commit()

    # create a another test title
    t = Task(title="First Title", date=datetime.utcnow())
    db.session.add(t)
    db.session.commit()


if __name__ == '__main__':
    init_db()
