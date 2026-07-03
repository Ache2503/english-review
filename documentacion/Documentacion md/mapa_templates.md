# Mapa de Templates del Sistema

## 1. Templates por Carpeta

### 1.1 Templates Raíz (app/templates/)

| Template | Usado por | Función |
|----------|-----------|---------|
| `base.html` | Todos | Template base con navbar, footer, theme |
| `index.html` | main.py | Página principal |
| `about.html` | main.py | Página about |
| `contact.html` | main.py | Página contacto |
| `dashboard.html` | dashboard.py | Dashboard principal |
| `unit_detail.html` | units.py | Detalle de unidad |
| `submission_view.html` | practice.py | Ver envío |
| `progress/progress.html` | dashboard.py | Progreso |

---

### 1.2 app/templates/auth/

| Template | Usado por | Función |
|----------|-----------|---------|
| `login.html` | auth.py | Inicio de sesión |
| `register.html` | auth.py | Registro |

---

### 1.3 app/templates/dashboard/

| Template | Usado por | Función |
|----------|-----------|---------|
| `dashboard.html` | dashboard.py | Dashboard |

---

### 1.4 app/templates/units/

| Template | Usado por | Función |
|----------|-----------|---------|
| `topic_detail.html` | units.py | Detalle de tema |

---

### 1.5 app/templates/study/

| Template | Usado por | Función |
|----------|-----------|---------|
| `index.html` | study.py | Home estudio |
| `topic.html` | study.py | Estudiar tema |

---

### 1.6 app/templates/practice/

| Template | Usado por | Función |
|----------|-----------|---------|
| `practice.html` | practice.py | Práctica general |

---

### 1.7 app/templates/writing/

| Template | Usado por | Función |
|----------|-----------|---------|
| `analyze.html` | writing.py | Análisis de escritura |
| `practice.html` | writing.py | Práctica escritura |
| `writing_practice.html` | writing.py | Práctica escritura |
| `writing_exercise.html` | writing.py | Ejercicio escritura |
| `history.html` | writing.py | Historial |

---

### 1.8 app/templates/sentences/

| Template | Usado por | Función |
|----------|-----------|---------|
| `sentence_practice.html` | practice.py | Práctica oraciones |
| `sentence_exercises.html` | practice.py | Ejercicios oraciones |
| `sentence_structures.html` | practice.py | Estructuras oraciones |

---

### 1.9 app/templates/grammar/

| Template | Usado por | Función |
|----------|-----------|---------|
| `index.html` | grammar.py | Índice gramática |
| `grammar_view.html` | grammar.py | Ver gramática |
| `topic.html` | grammar.py | Tema gramática |
| `verbs.html` | grammar.py | Verbos |
| `sentences.html` | grammar.py | Oraciones |
| `progress.html` | grammar.py | Progreso gramática |
| `my_sentences.html` | grammar.py | Mis oraciones |

---

### 1.10 app/templates/flashcards/

| Template | Usado por | Función |
|----------|-----------|---------|
| `srs_overview.html` | flashcards.py | Resumen SRS |
| `srs_study.html` | flashcards.py | Estudiar tarjetas |
| `unit_flashcards.html` | flashcards.py | Tarjetas por unidad |

---

### 1.11 app/templates/games/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | games.py | Lista de juegos |
| `word_scramble.html` | games.py | Palabras mezcladas |
| `hangman.html` | games.py | Ahorcado |
| `memory.html` | games.py | Memoria |
| `fill_gaps.html` | games.py | Completar espacios |
| `quick_quiz.html` | games.py | Quiz rápido |
| `speed_typing.html` | games.py | Mecanografía |
| `reading_list.html` | games.py | Lista lecturas |
| `reading_detail.html` | games.py | Detalle lectura |

---

### 1.12 app/templates/kids/

| Template | Usado por | Función |
|----------|-----------|---------|
| `select_profile.html` | kids.py | Seleccionar perfil |
| `add_profile.html` | kids.py | Agregar perfil |
| `map.html` | kids.py | Mapa infantil |
| `topic_view.html` | kids.py | Ver tema |

---

### 1.13 app/templates/exams/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | exams.py | Lista exámenes |
| `detail.html` | exams.py | Detalle examen |
| `take.html` | exams.py | Tomar examen |
| `result.html` | exams.py | Resultado examen |

---

### 1.14 app/templates/conversation/

| Template | Usado por | Función |
|----------|-----------|---------|
| `conversation_list.html` | conversation.py | Lista conversaciones |
| `conversation_detail.html` | conversation.py | Practicar conversación |

---

### 1.15 app/templates/scenarios/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | scenarios.py | Lista escenarios |
| `dashboard.html` | scenarios.py | Dashboard escenario |
| `preview.html` | scenarios.py | Preview escenario |
| `simulation.html` | scenarios.py | Simulación |

---

### 1.16 app/templates/badges/

| Template | Usado por | Función |
|----------|-----------|---------|
| `my_badges.html` | badges.py | Mis logros |
| `all_badges.html` | badges.py | Todos los logros |

---

### 1.17 app/templates/challenges/

| Template | Usado por | Función |
|----------|-----------|---------|
| `daily.html` | challenges.py | Reto diario |
| `leaderboard.html` | challenges.py | Tabla clasificación |
| `points.html` | challenges.py | Mis puntos |

---

