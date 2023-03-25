from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models.flask_md_db import Post, User, GuessBookItem

class UserForm(ModelForm):
    class Meta:
        model = User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = ['user_id', ]

class GuessBookForm(ModelForm):
    class Meta:
        model = GuessBookItem