# Mapa de Funciones del Sistema

## 1. Funciones por Archivo

### 1.1 app/__init__.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `create_app()` | Factory | Crea y configura la aplicación Flask |
| `markdown_to_html()` | Helper | Convierte markdown a HTML |
| `cache` | Variable | Instancia de caché |

---

### 1.2 app/extensions.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `db` | Variable | Instancia SQLAlchemy |
| `login_manager` | Variable | Instancia Flask-Login |
| `migrate` | Variable | Instancia Flask-Migrate |
| `mail` | Variable | Instancia Flask-Mail |
| `init_app()` | Función | Inicializa extensiones con la app |

---

### 1.3 app/decorators.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `rate_limit()` | Decorador | Limita intentos en período de tiempo |
| `json_response()` | Decorador | Captura excepciones y retorna JSON |
| `adults_only()` | Decorador | Bloquea menores de 15 años |
| `require_scenario_access()` | Decorador | Verifica acceso a escenario |

---

### 1.4 app/routes/main.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `index()` | Ruta | Página principal |
| `about()` | Ruta | Página about |
| `contact()` | Ruta | Página contacto |

---

### 1.5 app/routes/auth.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `register()` | Ruta | Registro de nuevos usuarios |
| `login()` | Ruta | Inicio de sesión |
| `logout()` | Ruta | Cierre de sesión |
| `send_welcome_email_if_enabled()` | Helper | Envía email de bienvenida |

---

### 1.6 app/routes/dashboard.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `index()` | Ruta | Dashboard principal del usuario |
| `progress()` | Ruta | Vista de progreso detallado |
| `get_random_daily_challenge()` | Helper | Selecciona juego aleatorio |

---

### 1.7 app/routes/units.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `view_unit()` | Ruta | Ver detalles de unidad |
| `view_grammar()` | Ruta | Ver reglas gramaticales |
| `view_vocabulary()` | Ruta | Ver vocabulario |
| `view_writing_practices()` | Ruta | Ver ejercicios de escritura |
| `mark_complete()` | Ruta | Marcar unidad completada |

---

### 1.8 app/routes/practice.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `writing_practice()` | Ruta | Ejercicio de escritura |
| `sentence_practice()` | Ruta | Práctica de oraciones |
| `sentence_exercises()` | Ruta | Ejercicios estructurados |
| `submit_exercise()` | Ruta | Enviar respuesta |
| `api_analyze()` | API | Análisis de texto |

---

### 1.9 app/routes/quiz.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `list_quizzes()` | Ruta | Lista de quizzes |
| `take_quiz()` | Ruta | Tomar quiz |
| `submit_quiz()` | Ruta | Enviar quiz |
| `quiz_result()` | Ruta | Ver resultado |
| `unit_quiz()` | Ruta | Quiz por unidad |

---

### 1.10 app/routes/reading.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `reading_list()` | Ruta | Lista de lecturas |
| `view_reading()` | Ruta | Ver lectura |
| `submit_reading()` | Ruta | Enviar respuestas |

---

### 1.11 app/routes/badges.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `my_badges()` | Ruta | Mis logros |
| `all_badges()` | Ruta | Todos los logros |
| `earn_badge()` | Ruta | Obtener logro |
| `badge_detail()` | Ruta | Detalle de logro |

---

### 1.12 app/routes/flashcards.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `srs_overview()` | Ruta | Resumen SRS |
| `srs_study()` | Ruta | Estudiar tarjetas |
| `srs_review()` | Ruta | Revisar tarjetas |
| `add_flashcard()` | Ruta | Agregar tarjeta |
| `delete_flashcard()` | Ruta | Eliminar tarjeta |

---

### 1.13 app/routes/conversation.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `list()` | Ruta | Listar conversaciones |
| `detail()` | Ruta | Practicar conversación |
| `calculate_score()` | Helper | Calcular puntuación |
| `get_feedback()` | Helper | Obtener feedback |
| `detect_pattern_type()` | Helper | Detectar tipo de patrón |
| `save_alternative_response()` | Helper | Guardar respuesta alternativa |

---

