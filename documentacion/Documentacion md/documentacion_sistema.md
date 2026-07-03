# Documentación Técnica del Sistema English Learning Platform

## 1. Descripción General del Sistema

**English Learning Platform** es una plataforma web interactiva para el aprendizaje del idioma inglés, desarrollada con tecnologías modernas y escalables. El sistema ofrece múltiples modalidades de aprendizaje: estudio estructurado por unidades, repetición espaciada (SRS), juegos educativos, práctica de conversación, exámenes simulados y zona infantil.

### Propósito del Sistema
- Proporcionar una experiencia de aprendizaje inmersiva y gamificada
- Permitir seguimiento del progreso del usuario
- Ofrecer contenido adaptativo según el nivel del estudiante
- Monetizar el servicio mediante suscripciones y compras individuales

---

## 2. Arquitectura del Sistema

### Patrón de Diseño: **Blueprint + Factory**

```
run.py → create_app() → Config → Blueprints → DB → App
```

### Componentes Principales

| Componente | Tecnología | Propósito |
|------------|------------|-----------|
| Backend | Python Flask 3.0 | Framework web |
| ORM | SQLAlchemy 2.0 | Abstracción de base de datos |
| Templates | Jinja2 3.1 | Renderizado de vistas |
| Frontend | HTML5, CSS3, Bootstrap 5 | Interfaz de usuario |
| Base de Datos | PostgreSQL | Almacenamiento persistente |
| Autenticación | Flask-Login | Gestión de sesiones |
| Migraciones | Alembic | Control de versiones DB |

### Diagrama de Flujo

```
┌─────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │ Templates│ │   CSS    │ │   JS     │ │ Bootstrap 5.3    │   │
│  │  Jinja2  │ │ Modular  │ │  Theme   │ │ Font Awesome 6   │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      BUSINESS LOGIC LAYER                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │ Routes   │ │Services  │ │Decorators│ │   Filters/Jinja  │   │
│  │ (32 BP)  │ │  (11)    │ │  (4)     │ │   (md, markdown) │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        DATA ACCESS LAYER                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │  Models  │ │  ORM     │ │ Migrations│ │   Extensions    │   │
│  │ (91 cls) │ │SQLAlchemy│ │ Alembic  │ │   Flask-*       │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      INFRASTRUCTURE LAYER                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │PostgreSQL│ │  Nginx   │ │  Cache   │ │   Email (SMTP)   │   │
│  │  15+ TB  │ │ Config   │ │  Simple  │ │   Flask-Mail     │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Estructura del Proyecto

```
english-review/
├── app/                           # Paquete principal
│   ├── __init__.py               # Factory create_app()
│   ├── models.py                # 91 modelos de datos
│   ├── extensions.py            # Extensiones Flask
│   ├── decorators.py            # Decoradores de seguridad
│   ├── routes/                  # 32 blueprints
│   │   ├── main.py             # Rutas principales (/)
│   │   ├── auth.py             # Autenticación (/auth)
│   │   ├── dashboard.py        # Dashboard (/dashboard)
│   │   ├── units.py            # Unidades (/units)
│   │   ├── grammar.py          # Gramática (/grammar)
│   │   ├── flashcards.py       # SRS (/flashcards)
│   │   ├── games.py            # Juegos (/games)
│   │   ├── conversation.py     # Conversación (/conversation)
│   │   ├── scenarios.py        # Escenarios (/scenarios)
│   │   ├── exams.py            # Exámenes (/exams)
│   │   ├── kids.py             # Zona infantil (/kids)
│   │   ├── challenges.py       # Retos (/challenges)
│   │   ├── stats.py            # Estadísticas (/stats)
│   │   ├── review.py           # Repaso (/review)
│   │   ├── writing.py          # Escritura (/writing)
│   │   ├── study.py            # Estudio (/study)
│   │   ├── badges.py           # Logros (/badges)
│   │   ├── certificates.py     # Certificados
│   │   ├── profile.py          # Perfil usuario
│   │   ├── bookmarks.py        # Favoritos
│   │   ├── feedback.py         # Feedback
│   │   ├── legal.py            # Legal (T&C, Privacy)
│   │   ├── quiz.py             # Cuestionarios
│   │   ├── reading.py          # Lecturas
│   │   ├── drills.py           # Ejercicios
│   │   ├── idioms.py           # Idioms
│   │   ├── reports.py          # Reportes
│   │   ├── explanations.py     # Explicaciones
│   │   ├── errors.py           # Errores
│   │   ├── practice.py         # Práctica
│   │   ├── unit_challenge.py   # Desafío unidad
│   │   ├── simulation_api.py   # API simulación
│   │   └── certificates.py     # Certificados
│   ├── services/               # Lógica de negocio
│   │   ├── srs.py             # Algoritmo SM-2
│   │   ├── streaks.py         # Sistema rachas
│   │   ├── unit_unlock.py     # Desbloqueo unidades
│   │   ├── email_service.py   # Emails
│   │   ├── statistics.py      # Estadísticas
│   │   ├── review_system.py   # Sistema repaso
│   │   ├── writing_analysis.py# Análisis escritura
│   │   ├── study_content.py   # Contenido estudio
│   │   ├── feedback.py        # Feedback
│   │   ├── roleplay_simulator.py
│   │   ├── certificate_generator.py
│   │   └── unit_unlock.py
│   ├── templates/              # 100+ templates Jinja2
│   │   ├── base.html         # Template base
│   │   ├── auth/             # Login, register
│   │   ├── dashboard/        # Dashboard
│   │   ├── grammar/          # Gramática
│   │   ├── flashcards/       # SRS
│   │   ├── games/            # Juegos
│   │   ├── kids/             # Zona infantil
│   │   ├── exams/            # Exámenes
│   │   ├── scenarios/        # Escenarios
│   │   └── ...
│   └── static/               # Archivos estáticos
│       ├── css/
│       │   ├── main.css     # Archivo principal
│       │   ├── core/        # Variables, reset, layout
│       │   ├── components/  # Botones, navbar, cards, etc
│       │   └── modules/     # Por funcionalidad
│       └── js/
│           ├── theme-detector.js
│           └── notifications.js
├── config.py                  # Configuración multi-entorno
├── run.py                     # Punto de entrada
├── requirements.txt           # Dependencias Python
├── migrations/                # Alembic
├── seeds/                     # Scripts seeding
└── nginx-config.conf         # Nginx config
```

---

## 4. Descripción de Módulos

### Módulo de Autenticación (`auth.py`)
- Login, registro, logout
- Gestión de sesiones con Flask-Login
- Rate limiting para proteger contra ataques brute-force

### Módulo de Estudio (`study.py`)
- Estudio intensivo por unidades
- Sistema de progresión
- Contenido adaptativo

### Módulo de Repetición Espaciada (`flashcards.py`)
- Implementación del algoritmo SM-2
- Seguimiento de tarjetas por usuario
- Programación de repasos

### Módulo de Juegos (`games.py`)
- 7+ tipos de juegos educativos
- Puntuaciones y logros
- Leaderboard

### Módulo de Exámenes (`exams.py`)
- Simuladores TOEFL, IELTS, Cambridge
- Secciones: Reading, Grammar, Writing
- Historial de intentos

### Módulo Infantil (`kids.py`)
- Perfiles de niños
- Contenido adaptado
- Gamificación con estrellas

### Módulo de Suscripciones (`models.py` - Subscription)
- Planes: free, premium_all_access, kids_pass
- Compras "a la carta" de escenarios

---

## 5. Backend

### Configuración Multi-Entorno

```python
# config.py
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

