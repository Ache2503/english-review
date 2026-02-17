from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Tabla de asociación para User-Badge (muchos a muchos)
user_badges = db.Table(
    'user_badges',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('badge_id', db.Integer, db.ForeignKey('badges.id'), primary_key=True),
    db.Column('earned_at', db.DateTime, default=datetime.utcnow)
)


class User(UserMixin, db.Model):
    """Modelo de usuario con seguimiento de progreso"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    last_login_date = db.Column(db.Date, nullable=True)  # Para el reto diario
    daily_challenge_completed = db.Column(db.Boolean, default=False)  # Si completó el reto de hoy
    
    # Relaciones
    progress = db.relationship('UserProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    badges_earned = db.relationship('Badge', secondary=user_badges, backref='owners')

    def set_password(self, password):
        """Hashear y guardar contraseña"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verificar contraseña"""
        return check_password_hash(self.password_hash, password)
    
    def get_progress(self):
        """Obtener progreso del usuario"""
        total_units = Unit.query.count()
        completed_units = self.progress.filter_by(completed=True).count()
        return {
            'total_units': total_units,
            'completed_units': completed_units,
            'percentage': (completed_units / total_units * 100) if total_units > 0 else 0
        }
    
    def __repr__(self):
        return f'<User {self.username}>'


