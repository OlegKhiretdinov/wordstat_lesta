# Расчёт частоты слов
Расчитывает показатели [tf и idf](https://ru.wikipedia.org/wiki/TF-IDF) в коллекции .txt файлов

## Зависимости
* Python >= 3.10
* Poetry 1.4
* PostgreSQL 16

## Развёртывание
* Указать необходимые переменные окружения в .env(список в файле .env_EXAMPLE).
* Установить зависимости
```commandline
poetry install
```
* Создать таблицы в бд.
```commandline
alembic upgrade head
```

## Запуск
### Для разработки
```commandline
make dev
```
### Продакшн
```commandline
make start
```

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
[doc](https://python-babel.github.io/flask-babel/#translating-applications)

 В папке с приложением:
 * создать новый messages.pot
```commandline
 make add_pot
```
* обновить фаилы локализаций
```commandline
make update_translation
```
* отредактировать фаилы локализаций .po
* Обновить локализацию
```commandline
make translate
```