### 1.14 app/routes/grammar.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `index()` | Ruta | Índice gramática |
| `rule_detail()` | Ruta | Detalle de regla |
| `grammar_exercises()` | Ruta | Ejercicios gramática |

---

### 1.15 app/routes/stats.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `index()` | Ruta | Estadísticas principales |
| `api_activity_heatmap()` | API | Heatmap de actividad |
| `api_weekly_progress()` | API | Progreso semanal |
| `api_performance_skill()` | API | Rendimiento por habilidad |

---

### 1.16 app/routes/study.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `study_home()` | Ruta | Home estudio |
| `study_topic()` | Ruta | Estudiar tema |
| `mark_topic_complete()` | Ruta | Marcar tema completado |

---

### 1.17 app/routes/challenges.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `daily_challenge()` | Ruta | Reto diario |
| `submit_daily_challenge()` | Ruta | Enviar reto |
| `leaderboard()` | Ruta | Tabla clasificación |
| `my_points()` | Ruta | Mis puntos |
| `add_points()` | Helper | Agregar puntos |
| `update_streak()` | Helper | Actualizar racha |

---

### 1.18 app/routes/exams.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `exam_list()` | Ruta | Lista exámenes |
| `start_exam()` | Ruta | Iniciar examen |
| `submit_exam()` | Ruta | Enviar examen |
| `exam_result()` | Ruta | Resultado examen |

---

### 1.19 app/routes/games.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `game_list()` | Ruta | Lista de juegos |
| `word_scramble()` | Ruta | Juego palabras |
| `hangman()` | Ruta | Ahorcado |
| `memory_game()` | Ruta | Memoria |
| `fill_gaps()` | Ruta | Completar espacios |
| `quick_quiz()` | Ruta | Quiz rápido |
| `speed_typing()` | Ruta | Mecanografía |
| `save_score()` | Ruta | Guardar puntuación |

---

### 1.20 app/routes/drills.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `drill_list()` | Ruta | Lista de drills |
| `drill_exercise()` | Ruta | Hacer drill |
| `submit_drill()` | Ruta | Enviar drill |
| `error_drills()` | Ruta | Drills de errores |

---

### 1.21 app/routes/idioms.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `idioms_list()` | Ruta | Lista de idioms |
| `phrasal_verbs()` | Ruta | Verbos phrasales |
| `idiom_detail()` | Ruta | Detalle idiom |

---

### 1.22 app/routes/reports.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `reports_home()` | Ruta | Home reportes |
| `achievements()` | Ruta | Logros |
| `weekly_summary()` | Ruta | Resumen semanal |

---

### 1.23 app/routes/review.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `dashboard()` | Ruta | Dashboard repaso |
| `start_review()` | Ruta | Iniciar repaso |
| `practice_review()` | Ruta | Practicar repaso |
| `submit_review()` | Ruta | Enviar repaso |

---

### 1.24 app/routes/writing.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `analyze_page()` | Ruta | Página análisis |
| `analyze_text()` | Ruta | Analizar texto |
| `quick_check()` | Ruta | Análisis rápido |
| `suggest_improvements()` | Ruta | Sugerencias |
| `history()` | Ruta | Historial |

---

### 1.25 app/routes/scenarios.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `list_scenarios()` | Ruta | Lista escenarios |
| `scenario_dashboard()` | Ruta | Dashboard escenario |
| `scenario_detail()` | Ruta | Detalle escenario |
| `unlock_scenario()` | Ruta | Desbloquear escenario |

---

### 1.26 app/routes/kids.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `kids_home()` | Ruta | Home zona kids |
| `select_profile()` | Ruta | Seleccionar perfil |
| `profile_map()` | Ruta | Mapa de perfil |
| `kids_game()` | Ruta | Juego infantil |

---

### 1.27 app/routes/certificates.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `list_certificates()` | Ruta | Lista certificados |
| `generate_certificate()` | Ruta | Generar certificado |
| `verify_certificate()` | Ruta | Verificar certificado |
| `download_certificate()` | Ruta | Descargar certificado |

---