class Unit(db.Model):
    """Modelo para cada unidad de estudio"""
    __tablename__ = 'units'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.Integer, unique=True, nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    detailed_explanation = db.Column(db.Text)  # Explicación detallada de la unidad
    learning_objectives = db.Column(db.JSON)  # Objetivos de aprendizaje en array
    overview = db.Column(db.Text)  # Vista general de los temas
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    topics = db.relationship('Topic', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    grammar_rules = db.relationship('GrammarRule', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    vocabulary_categories = db.relationship('VocabularyCategory', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    writing_practices = db.relationship('WritingPractice', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    user_progress = db.relationship('UserProgress', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    explanations = db.relationship('UnitExplanation', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    # Extra JSON data per unit (optional one-to-one)
    # extra relationship can be added later if needed
    
    def __repr__(self):
        return f'<Unit {self.unit_number}: {self.title}>'


class Topic(db.Model):
    """Modelo para tópicos dentro de cada unidad"""
    __tablename__ = 'topics'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    detailed_explanation = db.Column(db.Text)  # Explicación detallada del tema
    key_concepts = db.Column(db.JSON)  # Conceptos clave en array
    common_mistakes = db.Column(db.JSON)  # Errores comunes en array
    tips = db.Column(db.JSON)  # Consejos útiles en array
    examples = db.Column(db.JSON)  # Ejemplos ilustrativos en array
    order = db.Column(db.Integer, default=0)
    
    # Relaciones
    explanations = db.relationship('TopicExplanation', backref='topic', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Topic {self.title}>'


class GrammarRule(db.Model):
    """Modelo para reglas gramaticales"""
    __tablename__ = 'grammar_rules'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    topic = db.Column(db.String(200), nullable=False)
    rule = db.Column(db.Text, nullable=False)
    detailed_explanation = db.Column(db.Text)  # Explicación detallada de la regla
    example = db.Column(db.Text)
    examples = db.Column(db.JSON)  # Múltiples ejemplos en array
    correct_usage = db.Column(db.JSON)  # Usos correctos en array
    incorrect_usage = db.Column(db.JSON)  # Usos incorrectos en array
    common_errors = db.Column(db.JSON)  # Errores comunes en array
    exceptions = db.Column(db.Text)  # Excepciones a la regla
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GrammarRule {self.topic}>'


class VocabularyCategory(db.Model):
    """Modelo para categorías de vocabulario"""
    __tablename__ = 'vocabulary_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    category_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    order = db.Column(db.Integer, default=0)
    
    # Relaciones
    vocabulary_items = db.relationship('VocabularyItem', backref='category', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<VocabularyCategory {self.category_name}>'


class VocabularyItem(db.Model):
    """Modelo para palabras individuales"""
    __tablename__ = 'vocabulary_items'
    
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('vocabulary_categories.id'), nullable=False, index=True)
    word = db.Column(db.String(200), nullable=False)
    definition = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text)
    pronunciation = db.Column(db.String(200))
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<VocabularyItem {self.word}>'


class WritingPractice(db.Model):
    """Modelo para ejercicios de escritura"""
    __tablename__ = 'writing_practices'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    example_text = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), default='intermediate')  # beginner, intermediate, advanced
    order = db.Column(db.Integer, default=0)
    
    # Relaciones
    user_submissions = db.relationship('UserWritingSubmission', backref='practice', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<WritingPractice {self.title}>'


class UserProgress(db.Model):
    """Modelo para rastrear el progreso del usuario por unidad"""
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    completed = db.Column(db.Boolean, default=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    progress_percentage = db.Column(db.Float, default=0.0)
    
    # Nuevos campos para el sistema de desbloqueo
    grammar_completed = db.Column(db.Boolean, default=False)
    vocabulary_completed = db.Column(db.Boolean, default=False)
    exercises_completed = db.Column(db.Boolean, default=False)
    challenge_passed = db.Column(db.Boolean, default=False)
    challenge_score = db.Column(db.Float, default=0.0)
    challenge_attempts = db.Column(db.Integer, default=0)
    unlocked = db.Column(db.Boolean, default=False)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'unit_id', name='uq_user_unit'),)
    
    def can_take_challenge(self):
        """Verificar si puede tomar el desafío final"""
        return self.grammar_completed and self.vocabulary_completed and self.exercises_completed
    
    def is_unit_completed(self):
        """Verificar si la unidad está completamente terminada"""
        return self.challenge_passed
    
    def __repr__(self):
        return f'<UserProgress User:{self.user_id} Unit:{self.unit_id}>'


class UnitChallenge(db.Model):
    """Modelo para desafíos de desbloqueo de unidad"""
    __tablename__ = 'unit_challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    passing_score = db.Column(db.Float, default=70.0)  # Porcentaje mínimo para pasar
    time_limit = db.Column(db.Integer, default=30)  # Minutos
    max_attempts = db.Column(db.Integer, default=3)  # Intentos máximos por día
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    questions = db.relationship('ChallengeQuestion', backref='challenge', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<UnitChallenge Unit:{self.unit_id}>'


class ChallengeQuestion(db.Model):
    """Preguntas para los desafíos de unidad"""
    __tablename__ = 'challenge_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('unit_challenges.id'), nullable=False, index=True)
    question_type = db.Column(db.String(50), nullable=False)  # multiple_choice, fill_blank, translation, listening, writing
    question_text = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON)  # Para preguntas de opción múltiple
    explanation = db.Column(db.Text)  # Explicación de la respuesta correcta
    points = db.Column(db.Integer, default=10)
    difficulty = db.Column(db.String(20), default='medium')  # easy, medium, hard
    skill_tested = db.Column(db.String(50))  # grammar, vocabulary, reading, writing
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<ChallengeQuestion {self.id}>'


class UserChallengeAttempt(db.Model):
    """Registro de intentos de desafío del usuario"""
    __tablename__ = 'user_challenge_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('unit_challenges.id'), nullable=False, index=True)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    score = db.Column(db.Float, default=0.0)
    passed = db.Column(db.Boolean, default=False)
    answers = db.Column(db.JSON)  # Respuestas del usuario
    time_taken = db.Column(db.Integer)  # Segundos
    
    # Relaciones
    user = db.relationship('User', backref='challenge_attempts')
    challenge = db.relationship('UnitChallenge', backref='attempts')
    
    def __repr__(self):
        return f'<UserChallengeAttempt User:{self.user_id} Challenge:{self.challenge_id}>'


class UserWritingSubmission(db.Model):
    """Modelo para guardar envíos de escritura del usuario"""
    __tablename__ = 'user_writing_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    practice_id = db.Column(db.Integer, db.ForeignKey('writing_practices.id'), nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text)
    score = db.Column(db.Float)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    user = db.relationship('User', backref='writing_submissions')
    
    def __repr__(self):
        return f'<UserWritingSubmission {self.id}>'


class UserSentencePractice(db.Model):
    __tablename__ = 'user_sentence_practices'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    sentence = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text)
    score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='sentence_practices')


class SentenceExercise(db.Model):
    """Modelo para ejercicios de oraciones específicos por gramática"""
    __tablename__ = 'sentence_exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    grammar_rule_id = db.Column(db.Integer, db.ForeignKey('grammar_rules.id'))  # Opcional: regla específica
    exercise_type = db.Column(db.String(50), nullable=False)  # fill_blank, rearrange, translate, build
    instruction = db.Column(db.String(500), nullable=False)  # Instrucción del ejercicio
    prompt = db.Column(db.String(500))  # Texto base o contexto
    correct_answer = db.Column(db.String(500), nullable=False)  # Respuesta correcta principal
    alternative_answers = db.Column(db.JSON)  # Respuestas alternativas válidas (JSON array)
    options = db.Column(db.JSON)  # Opciones para ejercicios de selección (JSON array)
    difficulty = db.Column(db.String(20), default='beginner')  # beginner, intermediate, advanced
    grammar_focus = db.Column(db.String(200))  # Ej: "Used to", "First Conditional"
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    unit = db.relationship('Unit', backref='sentence_exercises')
    grammar_rule = db.relationship('GrammarRule', backref='exercises')
    
    def get_all_correct_answers(self):
        """Retorna todas las respuestas válidas (principal + alternativas)"""
        answers = [self.correct_answer]
        if self.alternative_answers:
            answers.extend(self.alternative_answers)
        return answers
    
    def __repr__(self):
        return f'<SentenceExercise {self.id}: {self.grammar_focus}>'


class UserSentenceExercise(db.Model):
    """Modelo para guardar respuestas de ejercicios de oraciones"""
    __tablename__ = 'user_sentence_exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('sentence_exercises.id'), nullable=False, index=True)
    user_answer = db.Column(db.String(500), nullable=False)
    is_correct = db.Column(db.Boolean)
    feedback = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    user = db.relationship('User', backref='exercise_submissions')
    exercise = db.relationship('SentenceExercise', backref='submissions')
    
    def __repr__(self):
        return f'<UserSentenceExercise User:{self.user_id} Exercise:{self.exercise_id}>'


class Flashcard(db.Model):
    """Modelo para flashcards de vocabulario"""
    __tablename__ = 'flashcards'

    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    front = db.Column(db.String(255), nullable=False)  # palabra o frase
    back = db.Column(db.String(500), nullable=False)  # definición o traducción
    example = db.Column(db.Text)
    difficulty = db.Column(db.String(20), default='beginner')
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    unit = db.relationship('Unit', backref='flashcards')

    def __repr__(self):
        return f'<Flashcard {self.front}>'


class UserFlashcardReview(db.Model):
    """Registro de repaso de flashcards por usuario"""
    __tablename__ = 'user_flashcard_reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    flashcard_id = db.Column(db.Integer, db.ForeignKey('flashcards.id'), nullable=False, index=True)
    is_correct = db.Column(db.Boolean, default=False)
    reviewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='flashcard_reviews')
    flashcard = db.relationship('Flashcard', backref='reviews')

    def __repr__(self):
        return f'<UserFlashcardReview User:{self.user_id} Flashcard:{self.flashcard_id}>'


class UserFlashcardSRS(db.Model):
    """
    Sistema de Repetición Espaciada (SRS) para flashcards.
    Almacena el estado del algoritmo SM-2 por usuario/flashcard.
    """
    __tablename__ = 'user_flashcard_srs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    flashcard_id = db.Column(db.Integer, db.ForeignKey('flashcards.id'), nullable=False, index=True)
    
    # Parámetros del algoritmo SM-2
    ease_factor = db.Column(db.Float, default=2.5)  # Factor de facilidad (mínimo 1.3)
    interval = db.Column(db.Integer, default=1)  # Intervalo actual en días
    repetitions = db.Column(db.Integer, default=0)  # Repeticiones exitosas consecutivas
    
    # Fechas
    next_review_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    last_reviewed_at = db.Column(db.DateTime)
    
    # Estadísticas
    total_reviews = db.Column(db.Integer, default=0)
    correct_reviews = db.Column(db.Integer, default=0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref='flashcard_srs')
    flashcard = db.relationship('Flashcard', backref='srs_records')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'flashcard_id', name='unique_user_flashcard_srs'),
        db.Index('idx_srs_next_review', 'user_id', 'next_review_date'),
    )

    @property
    def retention_rate(self):
        """Porcentaje de respuestas correctas"""
        if self.total_reviews == 0:
            return 0
        return round((self.correct_reviews / self.total_reviews) * 100, 1)
    
    @property
    def status(self):
        """Estado de aprendizaje: new, learning, learned, mastered"""
        if self.repetitions == 0:
            return 'new'
        elif self.repetitions < 3:
            return 'learning'
        elif self.repetitions < 6:
            return 'learned'
        else:
            return 'mastered'

    def __repr__(self):
        return f'<UserFlashcardSRS User:{self.user_id} Card:{self.flashcard_id} Next:{self.next_review_date}>'


