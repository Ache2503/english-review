#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import (
    SentencePatternContent,
    ConceptSynonym,
    ErrorTipContent,
    AchievementMilestone,
)

SENTENCE_PATTERNS = {
    'Articles': {
        'patterns': [
            {'structure': 'I go to [the] school', 'meaning': '[the] = edificio específico | sin artículo = como estudiante'},
            {'structure': 'Use [the] for specific things', 'meaning': 'Ej: The cat is black (gato específico)'},
            {'structure': 'Use [a/an] for general things', 'meaning': 'Ej: A cat is an animal (categoría general)'}
        ]
    },
    'Used to': {
        'patterns': [
            {'structure': 'Subject + used to + verb', 'meaning': 'Ej: I used to play soccer'},
            {'structure': 'I used to wake up early', 'meaning': 'Acción habitual en el pasado (ya no ocurre)'},
            {'structure': 'Did you use to...? / He used to...', 'meaning': 'Preguntas y respuestas negativas'}
        ]
    },
    'Reflexive Pronouns': {
        'patterns': [
            {'structure': 'Subject + verb + reflexive pronoun', 'meaning': 'Ej: I hurt myself'},
            {'structure': 'myself, yourself, himself, herself, itself, ourselves, yourselves, themselves', 'meaning': 'Cuando el sujeto y objeto son el mismo'},
            {'structure': 'She taught herself to code', 'meaning': 'Ella misma se enseñó (por su propia acción)'}
        ]
    },
    'Infinitive of Purpose': {
        'patterns': [
            {'structure': 'Subject + verb + to + infinitive', 'meaning': 'Ej: I went to the store to buy milk'},
            {'structure': '[action] + TO + [reason/purpose]', 'meaning': 'Ej: He exercises to stay healthy'},
            {'structure': 'I came to help you', 'meaning': 'Viniste CON EL PROPÓSITO DE ayudar'}
        ]
    },
    'First Conditional': {
        'patterns': [
            {'structure': 'If + Present + will + verb', 'meaning': 'Situación real/posible'},
            {'structure': 'If it rains, I will stay home', 'meaning': 'Si llueve (probable), me quedaré en casa'},
            {'structure': 'If you study, you will pass the exam', 'meaning': 'Resultado natural y lógico'}
        ]
    },
    'Second Conditional': {
        'patterns': [
            {'structure': 'If + Past + would + verb', 'meaning': 'Situación imaginaria/hipotética'},
            {'structure': 'If I had money, I would travel', 'meaning': 'Si tuviera dinero (no tengo), viajaría'},
            {'structure': 'If she were a bird, she would fly', 'meaning': 'Imaginario, no es real'}
        ]
    },
    'Gerunds': {
        'patterns': [
            {'structure': 'Verb + -ing (actuando como sustantivo)', 'meaning': 'Ej: Swimming is fun'},
            {'structure': 'Subject + verb + gerund', 'meaning': 'Ej: I enjoy reading books'},
            {'structure': 'Spending money is easy', 'meaning': 'El acto/acción como sustantivo'}
        ]
    },
    'Comparatives': {
        'patterns': [
            {'structure': 'Subject + verb + adjective + than + object', 'meaning': 'Ej: My house is bigger than yours'},
            {'structure': 'More + adjective + than', 'meaning': 'Para adjetivos largos: more expensive than'},
            {'structure': 'Adjective + -er + than', 'meaning': 'Para adjetivos cortos: faster than, taller than'}
        ]
    },
    'Superlatives': {
        'patterns': [
            {'structure': 'The + adjective + -est', 'meaning': 'Ej: the tallest, the fastest'},
            {'structure': 'The most + adjective', 'meaning': 'Para adjetivos largos: the most beautiful'},
            {'structure': 'Subject + verb + the + superlative', 'meaning': 'Ej: She is the smartest student'}
        ]
    },
    'Passive Voice': {
        'patterns': [
            {'structure': 'Object + be + past participle + by + subject', 'meaning': 'Ej: The car was washed by John'},
            {'structure': 'Plastic is found everywhere', 'meaning': 'La acción es más importante que quien la hace'},
            {'structure': 'The book was written by the author', 'meaning': 'Se enfoca en lo que pasó, no en quién lo hizo'}
        ]
    }
}

CONCEPT_SYNONYMS = {
    'articles': ['article', 'articles', 'a/an/the', 'definite article', 'indefinite article', 'zero article', 'no article'],
    'used to': ['used to'],
    'reflexive pronouns': ['reflexive pronouns', 'reflexive'],
    'infinitive of purpose': ['infinitive of purpose', 'to-infinitive', 'purpose'],
    'first conditional': ['first conditional', 'conditional type 1', 'type 1 conditional'],
    'second conditional': ['second conditional', 'conditional type 2', 'type 2 conditional'],
    'gerunds': ['gerunds', 'gerund', '-ing form as noun'],
    'adjective clauses': ['adjective clauses', 'essential adjective clauses', 'relative clauses'],
    'comparatives': ['comparatives', 'comparative', 'more/less than', 'er than'],
    'superlatives': ['superlatives', 'superlative', 'the most', 'the least', 'est'],
    'need to': ['need to', 'need'],
    'passive voice': ['passive voice', 'passive'],
    'adjective + infinitive': ['adjective + infinitive', 'it is adj to verb'],
    'where words': ['words with -where', 'somewhere', 'nowhere', 'everywhere', '-where'],
    'reported speech': ['reported speech', 'indirect speech', 'reported statements'],
    'past perfect': ['past perfect', 'pluperfect'],
    'should': ['should']
}

