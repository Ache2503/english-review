#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import WritingErrorPattern, WritingTipContent

COMMON_SPANISH_ERRORS = {
    r"\bi am agree\b": "Use 'I agree' (not 'I am agree')",
    r"\bthe people is\b": "Use 'people are' (people is plural)",
    r"\bpeoples\b": "Use 'people' (already plural, no 's' needed)",
    r"\binformations?\b": "'Information' is uncountable (no plural)",
    r"\badvices?\b": "'Advice' is uncountable (use 'pieces of advice')",
    r"\bin the last years\b": "Use 'in recent years' or 'in the last few years'",
    r"\bactually\b": "Make sure 'actually' means 'really' (not 'currently')",
    r"\beventually\b": "Check if you mean 'finally' or 'possibly' (common false friend)",
    r"\bsince \d+ years\b": "Use 'for X years' (since + point in time)",
    r"\bfor a long time ago\b": "Use 'a long time ago' (without 'for')",
    r"\bI have \d+ years\b": "Use 'I am X years old' or 'I've been X for X years'",
    r"\bis very\b(?!\s+\w+\s+(?:to|that))": "Consider using stronger adjectives instead of 'very + adjective'",
    r"\bmake a party\b": "Use 'have/throw a party' (not 'make')",
    r"\bdo a mistake\b": "Use 'make a mistake' (not 'do')",
    r"\bopen the light\b": "Use 'turn on the light' (not 'open')",
    r"\bclose the light\b": "Use 'turn off the light' (not 'close')",
}

STYLE_IMPROVEMENTS = {
    r"\bvery good\b": ["excellent", "outstanding", "superb"],
    r"\bvery bad\b": ["terrible", "awful", "dreadful"],
    r"\bvery big\b": ["huge", "enormous", "massive"],
    r"\bvery small\b": ["tiny", "minute", "minuscule"],
    r"\bvery happy\b": ["delighted", "thrilled", "ecstatic"],
    r"\bvery sad\b": ["devastated", "heartbroken", "miserable"],
    r"\bvery tired\b": ["exhausted", "worn out", "drained"],
    r"\bvery angry\b": ["furious", "livid", "irate"],
    r"\bvery scared\b": ["terrified", "petrified", "horrified"],
    r"\bvery cold\b": ["freezing", "frigid", "icy"],
    r"\bvery hot\b": ["scorching", "boiling", "sweltering"],
}

CONNECTORS_BY_LEVEL = {
    'basic': ['and', 'but', 'or', 'so', 'because'],
    'intermediate': ['however', 'therefore', 'moreover', 'although', 'nevertheless'],
    'advanced': ['consequently', 'furthermore', 'notwithstanding', 'hence', 'thus']
}

TIPS_DATABASE = {
    "SPANISH_SPEAKER_ERROR": {
        "title": "Errores comunes de hispanohablantes",
        "description": "Estos errores son típicos al traducir directamente del español.",
        "tips": [
            "Evita traducciones literales del español",
            "Recuerda que 'people' es plural en inglés",
            "Algunos sustantivos son incontables: information, advice, news",
            "'Actually' significa 'en realidad', no 'actualmente'",
            "Usa 'for' con duraciones y 'since' con puntos en el tiempo",
        ],
        "examples": [
            {"wrong": "I am agree", "correct": "I agree"},
            {"wrong": "The people is happy", "correct": "The people are happy"},
            {"wrong": "I have 25 years", "correct": "I am 25 years old"},
        ],
    },
    "STYLE_IMPROVEMENT": {
        "title": "Mejoras de estilo",
        "description": "Usa palabras más precisas para un inglés más natural.",
        "tips": [
            "Evita 'very + adjective', usa adjetivos más fuertes",
            "Varía las estructuras de tus oraciones",
            "Usa conectores para mejorar la fluidez",
            "Evita repetir las mismas palabras",
        ],
        "examples": [
            {"wrong": "very happy", "correct": "delighted, thrilled, ecstatic"},
            {"wrong": "very big", "correct": "huge, enormous, massive"},
            {"wrong": "very good", "correct": "excellent, outstanding, superb"},
        ],
    },
    "SENTENCE_CASE": {
        "title": "Uso de mayúsculas",
        "description": "Las reglas de capitalización en inglés.",
        "tips": [
            "Siempre inicia las oraciones con mayúscula",
            "Los nombres propios llevan mayúscula",
            "Los días de la semana y meses van con mayúscula",
            "'I' siempre va en mayúscula",
        ],
        "examples": [
            {
                "wrong": "i went to london on monday",
                "correct": "I went to London on Monday",
            },
        ],
    },
    "default": {
        "title": "Consejos generales de escritura",
        "description": "Mejora tu escritura en inglés con estos consejos.",
        "tips": [
            "Lee en voz alta para detectar errores",
            "Revisa la concordancia sujeto-verbo",
            "Verifica los tiempos verbales",
            "Usa puntuación correctamente",
            "Practica escribiendo regularmente",
        ],
        "examples": [],
    },
}


