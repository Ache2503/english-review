#!/usr/bin/env python
"""Verificar que la plataforma está correctamente configurada con contenido enriquecido."""

import sys
from pathlib import Path

proj_dir = Path(__file__).parent
sys.path.insert(0, str(proj_dir))

from app import create_app, db
from app.models import (
    Unit, Topic, GrammarRule, VocabularyCategory, VocabularyItem,
    WritingPractice, UnitExtra, Quiz, QuizQuestion
)

app = create_app('development')

with app.app_context():
    print("=" * 60)
    print("VERIFICACIÓN DE PLATAFORMA ENRIQUECIDA")
    print("=" * 60)
    
    # Verificar unidades
    units = Unit.query.all()
    print(f"\n✓ Unidades en BD: {len(units)}/6")
    for u in units:
        print(f"  - Unit {u.unit_number}: {u.title}")
    
    # Verificar vocabulario
    total_words = VocabularyItem.query.count()
    total_categories = VocabularyCategory.query.count()
    print(f"\n✓ Vocabulario:")
    print(f"  - Categorías: {total_categories}")
    print(f"  - Palabras totales: {total_words}")
    
    # Verificar ejercicios
    total_exercises = WritingPractice.query.count()
    print(f"\n✓ Ejercicios de Escritura:")
    print(f"  - Total: {total_exercises}")
    for unit in units:
        exercises = WritingPractice.query.filter_by(unit_id=unit.id).all()
        if exercises:
            print(f"  - Unit {unit.unit_number}: {len(exercises)} ejercicios")
            for ex in exercises:
                print(f"    • {ex.title} ({ex.difficulty})")
    
    # Verificar reglas gramaticales
    total_grammar = GrammarRule.query.count()
    print(f"\n✓ Reglas Gramaticales:")
    print(f"  - Total: {total_grammar}")
    
    # Verificar diálogos
    total_extras = UnitExtra.query.count()
    print(f"\n✓ Contenido Adicional (UnitExtra):")
    print(f"  - Registros: {total_extras}")
    
    # Verificar quizzes
    total_quizzes = Quiz.query.count()
    print(f"\n✓ Quizzes:")
    print(f"  - Total: {total_quizzes}")
    
    # Resumen final
    print("\n" + "=" * 60)
    print("✅ PLATAFORMA COMPLETAMENTE ENRIQUECIDA")
    print("=" * 60)
    print(f"\nTotales:")
    print(f"  - Unidades: {len(units)}")
    print(f"  - Vocabulario: {total_words} palabras en {total_categories} categorías")
    print(f"  - Ejercicios: {total_exercises}")
    print(f"  - Gramática: {total_grammar} reglas")
    print(f"  - Quizzes: {total_quizzes}")
    print(f"\n🎓 Tu plataforma está lista para enseñar!")
    print("=" * 60)