class ErrorLog(db.Model):
    """Registro de errores gramaticales del usuario"""
    __tablename__ = 'error_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), index=True)
    source = db.Column(db.String(50), nullable=False)  # writing, sentence, exercise, quiz
    message = db.Column(db.String(500), nullable=False)
    context = db.Column(db.String(500))
    rule = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='error_logs')
    unit = db.relationship('Unit', backref='error_logs')

    def __repr__(self):
        return f'<ErrorLog User:{self.user_id} Source:{self.source}>'


class UserStreak(db.Model):
    """Rachas de estudio del usuario"""
    __tablename__ = 'user_streaks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True, index=True)
    current_streak = db.Column(db.Integer, default=0)
    longest_streak = db.Column(db.Integer, default=0)
    last_activity_date = db.Column(db.Date)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref='streak')

    def __repr__(self):
        return f'<UserStreak User:{self.user_id} Current:{self.current_streak}>'

    def __repr__(self):
        return f'<UserSentencePractice {self.id} Unit:{self.unit_id}>'


class UnitExtra(db.Model):
    """Extra JSON content per unit: study/practice/tips/prompts"""
    __tablename__ = 'unit_extras'

    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, unique=True, index=True)
    data = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    unit = db.relationship('Unit', backref=db.backref('extra', uselist=False))

    def __repr__(self):
        return f'<UnitExtra Unit:{self.unit_id}>'


class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    unit = db.relationship('Unit', backref='quizzes')
    questions = db.relationship('QuizQuestion', backref='quiz', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Quiz {self.title} Unit:{self.unit_id}>'


class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False, index=True)
    prompt = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0)

    options = db.relationship('QuizOption', backref='question', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<QuizQuestion {self.id}>'


class QuizOption(db.Model):
    __tablename__ = 'quiz_options'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.id'), nullable=False, index=True)
    text = db.Column(db.String(300), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<QuizOption {self.id} Correct:{self.is_correct}>'


class UserQuizSubmission(db.Model):
    __tablename__ = 'user_quiz_submissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False, index=True)
    score = db.Column(db.Float)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='quiz_submissions')
    quiz = db.relationship('Quiz', backref='submissions')

    def __repr__(self):
        return f'<UserQuizSubmission {self.id} Quiz:{self.quiz_id}>'


class Reading(db.Model):
    """Modelo para lecturas con extracción de oraciones"""
    __tablename__ = 'readings'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)  # El texto completo de la lectura
    difficulty = db.Column(db.String(20), default='intermediate')  # beginner, intermediate, advanced
    instructions = db.Column(db.String(500))  # Instrucción para el usuario
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    unit = db.relationship('Unit', backref='readings')
    submissions = db.relationship('UserReadingSubmission', backref='reading', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Reading {self.id}: {self.title}>'


class UserReadingSubmission(db.Model):
    """Modelo para las respuestas del usuario en lecturas"""
    __tablename__ = 'user_reading_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    reading_id = db.Column(db.Integer, db.ForeignKey('readings.id'), nullable=False, index=True)
    extracted_sentences = db.Column(db.Text, nullable=False)  # JSON list de oraciones extraídas
    feedback = db.Column(db.Text)  # Retroalimentación automática
    score = db.Column(db.Float)  # Puntuación de 0-100
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='reading_submissions')
    
    def __repr__(self):
        return f'<UserReadingSubmission {self.id} User:{self.user_id}>'


class MotivationalMessage(db.Model):
    """Modelo para mensajes psicológicos motivacionales"""
    __tablename__ = 'motivational_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Categoría: mindset, progression, effort, etc
    content = db.Column(db.String(500), nullable=False)  # El mensaje
    icon = db.Column(db.String(50))  # Emoji o ícono
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'))  # Opcional: para unidades específicas
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<MotivationalMessage {self.id}: {self.title}>'


class Badge(db.Model):
    """Modelo para badges/logros"""
    __tablename__ = 'badges'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # Ej: "Primer Paso"
    description = db.Column(db.String(500), nullable=False)  # Descripción del logro
    icon = db.Column(db.String(50), nullable=False)  # Emoji o ícono (ej: 🏆)
    color = db.Column(db.String(20), default='primary')  # Color bootstrap (primary, success, warning, etc)
    badge_type = db.Column(db.String(50), nullable=False)  # Tipo: completion, writing, reading, quiz, streak, perfect
    criteria = db.Column(db.String(200))  # Criterio de obtención (para referencia)
    is_active = db.Column(db.Boolean, default=True)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Badge {self.name}>'


class UnitExplanation(db.Model):
    """Modelo para explicaciones detalladas de cada unidad"""
    __tablename__ = 'unit_explanations'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    section_title = db.Column(db.String(200), nullable=False)  # Ej: "Introducción", "Conceptos Clave", "Aplicación"
    content = db.Column(db.Text, nullable=False)  # Contenido de la sección
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<UnitExplanation Unit:{self.unit_id} {self.section_title}>'


class TopicExplanation(db.Model):
    """Modelo para explicaciones detalladas de cada tema/tópico"""
    __tablename__ = 'topic_explanations'
    
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False, index=True)
    section_title = db.Column(db.String(200), nullable=False)  # Ej: "Definición", "Casos de uso", "Ejemplos prácticos"
    content = db.Column(db.Text, nullable=False)  # Contenido detallado
    visual_aids = db.Column(db.JSON)  # Links a imágenes o diagramas
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<TopicExplanation Topic:{self.topic_id} {self.section_title}>'


# Conversational Practice Models
class Conversation(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.Integer, primary_key=True)
    scenario = db.Column(db.String(100), nullable=False, unique=True, index=True)  # Ej: 'tienda', 'saludos'
    title = db.Column(db.String(200), nullable=False)  # Ej: 'En la tienda'
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    lines = db.relationship('ConversationLine', backref='conversation', lazy='dynamic', cascade='all, delete-orphan')