ERROR_TIPS = {
    'grammar': {
        'verb_tenses': [
            'Practica identificar el tiempo verbal en oraciones',
            'Crea tarjetas con las conjugaciones irregulares',
            'Lee textos y subraya los verbos'
        ],
        'articles': [
            'Recuerda: "a" antes de consonante, "an" antes de vocal',
            'Los nombres propios no llevan artículo',
            'Usa "the" para cosas específicas'
        ],
        'prepositions': [
            'Las preposiciones de tiempo: in (meses/años), on (días), at (hora)',
            'Memoriza las combinaciones verbo + preposición',
            'Practica con ejercicios de fill-in-the-blank'
        ]
    },
    'vocabulary': {
        'spelling': [
            'Lee en voz alta mientras escribes',
            'Usa la técnica de "look, cover, write, check"',
            'Agrupa palabras con patrones similares'
        ],
        'word_choice': [
            'Usa un diccionario de sinónimos',
            'Aprende palabras en contexto, no aisladas',
            'Practica con ejercicios de matching'
        ]
    }
}

ACHIEVEMENT_MILESTONES = [
    {'name': 'First 100 Points', 'milestone_type': 'points', 'threshold': 100, 'description': 'Alcanza 100 puntos totales', 'icon': '🏆'},
    {'name': 'Reach 500 Points', 'milestone_type': 'points', 'threshold': 500, 'description': 'Alcanza 500 puntos totales', 'icon': '🏆'},
    {'name': '7-Day Streak', 'milestone_type': 'streak', 'threshold': 7, 'description': 'Mantén una racha de 7 días', 'icon': '🔥'},
    {'name': '30-Day Streak', 'milestone_type': 'streak', 'threshold': 30, 'description': 'Mantén una racha de 30 días', 'icon': '🔥'},
]


def seed_sentence_patterns():
    print("=" * 70)
    print("SEEDING SENTENCE PATTERNS")
    print("=" * 70)
    added = 0
    skipped = 0
    for topic_name, data in SENTENCE_PATTERNS.items():
        existing = SentencePatternContent.query.filter_by(topic_name=topic_name).first()
        if existing:
            skipped += 1
            continue
        record = SentencePatternContent(topic_name=topic_name, patterns=data['patterns'])
        db.session.add(record)
        added += 1
    db.session.commit()
    print(f"  Added: {added}")
    print(f"  Skipped (already exist): {skipped}")
    print()


def seed_concept_synonyms():
    print("=" * 70)
    print("SEEDING CONCEPT SYNONYMS")
    print("=" * 70)
    added = 0
    skipped = 0
    for concept_key, synonyms in CONCEPT_SYNONYMS.items():
        existing = ConceptSynonym.query.filter_by(concept_key=concept_key).first()
        if existing:
            skipped += 1
            continue
        record = ConceptSynonym(concept_key=concept_key, synonyms=synonyms)
        db.session.add(record)
        added += 1
    db.session.commit()
    print(f"  Added: {added}")
    print(f"  Skipped (already exist): {skipped}")
    print()


def seed_error_tips():
    print("=" * 70)
    print("SEEDING ERROR TIPS")
    print("=" * 70)
    added = 0
    skipped = 0
    for category, error_types in ERROR_TIPS.items():
        for error_type, tips in error_types.items():
            existing = ErrorTipContent.query.filter_by(
                category=category, error_type=error_type
            ).first()
            if existing:
                skipped += 1
                continue
            record = ErrorTipContent(category=category, error_type=error_type, tips=tips)
            db.session.add(record)
            added += 1
    db.session.commit()
    print(f"  Added: {added}")
    print(f"  Skipped (already exist): {skipped}")
    print()


def seed_achievement_milestones():
    print("=" * 70)
    print("SEEDING ACHIEVEMENT MILESTONES")
    print("=" * 70)
    added = 0
    skipped = 0
    for milestone in ACHIEVEMENT_MILESTONES:
        existing = AchievementMilestone.query.filter_by(
            name=milestone['name']
        ).first()
        if existing:
            skipped += 1
            continue
        record = AchievementMilestone(
            name=milestone['name'],
            milestone_type=milestone['milestone_type'],
            threshold=milestone['threshold'],
            description=milestone['description'],
            icon=milestone['icon'],
            is_active=True,
        )
        db.session.add(record)
        added += 1
    db.session.commit()
    print(f"  Added: {added}")
    print(f"  Skipped (already exist): {skipped}")
    print()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_sentence_patterns()
        seed_concept_synonyms()
        seed_error_tips()
        seed_achievement_milestones()
        print("=" * 70)
        print("ALL DONE")
        print("=" * 70)