### Extensiones Registradas
- `db` - SQLAlchemy ORM
- `login_manager` - Autenticación
- `migrate` - Alembic
- `mail` - Emails
- `cache` - Caché en memoria

### Blueprints Registrados (32)
Cada blueprint encapsula funcionalidad relacionada con prefijos de URL específicos.

### Servicios
11 servicios que encapsulan lógica de negocio:
- SRS, Rachas, Desbloqueo de unidades
- Email, Estadísticas, Análisis de escritura
- Sistema de repaso, Certificates

---

## 6. Frontend

### Estructura de Templates

El template base `base.html` proporciona:
- Navbar dinámico (auth vs logged in)
- Theme toggle (light/dark)
- Flash messages
- Footer con enlaces
- Bloques para extensión: `content`, `extra_css`, `extra_js`

### CSS Modular
- **core/**: variables.css, reset.css, layout.css
- **components/**: 18 componentes reutilizables
- **modules/**: 15 módulos por funcionalidad

### Frameworks Externos (CDN)
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- Animate.css 4.1.1

---

## 7. Base de Datos

### Modelos Principales (91 clases)

| Categoría | Modelos |
|-----------|---------|
| Usuarios | User, ChildProfile, Subscription |
| Contenido | Unit, Topic, GrammarRule, VocabularyCategory, VocabularyItem |
| Progreso | UserProgress, UserGrammarProgress, UserVocabularyProgress |
| SRS | Flashcard, UserFlashcardReview, UserFlashcardSRS |
| Gamificación | Badge, UserStreak, UserPoints |
| Exámenes | ExamSimulator, ExamSection, UserExamAttempt |
| Juegos | MiniGame, MiniGameContent, UserGameScore |
| Conversación | Conversation, ConversationLine, ConversationPractice |

### Relaciones Principales
- **User-Badge**: Muchos a muchos (user_badges)
- **User-Scenario**: Muchos a muchos (user_unlocked_scenarios)
- **User-Unit**: Uno a muchos (UserProgress)
- **Unit-Topic**: Uno a muchos

---

## 8. Seguridad

### Medidas Implementadas
- Password hashing con Werkzeug
- SESSION_COOKIE_HTTPONLY = True
- SESSION_COOKIE_SAMESITE = 'Lax'
- Rate limiting en rutas sensibles
- Decoradores de acceso (@adults_only, @require_scenario_access)
- Protección CSRF en formularios

### Decoradores de Seguridad
```python
@rate_limit(max_attempts=5, window_seconds=900)
@adults_only
@require_scenario_access
@json_response
```

---

## 9. Reglas de Negocio

### Sistema de Suscripciones
- **free**: Acceso básico
- **premium_all_access**: Acceso total
- **kids_pass**: Acceso zona infantil

### Sistema de Progresión
- Units requieren completar: gramática, vocabulario, ejercicios, desafío
- Desbloqueo progresivo de contenido
- Rachas diarias con recompensas

### Sistema de Gamificación
- Badges por logros
- Puntos canjeables
- Niveles de usuario
- Leaderboards

---

## 10. Configuración de Producción

### Variables de Entorno Requeridas
```
SECRET_KEY=...
DATABASE_URL=postgresql://...
MAIL_SERVER=smtp.gmail.com
MAIL_USERNAME=...
MAIL_PASSWORD=...
MAIL_ENABLED=True|False
```

### Nginx Config
Configuración para servir la aplicación con proxy inverso.

---

*Documento generado automáticamente - English Learning Platform v1.0*