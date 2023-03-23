

from flask import Flask, request, render_template, flash

from flask_sqlalchemy import SQLAlchemy

import config as config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    from models.flask_md_db import Post, User
    from form.flash_form import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
            print('1')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = Post.query.all()
    print(posts[0].user_id)
    user = posts[0].user

    for post in posts:
        user_id = post.user_id
        user = User.query.filter_by(id=user_id).first()
        print(post.user_id, user)

        print(post.user)

    return render_template('home.txt', posts=posts)


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(username='Ivan', email='p@p.com')

    db.session.add(ivan)
    db.session.commit()  # note


if __name__ == '__main__':
    from models.flask_md_db import *
    db.create_all()

    if User.query.count() == 0:
        populate_db()
    user_test = User.query.all()

    app.run(debug=True)

