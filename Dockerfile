# Использовать официальный Docker-образ Python
FROM python:3.9

# Указать рабочую папку
WORKDIR /app

# Скопировать все файлы из текущей директории в контейнер
COPY . /app

# Установить зависимости с помощью pip
RUN pip install -r requirements.txt

# Открыть порт для принятия запросов
EXPOSE 8000

# Запустить Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
