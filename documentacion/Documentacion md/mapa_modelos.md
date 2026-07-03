# Mapa de Modelos del Sistema

## 1. Modelos por Categoría

### 1.1 Modelos de Usuario

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `User` | `users` | 1:N → UserProgress, Subscription, Certificate |
| `ChildProfile` | `child_profiles` | N:1 → User |
| `Subscription` | `subscriptions` | N:1 → User |

---

### 1.2 Modelos de Contenido

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Unit` | `units` | 1:N → Topic, GrammarRule, VocabularyCategory, Flashcard |
| `Topic` | `topics` | N:1 → Unit |
| `GrammarRule` | `grammar_rules` | N:1 → Unit |
| `VocabularyCategory` | `vocabulary_categories` | N:1 → Unit, 1:N → VocabularyItem |
| `VocabularyItem` | `vocabulary_items` | N:1 → VocabularyCategory |
| `Verb` | `verbs` | 1:N → VerbTense |
| `VerbTense` | `verb_tenses` | N:1 → Verb |
| `Idiom` | `idioms` | 1:N → UserIdiomProgress |
| `PhrasalVerb` | `phrasal_verbs` | 1:N → UserPhrasalVerbProgress |
| `Reading` | `readings` | 1:N → ReadingQuestion |
| `ReadingQuestion` | `reading_questions` | N:1 → Reading |
| `UnitExplanation` | `unit_explanations` | N:1 → Unit |
| `TopicExplanation` | `topic_explanations` | N:1 → Topic |

---

### 1.3 Modelos de Ejercicios

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Quiz` | `quizzes` | 1:N → QuizQuestion |
| `QuizQuestion` | `quiz_questions` | N:1 → Quiz, 1:N → QuizOption |
| `QuizOption` | `quiz_options` | N:1 → QuizQuestion |
| `SentenceExercise` | `sentence_exercises` | 1:N → UserSentenceExercise |
| `UserSentenceExercise` | `user_sentence_exercises` | N:1 → User, SentenceExercise |
| `GrammarDrill` | `grammar_drills` | 1:N → UserDrillResult |
| `UnitChallenge` | `unit_challenges` | 1:N → ChallengeQuestion |
| `ChallengeQuestion` | `challenge_questions` | N:1 → UnitChallenge |
| `DailyChallenge` | `daily_challenges` | 1:N → UserDailyChallenge |
| `QuickQuiz` | `quick_quizzes` | 1:N → UserQuizScore |

---

### 1.4 Modelos de Progreso

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `UserProgress` | `user_progress` | N:1 → User, Unit |
| `UserGrammarProgress` | `user_grammar_progress` | N:1 → User, GrammarRule |
| `UserVocabularyProgress` | `user_vocabulary_progress` | N:1 → User, VocabularyItem |
| `StudyProgress` | `study_progress` | N:1 → User |
| `UserReadingScore` | `user_reading_scores` | N:1 → User |
| `UserQuizScore` | `user_quiz_scores` | N:1 → User |
| `ChildProgress` | `child_progress` | N:1 → ChildProfile |

---

### 1.5 Modelos de SRS

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Flashcard` | `flashcards` | 1:N → UserFlashcardSRS, UserFlashcardReview |
| `UserFlashcardSRS` | `user_flashcard_srs` | N:1 → User, Flashcard |
| `UserFlashcardReview` | `user_flashcard_reviews` | N:1 → User, Flashcard |

---

### 1.6 Modelos de Gamificación

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Badge` | `badges` | N:N → User (via user_badges) |
| `UserStreak` | `user_streaks` | N:1 → User |
| `UserPoints` | `user_points` | N:1 → User |
| `PointsTransaction` | `points_transactions` | N:1 → User |
| `MiniGame` | `mini_games` | 1:N → MiniGameContent, UserGameScore |
| `MiniGameContent` | `mini_game_content` | N:1 → MiniGame |
| `UserGameScore` | `user_game_scores` | N:1 → User, MiniGame |

---

### 1.7 Modelos de Exámenes

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `ExamSimulator` | `exam_simulators` | 1:N → ExamSection |
| `ExamSection` | `exam_sections` | N:1 → ExamSimulator |
| `UserExamAttempt` | `user_exam_attempts` | N:1 → User, ExamSimulator |

---