class ConversationLine(db.Model):
    __tablename__ = 'conversation_lines'
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False, index=True)
    speaker = db.Column(db.String(100), nullable=False)  # Ej: 'Cliente', 'Vendedor'
    text = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0)  # Para el orden de las líneas
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ConversationPractice(db.Model):
    """Historial de prácticas de conversación del usuario"""
    __tablename__ = 'conversation_practices'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    scenario = db.Column(db.String(100), nullable=False)  # Ej: 'store', 'directions'
    final_score = db.Column(db.Float, nullable=False)
    total_responses = db.Column(db.Integer, nullable=False)
    practice_data = db.Column(db.JSON)  # Historial detallado de respuestas
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('conversation_practices', lazy='dynamic'))


class AlternativeResponse(db.Model):
    """Respuestas alternativas aprendidas de los usuarios"""
    __tablename__ = 'alternative_responses'
    id = db.Column(db.Integer, primary_key=True)
    scenario = db.Column(db.String(100), nullable=False, index=True)
    step = db.Column(db.Integer, nullable=False)  # Paso de la conversación
    original_expected = db.Column(db.Text, nullable=False)  # Respuesta esperada original
    alternative_text = db.Column(db.Text, nullable=False)  # Respuesta alternativa del usuario
    similarity_score = db.Column(db.Float)  # Similitud con la original
    times_used = db.Column(db.Integer, default=1)  # Veces que se ha usado esta respuesta
    approved = db.Column(db.Boolean, default=False)  # Si fue aprobada manualmente
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Índice compuesto para búsquedas eficientes
    __table_args__ = (
        db.Index('idx_scenario_step', 'scenario', 'step'),
    )

    def __repr__(self):
        return f'<AlternativeResponse {self.scenario}:{self.step} "{self.alternative_text[:30]}...">'


class ResponsePattern(db.Model):
    """Patrones de respuesta detectados entre escenarios"""
    __tablename__ = 'response_patterns'
    id = db.Column(db.Integer, primary_key=True)
    pattern_text = db.Column(db.Text, nullable=False)  # Texto del patrón
    pattern_type = db.Column(db.String(50))  # Tipo: 'greeting', 'thanks', 'question', etc.
    applicable_scenarios = db.Column(db.JSON)  # Lista de escenarios donde aplica
    usage_count = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_pattern_type', 'pattern_type'),
    )


# ==========================================
# MODELOS PARA SISTEMA DE GRAMÁTICA
# ==========================================

class UserSentence(db.Model):
    """Oraciones creadas por usuarios para práctica de gramática"""
    __tablename__ = 'user_sentences'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    grammar_topic = db.Column(db.String(100), nullable=False, index=True)  # ej: 'verb-to-be', 'present-simple'
    original_sentence = db.Column(db.Text, nullable=False)  # Oración original del usuario
    corrected_sentence = db.Column(db.Text)  # Oración corregida (si aplica)
    is_correct = db.Column(db.Boolean, default=False)  # Si la oración original era correcta
    correction_notes = db.Column(db.Text)  # Notas de corrección/explicación
    spanish_translation = db.Column(db.Text)  # Traducción al español
    is_approved = db.Column(db.Boolean, default=False)  # Si está aprobada para mostrar a otros
    is_featured = db.Column(db.Boolean, default=False)  # Destacada como buen ejemplo
    likes_count = db.Column(db.Integer, default=0)  # Votos positivos
    used_in_exercises = db.Column(db.Integer, default=0)  # Veces usada en ejercicios
    difficulty = db.Column(db.String(20), default='beginner')  # beginner, intermediate, advanced
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación con usuario
    user = db.relationship('User', backref=db.backref('sentences', lazy='dynamic'))
    
    __table_args__ = (
        db.Index('idx_sentence_topic_approved', 'grammar_topic', 'is_approved'),
        db.Index('idx_sentence_featured', 'is_featured', 'grammar_topic'),
    )
    
    def __repr__(self):
        return f'<UserSentence {self.id}: "{self.original_sentence[:40]}...">'


class SentenceLike(db.Model):
    """Likes de usuarios a oraciones"""
    __tablename__ = 'sentence_likes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sentence_id = db.Column(db.Integer, db.ForeignKey('user_sentences.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'sentence_id', name='unique_user_sentence_like'),
    )


class Verb(db.Model):
    """Tabla de verbos en inglés con conjugaciones"""
    __tablename__ = 'verbs'
    
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String(100), unique=True, nullable=False, index=True)  # Infinitivo (base form)
    past_simple = db.Column(db.String(100), nullable=False)  # Pasado simple
    past_participle = db.Column(db.String(100), nullable=False)  # Participio pasado
    present_participle = db.Column(db.String(100), nullable=False)  # Gerundio (-ing)
    third_person = db.Column(db.String(100), nullable=False)  # Tercera persona singular (he/she/it)
    spanish_translation = db.Column(db.String(200), nullable=False)  # Traducción al español
    pronunciation_ipa = db.Column(db.String(100))  # Pronunciación IPA
    is_irregular = db.Column(db.Boolean, default=False)  # Si es irregular
    is_modal = db.Column(db.Boolean, default=False)  # Si es modal (can, could, etc.)
    is_auxiliary = db.Column(db.Boolean, default=False)  # Si es auxiliar (be, have, do)
    frequency_rank = db.Column(db.Integer)  # Ranking de frecuencia de uso
    difficulty = db.Column(db.String(20), default='beginner')  # beginner, intermediate, advanced
    category = db.Column(db.String(50))  # Categoría: action, state, linking, etc.
    example_sentence = db.Column(db.Text)  # Ejemplo de uso
    example_translation = db.Column(db.Text)  # Traducción del ejemplo
    notes = db.Column(db.Text)  # Notas adicionales sobre uso
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_verb_irregular', 'is_irregular'),
        db.Index('idx_verb_frequency', 'frequency_rank'),
        db.Index('idx_verb_category', 'category'),
    )
    
    def get_conjugations(self):
        """Retorna todas las conjugaciones del verbo"""
        return {
            'infinitive': self.infinitive,
            'past_simple': self.past_simple,
            'past_participle': self.past_participle,
            'present_participle': self.present_participle,
            'third_person': self.third_person,
            'spanish': self.spanish_translation
        }
    
    def __repr__(self):
        return f'<Verb {self.infinitive} ({"irregular" if self.is_irregular else "regular"})>'


