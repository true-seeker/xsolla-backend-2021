
# xsolla-backend-2021
#### Этот репозиторий является тестовым заданием для Xsoola Summer School 2021 по направлению Backend.

Язык реализации: Python 3.9

Веб-фреймворк: Django 3.1.6

## Демонстрация работы на heroku

Веб-приложение установлено на heroku по [ссылке](https://xsolla-backend-2021.herokuapp.com/). По умолчанию  страница редиректит на этот репозиторий

## API

По умолчанию, доступ к api осуществляется через https://xsolla-backend-2021.herokuapp.com/api/.

Например, чтобы получить список всех товаров, необходимо отправить GET запрос по адресу https://xsolla-backend-2021.herokuapp.com/api/products/

##### Более подробная документация описана с помощью сервиса Swagger [по ссылке](https://app.swaggerhub.com/apis-docs/true-seeker/xsolla-backend-2021/)

## Локальное развёртывание


Чтобы осуществить локальное развёртывание, необходимо: 
1. Установить Python версии 3.5 и выше. [Ссылка для скачивания](https://www.python.org/)

   
2. Клонировать репозиторий на локальную машину
`git clone https://github.com/true-seeker/xsolla-backend-2021/`
   
   
3. Установить все необходимые пакеты с помощью пакетного менеджера из файла `requirements.txt`

`pip install -r requirements.txt`

Рекомендуется воспользоваться виртуальным окружением для установки пакетов.

4. Запустить сервер из корневой папки с помощью команды:
`python manage.py runserver`
   
При успешном запуске в терминале будет примерно такое сообщение:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 05, 2021 - 17:36:34
Django version 3.2.4, using settings 'xsolla_backend_2021.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
5. Зайти на сайт по адресу `http://127.0.0.1:8000/`. Должен произойти редирект на этот репозиторий.


6. Доступ к api осуществляется по адресу `http://127.0.0.1:8000/api/`

## Реализованные доп. задания

| Задание | Статус |
| ------ | ------ |
| Фильтрация товаров по их типу и/или стоимости в методе получения каталога товаров. |✅|
| Спецификация OpenAPI 2.0 или 3.0 |✅| 
| Dockerfile для создания образа приложения системы.  |❌|
| Модульные и функциональные тесты |❌|
| Развертывание приложения на любом публичном хостинге |✅|
