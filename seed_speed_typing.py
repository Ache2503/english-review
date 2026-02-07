#!/usr/bin/env python3
"""
Seed de Speed Typing - Contenido para el juego de escritura rápida
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import SpeedTyping

app = create_app()

SPEED_TYPING_CONTENT = [
    # A1 Level - Common Phrases
    {
        'phrase': 'Good morning',
        'category': 'greetings',
        'cefr_level': 'A1',
        'difficulty': 'easy',
        'pronunciation_hint': 'GOOD MOR-ning',
        'meaning': 'Saludo por la mañana / Hello in the morning',
        'example_sentence': 'Good morning! How are you today?'
    },
    {
        'phrase': 'Nice to meet you',
        'category': 'greetings',
        'cefr_level': 'A1',
        'difficulty': 'easy',
        'pronunciation_hint': 'NICE to MEET you',
        'meaning': 'Es un placer conocerte / Pleased to make your acquaintance',
        'example_sentence': 'Hi John! Nice to meet you. I\'m Sarah.'
    },
    {
        'phrase': 'How are you',
        'category': 'common_phrases',
        'cefr_level': 'A1',
        'difficulty': 'easy',
        'pronunciation_hint': 'HOW are YOU',
        'meaning': '¿Cómo estás? / Asking about someone\'s wellbeing',
        'example_sentence': 'How are you feeling today?'
    },
    {
        'phrase': 'Thank you very much',
        'category': 'polite_phrases',
        'cefr_level': 'A1',
        'difficulty': 'easy',
        'pronunciation_hint': 'THANK you VER-y MUCH',
        'meaning': 'Muchas gracias / Expressing gratitude',
        'example_sentence': 'Thank you very much for your help!'
    },
    {
        'phrase': 'What is your name',
        'category': 'common_phrases',
        'cefr_level': 'A1',
        'difficulty': 'easy',
        'pronunciation_hint': 'WHAT is your NAME',
        'meaning': '¿Cuál es tu nombre? / Asking for identification',
        'example_sentence': 'What is your name, please?'
    },
    {
        'phrase': 'Where is the bathroom',
        'category': 'common_phrases',
        'cefr_level': 'A1',
        'difficulty': 'medium',
        'pronunciation_hint': 'WHERE is the BATH-room',
        'meaning': '¿Dónde está el baño? / Asking for location',
        'example_sentence': 'Excuse me, where is the bathroom?'
    },
    {
        'phrase': 'Do you speak English',
        'category': 'common_phrases',
        'cefr_level': 'A1',
        'difficulty': 'medium',
        'pronunciation_hint': 'Do you SPEAK ENG-lish',
        'meaning': '¿Hablas inglés? / Asking about language ability',
        'example_sentence': 'Do you speak English? I can help you.'
    },
    {
        'phrase': 'I do not understand',
        'category': 'common_phrases',
        'cefr_level': 'A1',
        'difficulty': 'medium',
        'pronunciation_hint': 'I do NOT un-DER-stand',
        'meaning': 'No entiendo / Expressing lack of comprehension',
        'example_sentence': 'Could you speak more slowly? I do not understand.'
    },
    
    # A2 Level - Common Phrases
    {
        'phrase': 'I would like to order',
        'category': 'restaurant',
        'cefr_level': 'A2',
        'difficulty': 'medium',
        'pronunciation_hint': 'I would LIKE to OR-der',
        'meaning': 'Me gustaría pedir / Ordering food or service',
        'example_sentence': 'Excuse me, I would like to order a coffee, please.'
    },
    {
        'phrase': 'Can you recommend something',
        'category': 'restaurant',
        'cefr_level': 'A2',
        'difficulty': 'medium',
        'pronunciation_hint': 'CAN you REC-om-MEND some-THING',
        'meaning': '¿Puedes recomendar algo? / Asking for suggestions',
        'example_sentence': 'Can you recommend something delicious?'
    },
    {
        'phrase': 'How much does it cost',
        'category': 'shopping',
        'cefr_level': 'A2',
        'difficulty': 'medium',
        'pronunciation_hint': 'HOW MUCH does it COST',
        'meaning': '¿Cuánto cuesta? / Asking about price',
        'example_sentence': 'How much does it cost? I want to buy it.'
    },
    {
        'phrase': 'I am interested in learning English',
        'category': 'education',
        'cefr_level': 'A2',
        'difficulty': 'hard',
        'pronunciation_hint': 'I AM IN-ter-ESTED in LEARN-ing ENG-lish',
        'meaning': 'Me interesa aprender inglés / Expressing interest',
        'example_sentence': 'I am interested in learning English to improve my career.'
    },
    {
        'phrase': 'Could you help me please',
        'category': 'polite_phrases',
        'cefr_level': 'A2',
        'difficulty': 'medium',
        'pronunciation_hint': 'COULD you HELP me PLEASE',
        'meaning': '¿Podrías ayudarme por favor? / Polite request',
        'example_sentence': 'Could you help me please? I am lost.'
    },
    {
        'phrase': 'I am sorry for being late',
        'category': 'polite_phrases',
        'cefr_level': 'A2',
        'difficulty': 'hard',
        'pronunciation_hint': 'I am SOR-ry for BE-ing LATE',
        'meaning': 'Lo siento por llegar tarde / Apologizing',
        'example_sentence': 'I am sorry for being late. The traffic was terrible.'
    },
    
    # B1 Level - Idioms and Phrases
    {
        'phrase': 'break the ice',
        'category': 'idioms',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'BREAK the ICE',
        'meaning': 'Romper el hielo / To start a conversation in a social situation',
        'example_sentence': 'Let me tell a joke to break the ice at the party.'
    },
    {
        'phrase': 'piece of cake',
        'category': 'idioms',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'PIECE of CAKE',
        'meaning': 'Fácil / Very easy to do',
        'example_sentence': 'This exam was a piece of cake. I finished in 30 minutes.'
    },
    {
        'phrase': 'it is raining cats and dogs',
        'category': 'idioms',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'it is RAIN-ing CATS and DOGS',
        'meaning': 'Llueve a cántaros / Raining heavily',
        'example_sentence': 'It is raining cats and dogs outside. We should stay home.'
    },
    {
        'phrase': 'the best of both worlds',
        'category': 'idioms',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'the BEST of BOTH WORLDS',
        'meaning': 'Lo mejor de ambos mundos / The advantages of two different things',
        'example_sentence': 'Remote work is the best of both worlds: flexibility and productivity.'
    },
    {
        'phrase': 'I look forward to hearing from you',
        'category': 'business',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'I LOOK for-WARD to HEAR-ing FROM you',
        'meaning': 'Espero saber de ti / Professional closing phrase',
        'example_sentence': 'Thank you for your time. I look forward to hearing from you soon.'
    },
    {
        'phrase': 'I would appreciate your feedback',
        'category': 'business',
        'cefr_level': 'B1',
        'difficulty': 'hard',
        'pronunciation_hint': 'I would ap-PRE-ci-ATE your FEED-back',
        'meaning': 'Apreciaría tu comentario / Politely requesting opinion',
        'example_sentence': 'I would appreciate your feedback on this project proposal.'
    },
    
    # B2 Level - Complex Phrases
    {
        'phrase': 'not to mention the fact that',
        'category': 'discourse_markers',
        'cefr_level': 'B2',
        'difficulty': 'hard',
        'pronunciation_hint': 'not to MEN-tion the FACT that',
        'meaning': 'Sin mencionar que / And also remember that',
        'example_sentence': 'The project is delayed, not to mention the fact that costs have increased significantly.'
    },
    {
        'phrase': 'taking everything into account',
        'category': 'discourse_markers',
        'cefr_level': 'B2',
        'difficulty': 'hard',
        'pronunciation_hint': 'TAK-ing EV-ry-THING in-TO ac-COUNT',
        'meaning': 'Considerando todo / Considering all factors',
        'example_sentence': 'Taking everything into account, the merger is the best strategic move.'
    },
    {
        'phrase': 'it goes without saying that',
        'category': 'discourse_markers',
        'cefr_level': 'B2',
        'difficulty': 'hard',
        'pronunciation_hint': 'it GOES with-OUT SAY-ing that',
        'meaning': 'Huelga decir que / It is obvious that',
        'example_sentence': 'It goes without saying that safety is our top priority.'
    },
]


def seed_speed_typing():
    """Seed del contenido de Speed Typing"""
    with app.app_context():
        try:
            print("⚡ CREANDO SPEED TYPING")
            
            for content_data in SPEED_TYPING_CONTENT:
                # Verificar si ya existe
                existing = SpeedTyping.query.filter_by(
                    phrase=content_data['phrase']
                ).first()
                
                if not existing:
                    typing = SpeedTyping(
                        phrase=content_data['phrase'],
                        category=content_data.get('category'),
                        cefr_level=content_data.get('cefr_level'),
                        difficulty=content_data.get('difficulty'),
                        pronunciation_hint=content_data.get('pronunciation_hint'),
                        meaning=content_data.get('meaning'),
                        example_sentence=content_data.get('example_sentence'),
                        is_active=True
                    )
                    db.session.add(typing)
            
            db.session.commit()
            
            # Estadísticas
            total = SpeedTyping.query.count()
            print(f"✅ Frases creadas: {total}")
            
            # Contar por nivel
            for level in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
                count = SpeedTyping.query.filter_by(cefr_level=level).count()
                if count > 0:
                    print(f"   - {level}: {count} frases")
            
            # Contar por categoría
            categories = db.session.query(SpeedTyping.category, db.func.count(SpeedTyping.id)).group_by(SpeedTyping.category).all()
            if categories:
                print(f"\n📂 Por categoría:")
                for cat, count in categories:
                    print(f"   - {cat}: {count}")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()


if __name__ == '__main__':
    seed_speed_typing()
