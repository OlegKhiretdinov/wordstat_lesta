from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel

from .utils import parse_txt_collection, calculate_tf_idf


app = Flask(__name__)
app.config['BABEL_LANGUAGES'] = ['ru', 'en']
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

babel = Babel(app)


@app.get('/')
def home_page():
    return render_template('page/home_page.html')


@app.post('/collection/add')
def add_collection():
    files = request.files.getlist("files")

    files_stat, errors = parse_txt_collection(files)
    calculate_tf_idf(files_stat)
    print(files_stat)
    collection_name = request.form.get("collection-name")

    return redirect(url_for('home_page'))


@app.get('/file/')
def file_list():
    return 'file_list'


@app.get('/file/<int:file_id>/')
def file_info(file_id):
    return f'file id {file_id}'
