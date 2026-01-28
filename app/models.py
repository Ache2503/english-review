from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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
    
    # Relaciones
    progress = db.relationship('UserProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
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
    
    __table_args__ = (db.UniqueConstraint('user_id', 'unit_id', name='uq_user_unit'),)
    
    def __repr__(self):
        return f'<UserProgress User:{self.user_id} Unit:{self.unit_id}>'


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


# Tabla de asociación para User-Badge (muchos a muchos)
user_badges = db.Table(
    'user_badges',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('badge_id', db.Integer, db.ForeignKey('badges.id'), primary_key=True),
    db.Column('earned_at', db.DateTime, default=datetime.utcnow)
)