### 1.28 app/routes/profile.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `view()` | Ruta | Ver perfil |
| `edit()` | Ruta | Editar perfil |
| `preferences()` | Ruta | Preferencias |
| `update_avatar()` | Ruta | Actualizar avatar |

---

### 1.29 app/routes/bookmarks.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `list()` | Ruta | Lista favoritos |
| `add()` | Ruta | Agregar favorito |
| `remove()` | Ruta | Eliminar favorito |

---

### 1.30 app/routes/feedback.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `index()` | Ruta | Formulario feedback |
| `submit()` | Ruta | Enviar feedback |
| `admin_list()` | Ruta | Admin lista feedback |

---

### 1.31 app/routes/legal.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `terms()` | Ruta | Términos y condiciones |
| `privacy()` | Ruta | Política privacidad |

---

## 2. Funciones de Servicios

### 2.1 app/services/srs.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `calculate_next_review()` | Lógica | Algoritmo SM-2 |
| `quality_from_response()` | Helper | Convertir respuesta a calidad |
| `get_due_flashcards()` | Lógica | Obtener tarjetas pendientes |
| `get_srs_stats()` | Lógica | Estadísticas SRS |
| `review_flashcard_srs()` | Lógica | Procesar revisión |

---

### 2.2 app/services/unit_unlock.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `is_unit_unlocked()` | Lógica | Verificar desbloqueo |
| `get_all_units_status()` | Lógica | Estado de todas las unidades |
| `mark_section_complete()` | Lógica | Marcar sección completada |
| `can_attempt_challenge()` | Lógica | Verificar si puede tomar desafío |
| `submit_challenge()` | Lógica | Enviar desafío |

---

### 2.3 app/services/feedback.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `check_grammar_errors()` | Lógica | Verificar errores gramaticales |
| `check_answer_similarity()` | Lógica | Verificar similitud respuestas |
| `analyze_text()` | Lógica | Análisis de texto por unidad |
| `analyze_reading_sentences()` | Lógica | Análisis de oraciones |

---

### 2.4 app/services/statistics.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `get_activity_heatmap()` | Lógica | Heatmap de actividad |
| `get_weekly_progress()` | Lógica | Progreso semanal |
| `get_performance_by_skill()` | Lógica | Rendimiento por habilidad |
| `get_comprehensive_stats()` | Lógica | Estadísticas consolidadas |

---

### 2.5 app/services/streaks.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `get_streak()` | Lógica | Obtener racha |
| `update_streak()` | Lógica | Actualizar racha |
| `check_and_update()` | Lógica | Verificar y actualizar |

---

### 2.6 app/services/writing_analysis.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `analyze_writing()` | Lógica | Análisis avanzado escritura |
| `check_spelling()` | Lógica | Verificar ortografía |
| `check_grammar()` | Lógica | Verificar gramática |
| `get_suggestions()` | Lógica | Obtener sugerencias |

---

### 2.7 app/services/email_service.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `send_email()` | Lógica | Enviar email |
| `send_welcome()` | Lógica | Enviar bienvenida |
| `send_reminder()` | Lógica | Enviar recordatorio |

---

### 2.8 app/services/certificate_generator.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `generate_certificate()` | Lógica | Generar certificado PDF |
| `verify_certificate()` | Lógica | Verificar certificado |

---

### 2.9 app/services/review_system.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `get_review_items()` | Lógica | Obtener items para repaso |
| `calculate_review_score()` | Lógica | Calcular puntuación |

---

### 2.10 app/services/study_content.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `get_unit_content()` | Lógica | Obtener contenido de unidad |
| `get_topic_content()` | Lógica | Obtener contenido de tema |

---

### 2.11 app/services/roleplay_simulator.py

| Función | Tipo | Descripción |
|---------|------|-------------|
| `simulate_response()` | Lógica | Simular respuesta |
| `evaluate_input()` | Lógica | Evaluar input usuario |

---

## 3. Resumen

| Categoría | Cantidad |
|-----------|----------|
| Rutas (routes) | ~120+ |
| Servicios | 11 archivos |
| Decoradores | 4 |
| Helpers | ~30 |

---

*Mapa de funciones - English Learning Platform*