class VerbTense(db.Model):
    """Conjugaciones completas por tiempo verbal"""
    __tablename__ = 'verb_tenses'
    
    id = db.Column(db.Integer, primary_key=True)
    verb_id = db.Column(db.Integer, db.ForeignKey('verbs.id'), nullable=False, index=True)
    tense_name = db.Column(db.String(50), nullable=False)  # present_simple, past_simple, future, etc.
    i_form = db.Column(db.String(100))  # I work
    you_form = db.Column(db.String(100))  # You work
    he_she_it_form = db.Column(db.String(100))  # He/She/It works
    we_form = db.Column(db.String(100))  # We work
    they_form = db.Column(db.String(100))  # They work
    negative_form = db.Column(db.String(150))  # don't work / doesn't work
    question_form = db.Column(db.String(150))  # Do you work? / Does he work?
    example_affirmative = db.Column(db.Text)
    example_negative = db.Column(db.Text)
    example_question = db.Column(db.Text)
    
    verb = db.relationship('Verb', backref=db.backref('tenses', lazy='dynamic'))
    
    __table_args__ = (
        db.UniqueConstraint('verb_id', 'tense_name', name='unique_verb_tense'),
    )
    
    def __repr__(self):
        return f'<VerbTense {self.verb.infinitive if self.verb else "?"} - {self.tense_name}>'


class GrammarExerciseResult(db.Model):
    """Resultados de ejercicios de gramática de usuarios"""
    __tablename__ = 'grammar_exercise_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    grammar_topic = db.Column(db.String(100), nullable=False, index=True)
    exercise_type = db.Column(db.String(50))  # fill_blank, multiple_choice, reorder, etc.
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    score_percentage = db.Column(db.Float, default=0.0)
    time_spent_seconds = db.Column(db.Integer)  # Tiempo en segundos
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('grammar_results', lazy='dynamic'))
    
    __table_args__ = (
        db.Index('idx_grammar_result_user_topic', 'user_id', 'grammar_topic'),
    )


# ==========================================
# SISTEMA DE RETO DIARIO (Daily Challenge)
# ==========================================

class DailyChallenge(db.Model):
    """Retos diarios para los usuarios"""
    __tablename__ = 'daily_challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    challenge_date = db.Column(db.Date, nullable=False, unique=True, index=True)
    challenge_type = db.Column(db.String(50), nullable=False)  # vocabulary, grammar, reading, writing, mixed
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    questions = db.Column(db.JSON, nullable=False)  # Lista de preguntas
    difficulty = db.Column(db.String(20), default='intermediate')
    points_reward = db.Column(db.Integer, default=50)
    bonus_streak_points = db.Column(db.Integer, default=10)  # Puntos extra por racha
    time_limit_seconds = db.Column(db.Integer)  # Límite de tiempo opcional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<DailyChallenge {self.challenge_date}: {self.title}>'


class UserDailyChallenge(db.Model):
    """Registro de retos diarios completados por usuarios"""
    __tablename__ = 'user_daily_challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('daily_challenges.id'), nullable=False, index=True)
    score = db.Column(db.Float, nullable=False)
    points_earned = db.Column(db.Integer, default=0)
    answers = db.Column(db.JSON)  # Respuestas del usuario
    time_taken_seconds = db.Column(db.Integer)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='daily_challenges_completed')
    challenge = db.relationship('DailyChallenge', backref='completions')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'challenge_id', name='unique_user_challenge'),
    )


# ==========================================
# SIMULADOR DE EXÁMENES (Exam Simulator)
# ==========================================

class ExamSimulator(db.Model):
    """Exámenes simulados (TOEFL, IELTS, Cambridge)"""
    __tablename__ = 'exam_simulators'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_type = db.Column(db.String(50), nullable=False, index=True)  # TOEFL, IELTS, CAMBRIDGE_FCE, CAMBRIDGE_CAE
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.String(20))  # A1-C2
    sections = db.Column(db.JSON, nullable=False)  # Secciones del examen
    total_time_minutes = db.Column(db.Integer, nullable=False)
    passing_score = db.Column(db.Float, default=60.0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ExamSimulator {self.exam_type}: {self.title}>'


class ExamSection(db.Model):
    """Secciones de examen (Reading, Grammar, Writing, etc.)"""
    __tablename__ = 'exam_sections'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_simulators.id'), nullable=False, index=True)
    section_type = db.Column(db.String(50), nullable=False)  # reading, grammar, vocabulary, writing
    title = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.Text)
    questions = db.Column(db.JSON, nullable=False)  # Lista de preguntas
    time_limit_minutes = db.Column(db.Integer)
    points_per_question = db.Column(db.Float, default=1.0)
    order = db.Column(db.Integer, default=0)
    
    exam = db.relationship('ExamSimulator', backref='exam_sections')
    
    def __repr__(self):
        return f'<ExamSection {self.section_type}>'


class UserExamAttempt(db.Model):
    """Intentos de examen por usuario"""
    __tablename__ = 'user_exam_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_simulators.id'), nullable=False, index=True)
    section_scores = db.Column(db.JSON)  # Puntuación por sección
    total_score = db.Column(db.Float)
    percentage = db.Column(db.Float)
    passed = db.Column(db.Boolean)
    time_taken_minutes = db.Column(db.Integer)
    answers = db.Column(db.JSON)  # Todas las respuestas
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='exam_attempts')
    exam = db.relationship('ExamSimulator', backref='attempts')
    
    def __repr__(self):
        return f'<UserExamAttempt User:{self.user_id} Exam:{self.exam_id}>'


# ==========================================
# RASTREADOR DE ERRORES (Error Tracker)
# ==========================================

class UserErrorPattern(db.Model):
    """Patrones de errores del usuario para análisis"""
    __tablename__ = 'user_error_patterns'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    error_category = db.Column(db.String(100), nullable=False, index=True)  # grammar, vocabulary, spelling, punctuation
    error_type = db.Column(db.String(100), nullable=False)  # specific error type
    error_count = db.Column(db.Integer, default=1)
    examples = db.Column(db.JSON)  # Ejemplos de errores
    last_occurrence = db.Column(db.DateTime, default=datetime.utcnow)
    suggestions = db.Column(db.JSON)  # Sugerencias de mejora
    
    user = db.relationship('User', backref='error_patterns')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'error_category', 'error_type', name='unique_user_error'),
        db.Index('idx_error_user_category', 'user_id', 'error_category'),
    )


