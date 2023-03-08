from flask import Flask

app = Flask(__name__)

@app.route('/test/<num_one>/<num_two>')
def test(num_one, num_two):
    return 'Результат сложения' + str(int(num_one) + int(num_two))


@app.route('/string/<str_one>/<str_two>/<str_three>')
def string(str_one, str_two, str_three):
    abc = ''
    result = str_one if len(str_one) >= len(str_two) else str_two
    result = result if len(result) >= len(str_three) else str_three
    return result

if __name__ == '__main__':
    app.run()