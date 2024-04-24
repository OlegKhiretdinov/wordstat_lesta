from collections import defaultdict
import string
import math

import nltk
from nltk.tokenize import word_tokenize

ALLOWED_EXTENSIONS = {'txt'}

nltk.download('punkt')
punctuation = set(string.punctuation)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def parse_txt_collection(files):
    files_stat = []
    errors = []

    for file in files:
        words = defaultdict(int)

        if allowed_file(file.filename):
            for line in file.readlines():
                try:
                    for word in word_tokenize(line.decode().lower()):
                        if word not in punctuation:
                            words[word] += 1
                except UnicodeDecodeError:
                    errors.append({"file": file.filename, "message": 'unsupported_encoding'})

        else:
            errors.append({"file": file.filename, "message": 'unsupported_format'})

        files_stat.append({"name": file.filename, "words": words})
        file.close()

    return files_stat, errors


def calculate_tf_idf(collection):
    for file in collection:
        words_count = sum(file['words'].values())
        words = file['words']
        for word in words:
            idf_c = 0
            for item in collection:
                if word in item['words']:
                    idf_c += 1

            words[word] = {
                'count': words[word],
                'tf': words[word] / words_count,
                'idf': math.log10(len(collection) / idf_c)
            }
