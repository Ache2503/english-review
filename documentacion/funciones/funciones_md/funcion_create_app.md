# Función: create_app()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | create_app() |
| **Archivo** | app/__init__.py |
| **Ruta** | app/__init__.py:29 |
| **Tipo** | Factory |

## Propósito

Factory function que crea y configura la aplicación Flask. Es el punto de entrada principal del sistema que:
- Inicializa la aplicación Flask
- Carga la configuración
- Inicializa extensiones
- Registra blueprints
- Configura manejo de errores

## Flujo Lógico

1. Crea instancia de Flask
2. Carga variables de entorno con `load_dotenv()`
3. Carga configuración según entorno
4. Configura Flask-Mail desde variables de entorno
5. Inicializa caché
6. Registra filtros Jinja2 (markdown)
7. Inicializa extensiones (db, login_manager, migrate, mail)
8. Registra callback de usuario para Flask-Login
9. Crea tablas de base de datos
10. Registra todos los blueprints (32)
11. Define handlers de errores (404, 500)
12. Retorna la aplicación configurada

## Parámetros

| Parámetro | Tipo | Descripción |
|--------|
| config_name---|------|------------- | str | Entorno ('development', 'testing', 'production') |

## Tablas Utilizadas

- `users` - Para callback de login
- Todas las tablas (creación con `db.create_all()`)

## Templates Relacionados

No utiliza templates directamente (es configuración).

## Archivos Relacionados

- `config.py` - Configuraciones
- `app/extensions.py` - Extensiones
- `app/routes/*.py` - Todos los blueprints

## Dependencias

```python
from flask import Flask
from flask_caching import Cache
from config import config
from app.extensions import db, login_manager, init_app
from app.models import User
```

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Toda la aplicación
- Extensiones cargadas
- Rutas disponibles
- Base de datos

**Archivos a revisar:**
- `config.py`
- `app/extensions.py`
- Todos los blueprints
