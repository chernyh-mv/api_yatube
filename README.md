## Проект «API для Yatube»
---
Проект для знакомства с API, бибилотекой Django REST Framework, Сериализаторами и JWT.

В проекте api_yatube есть приложение posts с описанием моделей Yatube. Реализовано API для всех моделей приложения.

API доступен только аутентифицированным пользователям. Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.


**Для его создания использовались следующие технологии:**

*Python 3, Django, Django REST Framework, Simple-JWT*


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:chernyh-mv/api_yatube.git
```

```
cd api_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Cоздать базу данных и выполнить миграции

```
cd yatube_api/
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить сервер 
```
python manage.py runserver
```

___
___
*Автор: [Мария Черных](https://github.com/chernyh-mv)*
