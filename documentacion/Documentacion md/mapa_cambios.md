# Mapa de Cambios del Sistema

## 1. Guía de Modificaciones

Esta sección indica qué archivos modificar para cambiar funcionalidades específicas del sistema.

---

## 2. Autenticación y Usuarios

### Cambiar proceso de Login
**Archivos a modificar:**
- `app/routes/auth.py` → función `login()`
- `app/templates/auth/login.html` → Template de login
- `app/models.py` → Modelo `User` (métodos `check_password`, `set_password`)
- `app/extensions.py` → Configuración `login_manager`

### Cambiar proceso de Registro
**Archivos a modificar:**
- `app/routes/auth.py` → función `register()`
- `app/templates/auth/register.html` → Template de registro
- `app/models.py` → Modelo `User`

### Cambiar validación de contraseña
**Archivos a modificar:**
- `app/models.py` → `User.set_password()` y `User.check_password()`
- Utiliza `werkzeug.security.generate_password_hash()` y `check_password_hash()`

---

## 3. Sistema de Estudio

### Cambiar estructura de unidades
**Archivos a modificar:**
- `app/models.py` → Modelo `Unit`, `Topic`, `TopicExplanation`
- `app/routes/units.py` → funciones de visualización
- `app/templates/unit_detail.html` → Template de unidad

### Agregar nuevo tipo de contenido
**Archivos a modificar:**
- `app/models.py` → Nuevo modelo
- `app/routes/units.py` → Nueva ruta
- `app/templates/units/` → Nuevo template
- `app/services/study_content.py` → Lógica de contenido

### Cambiar desbloqueo de unidades
**Archivos a modificar:**
- `app/services/unit_unlock.py` → Lógica de desbloqueo
- `app/models.py` → Modelo `UserProgress`
- `app/routes/units.py` → Verificación de acceso

---

## 4. Sistema SRS (Repetición Espaciada)

### Cambiar algoritmo de SRS
**Archivos a modificar:**
- `app/services/srs.py` → función `calculate_next_review()`
- Algoritmo SM-2 implementado aquí

### Modificar intervalo de复习
**Archivos a modificar:**
- `app/services/srs.py` → `calculate_next_review()` (líneas 20-60)
- `app/models.py` → `UserFlashcardSRS` (ease_factor, interval)

### Cambiar visualización de tarjetas
**Archivos a modificar:**
- `app/routes/flashcards.py` → funciones SRS
- `app/templates/flashcards/srs_study.html` → Template de estudio

---

## 5. Gamificación

### Agregar nuevo badge
**Archivos a modificar:**
- `app/models.py` → Modelo `Badge`
- `app/routes/badges.py` → Verificación de logros
- `app/services/statistics.py` → Condiciones de logro
- `app/templates/badges/` → Templates de badges

### Cambiar sistema de puntos
**Archivos a modificar:**
- `app/models.py` → `UserPoints`, `PointsTransaction`
- `app/routes/challenges.py` → `add_points()`
- `app/services/streaks.py` → Lógica de rachas

### Modificar tablas de clasificación
**Archivos a modificar:**
- `app/routes/challenges.py` → función `leaderboard()`
- `app/templates/challenges/leaderboard.html` → Template

---

## 6. Juegos

### Agregar nuevo juego
**Archivos a modificar:**
- `app/models.py` → `MiniGame`, `MiniGameContent`, `UserGameScore`
- `app/routes/games.py` → Nueva función de juego
- `app/templates/games/` → Template del juego
- `app/static/css/modules/games/` → Estilos

### Cambiar scoring de juegos
**Archivos a modificar:**
- `app/routes/games.py` → función `save_score()`
- `app/models.py` → `UserGameScore`

---

## 7. Exámenes

### Agregar nuevo examen
**Archivos a modificar:**
- `app/models.py` → `ExamSimulator`, `ExamSection`
- `app/routes/exams.py` → Funciones de examen
- `app/templates/exams/` → Templates

### Cambiar cálculo de resultado
**Archivos a modificar:**
- `app/routes/exams.py` → función `submit_exam()` o `exam_result()`
- `app/models.py` → `UserExamAttempt`

---

## 8. Gramática y Vocabulario

