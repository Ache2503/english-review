#!/usr/bin/env python3
"""
Seed de Mini Games - Juegos interactivos para practicar inglés
Incluye: Word Scramble, Memory Match, Fill the Gaps, Word Search
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import MiniGame, MiniGameContent

app = create_app()

# Configuración de los juegos
MINI_GAMES = [
    {
        'game_type': 'word_scramble',
        'title': 'Word Scramble',
        'description': 'Unscramble the letters to form the correct English word!',
        'instructions': '''How to play:
1. Look at the scrambled letters
2. Rearrange them to form a correct English word
3. Type your answer and submit
4. You have 3 attempts per word
5. Faster answers earn more points!''',
        'difficulty_levels': {
            'beginner': {'time_per_word': 30, 'hint_available': True, 'letters_shown': 1},
            'intermediate': {'time_per_word': 20, 'hint_available': True, 'letters_shown': 0},
            'advanced': {'time_per_word': 15, 'hint_available': False, 'letters_shown': 0}
        },
        'points_per_level': {'beginner': 10, 'intermediate': 20, 'advanced': 30}
    },
    {
        'game_type': 'memory_match',
        'title': 'Memory Match',
        'description': 'Match English words with their Spanish translations or definitions!',
        'instructions': '''How to play:
1. Click on a card to reveal its content
2. Click on another card to find its match
3. Match words with their translations or definitions
4. Complete all pairs to win
5. Fewer attempts = higher score!''',
        'difficulty_levels': {
            'beginner': {'pairs': 6, 'time_limit': 120, 'show_preview': True},
            'intermediate': {'pairs': 8, 'time_limit': 90, 'show_preview': False},
            'advanced': {'pairs': 12, 'time_limit': 60, 'show_preview': False}
        },
        'points_per_level': {'beginner': 15, 'intermediate': 25, 'advanced': 40}
    },
    {
        'game_type': 'fill_gaps',
        'title': 'Fill the Gaps',
        'description': 'Complete the sentences with the correct words!',
        'instructions': '''How to play:
1. Read the sentence with a missing word
2. Choose the correct word from the options
3. Get points for each correct answer
4. Complete all sentences to finish!''',
        'difficulty_levels': {
            'beginner': {'sentences': 5, 'options': 3, 'hints': True},
            'intermediate': {'sentences': 8, 'options': 4, 'hints': False},
            'advanced': {'sentences': 10, 'options': 5, 'hints': False}
        },
        'points_per_level': {'beginner': 10, 'intermediate': 20, 'advanced': 35}
    },
    {
        'game_type': 'hangman',
        'title': 'Hangman',
        'description': 'Guess the word letter by letter before the hangman is complete!',
        'instructions': '''How to play:
1. A word is hidden with blanks
2. Guess one letter at a time
3. Correct guesses reveal the letters
4. Wrong guesses add parts to the hangman
5. Complete the word before 6 wrong guesses!''',
        'difficulty_levels': {
            'beginner': {'max_wrong': 8, 'show_category': True, 'word_length': '4-6'},
            'intermediate': {'max_wrong': 6, 'show_category': True, 'word_length': '5-8'},
            'advanced': {'max_wrong': 5, 'show_category': False, 'word_length': '6-10'}
        },
        'points_per_level': {'beginner': 15, 'intermediate': 25, 'advanced': 40}
    },
]

# Contenido para Word Scramble
WORD_SCRAMBLE_CONTENT = {
    'A1': [
        {'word': 'hello', 'category': 'greetings', 'hint': 'A common greeting'},
        {'word': 'water', 'category': 'food', 'hint': 'You drink this'},
        {'word': 'house', 'category': 'places', 'hint': 'Where you live'},
        {'word': 'happy', 'category': 'emotions', 'hint': 'Feeling of joy'},
        {'word': 'book', 'category': 'objects', 'hint': 'You read this'},
        {'word': 'apple', 'category': 'food', 'hint': 'A red or green fruit'},
        {'word': 'mother', 'category': 'family', 'hint': 'Your female parent'},
        {'word': 'school', 'category': 'places', 'hint': 'Where you study'},
        {'word': 'friend', 'category': 'people', 'hint': 'Someone you like'},
        {'word': 'music', 'category': 'entertainment', 'hint': 'Songs and sounds'},
    ],
    'A2': [
        {'word': 'weather', 'category': 'nature', 'hint': 'Sun, rain, or snow'},
        {'word': 'kitchen', 'category': 'rooms', 'hint': 'Where you cook'},
        {'word': 'beautiful', 'category': 'adjectives', 'hint': 'Very pretty'},
        {'word': 'exercise', 'category': 'health', 'hint': 'Physical activity'},
        {'word': 'breakfast', 'category': 'meals', 'hint': 'Morning meal'},
        {'word': 'hospital', 'category': 'places', 'hint': 'Where doctors work'},
        {'word': 'vacation', 'category': 'travel', 'hint': 'Time off from work'},
        {'word': 'neighbor', 'category': 'people', 'hint': 'Lives next to you'},
        {'word': 'remember', 'category': 'verbs', 'hint': 'Not forget'},
        {'word': 'dangerous', 'category': 'adjectives', 'hint': 'Not safe'},
    ],
    'B1': [
        {'word': 'environment', 'category': 'nature', 'hint': 'Nature around us'},
        {'word': 'experience', 'category': 'life', 'hint': 'Something you go through'},
        {'word': 'advertisement', 'category': 'media', 'hint': 'Promotes products'},
        {'word': 'opportunity', 'category': 'life', 'hint': 'A chance to do something'},
        {'word': 'achievement', 'category': 'success', 'hint': 'Something accomplished'},
        {'word': 'comfortable', 'category': 'adjectives', 'hint': 'At ease, relaxed'},
        {'word': 'communicate', 'category': 'verbs', 'hint': 'To share information'},
        {'word': 'disappointed', 'category': 'emotions', 'hint': 'Sad expectation not met'},
        {'word': 'temperature', 'category': 'weather', 'hint': 'Hot or cold measure'},
        {'word': 'responsible', 'category': 'traits', 'hint': 'Reliable, trustworthy'},
    ],
    'B2': [
        {'word': 'entrepreneur', 'category': 'business', 'hint': 'Starts businesses'},
        {'word': 'sophisticated', 'category': 'adjectives', 'hint': 'Complex, refined'},
        {'word': 'circumstances', 'category': 'life', 'hint': 'Conditions, situation'},
        {'word': 'nevertheless', 'category': 'connectors', 'hint': 'However, in spite of'},
        {'word': 'acknowledge', 'category': 'verbs', 'hint': 'To recognize, admit'},
        {'word': 'controversial', 'category': 'adjectives', 'hint': 'Causes disagreement'},
        {'word': 'consequences', 'category': 'results', 'hint': 'Results of actions'},
        {'word': 'enthusiasm', 'category': 'emotions', 'hint': 'Great excitement'},
        {'word': 'maintenance', 'category': 'actions', 'hint': 'Keeping in good condition'},
        {'word': 'psychological', 'category': 'science', 'hint': 'Related to the mind'},
    ],
}

# Contenido para Memory Match
MEMORY_MATCH_CONTENT = {
    'A1': [
        {'english': 'hello', 'spanish': 'hola'},
        {'english': 'goodbye', 'spanish': 'adiós'},
        {'english': 'thank you', 'spanish': 'gracias'},
        {'english': 'please', 'spanish': 'por favor'},
        {'english': 'water', 'spanish': 'agua'},
        {'english': 'food', 'spanish': 'comida'},
        {'english': 'house', 'spanish': 'casa'},
        {'english': 'car', 'spanish': 'carro/coche'},
        {'english': 'dog', 'spanish': 'perro'},
        {'english': 'cat', 'spanish': 'gato'},
        {'english': 'book', 'spanish': 'libro'},
        {'english': 'school', 'spanish': 'escuela'},
    ],
    'A2': [
        {'english': 'weather', 'spanish': 'clima'},
        {'english': 'breakfast', 'spanish': 'desayuno'},
        {'english': 'kitchen', 'spanish': 'cocina'},
        {'english': 'bedroom', 'spanish': 'dormitorio'},
        {'english': 'newspaper', 'spanish': 'periódico'},
        {'english': 'airport', 'spanish': 'aeropuerto'},
        {'english': 'vacation', 'spanish': 'vacaciones'},
        {'english': 'birthday', 'spanish': 'cumpleaños'},
        {'english': 'neighbor', 'spanish': 'vecino'},
        {'english': 'sometimes', 'spanish': 'a veces'},
        {'english': 'already', 'spanish': 'ya'},
        {'english': 'still', 'spanish': 'todavía'},
    ],
    'B1': [
        {'english': 'achievement', 'spanish': 'logro'},
        {'english': 'environment', 'spanish': 'medio ambiente'},
        {'english': 'opportunity', 'spanish': 'oportunidad'},
        {'english': 'experience', 'spanish': 'experiencia'},
        {'english': 'knowledge', 'spanish': 'conocimiento'},
        {'english': 'behavior', 'spanish': 'comportamiento'},
        {'english': 'challenge', 'spanish': 'desafío'},
        {'english': 'success', 'spanish': 'éxito'},
        {'english': 'failure', 'spanish': 'fracaso'},
        {'english': 'improve', 'spanish': 'mejorar'},
        {'english': 'despite', 'spanish': 'a pesar de'},
        {'english': 'although', 'spanish': 'aunque'},
    ],
    'B2': [
        {'english': 'acknowledge', 'spanish': 'reconocer'},
        {'english': 'compromise', 'spanish': 'compromiso'},
        {'english': 'conscientious', 'spanish': 'concienzudo'},
        {'english': 'entrepreneur', 'spanish': 'emprendedor'},
        {'english': 'nevertheless', 'spanish': 'sin embargo'},
        {'english': 'straightforward', 'spanish': 'directo/sencillo'},
        {'english': 'overwhelming', 'spanish': 'abrumador'},
        {'english': 'thorough', 'spanish': 'exhaustivo'},
        {'english': 'sustainable', 'spanish': 'sostenible'},
        {'english': 'feasible', 'spanish': 'factible'},
        {'english': 'accountable', 'spanish': 'responsable'},
        {'english': 'leverage', 'spanish': 'aprovechar'},
    ],
}

# Contenido para Fill the Gaps
FILL_GAPS_CONTENT = {
    'A1': [
        {'sentence': 'I ___ a student.', 'correct': 'am', 'options': ['am', 'is', 'are'], 'explanation': 'Use "am" with "I".'},
        {'sentence': 'She ___ to school every day.', 'correct': 'goes', 'options': ['go', 'goes', 'going'], 'explanation': 'Third person singular uses "goes".'},
        {'sentence': '___ you like coffee?', 'correct': 'Do', 'options': ['Do', 'Does', 'Are'], 'explanation': '"Do" is used with "you" for questions.'},
        {'sentence': 'They ___ playing football.', 'correct': 'are', 'options': ['is', 'am', 'are'], 'explanation': '"Are" is used with "they".'},
        {'sentence': 'I have ___ apple.', 'correct': 'an', 'options': ['a', 'an', 'the'], 'explanation': 'Use "an" before vowel sounds.'},
    ],
    'A2': [
        {'sentence': 'I ___ to Paris last year.', 'correct': 'went', 'options': ['go', 'went', 'gone'], 'explanation': '"Went" is the past tense of "go".'},
        {'sentence': 'She has ___ here for two hours.', 'correct': 'been', 'options': ['be', 'been', 'being'], 'explanation': 'Present perfect: has + been.'},
        {'sentence': 'We ___ do our homework now.', 'correct': 'must', 'options': ['must', 'have', 'can'], 'explanation': '"Must" indicates obligation.'},
        {'sentence': 'The book is ___ the table.', 'correct': 'on', 'options': ['in', 'on', 'at'], 'explanation': '"On" for surfaces.'},
        {'sentence': 'I\'m looking ___ my keys.', 'correct': 'for', 'options': ['for', 'at', 'to'], 'explanation': '"Look for" means to search.'},
    ],
    'B1': [
        {'sentence': 'If I ___ rich, I would travel.', 'correct': 'were', 'options': ['am', 'was', 'were'], 'explanation': 'Second conditional uses "were".'},
        {'sentence': 'By next year, I will ___ graduated.', 'correct': 'have', 'options': ['be', 'have', 'has'], 'explanation': 'Future perfect: will have + past participle.'},
        {'sentence': 'She suggested ___ early.', 'correct': 'leaving', 'options': ['to leave', 'leaving', 'leave'], 'explanation': '"Suggest" takes gerund.'},
        {'sentence': 'I\'m used ___ early.', 'correct': 'to waking', 'options': ['to wake', 'to waking', 'waking'], 'explanation': '"Used to" + gerund for habits.'},
        {'sentence': 'He denied ___ the money.', 'correct': 'taking', 'options': ['to take', 'taking', 'take'], 'explanation': '"Deny" takes gerund.'},
    ],
    'B2': [
        {'sentence': 'Had I known, I ___ helped.', 'correct': 'would have', 'options': ['would have', 'will have', 'have'], 'explanation': 'Third conditional inversion.'},
        {'sentence': 'Not only ___ he late, but also unprepared.', 'correct': 'was', 'options': ['he was', 'was', 'is'], 'explanation': 'Inversion after "Not only".'},
        {'sentence': 'The more you practice, ___ you become.', 'correct': 'the better', 'options': ['better', 'the better', 'more better'], 'explanation': 'Comparative structure.'},
        {'sentence': 'Were it ___ for your help, I would have failed.', 'correct': 'not', 'options': ['not', 'never', 'but'], 'explanation': 'Conditional inversion.'},
        {'sentence': 'Rarely ___ such talent seen.', 'correct': 'is', 'options': ['is', 'it is', 'has'], 'explanation': 'Inversion after "Rarely".'},
    ],
}

# Contenido para Hangman
HANGMAN_CONTENT = {
    'A1': [
        {'word': 'apple', 'category': 'fruit', 'hint': 'Red or green fruit'},
        {'word': 'water', 'category': 'drink', 'hint': 'You drink this'},
        {'word': 'happy', 'category': 'emotion', 'hint': 'Feeling of joy'},
        {'word': 'house', 'category': 'place', 'hint': 'Where you live'},
        {'word': 'music', 'category': 'art', 'hint': 'Songs and melodies'},
        {'word': 'table', 'category': 'furniture', 'hint': 'You eat on this'},
        {'word': 'green', 'category': 'color', 'hint': 'Color of grass'},
        {'word': 'phone', 'category': 'device', 'hint': 'You call with this'},
    ],
    'A2': [
        {'word': 'weather', 'category': 'nature', 'hint': 'Rain, sun, snow'},
        {'word': 'kitchen', 'category': 'room', 'hint': 'Where you cook'},
        {'word': 'yesterday', 'category': 'time', 'hint': 'The day before today'},
        {'word': 'beautiful', 'category': 'adjective', 'hint': 'Very pretty'},
        {'word': 'important', 'category': 'adjective', 'hint': 'Has great value'},
        {'word': 'breakfast', 'category': 'meal', 'hint': 'Morning food'},
        {'word': 'neighbor', 'category': 'people', 'hint': 'Lives next door'},
        {'word': 'dangerous', 'category': 'adjective', 'hint': 'Not safe'},
    ],
    'B1': [
        {'word': 'achievement', 'category': 'success', 'hint': 'Something accomplished'},
        {'word': 'environment', 'category': 'nature', 'hint': 'World around us'},
        {'word': 'opportunity', 'category': 'life', 'hint': 'A chance'},
        {'word': 'comfortable', 'category': 'adjective', 'hint': 'Relaxed, at ease'},
        {'word': 'communicate', 'category': 'verb', 'hint': 'To share information'},
        {'word': 'responsible', 'category': 'adjective', 'hint': 'Trustworthy'},
        {'word': 'temperature', 'category': 'science', 'hint': 'Hot or cold'},
        {'word': 'disappointed', 'category': 'emotion', 'hint': 'Sad about outcome'},
    ],
    'B2': [
        {'word': 'entrepreneur', 'category': 'business', 'hint': 'Starts companies'},
        {'word': 'sophisticated', 'category': 'adjective', 'hint': 'Complex, refined'},
        {'word': 'consequently', 'category': 'adverb', 'hint': 'As a result'},
        {'word': 'acknowledge', 'category': 'verb', 'hint': 'To recognize'},
        {'word': 'controversial', 'category': 'adjective', 'hint': 'Causes debate'},
        {'word': 'nevertheless', 'category': 'connector', 'hint': 'However'},
        {'word': 'psychological', 'category': 'science', 'hint': 'About the mind'},
        {'word': 'circumstances', 'category': 'noun', 'hint': 'Conditions'},
    ],
}


def seed_mini_games():
    """Crear configuración de mini juegos y contenido"""
    with app.app_context():
        print("="*70)
        print("🎮 CREANDO MINI GAMES")
        print("="*70)
        
        games_added = 0
        content_added = 0
        
        # Crear configuración de juegos
        for game_data in MINI_GAMES:
            existing = MiniGame.query.filter_by(game_type=game_data['game_type']).first()
            if existing:
                print(f"   ⏭️ {game_data['title']} ya existe")
                continue
            
            game = MiniGame(
                game_type=game_data['game_type'],
                title=game_data['title'],
                description=game_data['description'],
                instructions=game_data['instructions'],
                difficulty_levels=game_data['difficulty_levels'],
                points_per_level=game_data['points_per_level'],
                is_active=True
            )
            db.session.add(game)
            games_added += 1
            print(f"   ✅ {game_data['title']} creado")
        
        db.session.commit()
        print(f"\n📊 Juegos creados: {games_added}")
        
        # Crear contenido para Word Scramble
        print("\n🔤 Creando contenido para Word Scramble...")
        for level, words in WORD_SCRAMBLE_CONTENT.items():
            existing = MiniGameContent.query.filter_by(
                game_type='word_scramble', level=level
            ).first()
            if not existing:
                content = MiniGameContent(
                    game_type='word_scramble',
                    level=level,
                    content_data={'words': words},
                    category='vocabulary',
                    is_active=True
                )
                db.session.add(content)
                content_added += 1
        
        # Crear contenido para Memory Match
        print("🃏 Creando contenido para Memory Match...")
        for level, pairs in MEMORY_MATCH_CONTENT.items():
            existing = MiniGameContent.query.filter_by(
                game_type='memory_match', level=level
            ).first()
            if not existing:
                content = MiniGameContent(
                    game_type='memory_match',
                    level=level,
                    content_data={'pairs': pairs},
                    category='vocabulary',
                    is_active=True
                )
                db.session.add(content)
                content_added += 1
        
        # Crear contenido para Fill the Gaps
        print("📝 Creando contenido para Fill the Gaps...")
        for level, sentences in FILL_GAPS_CONTENT.items():
            existing = MiniGameContent.query.filter_by(
                game_type='fill_gaps', level=level
            ).first()
            if not existing:
                content = MiniGameContent(
                    game_type='fill_gaps',
                    level=level,
                    content_data={'sentences': sentences},
                    category='grammar',
                    is_active=True
                )
                db.session.add(content)
                content_added += 1
        
        # Crear contenido para Hangman
        print("🎯 Creando contenido para Hangman...")
        for level, words in HANGMAN_CONTENT.items():
            existing = MiniGameContent.query.filter_by(
                game_type='hangman', level=level
            ).first()
            if not existing:
                content = MiniGameContent(
                    game_type='hangman',
                    level=level,
                    content_data={'words': words},
                    category='vocabulary',
                    is_active=True
                )
                db.session.add(content)
                content_added += 1
        
        db.session.commit()
        
        print(f"\n✅ Contenido de juegos creado: {content_added}")
        print(f"\n📊 Resumen por juego:")
        for game in MiniGame.query.all():
            count = MiniGameContent.query.filter_by(game_type=game.game_type).count()
            print(f"   {game.title}: {count} niveles")
        print("="*70)


if __name__ == '__main__':
    seed_mini_games()
