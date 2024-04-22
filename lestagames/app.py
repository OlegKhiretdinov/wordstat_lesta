from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['BABEL_LANGUAGES'] = ['ru', 'en']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@app.get('/')
def home_page():
    return render_template('page/home_page.html')


@app.get('/file/')
def file_list():
    return 'file_list'


@app.get('/file/<int:file_id>/')
def file_info(file_id):
    return f'file id {file_id}'
