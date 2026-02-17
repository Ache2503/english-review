#!/usr/bin/env python3
"""
Seed de Daily Challenges - Desafíos diarios para mantener el streak
Genera desafíos para los próximos 30 días
"""

import sys
sys.path.insert(0, '.')

from datetime import date, timedelta
from app import create_app
from app.extensions import db
from app.models import DailyChallenge

app = create_app()

# Tipos de desafíos
CHALLENGE_TYPES = ['vocabulary', 'grammar', 'reading', 'mixed']

# Plantillas de desafíos por tipo
CHALLENGE_TEMPLATES = {
    'vocabulary': [
        {
            'title': 'Word Power Challenge',
            'title_es': 'Desafío de Vocabulario',
            'description': 'Test your vocabulary knowledge with these word challenges!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'What is the synonym of "happy"?', 'options': ['sad', 'joyful', 'angry', 'tired'], 'correct': 1, 'explanation': '"Joyful" means feeling or expressing great happiness.'},
                {'type': 'multiple_choice', 'question': 'What is the antonym of "begin"?', 'options': ['start', 'end', 'continue', 'pause'], 'correct': 1, 'explanation': '"End" is the opposite of "begin".'},
                {'type': 'multiple_choice', 'question': 'Complete: I need to _____ my homework before dinner.', 'options': ['make', 'do', 'have', 'take'], 'correct': 1, 'explanation': 'We "do" homework, not "make" homework.'},
                {'type': 'fill_blank', 'question': 'The _____ (opposite of small) elephant walked slowly.', 'correct': ['big', 'large', 'huge'], 'explanation': 'Big, large, or huge are antonyms of small.'},
                {'type': 'multiple_choice', 'question': 'Which word means "very tired"?', 'options': ['energetic', 'exhausted', 'excited', 'enthusiastic'], 'correct': 1, 'explanation': '"Exhausted" means extremely tired.'},
            ]
        },
        {
            'title': 'Word Detective',
            'title_es': 'Detective de Palabras',
            'description': 'Find the correct words and their meanings!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'What does "abundant" mean?', 'options': ['scarce', 'plentiful', 'empty', 'missing'], 'correct': 1, 'explanation': '"Abundant" means existing in large quantities.'},
                {'type': 'multiple_choice', 'question': '"She has a bright future" - what does "bright" mean here?', 'options': ['shiny', 'colorful', 'promising', 'loud'], 'correct': 2, 'explanation': 'In this context, "bright" means promising or hopeful.'},
                {'type': 'multiple_choice', 'question': 'Choose the correct collocation:', 'options': ['make a mistake', 'do a mistake', 'have a mistake', 'take a mistake'], 'correct': 0, 'explanation': 'We "make" a mistake, not "do" a mistake.'},
                {'type': 'fill_blank', 'question': 'I\'m looking _____ my keys. Have you seen them?', 'correct': ['for'], 'explanation': '"Look for" means to search for something.'},
                {'type': 'multiple_choice', 'question': 'What is a "colleague"?', 'options': ['a family member', 'a friend', 'a coworker', 'a neighbor'], 'correct': 2, 'explanation': 'A colleague is someone you work with.'},
            ]
        },
        {
            'title': 'Phrasal Verb Power',
            'title_es': 'Poder de los Phrasal Verbs',
            'description': 'Master these essential phrasal verbs!',
            'questions': [
                {'type': 'multiple_choice', 'question': '"Give up" means:', 'options': ['to donate', 'to stop trying', 'to raise', 'to offer'], 'correct': 1, 'explanation': '"Give up" means to stop trying or quit.'},
                {'type': 'multiple_choice', 'question': 'Complete: Please turn _____ the lights when you leave.', 'options': ['on', 'off', 'up', 'in'], 'correct': 1, 'explanation': '"Turn off" means to switch off.'},
                {'type': 'fill_blank', 'question': 'I need to look _____ this word in the dictionary.', 'correct': ['up'], 'explanation': '"Look up" means to search for information.'},
                {'type': 'multiple_choice', 'question': '"Break down" can mean:', 'options': ['to repair', 'to stop working', 'to build', 'to clean'], 'correct': 1, 'explanation': '"Break down" means to stop functioning.'},
                {'type': 'multiple_choice', 'question': '"Put off" means:', 'options': ['to wear', 'to postpone', 'to remove', 'to place'], 'correct': 1, 'explanation': '"Put off" means to delay or postpone.'},
            ]
        },
    ],
    'grammar': [
        {
            'title': 'Tense Master',
            'title_es': 'Maestro de los Tiempos',
            'description': 'Perfect your use of English tenses!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'She _____ to the gym every day.', 'options': ['go', 'goes', 'going', 'gone'], 'correct': 1, 'explanation': 'Third person singular (she) requires "goes" in present simple.'},
                {'type': 'multiple_choice', 'question': 'I _____ my homework when you called.', 'options': ['did', 'was doing', 'have done', 'do'], 'correct': 1, 'explanation': 'Past continuous for an action in progress when interrupted.'},
                {'type': 'fill_blank', 'question': 'They have _____ (live) here since 2010.', 'correct': ['lived'], 'explanation': 'Present perfect requires past participle: have + lived.'},
                {'type': 'multiple_choice', 'question': 'By next year, I _____ graduated.', 'options': ['will', 'will have', 'have', 'had'], 'correct': 1, 'explanation': 'Future perfect: will have + past participle.'},
                {'type': 'multiple_choice', 'question': 'If I _____ rich, I would travel the world.', 'options': ['am', 'was', 'were', 'be'], 'correct': 2, 'explanation': 'Second conditional uses "were" for all subjects.'},
            ]
        },
        {
            'title': 'Article Expert',
            'title_es': 'Experto en Artículos',
            'description': 'Master the use of a, an, and the!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'I saw _____ elephant at the zoo.', 'options': ['a', 'an', 'the', '-'], 'correct': 1, 'explanation': 'Use "an" before vowel sounds.'},
                {'type': 'multiple_choice', 'question': '_____ sun rises in the east.', 'options': ['A', 'An', 'The', '-'], 'correct': 2, 'explanation': 'Use "the" for unique objects.'},
                {'type': 'fill_blank', 'question': 'She is _____ honest person.', 'correct': ['an'], 'explanation': '"Honest" starts with a vowel sound, so use "an".'},
                {'type': 'multiple_choice', 'question': 'I love _____ music.', 'options': ['a', 'an', 'the', '-'], 'correct': 3, 'explanation': 'No article with general/abstract nouns.'},
                {'type': 'multiple_choice', 'question': 'Could you pass me _____ salt?', 'options': ['a', 'an', 'the', '-'], 'correct': 2, 'explanation': 'Use "the" when both know which one.'},
            ]
        },
        {
            'title': 'Preposition Pro',
            'title_es': 'Profesional de las Preposiciones',
            'description': 'Get your prepositions right!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'I\'ll meet you _____ Monday.', 'options': ['in', 'on', 'at', 'by'], 'correct': 1, 'explanation': 'Use "on" with days of the week.'},
                {'type': 'multiple_choice', 'question': 'She lives _____ New York.', 'options': ['in', 'on', 'at', 'to'], 'correct': 0, 'explanation': 'Use "in" with cities and countries.'},
                {'type': 'fill_blank', 'question': 'The meeting is _____ 3 PM.', 'correct': ['at'], 'explanation': 'Use "at" with specific times.'},
                {'type': 'multiple_choice', 'question': 'I\'m interested _____ learning English.', 'options': ['in', 'on', 'at', 'to'], 'correct': 0, 'explanation': '"Interested" is followed by "in".'},
                {'type': 'multiple_choice', 'question': 'We arrived _____ the airport early.', 'options': ['in', 'on', 'at', 'to'], 'correct': 2, 'explanation': 'Use "at" for specific locations/buildings.'},
            ]
        },
    ],
    'reading': [
        {
            'title': 'Reading Comprehension Challenge',
            'title_es': 'Desafío de Comprensión Lectora',
            'description': 'Read the passage and answer the questions!',
            'questions': [
                {'type': 'reading', 'passage': 'John woke up late on Monday morning. He rushed to get ready and skipped breakfast. When he arrived at work, his boss was already in a meeting. John felt relieved that no one noticed he was late. He promised himself to set two alarms from now on.', 'question': 'Why did John skip breakfast?', 'options': ['He wasn\'t hungry', 'He woke up late', 'He had eaten earlier', 'His boss called him'], 'correct': 1, 'explanation': 'The text says he "woke up late" and "rushed to get ready", implying he had no time for breakfast.'},
                {'type': 'reading', 'passage': 'John woke up late on Monday morning. He rushed to get ready and skipped breakfast. When he arrived at work, his boss was already in a meeting. John felt relieved that no one noticed he was late. He promised himself to set two alarms from now on.', 'question': 'How did John feel when he arrived at work?', 'options': ['Angry', 'Relieved', 'Tired', 'Hungry'], 'correct': 1, 'explanation': 'The text explicitly says "John felt relieved".'},
                {'type': 'reading', 'passage': 'John woke up late on Monday morning. He rushed to get ready and skipped breakfast. When he arrived at work, his boss was already in a meeting. John felt relieved that no one noticed he was late. He promised himself to set two alarms from now on.', 'question': 'What will John do differently?', 'options': ['Wake up earlier', 'Set two alarms', 'Skip work', 'Talk to his boss'], 'correct': 1, 'explanation': 'The text says he "promised himself to set two alarms".'},
                {'type': 'multiple_choice', 'question': 'What day was it?', 'options': ['Sunday', 'Monday', 'Friday', 'Saturday'], 'correct': 1, 'explanation': 'The text begins with "Monday morning".'},
                {'type': 'multiple_choice', 'question': 'Where was John\'s boss?', 'options': ['At home', 'In a meeting', 'Outside', 'On vacation'], 'correct': 1, 'explanation': 'The text says "his boss was already in a meeting".'},
            ]
        },
    ],
    'mixed': [
        {
            'title': 'Mixed Skills Challenge',
            'title_es': 'Desafío de Habilidades Mixtas',
            'description': 'Test all your English skills in one challenge!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'She _____ English very well.', 'options': ['speak', 'speaks', 'speaking', 'spoke'], 'correct': 1, 'explanation': 'Present simple with third person singular requires -s.'},
                {'type': 'multiple_choice', 'question': 'What is the past tense of "go"?', 'options': ['goed', 'gone', 'went', 'going'], 'correct': 2, 'explanation': '"Went" is the irregular past tense of "go".'},
                {'type': 'fill_blank', 'question': 'I\'m looking forward _____ meeting you.', 'correct': ['to'], 'explanation': '"Look forward to" requires the preposition "to".'},
                {'type': 'multiple_choice', 'question': '"Run out of" means:', 'options': ['to have plenty', 'to have none left', 'to buy more', 'to save'], 'correct': 1, 'explanation': '"Run out of" means to use all of something.'},
                {'type': 'multiple_choice', 'question': 'Choose the correct sentence:', 'options': ['I have much friends', 'I have many friends', 'I have a lot friend', 'I have lots friend'], 'correct': 1, 'explanation': '"Many" is used with countable nouns (friends).'},
            ]
        },
        {
            'title': 'Quick Fire Round',
            'title_es': 'Ronda Rápida',
            'description': 'Answer quickly and correctly!',
            'questions': [
                {'type': 'multiple_choice', 'question': 'Opposite of "easy":', 'options': ['simple', 'difficult', 'light', 'slow'], 'correct': 1, 'explanation': '"Difficult" is the opposite of "easy".'},
                {'type': 'multiple_choice', 'question': 'I _____ born in 1990.', 'options': ['am', 'was', 'were', 'be'], 'correct': 1, 'explanation': 'Use "was" for past tense with "I".'},
                {'type': 'fill_blank', 'question': 'Have you ever _____ (be) to Paris?', 'correct': ['been'], 'explanation': 'Present perfect: have + been (past participle).'},
                {'type': 'multiple_choice', 'question': '"A piece of cake" means:', 'options': ['delicious food', 'something easy', 'a birthday party', 'a bakery'], 'correct': 1, 'explanation': 'This idiom means something very easy.'},
                {'type': 'multiple_choice', 'question': 'Complete: Neither John _____ Mary came.', 'options': ['or', 'and', 'nor', 'but'], 'correct': 2, 'explanation': '"Neither... nor" is the correct pair.'},
            ]
        },
    ]
}


