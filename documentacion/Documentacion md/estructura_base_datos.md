# Estructura de Base de Datos

## 1. Tablas del Sistema

### 1.1 Tablas de Usuarios

#### users
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| username | VARCHAR(80) | UK | Nombre de usuario |
| email | VARCHAR(120) | UK | Correo electrónico |
| password_hash | VARCHAR(255) | - | Hash de contraseña |
| full_name | VARCHAR(120) | - | Nombre completo |
| created_at | DATETIME | - | Fecha de creación |
| updated_at | DATETIME | - | Fecha de actualización |
| is_active | BOOLEAN | - | Estado de cuenta |
| is_admin | BOOLEAN | - | Es administrador |
| last_login_date | DATE | - | Último inicio de sesión |
| daily_challenge_completed | BOOLEAN | - | Reto diario completado |
| date_of_birth | DATE | - | Fecha de nacimiento |
| avatar_url | VARCHAR(500) | - | URL del avatar |
| bio | VARCHAR(500) | - | Biografía |
| country | VARCHAR(100) | - | País |
| preferred_language | VARCHAR(10) | - | Idioma preferido |
| timezone | VARCHAR(50) | - | Zona horaria |
| notification_email | BOOLEAN | - | Notificaciones email |
| notification_daily | BOOLEAN | - | Recordatorios diarios |
| daily_goal_minutes | INTEGER | - | Meta diaria (minutos) |
| show_progress | BOOLEAN | - | Mostrar progreso |
| onboarding_completed | BOOLEAN | - | Tour completado |
| subscription_type | VARCHAR(50) | - | Tipo suscripción |
| subscription_expires_at | DATETIME | - | Expiración suscripción |

#### child_profiles
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario padre |
| child_name | VARCHAR(100) | - | Nombre del niño |
| avatar | VARCHAR(200) | - | Avatar |
| total_stars | INTEGER | - | Estrellas acumuladas |
| created_at | DATETIME | - | Fecha de creación |

---

### 1.2 Tablas de Contenido

#### units
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| unit_number | INTEGER | UK | Número de unidad |
| title | VARCHAR(200) | - | Título |
| description | TEXT | - | Descripción |
| detailed_explanation | TEXT | - | Explicación detallada |
| learning_objectives | JSON | - | Objetivos de aprendizaje |
| overview | TEXT | - | Vista general |
| created_at | DATETIME | - | Fecha de creación |
| updated_at | DATETIME | - | Fecha de actualización |

#### topics
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| unit_id | INTEGER | FK | Unidad padre |
| title | VARCHAR(200) | - | Título del tema |
| content | TEXT | - | Contenido |
| order | INTEGER | - | Orden |

#### grammar_rules
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| title | VARCHAR(200) | - | Título |
| explanation | TEXT | - | Explicación |
| examples | TEXT | - | Ejemplos |
| unit_id | INTEGER | FK | Unidad asociada |

#### vocabulary_categories
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| name | VARCHAR(100) | - | Nombre |
| description | TEXT | - | Descripción |
| unit_id | INTEGER | FK | Unidad asociada |

#### vocabulary_items
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| word | VARCHAR(100) | - | Palabra |
| translation | VARCHAR(100) | - | Traducción |
| pronunciation | VARCHAR(100) | - | Pronunciación |
| example | TEXT | - | Ejemplo |
| audio_url | VARCHAR(500) | - | URL audio |
| category_id | INTEGER | FK | Categoría |

#### verbs
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| infinitive | VARCHAR(100) | - | Infinitivo |
| past_simple | VARCHAR(100) | - | Pasado simple |
| past_participle | VARCHAR(100) | - | Participio pasado |
| translation | VARCHAR(100) | - | Traducción |

#### verb_tenses
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| verb_id | INTEGER | FK | Verbo padre |
| tense | VARCHAR(50) | - | Tiempo verbal |
| conjugation | VARCHAR(200) | - | Conjugación |

#### idioms
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| idiom | VARCHAR(200) | - | Modismo |
| meaning | TEXT | - | Significado |
| example | TEXT | - | Ejemplo |

#### phrasal_verbs
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| verb | VARCHAR(50) | - | Verbo |
| particle | VARCHAR(20) | - | Partícula |
| meaning | TEXT | - | Significado |
| example | TEXT | - | Ejemplo |

---

### 1.3 Tablas de Progreso

#### user_progress
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| unit_id | INTEGER | FK | Unidad |
| completed | BOOLEAN | - | Completado |
| completed_topics | JSON | - | Temas completados |
| score | INTEGER | - | Puntuación |
| completed_at | DATETIME | - | Fecha completado |

#### user_grammar_progress
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| rule_id | INTEGER | FK | Regla gramatical |
| mastered | BOOLEAN | - | Dominado |
| practice_count | INTEGER | - | Veces practicado |

#### user_vocabulary_progress
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| vocabulary_id | INTEGER | FK | Vocabulario |
| learned | BOOLEAN | - | Aprendido |
| review_count | INTEGER | - | Veces repasado |

#### user_idiom_progress
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| idiom_id | INTEGER | FK | Modismo |
| learned | BOOLEAN | - | Aprendido |

