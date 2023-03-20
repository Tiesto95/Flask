

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_md_db import *
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    print(User.query.count())
    app.run()