### 1.8 Modelos de Conversación

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Conversation` | `conversations` | 1:N → ConversationLine |
| `ConversationLine` | `conversation_lines` | N:1 → Conversation |
| `ConversationPractice` | `conversation_practice` | N:1 → User, Conversation |
| `AlternativeResponse` | `alternative_responses` | N:1 → ConversationLine |
| `ResponsePattern` | `response_patterns` | N:1 → ConversationLine |
| `UserSentence` | `user_sentences` | N:1 → User |
| `SentenceLike` | `sentence_likes` | N:1 → UserSentence |

---

### 1.9 Modelos de Escenarios

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `ThematicScenario` | `thematic_scenarios` | N:N → User (via user_unlocked_scenarios) |
| `ScenarioVocabulary` | `scenario_vocabulary` | N:1 → ThematicScenario |
| `ScenarioPhrase` | `scenario_phrases` | N:1 → ThematicScenario |
| `ScenarioSimulation` | `scenario_simulations` | N:1 → ThematicScenario |
| `UserScenarioProgress` | `user_scenario_progress` | N:1 → User, ThematicScenario |

---

### 1.10 Modelos de Certificados

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `Certificate` | `certificates` | N:1 → User |

---

### 1.11 Modelos de Feedback

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `UserFeedback` | `user_feedback` | N:1 → User |
| `UserActivity` | `user_activities` | N:1 → User |
| `Bookmark` | `bookmarks` | N:1 → User |

---

### 1.12 Modelos de Análisis

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `WritingPractice` | `writing_practice` | N:1 → User |
| `UserWritingSubmission` | `user_writing_submissions` | N:1 → User |
| `UserReadingSubmission` | `user_reading_submissions` | N:1 → User, Reading |
| `UserSentencePractice` | `user_sentence_practice` | N:1 → User |
| `QuizSubmission` | `quiz_submissions` | N:1 → User, Quiz |
| `UserChallengeAttempt` | `user_challenge_attempts` | N:1 → User, UnitChallenge |
| `UserDailyChallenge` | `user_daily_challenges` | N:1 → User, DailyChallenge |
| `UserTypingScore` | `user_typing_scores` | N:1 → User |
| `WritingAnalysisLog` | `writing_analysis_logs` | N:1 → User |
| `ReviewSessionLog` | `review_session_logs` | N:1 → User |
| `GrammarExerciseResult` | `grammar_exercise_results` | N:1 → User |
| `ErrorLog` | `error_logs` | N:1 → User |
| `UserErrorPattern` | `user_error_patterns` | N:1 → User |

---

### 1.13 Modelos de Sistema

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `MotivationalMessage` | `motivational_messages` | - |
| `AudioFile` | `audio_files` | - |

---

### 1.14 Modelos de Licencias (Business)

| Modelo | Tabla | Relaciones |
|--------|-------|------------|
| `RestaurantLicense` | `restaurant_licenses` | N:1 → User |
| `RestaurantEmployee` | `restaurant_employees` | N:1 → RestaurantLicense |

---

## 2. Tablas de Asociación

| Tabla | Relaciones Many-to-Many |
|-------|------------------------|
| `user_badges` | User ↔ Badge |
| `user_unlocked_scenarios` | User ↔ ThematicScenario |

---

## 3. Resumen de Relaciones

### One-to-Many (1:N)
- User → UserProgress
- User → Subscription
- User → Certificate
- User → ChildProfile
- User → UserStreak
- User → Badge
- Unit → Topic
- Unit → GrammarRule
- Unit → VocabularyCategory
- Unit → Flashcard
- VocabularyCategory → VocabularyItem
- Verb → VerbTense
- Quiz → QuizQuestion
- QuizQuestion → QuizOption
- Conversation → ConversationLine
- ExamSimulator → ExamSection

### Many-to-Many (N:N)
- User ↔ Badge (via user_badges)
- User ↔ ThematicScenario (via user_unlocked_scenarios)

---

## 4. Modelos con Campos JSON

| Modelo | Campo JSON |
|--------|------------|
| `Unit` | learning_objectives |
| `UserProgress` | completed_topics |
| `Badge` | criteria |
| `MiniGameContent` | content |
| `UserActivity` | metadata |
| `StudyProgress` | completed_items |

---

*Mapa de modelos - English Learning Platform*