### 1.18 app/templates/challenge/

| Template | Usado por | Función |
|----------|-----------|---------|
| `units_overview.html` | unit_challenge.py | Vista general |
| `unit_requirements.html` | unit_challenge.py | Requisitos |
| `take_challenge.html` | unit_challenge.py | Tomar desafío |
| `challenge_result.html` | unit_challenge.py | Resultado |

---

### 1.19 app/templates/review/

| Template | Usado por | Función |
|----------|-----------|---------|
| `dashboard.html` | review.py | Dashboard repaso |
| `start_session.html` | review.py | Iniciar repaso |
| `practice.html` | review.py | Practicar repaso |
| `results.html` | review.py | Resultados |

---

### 1.20 app/templates/reading/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | reading.py | Lista lecturas |
| `view.html` | reading.py | Ver lectura |
| `submission_detail.html` | reading.py | Detalle envío |
| `history.html` | reading.py | Historial |

---

### 1.21 app/templates/stats/

| Template | Usado por | Función |
|----------|-----------|---------|
| `dashboard.html` | stats.py | Dashboard estadísticas |

---

### 1.22 app/templates/drills/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | drills.py | Lista drills |
| `take.html` | drills.py | Hacer drill |
| `errors.html` | drills.py | Drills de errores |

---

### 1.23 app/templates/idioms/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | idioms.py | Lista idioms |
| `detail.html` | idioms.py | Detalle idiom |
| `practice.html` | idioms.py | Práctica idiom |
| `phrasal_verbs.html` | idioms.py | Verbos phrasales |
| `phrasal_detail.html` | idioms.py | Detalle phrasal |
| `phrasal_practice.html` | idioms.py | Práctica phrasal |

---

### 1.24 app/templates/reports/

| Template | Usado por | Función |
|----------|-----------|---------|
| `dashboard.html` | reports.py | Dashboard reportes |
| `detailed.html` | reports.py | Reporte detallado |
| `weekly_summary.html` | reports.py | Resumen semanal |
| `achievements.html` | reports.py | Logros |

---

### 1.25 app/templates/profile/

| Template | Usado por | Función |
|----------|-----------|---------|
| `view.html` | profile.py | Ver perfil |
| `edit.html` | profile.py | Editar perfil |
| `preferences.html` | profile.py | Preferencias |
| `account.html` | profile.py | Cuenta |
| `onboarding.html` | profile.py | Onboarding |

---

### 1.26 app/templates/feedback/

| Template | Usado por | Función |
|----------|-----------|---------|
| `index.html` | feedback.py | Formulario feedback |

---

### 1.27 app/templates/legal/

| Template | Usado por | Función |
|----------|-----------|---------|
| `terms.html` | legal.py | Términos |
| `privacy.html` | legal.py | Privacidad |

---

### 1.28 app/templates/certificates/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | certificates.py | Lista certificados |
| `view.html` | certificates.py | Ver certificado |
| `verify.html` | certificates.py | Verificar |

---

### 1.29 app/templates/bookmarks/

| Template | Usado por | Función |
|----------|-----------|---------|
| `list.html` | bookmarks.py | Lista favoritos |

---

### 1.30 app/templates/explanations/

| Template | Usado por | Función |
|----------|-----------|---------|
| `unit_explanation.html` | explanations.py | Explicación unidad |
| `topic_explanation.html` | explanations.py | Explicación tema |

---

### 1.31 app/templates/errors/

| Template | Usado por | Función |
|----------|-----------|---------|
| `my_errors.html` | errors.py | Mis errores |

---

### 1.32 app/templates/progress/

| Template | Usado por | Función |
|----------|-----------|---------|
| `progress.html` | dashboard.py | Progreso |

---

## 2. Resumen

| Carpeta | Cantidad Templates |
|---------|-------------------|
| raíz | 10 |
| auth | 2 |
| dashboard | 1 |
| units | 1 |
| study | 2 |
| practice | 1 |
| writing | 5 |
| sentences | 3 |
| grammar | 7 |
| flashcards | 3 |
| games | 9 |
| kids | 4 |
| exams | 4 |
| conversation | 2 |
| scenarios | 4 |
| badges | 2 |
| challenges | 3 |
| challenge | 4 |
| review | 4 |
| reading | 4 |
| stats | 1 |
| drills | 3 |
| idioms | 6 |
| reports | 4 |
| profile | 5 |
| feedback | 1 |
| legal | 2 |
| certificates | 3 |
| bookmarks | 1 |
| explanations | 2 |
| errors | 1 |
| progress | 1 |
| **TOTAL** | **~120** |

---

## 3. Templates por Función

### Autenticación
- `auth/login.html`
- `auth/register.html`

### Dashboard
- `dashboard.html`
- `stats/dashboard.html`
- `progress/progress.html`

### Estudio
- `study/index.html`
- `study/topic.html`
- `unit_detail.html`

### Juegos
- `games/list.html`
- `games/word_scramble.html`
- `games/hangman.html`
- `games/memory.html`
- `games/fill_gaps.html`
- `games/quick_quiz.html`
- `games/speed_typing.html`

### Gramática
- `grammar/index.html`
- `grammar/grammar_view.html`
- `grammar/verbs.html`

### SRS
- `flashcards/srs_overview.html`
- `flashcards/srs_study.html`

---

*Mapa de templates - English Learning Platform*