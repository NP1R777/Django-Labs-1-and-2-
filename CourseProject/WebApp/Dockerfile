# WebApp/Dockerfile
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка зависимостей
COPY WebApp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY WebApp/ .

# Настройка CORS
ENV CORS_ALLOWED_ORIGINS=http://localhost:3000

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "127.0.0.1:8001"]