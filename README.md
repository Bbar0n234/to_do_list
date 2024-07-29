# Приложение "To Do List"

## Обзор

Добро пожаловать в административное приложение "To Do List", созданное для управления пользователями и их задачами. Это веб-приложение разработано с использованием FastAPI, PostgreSQL и Alembic. С его помощью администраторы могут просматривать, добавлять и удалять пользователей, а также управлять их задачами.

## Функциональные возможности

- **Управление пользователями**: просмотр списка всех пользователей, создание новых пользователей и удаление существующих.
- **Управление задачами пользователей**: просмотр задач конкретного пользователя, создание новых задач и удаление существующих задач.

## Установка и запуск

### 1. Создание .env файла

Перед запуском приложения необходимо создать файл `.env` в корневой директории проекта. Вы можете скопировать и переименовать файл `.env_example` в `.env`, а затем заменить значения переменных на свои. Пример файла `.env`:

```plaintext
# Конфигурация базы данных PostgreSQL
POSTGRES_DB=ваше_имя_базы_данных
POSTGRES_USER=ваше_имя_пользователя
POSTGRES_PASSWORD=ваш_пароль
POSTGRES_OUT_PORT=порт_для_доступа_извне
POSTGRES_IN_PORT=5432

# Конфигурация pgAdmin
PGADMIN_DEFAULT_EMAIL=ваш_email@пример.org
PGADMIN_DEFAULT_PASSWORD=ваш_пароль
PGADMIN_PORT=порт_pgadmin

# Конфигурация FastAPI
APP_CONFIG__DB__URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@pg_db:${POSTGRES_IN_PORT}/${POSTGRES_DB}
FASTAPI_PORT=порт_для_доступа_к_fastapi
```

### 2. Запуск с использованием Docker

Для запуска приложения используйте Docker и Docker Compose. Выполните следующие команды в терминале:

```bash
docker-compose build
docker-compose up
```

Это запустит все необходимые сервисы, включая PostgreSQL, pgAdmin и FastAPI.

## Технологии

- **FastAPI** - современный, быстрый (высокопроизводительный) веб-фреймворк для создания API.
- **PostgreSQL** - мощная, объектно-реляционная система управления базами данных.
- **Alembic** - инструмент для управления миграциями базы данных.