# Task Manager

Una aplicación web de tareas construida con Flask y SQLite.

## Descripción

Task Manager permite crear, listar, completar y eliminar tareas desde una interfaz sencilla y responsive.

Principales características:
- Registro e inicio de sesión de usuarios
- Creación de tareas con título, descripción y prioridad
- Visualización de tareas pendientes y completadas
- Tareas completadas se muestran al final de la lista
- Diseño móvil-friendly con una paleta de colores moderna

## Demo

Puedes ver la aplicación en funcionamiento aquí: [https://roigmar.github.io/task-manager/](https://roigmar.github.io/task-manager/)

## Capturas de pantalla

> - `templates/screenshots/login.png`
> - `templates/screenshots/tasks.png`
> - `templates/screenshots/new_task.png`
> - `templates/screenshots/register.png`


## Requerimientos

- Python 3.11+ (recomendado)
- Flask
- SQLite

## Instalación

1. Clona el repositorio:

```bash
git clone <tu-repositorio> task-manager
cd task-manager
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Inicia la aplicación:

```bash
python app.py
```

2. Abre tu navegador y visita:

```
http://127.0.0.1:5000
```

## Uso

- Regístrate con un usuario nuevo.
- Inicia sesión.
- Crea nuevas tareas desde la pantalla de tareas.
- Marca tareas como completadas o elimina las que ya no necesites.

## Estructura de carpetas

- `app.py` - aplicación Flask principal con rutas y lógica de negocio.
- `database.py` - configuración y conexión a SQLite.
- `requirements.txt` - dependencias del proyecto.
- `static/` - estilos CSS y activos estáticos.
- `templates/` - plantillas HTML de Flask.

## Mejoras futuras

- Agregar edición de tareas y fechas de vencimiento.
- Implementar filtros por prioridad o estado.
- Añadir un panel de usuario con estadísticas de tareas.
- Integrar autenticación más segura y manejo de sesiones extendido.
- Soporte para múltiples listas o proyectos de tareas.

## Notas

- La aplicación usa SQLite para almacenar usuarios y tareas.
- Si querés cambiar la configuración de Flask, revisá `app.py`.
