from flask import request, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, Form, ValidationError, validators
import datetime


def validate_job(form, field):
    ls = ['IT', 'Bank', 'HR']
    if field.data not in ls:
        raise ValidationError('Ваша специальность нам не подходит')

def validate_age(form, field):
    ls = field.data.split('.')
    age_date = datetime.datetime.now()
    if not age_date.month == int(ls[1]):
        raise ValidationError('Приходите в другой месяц')


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[validators.Length(min=3, max=25)])
    email = StringField(label='Email', validators=[validators.Length(min=6, max=35), validators.Email()])
    job = StringField(label='Work', validators=[validators.DataRequired(), validate_job])
    age = StringField(label='Age', validators=[validators.DataRequired(), validate_age])


app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'This my key the best of the best',
    WTF_CSRF_ENABLED=False
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('Invalid', 400)
    if request.method == 'GET':
        return 'hello word!!', 200

if __name__ == '__main__':
    app.run()