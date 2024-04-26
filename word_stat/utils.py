import math
import string
from collections import defaultdict

import nltk
from nltk.tokenize import word_tokenize

ALLOWED_EXTENSIONS = {'txt'}

nltk.download('punkt')
punctuation = set(string.punctuation)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def parse_txt_collection(files):
    files_stat = []

    for file in files:
        words = defaultdict(int)

        if allowed_file(file.filename):
            try:
                for line in file.readlines():
                    for word in word_tokenize(line.decode().lower()):
                        if word not in punctuation:
                            words[word] += 1
                files_stat.append({"name": file.filename, "status": "parsed", "words": words})
            except UnicodeDecodeError:
                files_stat.append({"name": file.filename, "status": 'unsupported_encoding'})

        else:
            files_stat.append({"name": file.filename, "status": 'unsupported_format'})

        file.close()

    return files_stat


def calculate_tf_idf(collection):
    """
    Изменяет коллекцию. Добавляет к словам значения tf, idf
    :param collection:
    :return: None
    """
    for file in collection:
        if "words" not in file:
            continue
        print(file)
        words_count = sum(file['words'].values())
        words = file['words']
        for word in words:
            idf_c = 0
            for item in collection:
                if "words" in item and word in item['words']:
                    idf_c += 1

            words[word] = {
                'count': words[word],
                'tf': words[word] / words_count,
                'idf': math.log10(len(collection) / idf_c)
            }


def get_paginator_obj(limit, page, items_count):
    limit = max(limit, 1)
    pages_count = math.ceil(items_count / limit)
    current_page = min((1 if page < 1 else page), pages_count)

    return {'limit': limit, 'current_page': current_page, 'pages_count': pages_count}