# ==========================================
# MINI JUEGOS (Mini Games)
# ==========================================

class MiniGame(db.Model):
    """Configuración de mini juegos"""
    __tablename__ = 'mini_games'
    
    id = db.Column(db.Integer, primary_key=True)
    game_type = db.Column(db.String(50), nullable=False, unique=True)  # word_scramble, hangman, memory, fill_gaps
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    instructions = db.Column(db.Text)
    difficulty_levels = db.Column(db.JSON)  # Configuración por nivel
    points_per_level = db.Column(db.JSON)  # Puntos por nivel
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<MiniGame {self.game_type}>'


class MiniGameContent(db.Model):
    """Contenido para mini juegos"""
    __tablename__ = 'mini_game_contents'
    
    id = db.Column(db.Integer, primary_key=True)
    game_type = db.Column(db.String(50), nullable=False, index=True)
    level = db.Column(db.String(20), nullable=False)  # A1-C2 o beginner/intermediate/advanced
    content_data = db.Column(db.JSON, nullable=False)  # Datos específicos del juego
    category = db.Column(db.String(100))  # Categoría temática
    is_active = db.Column(db.Boolean, default=True)
    
    __table_args__ = (
        db.Index('idx_game_level', 'game_type', 'level'),
    )


class UserGameScore(db.Model):
    """Puntuaciones de usuarios en mini juegos"""
    __tablename__ = 'user_game_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    game_type = db.Column(db.String(50), nullable=False, index=True)
    level = db.Column(db.String(20))
    score = db.Column(db.Integer, nullable=False)
    time_seconds = db.Column(db.Integer)
    words_completed = db.Column(db.Integer)
    streak_bonus = db.Column(db.Integer, default=0)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='game_scores')
    
    __table_args__ = (
        db.Index('idx_user_game', 'user_id', 'game_type'),
    )


# ==========================================
# GRAMMAR DRILLS (Ejercicios intensivos)
# ==========================================

class GrammarDrill(db.Model):
    """Ejercicios intensivos de gramática cronometrados"""
    __tablename__ = 'grammar_drills'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    grammar_topic = db.Column(db.String(100), nullable=False, index=True)
    level = db.Column(db.String(20), nullable=False)  # A1-C2
    questions = db.Column(db.JSON, nullable=False)  # Lista de ejercicios
    time_limit_seconds = db.Column(db.Integer, default=300)  # 5 min por defecto
    passing_score = db.Column(db.Float, default=70.0)
    instructions = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GrammarDrill {self.grammar_topic} {self.level}>'


class UserDrillResult(db.Model):
    """Resultados de drills de usuarios"""
    __tablename__ = 'user_drill_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    drill_id = db.Column(db.Integer, db.ForeignKey('grammar_drills.id'), nullable=False, index=True)
    score = db.Column(db.Float, nullable=False)
    correct_answers = db.Column(db.Integer)
    total_questions = db.Column(db.Integer)
    time_taken_seconds = db.Column(db.Integer)
    passed = db.Column(db.Boolean)
    answers = db.Column(db.JSON)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='drill_results')
    drill = db.relationship('GrammarDrill', backref='results')


# ==========================================
# LEADERBOARD (Tabla de clasificación)
# ==========================================

class UserPoints(db.Model):
    """Sistema de puntos del usuario"""
    __tablename__ = 'user_points'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True, index=True)
    total_points = db.Column(db.Integer, default=0)
    weekly_points = db.Column(db.Integer, default=0)
    monthly_points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)
    last_points_update = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('points', uselist=False))
    
    def __repr__(self):
        return f'<UserPoints User:{self.user_id} Total:{self.total_points}>'


class PointsTransaction(db.Model):
    """Historial de transacciones de puntos"""
    __tablename__ = 'points_transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    points = db.Column(db.Integer, nullable=False)  # Positivo o negativo
    source = db.Column(db.String(100), nullable=False)  # challenge, quiz, game, drill, etc.
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='points_history')


# ==========================================
# IDIOMS & PHRASAL VERBS
# ==========================================

class Idiom(db.Model):
    """Modismos en inglés"""
    __tablename__ = 'idioms'
    
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(200), nullable=False, unique=True)
    meaning = db.Column(db.Text, nullable=False)
    spanish_equivalent = db.Column(db.String(200))
    example_sentence = db.Column(db.Text)
    example_translation = db.Column(db.Text)
    origin = db.Column(db.Text)  # Origen del modismo
    category = db.Column(db.String(100))  # animals, food, body, weather, etc.
    level = db.Column(db.String(20), default='B1')  # A1-C2
    usage_notes = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_idiom_level', 'level'),
        db.Index('idx_idiom_category', 'category'),
    )
    
    def __repr__(self):
        return f'<Idiom {self.phrase}>'


class PhrasalVerb(db.Model):
    """Phrasal verbs en inglés"""
    __tablename__ = 'phrasal_verbs'
    
    id = db.Column(db.Integer, primary_key=True)
    verb = db.Column(db.String(100), nullable=False)  # Base verb: look, get, put
    particle = db.Column(db.String(50), nullable=False)  # up, down, on, off, etc.
    full_form = db.Column(db.String(150), nullable=False, unique=True)  # look up, get on
    meaning = db.Column(db.Text, nullable=False)
    spanish_translation = db.Column(db.String(200))
    is_separable = db.Column(db.Boolean, default=False)  # Si se puede separar
    example_sentence = db.Column(db.Text)
    example_translation = db.Column(db.Text)
    additional_meanings = db.Column(db.JSON)  # Otros significados
    category = db.Column(db.String(100))  # movement, communication, relationship
    level = db.Column(db.String(20), default='B1')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_phrasal_verb_level', 'level'),
        db.Index('idx_phrasal_verb_base', 'verb'),
    )
    
    def __repr__(self):
        return f'<PhrasalVerb {self.full_form}>'


class UserIdiomProgress(db.Model):
    """Progreso del usuario en idioms"""
    __tablename__ = 'user_idiom_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    idiom_id = db.Column(db.Integer, db.ForeignKey('idioms.id'), nullable=False, index=True)
    times_reviewed = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    mastery_level = db.Column(db.String(20), default='new')  # new, learning, mastered
    last_reviewed = db.Column(db.DateTime)
    next_review = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='idiom_progress')
    idiom = db.relationship('Idiom', backref='user_progress')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'idiom_id', name='unique_user_idiom'),
    )


