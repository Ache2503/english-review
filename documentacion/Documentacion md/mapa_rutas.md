# Mapa de Rutas del Sistema

## 1. Rutas por Blueprint

### 1.1 Main Blueprint (main_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/` | GET | `index` | main.py |
| `/about` | GET | `about` | main.py |
| `/contact` | GET | `contact` | main.py |

---

### 1.2 Auth Blueprint (auth_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/auth/register` | GET, POST | `register` | auth.py |
| `/auth/login` | GET, POST | `login` | auth.py |
| `/auth/logout` | GET | `logout` | auth.py |

---

### 1.3 Dashboard Blueprint (dashboard_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/dashboard/` | GET | `index` | dashboard.py |
| `/dashboard/progress` | GET | `progress` | dashboard.py |

---

### 1.4 Units Blueprint (units_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/units/<int:unit_id>` | GET | `view_unit` | units.py |
| `/units/<int:unit_id>/grammar` | GET | `view_grammar` | units.py |
| `/units/<int:unit_id>/vocabulary` | GET | `view_vocabulary` | units.py |
| `/units/<int:unit_id>/writing` | GET | `view_writing_practices` | units.py |
| `/units/<int:unit_id>/complete` | POST | `mark_complete` | units.py |

---

### 1.5 Practice Blueprint (practice_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/practice/writing` | GET, POST | `writing_practice` | practice.py |
| `/practice/sentence` | GET, POST | `sentence_practice` | practice.py |
| `/practice/exercises` | GET | `sentence_exercises` | practice.py |
| `/practice/submit` | POST | `submit_exercise` | practice.py |
| `/practice/api/analyze` | POST | `api_analyze` | practice.py |

---

### 1.6 Quiz Blueprint (quiz_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/quiz/` | GET | `list_quizzes` | quiz.py |
| `/quiz/<int:quiz_id>/take` | GET | `take_quiz` | quiz.py |
| `/quiz/<int:quiz_id>/submit` | POST | `submit_quiz` | quiz.py |
| `/quiz/<int:attempt_id>/result` | GET | `quiz_result` | quiz.py |
| `/quiz/unit/<int:unit_id>` | GET | `unit_quiz` | quiz.py |

---

### 1.7 Reading Blueprint (reading_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/reading/` | GET | `reading_list` | reading.py |
| `/reading/<int:reading_id>` | GET | `view_reading` | reading.py |
| `/reading/<int:reading_id>/submit` | POST | `submit_reading` | reading.py |

---

### 1.8 Badges Blueprint (badges_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/badges/my-badges` | GET | `my_badges` | badges.py |
| `/badges/all` | GET | `all_badges` | badges.py |
| `/badges/<int:badge_id>` | GET | `badge_detail` | badges.py |

---

### 1.9 Flashcards Blueprint (flashcards_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/flashcards/srs` | GET | `srs_overview` | flashcards.py |
| `/flashcards/srs/study` | GET | `srs_study` | flashcards.py |
| `/flashcards/srs/review` | GET | `srs_review` | flashcards.py |
| `/flashcards/add` | POST | `add_flashcard` | flashcards.py |
| `/flashcards/<int:card_id>/delete` | POST | `delete_flashcard` | flashcards.py |

---

### 1.10 Conversation Blueprint (conversation_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/conversation/` | GET | `list` | conversation.py |
| `/conversation/<scenario>` | GET | `detail` | conversation.py |

---

### 1.11 Grammar Blueprint (grammar_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/grammar/` | GET | `index` | grammar.py |
| `/grammar/<rule_id>` | GET | `rule_detail` | grammar.py |
| `/grammar/exercises` | GET | `grammar_exercises` | grammar.py |

---

### 1.12 Stats Blueprint (stats_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/stats/` | GET | `index` | stats.py |
| `/stats/api/activity-heatmap` | GET | `api_activity_heatmap` | stats.py |
| `/stats/api/weekly-progress` | GET | `api_weekly_progress` | stats.py |
| `/stats/api/performance-skill` | GET | `api_performance_skill` | stats.py |

