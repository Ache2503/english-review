#!/usr/bin/env python3
"""
Script para generar flashcards a partir del vocabulario.
Ejecutar: python seed_flashcards.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import VocabularyItem, VocabularyCategory, Flashcard

def add_flashcards():
    app = create_app()
    with app.app_context():
        print("=" * 70)
        print("AGREGANDO FLASHCARDS DESDE VOCABULARIO")
        print("=" * 70)

        items = VocabularyItem.query.all()
        added = 0
        skipped = 0

        for item in items:
            category = VocabularyCategory.query.get(item.category_id)
            unit_id = category.unit_id if category else None
            if not unit_id:
                skipped += 1
                continue

            existing = Flashcard.query.filter_by(unit_id=unit_id, front=item.word).first()
            if existing:
                skipped += 1
                continue

            flashcard = Flashcard(
                unit_id=unit_id,
                front=item.word,
                back=item.definition,
                example=item.example,
                difficulty='beginner',
                order=item.order or 0,
                is_active=True
            )
            db.session.add(flashcard)
            added += 1

        db.session.commit()

        print(f"✓ Flashcards agregadas: {added}")
        print(f"- Omitidas: {skipped}")
        print("=" * 70)
        print("✅ ¡FLASHCARDS LISTAS!")

if __name__ == "__main__":
    add_flashcards()
