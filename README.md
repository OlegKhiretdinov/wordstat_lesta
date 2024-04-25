# Расчёт частоты слов
Расчитывает показатели [tf и idf](https://ru.wikipedia.org/wiki/TF-IDF) в коллекции .txt файлов

## Зависимости
* Python >= 3.10
* Poetry 1.4
* PostgreSQL 16

## Развёртывание



Список необходимых переменных в файле .env_EXAMPLE

Для работы с базами данных используются библиотеки SQLAlchemy и Alembic

## Миграции
В корне проекта выполнить
* Создать миграцию.
```commandline
alembic revision --autogenerate -m "migration_name_optional"
```
* Применить миграцию
```commandline
alembic upgrade head
```

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