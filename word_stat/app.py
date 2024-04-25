import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from .models import Word, File, FileCollection
from .utils import parse_txt_collection, calculate_tf_idf

app = Flask(__name__)
load_dotenv()

app.config['BABEL_LANGUAGES'] = ['ru']
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

babel = Babel(app)

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(f'postgresql://{DATABASE_URL}', echo=True)


@app.get('/')
def home_page():
    return render_template('page/home_page.html')


@app.post('/collection/add')
def add_collection():
    files = request.files.getlist("files")
    collection_name = request.form.get("collection-name")
    files_stat = parse_txt_collection(files)
    calculate_tf_idf(files_stat)

    with Session(engine) as session:
        collection = FileCollection(name=collection_name)
        session.add(collection)
        session.flush()
        collection_id = collection.id

        for item in files_stat:
            file = File(name=item["name"], status=item["status"], collection_id=collection_id)
            session.add(file)
            session.flush()
            file_id = file.id

            if words := item.get("words"):
                session.add_all([Word(word=word, file_id=file_id, **words[word]) for word in words])

        session.commit()

    return redirect(url_for('collection_info', collection_id=collection_id))


@app.get('/collection/')
def collections_list():
    limit = int(request.values.get("limit", 10))
    page = int(request.values.get("page", 1))

    with Session(engine) as session:
        query = select(
            FileCollection.id,
            FileCollection.name,
            FileCollection.created_at
        ).limit(limit).offset(limit * (page - 1))
        collections = session.execute(query).all()

    return render_template('page/collections_list.html', collections=collections)


@app.get('/collection/<int:collection_id>/')
def collection_info(collection_id):
    limit = int(request.values.get("limit", 50))
    page = int(request.values.get("page", 1))

    with Session(engine) as session:
        query = select(
            Word.word,
            Word.count,
            Word.tf,
            Word.idf,
            File.name).\
            join(File).\
            where(File.collection_id == collection_id).\
            limit(limit).offset(limit * (page - 1)).order_by(Word.idf.desc())

        words = session.execute(query).all()

        coll_query = select(FileCollection.id, FileCollection.name, FileCollection.created_at).\
            where(FileCollection.id == collection_id)

        collection = session.execute(coll_query).fetchone()

    return render_template('page/collection_info.html', words=words, collection=collection)
