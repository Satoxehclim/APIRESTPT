# Mini API de Tareas (Djano REST)

Prueba técnica: API CRUD con autenticación.

## Tecnologías
* python 3 + Django REST Framework
* Base de datos SQLite

## Funcionalidades
* API segura con autenticacion basica (Usuario y contraseña).
* Manejo mediante HTTP (GET,POST PATCH, DELETE).
* Respuestas en formato JSON.

## Instalación

1. Clonar repositorio
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python3 manage.py migrate`
6. `python3 manage.py createsuperuser`  <-- (Sigue las instrucciones para crear tu admin)
7. `python3 manage.py runserver`