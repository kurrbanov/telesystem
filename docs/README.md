# Система учёта абонентов телефонной сети

## О проекте:
Проект представляет из себя полноценный CRUD с возможностью создавать абонента, просматривать, изменять и удалять его данные.

## Как запустить проект у себя?

### Приготовления
Для начала клонируйте репозиторий и определите переменные окружения в файле src/.env.example
```
git clone https://github.com/kurrbanov/telesystem.git
```
Переименуйте файл .env.example в .env и измените переменные окружения:
```
mv .env.example .env
```

```bash
SECRET_KEY="your-secret-key"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_DB="name_of_db"
```

### Вариант с Docker
Для этого должен быть установлен Docker
Поднимает
```
docker-compose up -d --build
```
И откройте в браузере **http://0.0.0.0:8000**


### Вариант без Docker
Установите poetry:
```
pip install poetry
```
Перейдите в папку */src*
```
cd src
```
И активируйте вирутальное окружение:
```
poetry shell
poetry install
```
Накатите миграции и запустите сервер:
```
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py runserver
```
И откройте в браузере **http://0.0.0.0:8000**
