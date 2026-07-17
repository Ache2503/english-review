# 🚀 Guía de Despliegue y Mantenimiento (Render + Flask)

Este documento contiene los comandos y flujos de trabajo críticos para mantener la aplicación `english-review` en producción sobre Render, así como las instrucciones para resolver conflictos con la base de datos PostgreSQL.

---

## ⚙️ 1. Configuración del Servidor en Render

Para que la aplicación funcione en Render, el panel de configuración (Web Service) debe tener los siguientes parámetros:

### Comandos Principales
* **Build Command:** ```bash
    pip install -r requirements.txt && FLASK_APP=run.py flask db upgrade
    ```
* **Start Command:** ```bash
    gunicorn run:app
    ```

### Variables de Entorno (Environment)
* `PYTHON_VERSION`: `3.11.9` *(Crucial para evitar conflictos con SQLAlchemy)*.
* `FLASK_ENV`: `production` *(Activa las cookies seguras y la configuración de producción)*.
* `SECRET_KEY`: `[tu_clave_secreta_aqui]`
* `DATABASE_URL`: `postgres://usuario...` *(El código en `config.py` ya está preparado para reemplazar automáticamente "postgres://" por "postgresql://").*

---

## 🚑 2. Rescate de Base de Datos y Migraciones

Si el historial de migraciones (`migrations/`) se corrompe o Render falla indicando que una tabla "no existe" o "ya existe", sigue estos pasos para sincronizar la base de datos local con la de producción sin perder datos:

### Paso 1: Limpiar la memoria local (Terminal local)
Borra el registro antiguo directamente en la base de datos local:
```bash
python -c "from run import app; from app.extensions import db; from sqlalchemy import text; app.app_context().push(); db.session.execute(text('DROP TABLE IF EXISTS alembic_version')); db.session.commit()"

```

Luego, elimina manualmente la carpeta `migrations/` de tu proyecto.

### Paso 2: Crear un historial limpio (Terminal local)

```bash
flask db init
flask db migrate -m "Reinicio de migraciones para produccion"
git add .
git commit -m "Reinicio de migraciones"
git push origin main

```

### Paso 3: Sellar la versión en Render

Ve a los **Settings** de Render y cambia temporalmente el **Build Command** a:

```bash
pip install -r requirements.txt && FLASK_APP=run.py flask db stamp head

```

Guarda y espera a que el despliegue termine. (Esto le dice a la base de datos que asuma que ya tiene las tablas actuales).

### Paso 4: Restaurar el comando

Regresa a Render y vuelve a poner el comando normal:

```bash
pip install -r requirements.txt && FLASK_APP=run.py flask db upgrade

```

---

## 🔄 3. Flujo de Trabajo Diario (Metodología de Actualización)

Para agregar nuevas funciones (juegos, tablas, rutas) sin romper la aplicación en vivo, utiliza siempre este flujo:

### 1. Desarrollar en un entorno seguro

Crea una rama nueva para trabajar sin tocar `main`:

```bash
git checkout -b nombre-de-la-nueva-funcion

```

### 2. Actualizar la Base de Datos (Si modificaste `models.py`)

Crea y aplica la migración localmente para probar:

```bash
flask db migrate -m "Agregado X modelo o Y columna"
flask db upgrade

```

*(Si instalaste nuevas librerías, actualiza con: `pip freeze > requirements.txt`)*.

### 3. Verificar y Testear

Ejecuta el script de pruebas existente para asegurar que nada se rompió:

```bash
python "verificacion y test/run_all_tests.py"

```

### 4. Fusión y Despliegue (Deploy)

Si todo funciona localmente, guarda, fusiona y sube los cambios. Render se encargará del resto automáticamente:

```bash
git add .
git commit -m "Descripción clara de la mejora"
git checkout main
git merge nombre-de-la-nueva-funcion
git push origin main

```

```

```