class UserPhrasalVerbProgress(db.Model):
    """Progreso del usuario en phrasal verbs"""
    __tablename__ = 'user_phrasal_verb_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    phrasal_verb_id = db.Column(db.Integer, db.ForeignKey('phrasal_verbs.id'), nullable=False, index=True)
    times_reviewed = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    mastery_level = db.Column(db.String(20), default='new')
    last_reviewed = db.Column(db.DateTime)
    next_review = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='phrasal_verb_progress')
    phrasal_verb = db.relationship('PhrasalVerb', backref='user_progress')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'phrasal_verb_id', name='unique_user_phrasal'),
    )


# ==========================================
# MODELOS PARA SISTEMA DE REPASO Y ESCRITURA
# ==========================================

class UserVocabularyProgress(db.Model):
    """Progreso del usuario en vocabulario"""
    __tablename__ = 'user_vocabulary_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    vocabulary_id = db.Column(db.Integer, db.ForeignKey('vocabulary_items.id'), nullable=False, index=True)
    times_reviewed = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    mastery_level = db.Column(db.Integer, default=0)  # 0-5
    last_reviewed = db.Column(db.DateTime)
    next_review = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='vocabulary_progress')
    vocabulary = db.relationship('VocabularyItem', backref='user_progress')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'vocabulary_id', name='unique_user_vocabulary'),
    )
    
    @property
    def accuracy(self):
        if self.times_reviewed == 0:
            return 0
        return round((self.times_correct / self.times_reviewed) * 100, 1)
    
    def __repr__(self):
        return f'<UserVocabularyProgress User:{self.user_id} Vocab:{self.vocabulary_id}>'


class ReviewSessionLog(db.Model):
    """Registro de sesiones de repaso completadas"""
    __tablename__ = 'review_session_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    session_type = db.Column(db.String(50))  # mixed, flashcards, vocabulary, idioms, etc.
    total_items = db.Column(db.Integer, default=0)
    correct_count = db.Column(db.Integer, default=0)
    wrong_count = db.Column(db.Integer, default=0)
    score = db.Column(db.Float)
    time_spent_seconds = db.Column(db.Integer)
    focus_areas = db.Column(db.JSON)  # Áreas de enfoque de la sesión
    items_reviewed = db.Column(db.JSON)  # Detalle de cada item revisado
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='review_sessions')
    
    def __repr__(self):
        return f'<ReviewSessionLog User:{self.user_id} Score:{self.score}>'


class WritingAnalysisLog(db.Model):
    """Registro de análisis de escritura realizados"""
    __tablename__ = 'writing_analysis_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), index=True)
    original_text = db.Column(db.Text, nullable=False)
    word_count = db.Column(db.Integer)
    sentence_count = db.Column(db.Integer)
    score = db.Column(db.Float)
    grade = db.Column(db.String(10))  # A+, A, B, etc.
    grammar_errors = db.Column(db.Integer, default=0)
    spelling_errors = db.Column(db.Integer, default=0)
    style_errors = db.Column(db.Integer, default=0)
    errors_detail = db.Column(db.JSON)  # Detalle de errores encontrados
    strengths = db.Column(db.JSON)  # Lista de fortalezas
    improvements = db.Column(db.JSON)  # Sugerencias de mejora
    analyzed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='writing_analyses')
    unit = db.relationship('Unit', backref='writing_analyses')
    
    def __repr__(self):
        return f'<WritingAnalysisLog User:{self.user_id} Score:{self.score}>'


class UserGrammarProgress(db.Model):
    """Progreso del usuario en temas gramaticales específicos"""
    __tablename__ = 'user_grammar_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    grammar_topic = db.Column(db.String(100), nullable=False, index=True)  # verb-to-be, present-simple, etc.
    times_practiced = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    mastery_level = db.Column(db.Integer, default=0)  # 0-5
    common_errors = db.Column(db.JSON)  # Errores frecuentes en este tema
    last_practiced = db.Column(db.DateTime)
    next_review = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='grammar_progress')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'grammar_topic', name='unique_user_grammar_topic'),
    )
    
    @property
    def accuracy(self):
        if self.times_practiced == 0:
            return 0
        return round((self.times_correct / self.times_practiced) * 100, 1)
    
    def __repr__(self):
        return f'<UserGrammarProgress User:{self.user_id} Topic:{self.grammar_topic}>'


# ============================================================================
# NUEVOS JUEGOS - QUICK QUIZ, READING, SPEED TYPING
# ============================================================================

class QuickQuiz(db.Model):
    """Preguntas para Quick Quiz"""
    __tablename__ = 'quick_quiz_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    wrong_answers = db.Column(db.JSON, nullable=False)  # Lista de respuestas incorrectas
    explanation = db.Column(db.Text)
    category = db.Column(db.String(100))  # grammar, vocabulary, phrasal_verbs, etc.
    cefr_level = db.Column(db.String(10))  # A1, A2, B1, B2, C1, C2
    difficulty = db.Column(db.String(20), default='intermediate')  # easy, medium, hard
    image_url = db.Column(db.String(500))  # Opcional: imagen para la pregunta
    audio_url = db.Column(db.String(500))  # Opcional: audio para listening practice
    is_active = db.Column(db.Boolean, default=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_quiz_level_category', 'cefr_level', 'category'),
    )
    
    def get_options(self):
        """Obtener todas las opciones mezcladas"""
        import random
        options = [self.correct_answer] + self.wrong_answers
        random.shuffle(options)
        return options
    
    def __repr__(self):
        return f'<QuickQuiz {self.question[:50]}>'


class UserQuizScore(db.Model):
    """Puntuaciones de usuarios en Quick Quiz"""
    __tablename__ = 'user_quiz_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quick_quiz_questions.id'), nullable=False)
    
    is_correct = db.Column(db.Boolean, nullable=False)
    time_seconds = db.Column(db.Integer)
    score = db.Column(db.Integer, default=0)
    
    played_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='quiz_scores')
    quiz = db.relationship('QuickQuiz', backref='user_scores')
    
    __table_args__ = (
        db.Index('idx_user_quiz', 'user_id', 'quiz_id'),
    )
    
    def __repr__(self):
        return f'<UserQuizScore User:{self.user_id} Quiz:{self.quiz_id}>'


