# Cube Demo System

## Create Network

    docker network create cubedemo

## Deploy

    docker-compose up

## Migrate

    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
