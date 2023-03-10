from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import ValidationError, validators, StringField, Form, PasswordField
import json
import os


class ValidForm(FlaskForm):
    email = StringField(label='Электронная почта', validators=[validators.Email('Не верный ввод почтового адреса'), validators.DataRequired('Поля обязательно для заполнения')])
    pwd = PasswordField(label='Пароль', validators=[validators.EqualTo('confirm', message='Пароли не совпадают'), validators.length(min=6, max=255, message='Длина должна быть более 6 символов')])
    confirm = PasswordField('Повторения пароля')


app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'home work 10/03/2023',
    WTF_CSRF_ENABLED = False
)

@app.route('/serve/<path:filename>')
def serve(filename):
    path = 'files/' + filename
    if os.path.isfile(path):
        with open(path) as f:
            result = f.read()
        return result
    else:
        return 'Файла с таким именем не существует', 404

@app.route('/form/user', methods=['POST'])
def form():
    json_dict = {'status': 0, 'errors': []}
    form = ValidForm(request.form)
    if form.validate():
        json_dict['status'] = 1
    for k, v in form.errors.items():
        json_dict['errors'].append(v)
    return json.dumps(json_dict, indent=4)


@app.route('/locales')
def local_json():
    json_dict = {1:'ru', 2:'en', 3:'it'}
    return json.dumps(json_dict, indent=4)

@app.route('/sum/<int:first>/<int:second>')
def sum(first, second):
    return str(int(first) + int(second))

@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello, ' + user_name

if __name__ == '__main__':
    app.run()