---

### 1.13 Study Blueprint (study_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/study/` | GET | `study_home` | study.py |
| `/study/topic/<int:topic_id>` | GET | `study_topic` | study.py |
| `/study/topic/<int:topic_id>/complete` | POST | `mark_topic_complete` | study.py |

---

### 1.14 Challenges Blueprint (challenges_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/challenges/daily` | GET, POST | `daily_challenge` | challenges.py |
| `/challenges/submit` | POST | `submit_daily_challenge` | challenges.py |
| `/challenges/leaderboard` | GET | `leaderboard` | challenges.py |
| `/challenges/points` | GET | `my_points` | challenges.py |

---

### 1.15 Exams Blueprint (exams_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/exams/` | GET | `exam_list` | exams.py |
| `/exams/<int:exam_id>/start` | GET | `start_exam` | exams.py |
| `/exams/<int:exam_id>/submit` | POST | `submit_exam` | exams.py |
| `/exams/<int:attempt_id>/result` | GET | `exam_result` | exams.py |

---

### 1.16 Games Blueprint (games_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/games/` | GET | `game_list` | games.py |
| `/games/word-scramble` | GET | `word_scramble` | games.py |
| `/games/hangman` | GET | `hangman` | games.py |
| `/games/memory` | GET | `memory_game` | games.py |
| `/games/fill-gaps` | GET | `fill_gaps` | games.py |
| `/games/quick-quiz` | GET | `quick_quiz` | games.py |
| `/games/speed-typing` | GET | `speed_typing` | games.py |
| `/games/score` | POST | `save_score` | games.py |

---

### 1.17 Drills Blueprint (drills_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/drills/` | GET | `drill_list` | drills.py |
| `/drills/<int:drill_id>` | GET | `drill_exercise` | drills.py |
| `/drills/<int:drill_id>/submit` | POST | `submit_drill` | drills.py |
| `/drills/errors` | GET | `error_drills` | drills.py |

---

### 1.18 Idioms Blueprint (idioms_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/idioms/` | GET | `idioms_list` | idioms.py |
| `/idioms/phrasal-verbs` | GET | `phrasal_verbs` | idioms.py |
| `/idioms/<int:idiom_id>` | GET | `idiom_detail` | idioms.py |

---

### 1.19 Reports Blueprint (reports_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/reports/` | GET | `reports_home` | reports.py |
| `/reports/achievements` | GET | `achievements` | reports.py |
| `/reports/weekly-summary` | GET | `weekly_summary` | reports.py |

---

### 1.20 Review Blueprint (review_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/review/` | GET | `dashboard` | review.py |
| `/review/start` | GET | `start_review` | review.py |
| `/review/practice` | GET, POST | `practice_review` | review.py |
| `/review/submit` | POST | `submit_review` | review.py |

---

### 1.21 Writing Blueprint (writing_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/writing/analyze` | GET | `analyze_page` | writing.py |
| `/writing/analyze/text` | POST | `analyze_text` | writing.py |
| `/writing/quick-check` | POST | `quick_check` | writing.py |
| `/writing/improvements` | POST | `suggest_improvements` | writing.py |
| `/writing/history` | GET | `history` | writing.py |

---

### 1.22 Scenarios Blueprint (scenarios_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/scenarios/` | GET | `list_scenarios` | scenarios.py |
| `/scenarios/<int:scenario_id>/dashboard` | GET | `scenario_dashboard` | scenarios.py |
| `/scenarios/<int:scenario_id>` | GET | `scenario_detail` | scenarios.py |
| `/scenarios/<int:scenario_id>/unlock` | POST | `unlock_scenario` | scenarios.py |

---

