# Índice de Funciones Documentadas

## Resumen

Este documento lista todas las funciones que han sido documentadas en la carpeta `documentacion/funciones/`.

---

## Lista de Funciones Documentadas

| # | Archivo de Función | Descripción |
|---|-------------------|-------------|
| 1 | funcion_create_app.md | Factory de la aplicación Flask |
| 2 | funcion_register.md | Registro de nuevos usuarios |
| 3 | funcion_login.md | Inicio de sesión |
| 4 | funcion_calculate_next_review.md | Algoritmo SM-2 de SRS |
| 5 | funcion_dashboard_index.md | Dashboard principal del usuario |
| 6 | funcion_daily_challenge.md | Desafíos diarios |
| 7 | funcion_analyze_text.md | Análisis de escritura |
| 8 | funcion_check_grammar_errors.md | Verificación de gramática (LanguageTool) |
| 9 | funcion_srs_study.md | Estudio de flashcards SRS |
| 10 | funcion_start_exam.md | Iniciar examen simulado |
| 11 | funcion_view_unit.md | Ver detalles de unidad |
| 12 | funcion_game_list.md | Lista de juegos educativos |
| 13 | funcion_kids_home.md | Zona infantil |
| 14 | funcion_profile_view.md | Ver perfil de usuario |
| 15 | funcion_stats_index.md | Dashboard de estadísticas |
| 16 | funcion_grammar_index.md | Índice de gramática |
| 17 | funcion_conversation_list.md | Lista de conversaciones |
| 18 | funcion_review_dashboard.md | Dashboard de repaso |
| 19 | funcion_list_scenarios.md | Lista de escenarios temáticos |
| 20 | funcion_my_badges.md | Logros del usuario |

---

## Funciones Pendientes por Documentar

### Routes (32 archivos)

| Archivo | Funciones Principales |
|---------|---------------------|
| main.py | index, about, contact |
| practice.py | writing_practice, sentence_practice, api_analyze |
| quiz.py | list_quizzes, take_quiz, submit_quiz |
| reading.py | reading_list, view_reading |
| flashcards.py | srs_overview, srs_study, add_flashcard |
| study.py | study_home, study_topic |
| drills.py | drill_list, drill_exercise |
| idioms.py | idioms_list, phrasal_verbs |
| reports.py | reports_home, achievements |
| writing.py | analyze_page, quick_check, history |
| certificates.py | list_certificates, generate_certificate |
| bookmarks.py | list, add, remove |
| feedback.py | index, submit |
| legal.py | terms, privacy |
| unit_challenge.py | challenge_units, unit_challenge_detail |
| explanations.py | unit_explanations, topic_explanation |
| errors.py | my_errors |

### Services (11 archivos)

| Servicio | Funciones |
|----------|-----------|
| srs.py | get_due_flashcards, get_srs_stats, review_flashcard_srs |
| unit_unlock.py | is_unit_unlocked, get_all_units_status, mark_section_complete |
| streaks.py | get_streak, update_streak, check_and_update |
| writing_analysis.py | analyze_writing, check_spelling, check_grammar |
| statistics.py | get_activity_heatmap, get_weekly_progress, get_performance_by_skill |
| review_system.py | get_review_items, calculate_review_score |
| email_service.py | send_email, send_welcome, send_reminder |
| certificate_generator.py | generate_certificate, verify_certificate |
| feedback.py | check_answer_similarity, analyze_reading_sentences |
| study_content.py | get_unit_content, get_topic_content |
| roleplay_simulator.py | simulate_response, evaluate_input |

---

## Cómo Agregar Nueva Documentación

1. Crear archivo en `documentacion/funciones/funcion_<nombre>.md`
2. Usar la plantilla:

```markdown
# Función: <nombre>()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | <nombre>() |
| **Archivo** | app/routes/... |
| **Ruta** | app/routes/... |
| **Tipo** | Ruta Flask |

## Propósito

...

## Flujo Lógico

...

## Parámetros

...

## Tablas Utilizadas

...

## Templates Relacionados

...

## Impacto si se Modifica

...
```

---

*Índice de funciones - English Learning Platform*
