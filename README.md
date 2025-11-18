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

## Ejemplos de Funcionamiento

La API está protegida. Para probarla, puedes usar **Postman**, **Insomnia** o la terminal.

**Credenciales:** Usa el usuario y contraseña que creaste con `createsuperuser`.

### Opción A: Usando Terminal (cURL)

**1. Listar todas las tareas (GET)**
```bash
curl -u tu_usuario:tu_password -X GET [http://127.0.0.1:8000/api/tareas/](http://127.0.0.1:8000/api/tareas/)
```
**2. Crear una nueva tarea (POST)**
```bash
curl -u tu_usuario:tu_password -X POST \
-H "Content-Type: application/json" \
-d '{"nombre": "Revisar documentación", "completada": false}' \
[http://127.0.0.1:8000/api/tareas/](http://127.0.0.1:8000/api/tareas/)
```
**3. Actualizar una tarea (PATCH) Reemplaza 1 con el ID de la tarea.**
```bash
curl -u tu_usuario:tu_password -X PATCH \
-H "Content-Type: application/json" \
-d '{"completada": true}' \
[http://127.0.0.1:8000/api/tareas/1/](http://127.0.0.1:8000/api/tareas/1/)
```
**4. Eliminar una tarea (DELETE) Reemplaza 1 con el ID de la tarea.**
```bash
curl -u tu_usuario:tu_password -X DELETE [http://127.0.0.1:8000/api/tareas/1/](http://127.0.0.1:8000/api/tareas/1/)
```
### Opción B: Usando Insomnia / Postman
1. Auth: Selecciona Basic Auth e ingresa tus credenciales.
2. Body: Selecciona formato JSON.
3. Endpoints:
GET /api/tareas/
POST /api/tareas/ (JSON: {"nombre": "...", "completada": false})
PATCH /api/tareas/<id>/
DELETE /api/tareas/<id>/