### 1.23 Kids Blueprint (kids_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/kids/` | GET | `kids_home` | kids.py |
| `/kids/select-profile` | GET | `select_profile` | kids.py |
| `/kids/profile/<int:profile_id>/map` | GET | `profile_map` | kids.py |
| `/kids/game/<game>` | GET | `kids_game` | kids.py |

---

### 1.24 Certificates Blueprint (certificates_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/certificates/` | GET | `list_certificates` | certificates.py |
| `/certificates/generate` | POST | `generate_certificate` | certificates.py |
| `/certificates/verify/<code>` | GET | `verify_certificate` | certificates.py |
| `/certificates/<int:cert_id>/download` | GET | `download_certificate` | certificates.py |

---

### 1.25 Profile Blueprint (profile_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/profile/` | GET | `view` | profile.py |
| `/profile/edit` | GET, POST | `edit` | profile.py |
| `/profile/preferences` | GET, POST | `preferences` | profile.py |
| `/profile/avatar` | POST | `update_avatar` | profile.py |

---

### 1.26 Bookmarks Blueprint (bookmarks_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/bookmarks/` | GET | `list` | bookmarks.py |
| `/bookmarks/add` | POST | `add` | bookmarks.py |
| `/bookmarks/<int:bookmark_id>/remove` | POST | `remove` | bookmarks.py |

---

### 1.27 Feedback Blueprint (feedback_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/feedback/` | GET, POST | `index` | feedback.py |
| `/feedback/submit` | POST | `submit` | feedback.py |
| `/feedback/admin` | GET | `admin_list` | feedback.py |

---

### 1.28 Legal Blueprint (legal_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/legal/terms` | GET | `terms` | legal.py |
| `/legal/privacy` | GET | `privacy` | legal.py |

---

### 1.29 Unit Challenge Blueprint (unit_challenge_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/challenge/units` | GET | `challenge_units` | unit_challenge.py |
| `/challenge/unit/<int:unit_id>` | GET, POST | `unit_challenge_detail` | unit_challenge.py |

---

### 1.30 Explanations Blueprint (explanations_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/explanations/unit/<int:unit_id>` | GET | `unit_explanations` | explanations.py |
| `/explanations/topic/<int:topic_id>` | GET | `topic_explanation` | explanations.py |

---

### 1.31 Errors Blueprint (errors_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/errors/my-errors` | GET | `my_errors` | errors.py |
| `/errors/practice` | GET | `practice_errors` | errors.py |

---

### 1.32 Simulation API Blueprint (simulation_bp)

| Ruta | Método | Función | Archivo |
|------|--------|---------|---------|
| `/api/simulation/start` | POST | `start_simulation` | simulation_api.py |
| `/api/simulation/step` | POST | `next_step` | simulation_api.py |
| `/api/simulation/response` | POST | `process_response` | simulation_api.py |

---

## 2. Resumen de Rutas

| Blueprint | Cantidad Rutas |
|-----------|----------------|
| main | 3 |
| auth | 3 |
| dashboard | 2 |
| units | 5 |
| practice | 5 |
| quiz | 5 |
| reading | 3 |
| badges | 3 |
| flashcards | 5 |
| conversation | 2 |
| grammar | 3 |
| stats | 4 |
| study | 3 |
| challenges | 4 |
| exams | 4 |
| games | 8 |
| drills | 4 |
| idioms | 3 |
| reports | 3 |
| review | 4 |
| writing | 5 |
| scenarios | 4 |
| kids | 4 |
| certificates | 4 |
| profile | 4 |
| bookmarks | 3 |
| feedback | 3 |
| legal | 2 |
| unit_challenge | 2 |
| explanations | 2 |
| errors | 2 |
| simulation_api | 3 |
| **TOTAL** | **~120** |

---

## 3. Rutas por Método HTTP

### GET
~100 rutas

### POST
~20 rutas

### PUT/PATCH
~0 rutas (no implementado)

### DELETE
~0 rutas (no implementado)

---

*Mapa de rutas - English Learning Platform*