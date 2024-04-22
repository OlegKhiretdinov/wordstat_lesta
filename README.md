# Расчёт частоты слов в документах (tf, idf) 

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