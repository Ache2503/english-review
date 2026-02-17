#!/usr/bin/env python3
"""
Seed para las nuevas funcionalidades de la plataforma:
- Daily Challenges
- Exam Simulators
- Mini Games
- Grammar Drills
- Idioms
- Phrasal Verbs
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import (
    DailyChallenge, ExamSimulator, ExamSection,
    MiniGame, MiniGameContent, GrammarDrill,
    Idiom, PhrasalVerb
)

app = create_app()

def seed_daily_challenges():
    """Crear desafíos diarios de ejemplo"""
    from datetime import date, timedelta
    
    base_date = date.today()
    
    challenges = [
        {
            'challenge_date': base_date,
            'title': 'Vocabulary Sprint',
            'description': 'Learn 10 new words today',
            'challenge_type': 'vocabulary',
            'difficulty': 'beginner',
            'points_reward': 50,
            'questions': [
                {'q': 'What is the meaning of "happy"?', 'a': 'feeling pleasure', 'options': ['feeling sad', 'feeling pleasure', 'feeling tired']},
                {'q': 'What is the meaning of "big"?', 'a': 'large in size', 'options': ['small', 'large in size', 'fast']},
                {'q': 'What is the meaning of "fast"?', 'a': 'moving quickly', 'options': ['moving slowly', 'moving quickly', 'not moving']},
            ]
        },
        {
            'challenge_date': base_date + timedelta(days=1),
            'title': 'Grammar Challenge',
            'description': 'Master present simple tense',
            'challenge_type': 'grammar',
            'difficulty': 'beginner',
            'points_reward': 60,
            'questions': [
                {'q': 'She ___ to school every day.', 'a': 'goes', 'options': ['go', 'goes', 'going']},
                {'q': 'They ___ coffee in the morning.', 'a': 'drink', 'options': ['drink', 'drinks', 'drinking']},
                {'q': 'I ___ English every day.', 'a': 'study', 'options': ['study', 'studies', 'studying']},
            ]
        },
        {
            'challenge_date': base_date + timedelta(days=2),
            'title': 'Reading Comprehension',
            'description': 'Read and understand a short text',
            'challenge_type': 'reading',
            'difficulty': 'intermediate',
            'points_reward': 70,
            'questions': [
                {'q': 'John wakes up at 7 AM. What time does John wake up?', 'a': '7 AM', 'options': ['6 AM', '7 AM', '8 AM']},
                {'q': 'He has breakfast with his family. Who does John have breakfast with?', 'a': 'his family', 'options': ['his friends', 'his family', 'alone']},
            ]
        },
        {
            'challenge_date': base_date + timedelta(days=3),
            'title': 'Mixed Challenge',
            'description': 'Test your overall English skills',
            'challenge_type': 'mixed',
            'difficulty': 'intermediate',
            'points_reward': 80,
            'questions': [
                {'q': 'Choose the correct form: He ___ TV now.', 'a': 'is watching', 'options': ['watches', 'is watching', 'watch']},
                {'q': 'What is the past tense of "go"?', 'a': 'went', 'options': ['goed', 'went', 'gone']},
            ]
        },
        {
            'challenge_date': base_date + timedelta(days=4),
            'title': 'Writing Task',
            'description': 'Write about your daily routine',
            'challenge_type': 'writing',
            'difficulty': 'intermediate',
            'points_reward': 75,
            'questions': [
                {'q': 'Complete: In the morning, I usually ___.', 'a': 'wake up', 'type': 'open'},
                {'q': 'What do you do after school/work?', 'a': '', 'type': 'open'},
            ]
        },
    ]
    
    for data in challenges:
        existing = DailyChallenge.query.filter_by(challenge_date=data['challenge_date']).first()
        if not existing:
            challenge = DailyChallenge(**data)
            db.session.add(challenge)
    
    db.session.commit()
    print(f"✓ {len(challenges)} Daily Challenges creados")


def seed_exam_simulators():
    """Crear simuladores de examen"""
    exams = [
        {
            'title': 'TOEFL Practice Test 1',
            'exam_type': 'TOEFL',
            'level': 'B2',
            'description': 'Complete TOEFL practice test with all sections',
            'total_time_minutes': 120,
            'passing_score': 70.0,
            'sections': [
                {
                    'section_type': 'reading',
                    'title': 'Reading Comprehension',
                    'order_num': 1,
                    'time_limit_minutes': 35,
                    'instructions': 'Read the passages and answer the questions.',
                    'questions': [
                        {
                            'question_text': 'The word "elaborate" in paragraph 1 is closest in meaning to:',
                            'question_type': 'multiple_choice',
                            'options': ['simple', 'complex', 'brief', 'unclear'],
                            'correct_answer': 'complex',
                            'points': 1
                        },
                        {
                            'question_text': 'According to the passage, what is the main purpose of...',
                            'question_type': 'multiple_choice',
                            'options': ['To explain', 'To describe', 'To argue', 'To narrate'],
                            'correct_answer': 'To explain',
                            'points': 1
                        }
                    ]
                },
                {
                    'section_type': 'listening',
                    'title': 'Listening Section',
                    'order_num': 2,
                    'time_limit_minutes': 40,
                    'instructions': 'Listen carefully and answer the questions.',
                    'questions': []
                },
                {
                    'section_type': 'writing',
                    'title': 'Writing Section',
                    'order_num': 3,
                    'time_limit_minutes': 30,
                    'instructions': 'Write an essay on the given topic.',
                    'questions': [
                        {
                            'question_text': 'Do you agree or disagree: Technology has improved education.',
                            'question_type': 'essay',
                            'correct_answer': '',
                            'points': 5
                        }
                    ]
                }
            ]
        },
        {
            'title': 'IELTS Academic Practice',
            'exam_type': 'IELTS',
            'level': 'B2',
            'description': 'IELTS Academic format practice test',
            'total_time_minutes': 150,
            'passing_score': 60.0,
            'sections': [
                {
                    'section_type': 'reading',
                    'title': 'Academic Reading',
                    'order_num': 1,
                    'time_limit_minutes': 60,
                    'instructions': 'Answer all questions based on the reading passages.',
                    'questions': []
                },
                {
                    'section_type': 'writing',
                    'title': 'Academic Writing',
                    'order_num': 2,
                    'time_limit_minutes': 60,
                    'instructions': 'Complete both writing tasks.',
                    'questions': []
                }
            ]
        },
        {
            'title': 'Cambridge B2 First',
            'exam_type': 'Cambridge',
            'level': 'B2',
            'description': 'Cambridge B2 First (FCE) practice exam',
            'total_time_minutes': 90,
            'passing_score': 65.0,
            'sections': [
                {
                    'section_type': 'reading',
                    'title': 'Reading and Use of English',
                    'order_num': 1,
                    'time_limit_minutes': 45,
                    'instructions': 'Complete all parts of the reading section.',
                    'questions': []
                },
                {
                    'section_type': 'use of english',
                    'title': 'Use of English',
                    'order_num': 2,
                    'time_limit_minutes': 45,
                    'instructions': 'Complete the grammar and vocabulary exercises.',
                    'questions': []
                }
            ]
        }
    ]
    
    for exam_data in exams:
        existing = ExamSimulator.query.filter_by(title=exam_data['title']).first()
        if not existing:
            exam = ExamSimulator(**exam_data)
            db.session.add(exam)
    
    db.session.commit()
    print(f"✓ {len(exams)} Exam Simulators creados")


def seed_mini_games():
    """Crear mini juegos"""
    games = [
        {
            'game_type': 'word_scramble',
            'title': 'Word Scramble',
            'description': 'Unscramble the letters to form words',
            'instructions': 'Rearrange the letters to spell the correct word.',
            'difficulty_levels': {'easy': 1, 'medium': 2, 'hard': 3},
            'points_per_level': {'easy': 10, 'medium': 15, 'hard': 20},
            'content': [
                {'level': 'A1', 'word': 'APPLE', 'hint': 'A red or green fruit'},
                {'level': 'A1', 'word': 'HOUSE', 'hint': 'Where you live'},
                {'level': 'A1', 'word': 'WATER', 'hint': 'You drink this'},
                {'level': 'A2', 'word': 'BEAUTIFUL', 'hint': 'Very pretty'},
                {'level': 'A2', 'word': 'MORNING', 'hint': 'Early part of the day'},
                {'level': 'B1', 'word': 'ENVIRONMENT', 'hint': 'Nature around us'},
                {'level': 'B1', 'word': 'KNOWLEDGE', 'hint': 'What you learn'},
            ]
        },
        {
            'game_type': 'hangman',
            'title': 'Hangman',
            'description': 'Guess the word letter by letter',
            'instructions': 'Guess letters to reveal the hidden word before you run out of attempts.',
            'difficulty_levels': {'easy': 1, 'medium': 2, 'hard': 3},
            'points_per_level': {'easy': 10, 'medium': 15, 'hard': 20},
            'content': [
                {'level': 'A1', 'word': 'SCHOOL', 'category': 'Places'},
                {'level': 'A1', 'word': 'FAMILY', 'category': 'People'},
                {'level': 'A2', 'word': 'RESTAURANT', 'category': 'Places'},
                {'level': 'A2', 'word': 'COMPUTER', 'category': 'Technology'},
                {'level': 'B1', 'word': 'GOVERNMENT', 'category': 'Society'},
            ]
        },
        {
            'game_type': 'memory',
            'title': 'Memory Match',
            'description': 'Match words with their meanings',
            'instructions': 'Find pairs of words and their translations or meanings.',
            'difficulty_levels': {'easy': 1, 'medium': 2, 'hard': 3},
            'points_per_level': {'easy': 10, 'medium': 12, 'hard': 15},
            'content': [
                {'level': 'A1', 'pairs': [
                    {'word': 'Hello', 'match': 'Hola'},
                    {'word': 'Goodbye', 'match': 'Adiós'},
                    {'word': 'Thank you', 'match': 'Gracias'},
                    {'word': 'Please', 'match': 'Por favor'},
                ]},
                {'level': 'A2', 'pairs': [
                    {'word': 'Brave', 'match': 'Valiente'},
                    {'word': 'Clever', 'match': 'Inteligente'},
                    {'word': 'Lazy', 'match': 'Perezoso'},
                    {'word': 'Shy', 'match': 'Tímido'},
                ]},
            ]
        },
        {
            'game_type': 'fill_gaps',
            'title': 'Fill the Gaps',
            'description': 'Complete sentences with the correct words',
            'instructions': 'Fill in the blank with the appropriate word.',
            'difficulty_levels': {'easy': 1, 'medium': 2, 'hard': 3},
            'points_per_level': {'easy': 10, 'medium': 15, 'hard': 20},
            'content': [
                {'level': 'A1', 'sentence': 'I ___ a student.', 'answer': 'am', 'options': ['am', 'is', 'are']},
                {'level': 'A1', 'sentence': 'She ___ coffee every morning.', 'answer': 'drinks', 'options': ['drink', 'drinks', 'drinking']},
                {'level': 'A2', 'sentence': 'They have ___ been to Paris.', 'answer': 'never', 'options': ['ever', 'never', 'already']},
                {'level': 'B1', 'sentence': 'If I ___ rich, I would travel.', 'answer': 'were', 'options': ['was', 'were', 'am']},
            ]
        }
    ]
    
    for game_data in games:
        existing = MiniGame.query.filter_by(game_type=game_data['game_type']).first()
        if not existing:
            content_data = game_data.pop('content', [])
            game = MiniGame(**game_data)
            db.session.add(game)
            db.session.flush()
            
            for item in content_data:
                level = item.get('level', 'A1')
                content = MiniGameContent(
                    game_type=game_data['game_type'],
                    level=level,
                    content_data=item
                )
                db.session.add(content)
    
    db.session.commit()
    print(f"✓ {len(games)} Mini Games creados")


def seed_grammar_drills():
    """Crear ejercicios de gramática"""
    drills = [
        {
            'title': 'Present Simple Practice',
            'level': 'A1',
            'grammar_topic': 'Verb Tenses',
            'description': 'Practice the present simple tense',
            'time_limit_seconds': 600,
            'questions': [
                {'q': 'She ___ (work) at a hospital.', 'a': 'works', 'type': 'fill'},
                {'q': 'They ___ (not like) coffee.', 'a': "don't like", 'type': 'fill'},
                {'q': '___ he speak English?', 'a': 'Does', 'type': 'fill'},
                {'q': 'We ___ (go) to school every day.', 'a': 'go', 'type': 'fill'},
            ],
            'passing_score': 70.0
        },
        {
            'title': 'Past Simple vs Present Perfect',
            'level': 'B1',
            'grammar_topic': 'Verb Tenses',
            'description': 'Choose between past simple and present perfect',
            'time_limit_seconds': 900,
            'questions': [
                {'q': 'I ___ (already/finish) my homework.', 'a': 'have already finished', 'type': 'fill'},
                {'q': 'She ___ (go) to Paris last year.', 'a': 'went', 'type': 'fill'},
                {'q': 'We ___ (never/visit) Japan.', 'a': 'have never visited', 'type': 'fill'},
            ],
            'passing_score': 70.0
        },
        {
            'title': 'Articles: A, An, The',
            'level': 'A1',
            'grammar_topic': 'Articles',
            'description': 'Practice using articles correctly',
            'time_limit_seconds': 480,
            'questions': [
                {'q': 'I have ___ apple.', 'a': 'an', 'type': 'fill'},
                {'q': 'She is ___ teacher.', 'a': 'a', 'type': 'fill'},
                {'q': '___ sun is bright today.', 'a': 'The', 'type': 'fill'},
            ],
            'passing_score': 70.0
        },
        {
            'title': 'Conditionals Practice',
            'level': 'B2',
            'grammar_topic': 'Conditionals',
            'description': 'Master all types of conditionals',
            'time_limit_seconds': 1200,
            'questions': [
                {'q': 'If it rains, I ___ (stay) home.', 'a': 'will stay', 'type': 'fill'},
                {'q': 'If I were you, I ___ (accept) the offer.', 'a': 'would accept', 'type': 'fill'},
                {'q': 'If she had studied, she ___ (pass) the exam.', 'a': 'would have passed', 'type': 'fill'},
            ],
            'passing_score': 70.0
        },
        {
            'title': 'Prepositions of Time and Place',
            'level': 'A2',
            'grammar_topic': 'Prepositions',
            'description': 'Practice using in, on, at correctly',
            'time_limit_seconds': 600,
            'questions': [
                {'q': 'The meeting is ___ Monday.', 'a': 'on', 'type': 'fill'},
                {'q': 'I wake up ___ 7 AM.', 'a': 'at', 'type': 'fill'},
                {'q': 'She was born ___ 1990.', 'a': 'in', 'type': 'fill'},
            ],
            'passing_score': 70.0
        }
    ]
    
    for drill_data in drills:
        # Remove description from data since it's not in the model
        drill_data.pop('description', None)
        existing = GrammarDrill.query.filter_by(title=drill_data['title']).first()
        if not existing:
            drill = GrammarDrill(**drill_data)
            db.session.add(drill)
    
    db.session.commit()
    print(f"✓ {len(drills)} Grammar Drills creados")


def seed_idioms():
    """Crear idioms de ejemplo"""
    idioms = [
        {
            'phrase': "Break the ice",
            'meaning': "Start a conversation in a social situation",
            'spanish_equivalent': "Romper el hielo",
            'example_sentence': "He told a joke to break the ice at the meeting.",
            'level': 'B1',
            'category': 'social'
        },
        {
            'phrase': "Piece of cake",
            'meaning': "Something very easy to do",
            'spanish_equivalent': "Pan comido",
            'example_sentence': "The exam was a piece of cake!",
            'level': 'A2',
            'category': 'everyday'
        },
        {
            'phrase': "Hit the nail on the head",
            'meaning': "Be exactly right about something",
            'spanish_equivalent': "Dar en el clavo",
            'example_sentence': "You hit the nail on the head with that analysis.",
            'level': 'B2',
            'category': 'business'
        },
        {
            'phrase': "Under the weather",
            'meaning': "Feeling ill or sick",
            'spanish_equivalent': "Estar enfermo",
            'example_sentence': "I'm feeling a bit under the weather today.",
            'level': 'B1',
            'category': 'health'
        },
        {
            'phrase': "Cost an arm and a leg",
            'meaning': "Be very expensive",
            'spanish_equivalent': "Costar un ojo de la cara",
            'example_sentence': "That car costs an arm and a leg!",
            'level': 'B1',
            'category': 'money'
        },
        {
            'phrase': "Bite off more than you can chew",
            'meaning': "Take on more than you can handle",
            'spanish_equivalent': "Abarcar más de lo que puedes",
            'example_sentence': "Don't bite off more than you can chew with this project.",
            'level': 'B2',
            'category': 'work'
        },
        {
            'phrase': "Let the cat out of the bag",
            'meaning': "Reveal a secret accidentally",
            'spanish_equivalent': "Irse de la lengua",
            'example_sentence': "She let the cat out of the bag about the surprise party.",
            'level': 'B1',
            'category': 'communication'
        },
        {
            'phrase': "Kill two birds with one stone",
            'meaning': "Accomplish two things with a single action",
            'spanish_equivalent': "Matar dos pájaros de un tiro",
            'example_sentence': "By cycling to work, I kill two birds with one stone: I exercise and save money.",
            'level': 'B1',
            'category': 'everyday'
        },
        {
            'phrase': "Once in a blue moon",
            'meaning': "Very rarely",
            'spanish_equivalent': "De vez en cuando / muy rara vez",
            'example_sentence': "I only eat fast food once in a blue moon.",
            'level': 'B1',
            'category': 'time'
        },
        {
            'phrase': "The ball is in your court",
            'meaning': "It's your turn to take action",
            'spanish_equivalent': "La pelota está en tu tejado",
            'example_sentence': "I've made my offer, now the ball is in your court.",
            'level': 'B2',
            'category': 'business'
        }
    ]
    
    for idiom_data in idioms:
        existing = Idiom.query.filter_by(phrase=idiom_data['phrase']).first()
        if not existing:
            idiom = Idiom(**idiom_data)
            db.session.add(idiom)
    
    db.session.commit()
    print(f"✓ {len(idioms)} Idioms creados")


def seed_phrasal_verbs():
    """Crear phrasal verbs de ejemplo"""
    phrasal_verbs = [
        {
            'verb': 'look',
            'particle': 'up',
            'full_form': 'look up',
            'meaning': 'Search for information',
            'spanish_translation': 'Buscar',
            'example_sentence': 'I need to look up that word in the dictionary.',
            'additional_meanings': ['Improve'],
            'level': 'A2',
            'is_separable': True
        },
        {
            'verb': 'give',
            'particle': 'up',
            'full_form': 'give up',
            'meaning': 'Stop trying',
            'spanish_translation': 'Rendirse',
            'example_sentence': "Don't give up on your dreams.",
            'additional_meanings': ['Quit a habit'],
            'level': 'A2',
            'is_separable': True
        },
        {
            'verb': 'turn',
            'particle': 'off',
            'full_form': 'turn off',
            'meaning': 'Stop a device from working',
            'spanish_translation': 'Apagar',
            'example_sentence': 'Please turn off the lights.',
            'level': 'A1',
            'is_separable': True
        },
        {
            'verb': 'put',
            'particle': 'off',
            'full_form': 'put off',
            'meaning': 'Postpone',
            'spanish_translation': 'Posponer',
            'example_sentence': "Don't put off your homework.",
            'level': 'B1',
            'is_separable': True
        },
        {
            'verb': 'come',
            'particle': 'across',
            'full_form': 'come across',
            'meaning': 'Find by chance',
            'spanish_translation': 'Encontrar por casualidad',
            'example_sentence': 'I came across an old photo.',
            'additional_meanings': ['Give an impression'],
            'level': 'B1',
            'is_separable': False
        },
        {
            'verb': 'break',
            'particle': 'down',
            'full_form': 'break down',
            'meaning': 'Stop working (machine)',
            'spanish_translation': 'Averiarse',
            'example_sentence': 'My car broke down on the highway.',
            'additional_meanings': ['Lose emotional control'],
            'level': 'B1',
            'is_separable': False
        },
        {
            'verb': 'figure',
            'particle': 'out',
            'full_form': 'figure out',
            'meaning': 'Understand or solve',
            'spanish_translation': 'Descifrar',
            'example_sentence': "I can't figure out this puzzle.",
            'level': 'B1',
            'is_separable': True
        },
        {
            'verb': 'run',
            'particle': 'out of',
            'full_form': 'run out of',
            'meaning': 'Have no more of something',
            'spanish_translation': 'Quedarse sin',
            'example_sentence': 'We ran out of milk.',
            'level': 'A2',
            'is_separable': False
        },
        {
            'verb': 'get',
            'particle': 'along',
            'full_form': 'get along',
            'meaning': 'Have a good relationship',
            'spanish_translation': 'Llevarse bien',
            'example_sentence': 'Do you get along with your neighbors?',
            'level': 'A2',
            'is_separable': False
        },
        {
            'verb': 'carry',
            'particle': 'on',
            'full_form': 'carry on',
            'meaning': 'Continue',
            'spanish_translation': 'Continuar',
            'example_sentence': 'Carry on with your work.',
            'level': 'B1',
            'is_separable': False
        },
        {
            'verb': 'set',
            'particle': 'up',
            'full_form': 'set up',
            'meaning': 'Arrange or establish',
            'spanish_translation': 'Establecer',
            'example_sentence': 'We need to set up a meeting.',
            'level': 'B1',
            'is_separable': True
        },
        {
            'verb': 'work',
            'particle': 'out',
            'full_form': 'work out',
            'meaning': 'Exercise',
            'spanish_translation': 'Hacer ejercicio',
            'example_sentence': 'I work out at the gym.',
            'additional_meanings': ['Find a solution', 'Develop successfully'],
            'level': 'B1',
            'is_separable': True
        }
    ]
    
    for pv_data in phrasal_verbs:
        existing = PhrasalVerb.query.filter_by(full_form=pv_data['full_form']).first()
        if not existing:
            pv = PhrasalVerb(**pv_data)
            db.session.add(pv)
    
    db.session.commit()
    print(f"✓ {len(phrasal_verbs)} Phrasal Verbs creados")


def main():
    with app.app_context():
        print("\n=== Seeding New Features ===\n")
        
        seed_daily_challenges()
        seed_exam_simulators()
        seed_mini_games()
        seed_grammar_drills()
        seed_idioms()
        seed_phrasal_verbs()
        
        print("\n=== Seeding Complete! ===\n")


if __name__ == '__main__':
    main()