#### user_phrasal_verb_progress
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| phrasal_verb_id | INTEGER | FK | Phrasal verb |
| learned | BOOLEAN | - | Aprendido |

---

### 1.4 Tablas de SRS (Repetición Espaciada)

#### flashcards
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| front | TEXT | - | Anverso (pregunta) |
| back | TEXT | - | Reverso (respuesta) |
| unit_id | INTEGER | FK | Unidad asociada |
| category | VARCHAR(50) | - | Categoría |

#### user_flashcard_srs
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| flashcard_id | INTEGER | FK | Tarjeta |
| ease_factor | FLOAT | - | Factor de facilidad |
| interval | INTEGER | - | Intervalo (días) |
| repetitions | INTEGER | - | Repeticiones |
| next_review | DATETIME | - | Próximo repaso |

#### user_flashcard_review
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| flashcard_id | INTEGER | FK | Tarjeta |
| quality | INTEGER | - | Calidad (0-5) |
| reviewed_at | DATETIME | - | Fecha repaso |

---

### 1.5 Tablas de Gamificación

#### badges
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| name | VARCHAR(100) | - | Nombre |
| description | TEXT | - | Descripción |
| icon | VARCHAR(50) | - | Icono |
| criteria | JSON | - | Criterios |

#### user_badges (TABLA ASOCIACIÓN)
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| user_id | INTEGER | FK, PK | Usuario |
| badge_id | INTEGER | FK, PK | Badge |
| earned_at | DATETIME | - | Fecha obtención |

#### user_streaks
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| current_streak | INTEGER | - | Racha actual |
| longest_streak | INTEGER | - | Racha más larga |
| last_activity | DATETIME | - | Última actividad |

#### user_points
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| total_points | INTEGER | - | Puntos totales |
| points_spent | INTEGER | - | Puntos gastados |

#### points_transactions
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| amount | INTEGER | - | Cantidad |
| reason | VARCHAR(100) | - | Razón |
| created_at | DATETIME | - | Fecha |

---

### 1.6 Tablas de Exámenes

#### exam_simulators
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| name | VARCHAR(100) | - | Nombre (TOEFL, IELTS) |
| description | TEXT | - | Descripción |
| duration_minutes | INTEGER | - | Duración (min) |
| passing_score | INTEGER | - | Puntuación aprobatoria |

#### exam_sections
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| exam_id | INTEGER | FK | Examen padre |
| name | VARCHAR(100) | - | Nombre sección |
| type | VARCHAR(50) | - | Tipo (reading, grammar) |
| question_count | INTEGER | - | Preguntas |

#### user_exam_attempts
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| exam_id | INTEGER | FK | Examen |
| score | INTEGER | - | Puntuación |
| passed | BOOLEAN | - | Aprobado |
| completed_at | DATETIME | - | Fecha completado |

---

### 1.7 Tablas de Juegos

#### mini_games
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| name | VARCHAR(100) | - | Nombre |
| description | TEXT | - | Descripción |
| game_type | VARCHAR(50) | - | Tipo de juego |
| difficulty | VARCHAR(20) | - | Dificultad |

#### mini_game_content
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| game_id | INTEGER | FK | Juego |
| content | JSON | - | Contenido |

#### user_game_scores
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| game_id | INTEGER | FK | Juego |
| score | INTEGER | - | Puntuación |
| played_at | DATETIME | - | Fecha |

---

### 1.8 Tablas de Conversación

#### conversations
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| title | VARCHAR(200) | - | Título |
| scenario | TEXT | - | Escenario |
| difficulty | VARCHAR(20) | - | Dificultad |

#### conversation_lines
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| conversation_id | INTEGER | FK | Conversación |
| speaker | VARCHAR(50) | - | Hablador |
| line_order | INTEGER | - | Orden |
| text | TEXT | - | Texto |
| audio_url | VARCHAR(500) | - | Audio |

#### conversation_practice
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| conversation_id | INTEGER | FK | Conversación |
| completed | BOOLEAN | - | Completado |
| score | INTEGER | - | Puntuación |

---

### 1.9 Tablas de Escenarios

#### thematic_scenarios
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| name | VARCHAR(100) | - | Nombre |
| description | TEXT | - | Descripción |
| price | DECIMAL | - | Precio |
| premium_only | BOOLEAN | - | Solo premium |

#### user_unlocked_scenarios (TABLA ASOCIACIÓN)
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| user_id | INTEGER | FK, PK | Usuario |
| scenario_id | INTEGER | FK, PK | Escenario |
| unlocked_at | DATETIME | - | Fecha desbloqueo |
| purchase_method | VARCHAR(50) | - | Método compra |

---

### 1.10 Tablas de Suscripciones

#### subscriptions
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| plan_type | VARCHAR(50) | - | Tipo plan |
| status | VARCHAR(20) | - | Estado |
| start_date | DATETIME | - | Fecha inicio |
| end_date | DATETIME | - | Fecha fin |
| stripe_subscription_id | VARCHAR(100) | - | ID Stripe |

---

### 1.11 Tablas de Certificados