def seed_error_patterns():
    print("=" * 70)
    print("SEEDING WRITING_ERROR_PATTERNS")
    print("=" * 70)

    created = 0
    skipped = 0

    for pattern, message in COMMON_SPANISH_ERRORS.items():
        existing = WritingErrorPattern.query.filter_by(
            pattern_type="spanish_error", pattern=pattern
        ).first()
        if existing:
            skipped += 1
            continue
        db.session.add(
            WritingErrorPattern(
                pattern_type="spanish_error",
                pattern=pattern,
                message=message,
                replacements=None,
                level=None,
                is_active=True,
            )
        )
        created += 1
        print(f"  + spanish_error: {pattern[:50]}")

    for pattern, replacements in STYLE_IMPROVEMENTS.items():
        existing = WritingErrorPattern.query.filter_by(
            pattern_type="style_improvement", pattern=pattern
        ).first()
        if existing:
            skipped += 1
            continue
        db.session.add(
            WritingErrorPattern(
                pattern_type="style_improvement",
                pattern=pattern,
                message=None,
                replacements=replacements,
                level=None,
                is_active=True,
            )
        )
        created += 1
        print(f"  + style_improvement: {pattern[:50]}")

    for level, words in CONNECTORS_BY_LEVEL.items():
        for word in words:
            existing = WritingErrorPattern.query.filter_by(
                pattern_type="connector", pattern=word
            ).first()
            if existing:
                skipped += 1
                continue
            db.session.add(
                WritingErrorPattern(
                    pattern_type="connector",
                    pattern=word,
                    message=None,
                    replacements=None,
                    level=level,
                    is_active=True,
                )
            )
            created += 1
            print(f"  + connector [{level}]: {word}")

    db.session.commit()
    print(f"\n  Created: {created} | Skipped: {skipped}")
    print()


def seed_tip_contents():
    print("=" * 70)
    print("SEEDING WRITING_TIP_CONTENTS")
    print("=" * 70)

    created = 0
    skipped = 0

    for error_type, data in TIPS_DATABASE.items():
        existing = WritingTipContent.query.filter_by(error_type=error_type).first()
        if existing:
            skipped += 1
            print(f"  - already exists: {error_type}")
            continue
        db.session.add(
            WritingTipContent(
                error_type=error_type,
                title=data["title"],
                description=data["description"],
                tips=data["tips"],
                examples=data["examples"],
            )
        )
        created += 1
        print(f"  + {error_type}: {data['title']}")

    db.session.commit()
    print(f"\n  Created: {created} | Skipped: {skipped}")
    print()


def seed_writing_content():
    app = create_app()
    with app.app_context():
        seed_error_patterns()
        seed_tip_contents()

        total_patterns = WritingErrorPattern.query.count()
        total_tips = WritingTipContent.query.count()
        print("=" * 70)
        print(f"TOTAL writing_error_patterns: {total_patterns}")
        print(f"TOTAL writing_tip_contents:    {total_tips}")
        print("=" * 70)
        print("DONE.")


if __name__ == "__main__":
    seed_writing_content()