### Agregar nueva regla gramatical
**Archivos a modificar:**
- `app/models.py` → `GrammarRule`
- `app/routes/grammar.py` → Visualización
- `app/templates/grammar/` → Templates

### Cambiar contenido de vocabulario
**Archivos a modificar:**
- `app/models.py` → `VocabularyCategory`, `VocabularyItem`
- `app/routes/units.py` → `view_vocabulary()`

### Agregar nuevo idiom o phrasal verb
**Archivos a modificar:**
- `app/models.py` → `Idiom`, `PhrasalVerb`
- `app/routes/idioms.py` → Rutas

---

## 9. Estadísticas

### Agregar nueva métrica
**Archivos a modificar:**
- `app/services/statistics.py` → Nueva función
- `app/routes/stats.py` → Nueva API/ruta
- `app/templates/stats/dashboard.html` → Visualización

### Cambiar heatmap de actividad
**Archivos a modificar:**
- `app/services/statistics.py` → `get_activity_heatmap()`
- `app/routes/stats.py` → `api_activity_heatmap()`

---

## 10. Profile y Configuración

### Agregar campo a perfil de usuario
**Archivos a modificar:**
- `app/models.py` → Modelo `User`
- `app/routes/profile.py` → Funciones de edición
- `app/templates/profile/edit.html` → Template
- `app/templates/profile/view.html` → Template

### Cambiar preferencias
**Archivos a modificar:**
- `app/routes/profile.py` → función `preferences()`
- `app/templates/profile/preferences.html` → Template

---

## 11. Zona Infantil

### Agregar contenido para niños
**Archivos a modificar:**
- `app/models.py` → `ChildProfile`, `KidsTopic`, `KidsVocabulary`
- `app/routes/kids.py` → Rutas
- `app/templates/kids/` → Templates

### Cambiar lógica de perfiles
**Archivos a modificar:**
- `app/routes/kids.py` → `select_profile()`, `add_profile()`
- `app/models.py` → `ChildProfile`

---

## 12. Certificados

### Agregar nuevo tipo de certificado
**Archivos a modificar:**
- `app/models.py` → `Certificate`
- `app/routes/certificates.py` → Generación
- `app/services/certificate_generator.py` → Generación PDF

---

## 13. Errores Comunes y Dónde Buscarlos

### Error en autenticación
**Buscar en:**
- `app/routes/auth.py`
- `app/models.py` (User)
- `app/extensions.py` (login_manager)

### Error en base de datos
**Buscar en:**
- `app/models.py` (modelos)
- `app/extensions.py` (db)
- Migraciones en `migrations/`

### Error en rutas (404)
**Buscar en:**
- `app/__init__.py` (blueprints registrados)
- Ruta específica en `app/routes/`

### Error en templates
**Buscar en:**
- Template específico
- Variables pasadas desde la ruta
- `base.html` (herencia)

### Error en CSS/estilos
**Buscar en:**
- `app/static/css/main.css`
- `app/static/css/components/`
- `app/static/css/modules/`

---

## 14. Archivos de Configuración

### Cambiar configuración global
**Archivo:** `config.py`
- Configuraciones de desarrollo, testing, producción

### Cambiar variables de entorno
**Archivo:** `.env` (crear desde `.env.example`)
- SECRET_KEY
- DATABASE_URL
- MAIL_*

### Cambiar extensiones Flask
**Archivo:** `app/extensions.py`
- db, login_manager, migrate, mail

---

## 15. Problemas Conocidos

### Decoradores rotos (PRIORIDAD ALTA)
**Archivo:** `app/decorators.py` (líneas 86-144)
- Decoradores incompletos/duplicados
- Fix: Eliminar definiciones duplicadas

### Modelo UserStreak duplicado (PRIORIDAD ALTA)
**Archivo:** `app/models.py` (líneas 544-548)
- `__repr__` duplicado
- Fix: Eliminar segundo `__repr__`

### has_access_to_scenario siempre true (PRIORIDAD ALTA)
**Archivo:** `app/models.py` (líneas 96-102)
- Siempre retorna True
- Fix: Implementar lógica real

### Validación lectura vacía (MEDIA)
**Archivo:** `app/routes/reading.py` (líneas 108-110)
- `pass` en validación
- Fix: Implementar validación real

---

*Mapa de cambios - English Learning Platform*