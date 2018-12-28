# Cube Demo System

## Deploy

    docker-compose up

## Migrate

    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