def seed_daily_challenges():
    """Crear desafíos diarios para los próximos 30 días"""
    with app.app_context():
        print("="*70)
        print("📅 CREANDO DAILY CHALLENGES")
        print("="*70)
        
        added = 0
        skipped = 0
        today = date.today()
        
        # Crear desafíos para los próximos 30 días
        for day_offset in range(30):
            challenge_date = today + timedelta(days=day_offset)
            
            # Verificar si ya existe un desafío para esta fecha
            existing = DailyChallenge.query.filter_by(challenge_date=challenge_date).first()
            if existing:
                skipped += 1
                continue
            
            # Seleccionar tipo de desafío (rotando)
            challenge_type = CHALLENGE_TYPES[day_offset % len(CHALLENGE_TYPES)]
            
            # Seleccionar plantilla
            templates = CHALLENGE_TEMPLATES[challenge_type]
            template = templates[day_offset % len(templates)]
            
            # Determinar dificultad basada en el día de la semana
            weekday = challenge_date.weekday()
            if weekday < 3:  # Lun-Mié
                difficulty = 'beginner'
                points = 30
            elif weekday < 5:  # Jue-Vie
                difficulty = 'intermediate'
                points = 50
            else:  # Sáb-Dom
                difficulty = 'advanced'
                points = 75
            
            challenge = DailyChallenge(
                challenge_date=challenge_date,
                challenge_type=challenge_type,
                title=f"{template['title']} - Day {day_offset + 1}",
                description=template['description'],
                questions=template['questions'],
                difficulty=difficulty,
                points_reward=points,
                bonus_streak_points=10,
                time_limit_seconds=300  # 5 minutos
            )
            db.session.add(challenge)
            added += 1
        
        db.session.commit()
        
        print(f"✅ Daily Challenges creados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print(f"\n📊 Desafíos por tipo:")
        for ctype in CHALLENGE_TYPES:
            count = DailyChallenge.query.filter_by(challenge_type=ctype).count()
            print(f"   {ctype}: {count}")
        print(f"\n📆 Rango de fechas: {today} a {today + timedelta(days=29)}")
        print("="*70)


if __name__ == '__main__':
    seed_daily_challenges()
