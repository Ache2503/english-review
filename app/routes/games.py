"""
Rutas para Mini Games - Juegos educativos
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import MiniGame, MiniGameContent, UserGameScore, Idiom, PhrasalVerb
from datetime import datetime
from sqlalchemy import func
from app.routes.challenges import add_points
import random

games_bp = Blueprint('games', __name__, url_prefix='/games')


def complete_daily_challenge():
    """Marcar el reto diario como completado"""
    if current_user.is_authenticated:
        current_user.daily_challenge_completed = True
        db.session.commit()


@games_bp.route('/')
@login_required
def game_list():
    """Lista de mini juegos disponibles"""
    games = MiniGame.query.filter_by(is_active=True).all()
    
    # Estadísticas del usuario
    user_stats = {}
    for game in games:
        stats = db.session.query(
            func.count(UserGameScore.id),
            func.max(UserGameScore.score),
            func.avg(UserGameScore.score)
        ).filter(
            UserGameScore.user_id == current_user.id,
            UserGameScore.game_type == game.game_type
        ).first()
        
        user_stats[game.game_type] = {
            'games_played': stats[0] or 0,
            'best_score': stats[1] or 0,
            'avg_score': round(stats[2] or 0, 1)
        }
    
    return render_template(
        'games/list.html',
        games=games,
        user_stats=user_stats
    )


# ==========================================
# WORD SCRAMBLE
# ==========================================

@games_bp.route('/word-scramble')
@login_required
def word_scramble():
    """Juego de reordenar letras"""
    level = request.args.get('level', 'A1')
    
    return render_template(
        'games/word_scramble.html',
        level=level
    )


@games_bp.route('/word-scramble/get-words')
@login_required
def get_scramble_words():
    """Obtener palabras para el juego"""
    level = request.args.get('level', 'A1')
    count = int(request.args.get('count', 10))
    
    # Obtener contenido del juego
    content = MiniGameContent.query.filter_by(
        game_type='word_scramble',
        level=level,
        is_active=True
    ).all()
    
    words = []
    for c in content:
        if c.content_data and 'words' in c.content_data:
            words.extend(c.content_data['words'])
    
    # Si no hay contenido, usar palabras por defecto
    if not words:
        words = get_default_words(level)
    
    # Mezclar y limitar
    random.shuffle(words)
    selected = words[:count]
    
    # Scramble las palabras
    result = []
    for word_data in selected:
        word = word_data['word'] if isinstance(word_data, dict) else word_data
        hint = word_data.get('hint', '') if isinstance(word_data, dict) else ''
        
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)
        
        # Evitar que quede igual
        while scrambled == word and len(word) > 1:
            random.shuffle(letters)
            scrambled = ''.join(letters)
        
        result.append({
            'scrambled': scrambled,
            'answer': word,
            'hint': hint
        })
    
    return jsonify({'words': result})


@games_bp.route('/word-scramble/submit', methods=['POST'])
@login_required
def submit_word_scramble():
    """Guardar resultado de word scramble"""
    data = request.get_json()
    score = data.get('score', 0)
    level = data.get('level', 'A1')
    time_seconds = data.get('time_seconds', 0)
    words_completed = data.get('words_completed', 0)
    from_daily = data.get('from_daily', False)
    
    # Guardar puntuación
    game_score = UserGameScore(
        user_id=current_user.id,
        game_type='word_scramble',
        level=level,
        score=score,
        time_seconds=time_seconds,
        words_completed=words_completed
    )
    db.session.add(game_score)
    
    # Dar puntos
    points = score // 10 + words_completed
    add_points(current_user.id, points, 'game', f'Word Scramble - {level}')
    
    # Completar reto diario si aplica
    if from_daily:
        complete_daily_challenge()
    
    db.session.commit()
    
    return jsonify({'success': True, 'points_earned': points})


# ==========================================
# HANGMAN
# ==========================================

@games_bp.route('/hangman')
@login_required
def hangman():
    """Juego del ahorcado"""
    level = request.args.get('level', 'A1')
    
    return render_template(
        'games/hangman.html',
        level=level
    )


@games_bp.route('/hangman/get-word')
@login_required
def get_hangman_word():
    """Obtener palabra para hangman"""
    level = request.args.get('level', 'A1')
    
    content = MiniGameContent.query.filter_by(
        game_type='hangman',
        level=level,
        is_active=True
    ).all()
    
    words = []
    for c in content:
        if c.content_data and 'words' in c.content_data:
            words.extend(c.content_data['words'])
    
    if not words:
        words = get_default_words(level)
    
    word_data = random.choice(words)
    word = word_data['word'] if isinstance(word_data, dict) else word_data
    hint = word_data.get('hint', '') if isinstance(word_data, dict) else ''
    
    return jsonify({
        'length': len(word),
        'hint': hint,
        'word_id': hash(word) % 10000  # ID simple para verificar
    })


@games_bp.route('/hangman/check-letter', methods=['POST'])
@login_required
def check_hangman_letter():
    """Verificar letra en hangman"""
    data = request.get_json()
    letter = data.get('letter', '').lower()
    word = data.get('word', '').lower()
    
    positions = [i for i, c in enumerate(word) if c == letter]
    
    return jsonify({
        'found': len(positions) > 0,
        'positions': positions
    })


@games_bp.route('/hangman/submit', methods=['POST'])
@login_required
def submit_hangman():
    """Guardar resultado de hangman"""
    data = request.get_json()
    score = data.get('score', 0)
    level = data.get('level', 'A1')
    won = data.get('won', False)
    attempts_left = data.get('attempts_left', 0)
    word_length = data.get('word_length', 0)
    from_daily = data.get('from_daily', False)
    
    # Calcular puntos: más puntos si ganó y con más intentos restantes
    if won:
        bonus_points = attempts_left * 10  # 10 puntos por cada intento no usado
        total_score = score + bonus_points + word_length * 5
    else:
        total_score = score
    
    # Guardar puntuación
    game_score = UserGameScore(
        user_id=current_user.id,
        game_type='hangman',
        level=level,
        score=total_score,
        words_completed=1 if won else 0
    )
    db.session.add(game_score)
    
    # Dar puntos al usuario
    points = total_score // 10
    if won:
        points += 5  # Bonus por ganar
    add_points(current_user.id, points, 'game', f'Hangman - {level}')
    
    # Completar reto diario si aplica
    if from_daily:
        complete_daily_challenge()
    
    db.session.commit()
    
    return jsonify({
        'success': True, 
        'points_earned': points,
        'total_score': total_score,
        'won': won
    })


# ==========================================
# MEMORY MATCH
# ==========================================

@games_bp.route('/memory')
@login_required
def memory_game():
    """Juego de memoria"""
    level = request.args.get('level', 'A1')
    
    return render_template(
        'games/memory.html',
        level=level
    )


@games_bp.route('/memory/get-cards')
@login_required
def get_memory_cards():
    """Obtener tarjetas para juego de memoria"""
    level = request.args.get('level', 'A1')
    pairs = int(request.args.get('pairs', 8))
    
    content = MiniGameContent.query.filter_by(
        game_type='memory',
        level=level,
        is_active=True
    ).all()
    
    word_pairs = []
    for c in content:
        if c.content_data and 'pairs' in c.content_data:
            word_pairs.extend(c.content_data['pairs'])
    
    if not word_pairs:
        word_pairs = get_default_pairs(level)
    
    random.shuffle(word_pairs)
    selected = word_pairs[:pairs]
    
    # Crear tarjetas
    cards = []
    for i, pair in enumerate(selected):
        cards.append({'id': i * 2, 'content': pair['english'], 'pair_id': i})
        cards.append({'id': i * 2 + 1, 'content': pair['spanish'], 'pair_id': i})
    
    random.shuffle(cards)
    
    return jsonify({'cards': cards})


@games_bp.route('/memory/submit', methods=['POST'])
@login_required
def submit_memory():
    """Guardar resultado de memory"""
    data = request.get_json()
    score = data.get('score', 0)
    level = data.get('level', 'A1')
    time_seconds = data.get('time_seconds', 0)
    from_daily = data.get('from_daily', False)
    
    game_score = UserGameScore(
        user_id=current_user.id,
        game_type='memory',
        level=level,
        score=score,
        time_seconds=time_seconds
    )
    db.session.add(game_score)
    
    points = score + max(0, (120 - time_seconds) // 10)
    add_points(current_user.id, points, 'game', f'Memory Match - {level}')
    
    if from_daily:
        complete_daily_challenge()
    
    db.session.commit()
    
    return jsonify({'success': True, 'points_earned': points})


# ==========================================
# FILL THE GAPS
# ==========================================

@games_bp.route('/fill-gaps')
@login_required
def fill_gaps():
    """Juego de completar espacios"""
    level = request.args.get('level', 'A1')
    
    return render_template(
        'games/fill_gaps.html',
        level=level
    )


@games_bp.route('/fill-gaps/get-sentences')
@login_required
def get_fill_gaps_sentences():
    """Obtener oraciones para completar"""
    level = request.args.get('level', 'A1')
    count = int(request.args.get('count', 10))
    
    content = MiniGameContent.query.filter_by(
        game_type='fill_gaps',
        level=level,
        is_active=True
    ).all()
    
    sentences = []
    for c in content:
        if c.content_data and 'sentences' in c.content_data:
            sentences.extend(c.content_data['sentences'])
    
    if not sentences:
        sentences = get_default_sentences(level)
    
    random.shuffle(sentences)
    
    return jsonify({'sentences': sentences[:count]})


@games_bp.route('/fill-gaps/submit', methods=['POST'])
@login_required
def submit_fill_gaps():
    """Guardar resultado de fill gaps"""
    data = request.get_json()
    score = data.get('score', 0)
    level = data.get('level', 'A1')
    correct = data.get('correct', 0)
    total = data.get('total', 0)
    from_daily = data.get('from_daily', False)
    
    game_score = UserGameScore(
        user_id=current_user.id,
        game_type='fill_gaps',
        level=level,
        score=score,
        words_completed=correct
    )
    db.session.add(game_score)
    
    points = correct * 5
    add_points(current_user.id, points, 'game', f'Fill the Gaps - {level}')
    
    if from_daily:
        complete_daily_challenge()
    
    db.session.commit()
    
    return jsonify({'success': True, 'points_earned': points})


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_default_words(level):
    """Palabras por defecto si no hay contenido"""
    words_by_level = {
        'A1': [
            {'word': 'hello', 'hint': 'Greeting'},
            {'word': 'water', 'hint': 'Drink'},
            {'word': 'house', 'hint': 'Building'},
            {'word': 'table', 'hint': 'Furniture'},
            {'word': 'apple', 'hint': 'Fruit'},
            {'word': 'happy', 'hint': 'Emotion'},
            {'word': 'green', 'hint': 'Color'},
            {'word': 'friend', 'hint': 'Person'},
            {'word': 'school', 'hint': 'Education'},
            {'word': 'mother', 'hint': 'Family'}
        ],
        'A2': [
            {'word': 'beautiful', 'hint': 'Appearance'},
            {'word': 'important', 'hint': 'Significance'},
            {'word': 'yesterday', 'hint': 'Time'},
            {'word': 'different', 'hint': 'Not the same'},
            {'word': 'together', 'hint': 'Unity'},
            {'word': 'possible', 'hint': 'Can happen'},
            {'word': 'remember', 'hint': 'Memory'},
            {'word': 'question', 'hint': 'Inquiry'},
            {'word': 'favorite', 'hint': 'Preferred'},
            {'word': 'exercise', 'hint': 'Physical activity'}
        ],
        'B1': [
            {'word': 'achievement', 'hint': 'Success'},
            {'word': 'environment', 'hint': 'Nature'},
            {'word': 'comfortable', 'hint': 'At ease'},
            {'word': 'opportunity', 'hint': 'Chance'},
            {'word': 'relationship', 'hint': 'Connection'},
            {'word': 'experience', 'hint': 'Knowledge'},
            {'word': 'communicate', 'hint': 'Talk'},
            {'word': 'responsibility', 'hint': 'Duty'},
            {'word': 'entertainment', 'hint': 'Fun'},
            {'word': 'development', 'hint': 'Growth'}
        ]
    }
    return words_by_level.get(level, words_by_level['A1'])


def get_default_pairs(level):
    """Pares por defecto para memory"""
    pairs_by_level = {
        'A1': [
            {'english': 'Hello', 'spanish': 'Hola'},
            {'english': 'Goodbye', 'spanish': 'Adiós'},
            {'english': 'Thank you', 'spanish': 'Gracias'},
            {'english': 'Water', 'spanish': 'Agua'},
            {'english': 'Food', 'spanish': 'Comida'},
            {'english': 'House', 'spanish': 'Casa'},
            {'english': 'Family', 'spanish': 'Familia'},
            {'english': 'Friend', 'spanish': 'Amigo'},
            {'english': 'School', 'spanish': 'Escuela'},
            {'english': 'Work', 'spanish': 'Trabajo'}
        ],
        'A2': [
            {'english': 'Beautiful', 'spanish': 'Hermoso'},
            {'english': 'Important', 'spanish': 'Importante'},
            {'english': 'Difficult', 'spanish': 'Difícil'},
            {'english': 'Interesting', 'spanish': 'Interesante'},
            {'english': 'Favorite', 'spanish': 'Favorito'},
            {'english': 'Tomorrow', 'spanish': 'Mañana'},
            {'english': 'Yesterday', 'spanish': 'Ayer'},
            {'english': 'Together', 'spanish': 'Juntos'},
            {'english': 'Sometimes', 'spanish': 'A veces'},
            {'english': 'Always', 'spanish': 'Siempre'}
        ]
    }
    return pairs_by_level.get(level, pairs_by_level['A1'])


def get_default_sentences(level):
    """Oraciones por defecto para fill gaps"""
    sentences_by_level = {
        'A1': [
            {'sentence': 'I ___ a student.', 'answer': 'am', 'options': ['am', 'is', 'are']},
            {'sentence': 'She ___ to school every day.', 'answer': 'goes', 'options': ['go', 'goes', 'going']},
            {'sentence': 'They ___ very happy.', 'answer': 'are', 'options': ['is', 'am', 'are']},
            {'sentence': 'He ___ a car.', 'answer': 'has', 'options': ['have', 'has', 'having']},
            {'sentence': 'We ___ English.', 'answer': 'speak', 'options': ['speak', 'speaks', 'speaking']}
        ],
        'A2': [
            {'sentence': 'I ___ to the cinema yesterday.', 'answer': 'went', 'options': ['go', 'went', 'gone']},
            {'sentence': 'She has ___ her homework.', 'answer': 'done', 'options': ['do', 'did', 'done']},
            {'sentence': 'They are ___ for the bus.', 'answer': 'waiting', 'options': ['wait', 'waited', 'waiting']},
            {'sentence': 'He ___ play tennis tomorrow.', 'answer': 'will', 'options': ['will', 'would', 'was']},
            {'sentence': 'We have ___ here for two years.', 'answer': 'lived', 'options': ['live', 'living', 'lived']}
        ]
    }
    return sentences_by_level.get(level, sentences_by_level['A1'])


# ==========================================
# QUICK QUIZ
# ==========================================

@games_bp.route('/quick-quiz')
@login_required
def quick_quiz():
    """Página del juego Quick Quiz"""
    level = request.args.get('level', 'A1')
    category = request.args.get('category', '')
    
    return render_template(
        'games/quick_quiz.html',
        level=level,
        category=category
    )


@games_bp.route('/quick-quiz/get-questions')
@login_required
def get_quiz_questions():
    """Obtener preguntas de Quick Quiz"""
    from app.models import QuickQuiz, UserQuizScore
    
    level = request.args.get('level', 'A1')
    category = request.args.get('category', '')
    count = int(request.args.get('count', 5))
    
    # Obtener preguntas
    query = QuickQuiz.query.filter_by(cefr_level=level, is_active=True)
    
    if category:
        query = query.filter_by(category=category)
    
    questions = query.all()
    
    if not questions:
        return jsonify({'error': 'No questions found'}), 404
    
    # Seleccionar preguntas aleatorias
    random.shuffle(questions)
    selected = questions[:count]
    
    result = []
    for q in selected:
        result.append({
            'id': q.id,
            'question': q.question,
            'options': q.get_options(),
            'correct_answer': q.correct_answer,
            'explanation': q.explanation,
            'category': q.category
        })
    
    return jsonify(result)


@games_bp.route('/quick-quiz/submit-answer', methods=['POST'])
@login_required
def submit_quiz_answer():
    """Enviar respuesta de Quick Quiz"""
    from app.models import QuickQuiz, UserQuizScore
    
    data = request.get_json()
    quiz_id = data.get('quiz_id')
    answer = data.get('answer')
    time_seconds = data.get('time_seconds', 0)
    
    quiz = QuickQuiz.query.get(quiz_id)
    if not quiz:
        return jsonify({'error': 'Quiz not found'}), 404
    
    is_correct = answer.lower() == quiz.correct_answer.lower()
    
    # Calcular puntuación
    score = 0
    if is_correct:
        if time_seconds < 5:
            score = 50
        elif time_seconds < 10:
            score = 40
        else:
            score = 30
    
    # Guardar puntuación
    quiz_score = UserQuizScore(
        user_id=current_user.id,
        quiz_id=quiz_id,
        is_correct=is_correct,
        time_seconds=time_seconds,
        score=score
    )
    db.session.add(quiz_score)
    db.session.commit()
    
    # Agregar puntos al usuario
    if is_correct:
        add_points(current_user.id, score, 'game', f'Quick Quiz - {quiz.category}')
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': quiz.correct_answer,
        'explanation': quiz.explanation,
        'score': score
    })


@games_bp.route('/quick-quiz/submit-final', methods=['POST'])
@login_required
def submit_quiz_final():
    """Guardar resultado final del Quick Quiz"""
    data = request.get_json()
    score = data.get('score', 0)
    level = data.get('level', 'A1')
    correct_count = data.get('correct_count', 0)
    total_questions = data.get('total_questions', 5)
    time_seconds = data.get('time_seconds', 0)
    from_daily = data.get('from_daily', False)
    
    # Guardar puntuación en UserGameScore
    game_score = UserGameScore(
        user_id=current_user.id,
        game_type='quick_quiz',
        level=level,
        score=score,
        time_seconds=time_seconds,
        words_completed=correct_count
    )
    db.session.add(game_score)
    
    # Calcular puntos a dar al usuario
    points = correct_count * 5  # 5 puntos por cada respuesta correcta
    if correct_count == total_questions:
        points += 10  # Bonus por responder todas correctamente
    
    add_points(current_user.id, points, 'game', f'Quick Quiz - {level}')
    
    if from_daily:
        complete_daily_challenge()
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'total_score': score
    })


# ==========================================
# READING COMPREHENSION
# ==========================================

@games_bp.route('/reading')
@login_required
def reading_list():
    """Lista de lecturas disponibles"""
    from app.models import ReadingComprehension, UserReadingScore
    
    level = request.args.get('level', '')
    
    query = ReadingComprehension.query.filter_by(is_active=True)
    
    if level:
        query = query.filter_by(cefr_level=level)
    
    readings = query.all()
    
    # Estadísticas del usuario
    user_stats = {}
    for reading in readings:
        score = UserReadingScore.query.filter_by(
            user_id=current_user.id,
            reading_id=reading.id
        ).first()
        
        user_stats[reading.id] = {
            'completed': score is not None,
            'score': score.score if score else 0,
            'accuracy': round(score.accuracy_percentage(), 1) if score else 0
        }
    
    return render_template(
        'games/reading_list.html',
        readings=readings,
        user_stats=user_stats,
        selected_level=level
    )


@games_bp.route('/reading/<int:reading_id>')
@login_required
def reading_detail(reading_id):
    """Detalle de una lectura"""
    from app.models import ReadingComprehension
    
    reading = ReadingComprehension.query.get_or_404(reading_id)
    
    return render_template(
        'games/reading_detail.html',
        reading=reading
    )


@games_bp.route('/reading/<int:reading_id>/submit', methods=['POST'])
@login_required
def submit_reading_answers(reading_id):
    """Enviar respuestas de comprensión lectora"""
    from app.models import ReadingComprehension, UserReadingScore, ReadingQuestion
    
    reading = ReadingComprehension.query.get_or_404(reading_id)
    data = request.get_json()
    answers = data.get('answers', {})
    time_seconds = data.get('time_seconds', 0)
    from_daily = data.get('from_daily', False)
    
    # Verificar respuestas
    correct = 0
    total = 0
    
    for question_id, user_answer in answers.items():
        question = ReadingQuestion.query.get(question_id)
        if question:
            total += 1
            if user_answer.lower() == question.correct_answer.lower():
                correct += 1
    
    # Calcular puntuación
    accuracy = (correct / total * 100) if total > 0 else 0
    base_score = int((accuracy / 100) * 100)
    
    # Bonus por velocidad
    if time_seconds < reading.reading_time_minutes * 60:
        base_score += 20
    
    score = min(base_score, 100)
    
    # Guardar resultado
    reading_score = UserReadingScore(
        user_id=current_user.id,
        reading_id=reading_id,
        correct_answers=correct,
        total_questions=total,
        time_seconds=time_seconds,
        score=int(score)
    )
    db.session.add(reading_score)
    db.session.commit()
    
    # Agregar puntos
    add_points(current_user.id, int(score), 'game', f'Reading Comprehension - {reading.category}')
    
    if from_daily:
        complete_daily_challenge()
    
    return jsonify({
        'correct': correct,
        'total': total,
        'accuracy': round(accuracy, 1),
        'score': int(score)
    })


# ==========================================
# SPEED TYPING
# ==========================================

@games_bp.route('/speed-typing')
@login_required
def speed_typing():
    """Página del juego Speed Typing"""
    level = request.args.get('level', 'A1')
    category = request.args.get('category', '')
    
    return render_template(
        'games/speed_typing.html',
        level=level,
        category=category
    )


@games_bp.route('/speed-typing/get-phrases')
@login_required
def get_typing_phrases():
    """Obtener frases para Speed Typing"""
    from app.models import SpeedTyping
    
    level = request.args.get('level', 'A1')
    category = request.args.get('category', '')
    count = int(request.args.get('count', 10))
    
    query = SpeedTyping.query.filter_by(cefr_level=level, is_active=True)
    
    if category:
        query = query.filter_by(category=category)
    
    phrases = query.all()
    
    if not phrases:
        return jsonify({'error': 'No phrases found'}), 404
    
    # Seleccionar frases aleatorias
    random.shuffle(phrases)
    selected = phrases[:count]
    
    result = []
    for phrase in selected:
        result.append({
            'id': phrase.id,
            'phrase': phrase.phrase,
            'pronunciation_hint': phrase.pronunciation_hint,
            'meaning': phrase.meaning,
            'example_sentence': phrase.example_sentence
        })
    
    return jsonify(result)


@games_bp.route('/speed-typing/submit-answer', methods=['POST'])
@login_required
def submit_typing_answer():
    """Enviar respuesta de Speed Typing"""
    from app.models import SpeedTyping, UserTypingScore
    import difflib
    
    data = request.get_json()
    typing_id = data.get('typing_id')
    typed_text = data.get('typed_text', '')
    time_seconds = data.get('time_seconds', 0)
    from_daily = data.get('from_daily', False)
    is_last = data.get('is_last', False)
    
    typing = SpeedTyping.query.get(typing_id)
    if not typing:
        return jsonify({'error': 'Phrase not found'}), 404
    
    # Calcular precisión
    original = typing.phrase.lower()
    typed = typed_text.lower()
    
    # Usar SequenceMatcher para calcular similitud
    matcher = difflib.SequenceMatcher(None, original, typed)
    accuracy = matcher.ratio() * 100
    
    is_correct = typed == original
    
    # Calcular WPM (palabras por minuto)
    word_count = len(typed.split())
    minutes = time_seconds / 60 if time_seconds > 0 else 0.016
    wpm = word_count / minutes if minutes > 0 else 0
    
    # Calcular puntuación
    score = 0
    if is_correct:
        score = int(100 * (time_seconds / 10))  # Bonus por velocidad
        score = min(100, max(30, score))
    else:
        score = int(accuracy)
    
    # Guardar resultado
    typing_score = UserTypingScore(
        user_id=current_user.id,
        typing_id=typing_id,
        typed_text=typed_text,
        is_correct=is_correct,
        time_seconds=time_seconds,
        words_per_minute=round(wpm, 1),
        accuracy_percentage=round(accuracy, 1),
        score=score
    )
    db.session.add(typing_score)
    db.session.commit()
    
    # Agregar puntos
    add_points(current_user.id, score, 'game', f'Speed Typing - {typing.category}')
    
    # Completar reto diario si es el último y viene del daily challenge
    if from_daily and is_last:
        complete_daily_challenge()
    
    return jsonify({
        'is_correct': is_correct,
        'correct_phrase': typing.phrase,
        'accuracy': round(accuracy, 1),
        'wpm': round(wpm, 1),
        'score': score
    })
