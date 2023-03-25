from flask_db_orm import db
from datetime import datetime, date
from sqlalchemy.orm import validates


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __str__(self):
        return '<User %r id - %s>' % (self.username, self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    user = db.relationship(User, foreign_keys=[user_id, ])
    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today())
    is_visable = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r, user_id %s>'.format(self.title, self.user_id)

class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(40), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.today())
    is_visable = db.Column(db.Boolean, default=True, nullable=False)

    @validates('text')
    def validate_text(self, key, value):
        if len(value.strip()) < 5:
            raise ValueError('Длина текста должна быть не менее 5 символов')
        return value
