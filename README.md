# English Learning Platform (Flask + PostgreSQL)

Plataforma escalable para estudiar inglés con unidades (gramática, vocabulario, escritura), prácticas de oraciones con feedback automático y quizzes.

## Requisitos
- Python 3.12 (venv configurado)
- PostgreSQL local (socket o usuario/contraseña)

## Configuración
1. Variables de entorno:
   - Edita `.env`:
     - `SECRET_KEY`: clave segura
     - `DATABASE_URL`: `postgresql:///english_learning` (socket) o `postgresql://usuario:pass@localhost:5432/english_learning`

2. Instalar dependencias:
```bash
cd english-learning-platform
/home/axel-michael/Documentos/guia_estudio/.venv/bin/pip install -r requirements.txt
```

3. Crear DB (si no existe):
```bash
sudo -u postgres psql -c "CREATE DATABASE english_learning;"
# (opcional) crear rol igual al usuario del sistema
sudo -u postgres createuser -s "axel-michael"
```

## Migraciones
Inicializar y aplicar migraciones:
```bash
cd english-learning-platform
export FLASK_APP=run.py
export FLASK_ENV=development
/home/axel-michael/Documentos/guia_estudio/.venv/bin/flask db init || true
/home/axel-michael/Documentos/guia_estudio/.venv/bin/flask db migrate -m "initial schema"
/home/axel-michael/Documentos/guia_estudio/.venv/bin/flask db upgrade
```

## Carga de datos (seed)
Carga el contenido de las unidades, actividades y quizzes:
```bash
cd english-learning-platform
export DATABASE_URL=postgresql:///english_learning
/home/axel-michael/Documentos/guia_estudio/.venv/bin/python seed_db.py
```

## Ejecutar servidor
```bash
cd english-learning-platform
export DATABASE_URL=postgresql:///english_learning
/home/axel-michael/Documentos/guia_estudio/.venv/bin/python run.py
```
Abrir en: http://localhost:5000

## Pruebas (Testing)

El sistema incluye pruebas automatizadas completas:

### Ejecutar todas las pruebas
```bash
cd english-learning-platform
export DATABASE_URL=postgresql:///english_learning
/home/axel-michael/Documentos/guia_estudio/.venv/bin/python run_all_tests.py
```

### Pruebas individuales

**Sistema de retroalimentación por tema:**
```bash
/home/axel-michael/Documentos/guia_estudio/.venv/bin/python test_feedback_system.py
```
- Valida el análisis de texto por unidad
- Verifica que los chequeos se aplican según los temas de gramática
- Prueba scores con textos buenos y con errores

**Pruebas de integración:**
```bash
/home/axel-michael/Documentos/guia_estudio/.venv/bin/python test_integration.py
```
- API de análisis de texto (`/practice/api/analyze`)
- Envío de escritura con feedback automático
- Práctica de oraciones con retroalimentación

### Cobertura actual
- ✅ 18/18 pruebas del sistema de feedback
- ✅ 3/3 pruebas de integración de rutas
- ✅ Tasa de éxito: 100%

## Estructura
- `app/models.py`: modelos (Users, Units, Grammar, Vocabulary, Writing, Progress, SentencePractice, UnitExtra, Quiz)
- `app/routes/`: blueprints (`main`, `auth`, `dashboard`, `units`, `practice`, `quiz`)
- `app/services/feedback.py`: análisis de texto con retroalimentación por tema de gramática
- `app/templates/`: UI con Bootstrap
- `seeds/unit_data.json`: datos de unidades con gramática y vocabulario
- `test_feedback_system.py`: pruebas del sistema de retroalimentación
- `test_integration.py`: pruebas de integración de rutas
- `run_all_tests.py`: ejecutor maestro de todas las pruebas

## Características principales

### Sistema de Retroalimentación Inteligente
- Análisis automático de textos por unidad
- Feedback específico según los temas de gramática de cada unidad
- Reconocimiento de sinónimos (e.g., "indirect speech" → "reported speech")
- Scoring dinámico basado en uso correcto de estructuras gramaticales
- Sugerencias personalizadas para mejorar

### Práctica Interactiva
- Ejercicios de escritura con feedback instantáneo
- Práctica de oraciones con análisis en tiempo real
- Historial de envíos con scores y retroalimentación guardados
- API REST para análisis de texto desde el frontend

### Sistema de Evaluación
- Quizzes por unidad con preguntas de opción múltiple
- Evaluación automática y resultados inmediatos
- Historial de intentos de quiz por usuario

## Próximos pasos
- Añadir vocabulario detallado por categoría.
- Más tipos de quiz (true/false, fill-in-the-blank).
- Reportes y gráficas de progreso por unidad.
- Despliegue en producción (Gunicorn + Nginx + SSL).
