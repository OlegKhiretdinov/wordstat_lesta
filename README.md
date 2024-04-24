# Расчёт частоты слов
Расчитывает показатели [tf и idf](https://ru.wikipedia.org/wiki/TF-IDF) в коллекции .txt файлов

## Зависимости
* Python >= 3.10
* Poetry 1.4

## Обновление локализации

 В папке с приложением:
 * обновить messages.pot
```commandline
 pybabel extract -F babel.cfg -o messages.pot .
```
* Обновить локализацию
```commandline
pybabel update -i messages.pot -d translations
```