from flask import Flask, request
import random
from flask_wtf import FlaskForm
from wtforms import ValidationError, validators, Form, IntegerField


class ValidForm(FlaskForm):
    number = IntegerField(label='Число', validators=[validators.DataRequired('Вы не ввели число')])

class ObjNumber():
    rand_number = None

    @classmethod
    def rand_num(cls):
        cls.rand_number = random.randint(1, 101)

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='home work 14/03/2023',
    WTF_CSRF_ENABLED=False,
    FLASK_RANDOM_SEED=1
)


@app.route('/')
def home():
    ObjNumber.rand_num()
    return 'Число загадано'

@app.route('/guess', methods=['POST'])
def guess():
    form = request.form
    valid_form = ValidForm(form)
    if valid_form.validate():
        rand_number = ObjNumber.rand_number
        num = int(form['number'])
        if  num > rand_number:
            return 'Меньше'
        elif num < rand_number:
            return 'Больше'
        else:
            ObjNumber.rand_num()
            return 'Угадал'
    else:
        return 'Ошибка валидации'

if __name__ == '__main__':
    random.seed(app.config['FLASK_RANDOM_SEED'])
    ObjNumber.rand_num()
    app.run()