#### certificates
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| certificate_type | VARCHAR(50) | - | Tipo |
| issued_at | DATETIME | - | Fecha emisión |
| download_url | VARCHAR(500) | - | URL descarga |

---

### 1.12 Tablas de Feedback

#### user_feedback
| Campo | Tipo | Clve | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| category | VARCHAR(50) | - | Categoría |
| message | TEXT | - | Mensaje |
| created_at | DATETIME | - | Fecha |

---

### 1.13 Tablas de Favoritos

#### bookmarks
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| content_type | VARCHAR(50) | - | Tipo contenido |
| content_id | INTEGER | - | ID contenido |
| created_at | DATETIME | - | Fecha |

---

### 1.14 Tablas de Actividad

#### user_activities
| Campo | Tipo | Clave | Descripción |
|-------|------|-------|-------------|
| id | INTEGER | PK | Identificador único |
| user_id | INTEGER | FK | Usuario |
| activity_type | VARCHAR(50) | - | Tipo actividad |
| description | TEXT | - | Descripción |
| metadata | JSON | - | Metadatos |
| created_at | DATETIME | - | Fecha |

---

## 2. Relaciones entre Tablas

### 2.1 Diagrama de Relaciones

```
┌─────────────────────────────────────────────────────────────────┐
│                        USUARIOS                                 │
│  ┌─────────┐                                                   │
│  │  User   │◄────────┐                                         │
│  └─────────┘        │ 1:N                                      │
│       │             │     ┌───────────────┐                    │
│       │ 1:N         └────►│ ChildProfile  │                    │
│       │                   └───────────────┘                    │
│       │                                                     1:N │
│  ┌────┴───────────┬───────────────┬──────────┐   ┌────────────┐│
│  │               │               │          │   │Subscription││
│  │  ┌────────┐   │  ┌────────┐   │  ┌─────┐ │   └────────────┘│
│  │  │Badge   │   │  │Scenario│   │  │Cert │ │                 │
│  │  │(N:N)   │   │  │(N:N)   │   │  │(1:N)│ │                 │
│  │  └────────┘   │  └────────┘   │  └─────┘ │                 │
└──────────────────┴───────────────┴──────────┴─────────────────┘
                              │
                              │ 1:N
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CONTENIDO                                  │
│  ┌────────┐    1:N    ┌────────┐    1:N    ┌────────────┐     │
│  │  Unit  │──────────►│ Topic  │──────────►│GrammarRule │     │
│  └────────┘           └────────┘           └────────────┘     │
│       │                                            │           │
│       │ 1:N                                       │ 1:N       │
│       ▼                                           ▼           │
│  ┌─────────────────┐                    ┌────────────────┐    │
│  │VocabularyCategory│                   │VocabularyItem  │    │
│  └─────────────────┘                    └────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 1:N
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       PROGRESO                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌─────────────────┐  │
│  │UserProgress    │  │UserGrammar     │  │UserVocabulary   │  │
│  │(1:N User,Unit) │  │Progress        │  │Progress         │  │
│  └────────────────┘  └────────────────┘  └─────────────────┘  │
│         │                    │                    │            │
│         │ 1:N                │ 1:N                │ 1:N        │
│         ▼                    ▼                    ▼           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    SRS SYSTEM                            │  │
│  │  ┌────────────┐    ┌─────────────────┐                  │  │
│  │  │ Flashcard  │◄───│UserFlashcardSRS │                  │  │
│  │  └────────────┘    └─────────────────┘                  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Tipos de Relaciones

| Relación | Tablas | Tipo |
|----------|--------|------|
| User -> ChildProfile | users -> child_profiles | One-to-Many |
| User -> Badge | users -> user_badges -> badges | Many-to-Many |
| User -> Scenario | users -> user_unlocked_scenarios -> thematic_scenarios | Many-to-Many |
| User -> Subscription | users -> subscriptions | One-to-Many |
| User -> Certificate | users -> certificates | One-to-Many |
| User -> UserProgress | users -> user_progress | One-to-Many |
| Unit -> Topic | units -> topics | One-to-Many |
| Unit -> GrammarRule | units -> grammar_rules | One-to-Many |
| Unit -> VocabularyCategory | units -> vocabulary_categories | One-to-Many |
| Unit -> Flashcard | units -> flashcards | One-to-Many |
| Conversation -> ConversationLine | conversations -> conversation_lines | One-to-Many |
| Exam -> ExamSection | exam_simulators -> exam_sections | One-to-Many |
| MiniGame -> MiniGameContent | mini_games -> mini_game_content | One-to-Many |

---

## 3. Notas Técnicas

### 3.1 Claves Foráneas
- Todas las FK tienen `ondelete='CASCADE'` donde aplica
- Índices en campos de búsqueda frecuentes
- Constraints de unicidad en combinaciones necesarias

### 3.2 Tablas de Asociación
- `user_badges`: User-Badge (N:N)
- `user_unlocked_scenarios`: User-Scenario (N:N)

### 3.3 Campos JSON
- learning_objectives (units)
- criteria (badges)
- completed_topics (user_progress)
- content (mini_game_content)
- metadata (user_activities)

---

*Documento de estructura de base de datos - English Learning Platform*