class ReadingComprehension(db.Model):
    """Lecturas para comprensión lectora"""
    __tablename__ = 'reading_comprehensions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    passage = db.Column(db.Text, nullable=False)  # El texto a leer
    passage_summary = db.Column(db.Text)  # Resumen del pasaje
    cefr_level = db.Column(db.String(10), nullable=False)  # A1-C2
    category = db.Column(db.String(100))  # Technology, History, Culture, etc.
    word_count = db.Column(db.Integer)
    reading_time_minutes = db.Column(db.Integer)
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    questions = db.relationship('ReadingQuestion', backref='reading', cascade='all, delete-orphan')
    
    __table_args__ = (
        db.Index('idx_reading_level', 'cefr_level'),
    )
    
    def __repr__(self):
        return f'<ReadingComprehension {self.title}>'


class ReadingQuestion(db.Model):
    """Preguntas sobre un texto de comprensión"""
    __tablename__ = 'reading_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    reading_id = db.Column(db.Integer, db.ForeignKey('reading_comprehensions.id'), nullable=False, index=True)
    
    question = db.Column(db.String(500), nullable=False)
    question_type = db.Column(db.String(50), default='multiple_choice')  # multiple_choice, true_false, short_answer
    correct_answer = db.Column(db.String(500), nullable=False)
    wrong_answers = db.Column(db.JSON)  # Para multiple choice
    
    question_order = db.Column(db.Integer, default=1)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReadingQuestion {self.id}>'


class UserReadingScore(db.Model):
    """Puntuaciones en lecturas"""
    __tablename__ = 'user_reading_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    reading_id = db.Column(db.Integer, db.ForeignKey('reading_comprehensions.id'), nullable=False, index=True)
    
    correct_answers = db.Column(db.Integer, default=0)
    total_questions = db.Column(db.Integer, default=0)
    time_seconds = db.Column(db.Integer)
    score = db.Column(db.Integer, default=0)  # Puntuación total
    
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='reading_scores')
    reading = db.relationship('ReadingComprehension', backref='user_scores')
    
    __table_args__ = (
        db.Index('idx_user_reading', 'user_id', 'reading_id'),
    )
    
    def accuracy_percentage(self):
        """Porcentaje de aciertos"""
        if self.total_questions == 0:
            return 0
        return (self.correct_answers / self.total_questions) * 100
    
    def __repr__(self):
        return f'<UserReadingScore User:{self.user_id} Reading:{self.reading_id}>'


class SpeedTyping(db.Model):
    """Contenido para Speed Typing game"""
    __tablename__ = 'speed_typing_content'
    
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(500), nullable=False)  # Frase a escribir
    category = db.Column(db.String(100))  # common_phrases, idioms, grammar, vocabulary
    cefr_level = db.Column(db.String(10))  # A1-C2
    difficulty = db.Column(db.String(20), default='intermediate')  # easy, medium, hard
    pronunciation_hint = db.Column(db.String(200))  # Pista de pronunciación
    meaning = db.Column(db.Text)  # Significado/traducción
    example_sentence = db.Column(db.Text)  # Oración de ejemplo
    audio_url = db.Column(db.String(500))  # URL del audio
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_typing_level', 'cefr_level'),
    )
    
    def __repr__(self):
        return f'<SpeedTyping {self.phrase[:40]}>'


class UserTypingScore(db.Model):
    """Puntuaciones en Speed Typing"""
    __tablename__ = 'user_typing_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    typing_id = db.Column(db.Integer, db.ForeignKey('speed_typing_content.id'), nullable=False)
    
    typed_text = db.Column(db.String(500))  # Lo que escribió el usuario
    is_correct = db.Column(db.Boolean, nullable=False)
    time_seconds = db.Column(db.Float)
    words_per_minute = db.Column(db.Float)  # WPM
    accuracy_percentage = db.Column(db.Float)  # % de precisión (caracteres correctos)
    score = db.Column(db.Integer, default=0)  # Puntuación total
    
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='typing_scores')
    typing = db.relationship('SpeedTyping', backref='user_scores')
    
    __table_args__ = (
        db.Index('idx_user_typing', 'user_id'),
    )
    
    def __repr__(self):
        return f'<UserTypingScore User:{self.user_id} WPM:{self.words_per_minute}>'


# ===== ESTUDIO INTENSIVO =====
class StudyExerciseResult(db.Model):
    """Modelo para guardar resultados de ejercicios de estudio"""
    __tablename__ = 'study_exercise_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    topic_id = db.Column(db.String(100), nullable=False, index=True)  # ID del tema en JSON
    exercise_index = db.Column(db.Integer, nullable=False)  # Índice del ejercicio
    question_index = db.Column(db.Integer, nullable=False)  # Índice de pregunta
    user_answer = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    attempts = db.Column(db.Integer, default=1)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='study_results')
    
    __table_args__ = (
        db.Index('idx_user_topic_exercise', 'user_id', 'topic_id'),
        db.UniqueConstraint('user_id', 'topic_id', 'exercise_index', 'question_index', 
                           name='uq_study_exercise_result'),
    )
    
    def __repr__(self):
        return f'<StudyExerciseResult User:{self.user_id} Topic:{self.topic_id} Q:{self.question_index}>'


class StudyProgress(db.Model):
    """Modelo para rastrear progreso del usuario en temas de estudio"""
    __tablename__ = 'study_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    topic_id = db.Column(db.String(100), nullable=False, index=True)  # ID del tema en JSON
    
    # Progreso
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False)
    
    # Estadísticas
    exercises_attempted = db.Column(db.Integer, default=0)
    exercises_correct = db.Column(db.Integer, default=0)
    success_rate = db.Column(db.Float, default=0.0)  # Porcentaje de éxito
    time_spent_minutes = db.Column(db.Float, default=0.0)
    
    # Última actualización
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref='study_progress')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'topic_id', name='uq_user_topic_study'),
        db.Index('idx_user_study_progress', 'user_id'),
    )
    
    def calculate_success_rate(self):
        """Calcular tasa de éxito"""
        if self.exercises_attempted == 0:
            return 0.0
        return (self.exercises_correct / self.exercises_attempted) * 100
    
    def mark_completed(self):
        """Marcar tema como completado"""
        self.is_completed = True
        self.completed_at = datetime.utcnow()
        self.success_rate = self.calculate_success_rate()
    
    def __repr__(self):
        return f'<StudyProgress User:{self.user_id} Topic:{self.topic_id} Success:{self.success_rate}%>'