#!/usr/bin/env python3
"""
Script para agregar ejercicios de oraciones específicos por gramática.
Ejecutar: python seed_sentence_exercises.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Unit, SentenceExercise, GrammarRule

def add_sentence_exercises():
    """Agrega ejercicios de oraciones específicos por gramática de cada unidad."""
    
    app = create_app()
    with app.app_context():
        print("=" * 70)
        print("AGREGANDO EJERCICIOS DE ORACIONES POR GRAMÁTICA")
        print("=" * 70)
        
        # Unit 7 - MIND (Articles & Used to)
        unit7 = Unit.query.filter_by(unit_number=7).first()
        unit7_exercises = [
            {
                "grammar_focus": "Articles",
                "exercise_type": "fill_blank",
                "instruction": "Completa con 'a', 'an', 'the' o sin artículo:",
                "prompt": "I go to ___ school every day (como estudiante).",
                "correct_answer": "school",
                "alternative_answers": [],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Articles",
                "exercise_type": "fill_blank",
                "instruction": "Completa la oración correctamente:",
                "prompt": "I need to go to ___ school to pick up my son (el edificio).",
                "correct_answer": "the school",
                "alternative_answers": [],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Used to",
                "exercise_type": "build",
                "instruction": "Construye una oración usando 'used to' sobre un hábito pasado:",
                "prompt": "Algo que hacías antes pero ya no",
                "correct_answer": "I used to wake up late",
                "alternative_answers": [
                    "I used to wake late",
                    "I used to sleep late"
                ],
                "options": ["I", "used to", "play", "soccer", "wake up", "late", "every day"],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Used to",
                "exercise_type": "translate",
                "instruction": "Traduce al inglés usando 'used to':",
                "prompt": "Yo solía ver películas todos los domingos.",
                "correct_answer": "I used to watch movies every Sunday",
                "alternative_answers": [
                    "I used to watch films every Sunday",
                    "I used to see movies every Sunday",
                    "I used to watch movies on Sundays"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Articles",
                "exercise_type": "build",
                "instruction": "Escribe una oración usando 'the' para algo específico:",
                "prompt": "Ejemplo: el profesor específico",
                "correct_answer": "The teacher is in the classroom",
                "alternative_answers": [
                    "The teacher is in the room",
                    "The teacher is in class"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Used to",
                "exercise_type": "build",
                "instruction": "Crea una oración negativa con 'used to':",
                "prompt": "Algo que no solías hacer",
                "correct_answer": "I didn't use to eat vegetables",
                "alternative_answers": [
                    "I did not use to eat vegetables",
                    "I didn't use to like vegetables"
                ],
                "difficulty": "intermediate"
            },
        ]
        
        # Unit 8 - ART (Reflexive Pronouns, Infinitive of Purpose, First Conditional)
        unit8 = Unit.query.filter_by(unit_number=8).first()
        unit8_exercises = [
            {
                "grammar_focus": "Reflexive Pronouns",
                "exercise_type": "fill_blank",
                "instruction": "Completa con el pronombre reflexivo correcto:",
                "prompt": "She taught ___ to play guitar.",
                "correct_answer": "herself",
                "options": ["myself", "yourself", "himself", "herself", "itself"],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Reflexive Pronouns",
                "exercise_type": "build",
                "instruction": "Construye una oración usando un pronombre reflexivo:",
                "prompt": "Habla sobre alguien que se lastimó",
                "correct_answer": "He hurt himself",
                "alternative_answers": [
                    "She hurt herself",
                    "I hurt myself"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Infinitive of Purpose",
                "exercise_type": "build",
                "instruction": "Usa 'to + infinitive' para explicar el propósito:",
                "prompt": "¿Por qué fuiste a la tienda?",
                "correct_answer": "I went to the store to buy milk",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "First Conditional",
                "exercise_type": "build",
                "instruction": "Crea una oración con First Conditional (If + present, will):",
                "prompt": "Situación: Lluvia y quedarse en casa",
                "correct_answer": "If it rains I will stay home",
                "alternative_answers": [
                    "If it rains, I'll stay home",
                    "I will stay home if it rains"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Infinitive of Purpose",
                "exercise_type": "build",
                "instruction": "Crea una oración con 'to' para propósito:",
                "prompt": "Estudio inglés / conseguir un mejor trabajo",
                "correct_answer": "I study English to get a better job",
                "alternative_answers": [
                    "I study English to get a better job",
                    "I study English to find a better job"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Reflexive Pronouns",
                "exercise_type": "fill_blank",
                "instruction": "Completa con el pronombre reflexivo correcto:",
                "prompt": "We organized the event by ___.",
                "correct_answer": "ourselves",
                "alternative_answers": [],
                "difficulty": "beginner"
            },
        ]
        
        # Unit 9 - MONEY (Second Conditional, Gerunds)
        unit9 = Unit.query.filter_by(unit_number=9).first()
        unit9_exercises = [
            {
                "grammar_focus": "Second Conditional",
                "exercise_type": "build",
                "instruction": "Crea una oración con Second Conditional (If + past, would):",
                "prompt": "Situación imaginaria: Tener dinero y viajar",
                "correct_answer": "If I had money I would travel",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Second Conditional",
                "exercise_type": "fill_blank",
                "instruction": "Completa correctamente:",
                "prompt": "If I ___ (be) a bird, I would fly.",
                "correct_answer": "were",
                "alternative_answers": [],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Gerunds",
                "exercise_type": "build",
                "instruction": "Usa un gerundio (-ing) como sujeto de la oración:",
                "prompt": "Habla sobre gastar dinero",
                "correct_answer": "Spending money is easy",
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Gerunds",
                "exercise_type": "build",
                "instruction": "Construye una oración con gerundio:",
                "prompt": "¿Qué disfrutas hacer?",
                "correct_answer": "I enjoy reading books",
                "alternative_answers": [
                    "I enjoy watching movies",
                    "I enjoy playing soccer"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Second Conditional",
                "exercise_type": "translate",
                "instruction": "Traduce al inglés usando Second Conditional:",
                "prompt": "Si yo ganara la lotería, compraría una casa.",
                "correct_answer": "If I won the lottery I would buy a house",
                "alternative_answers": [
                    "If I won the lottery, I would buy a house",
                    "If I won the lottery I'd buy a house"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Gerunds",
                "exercise_type": "fill_blank",
                "instruction": "Completa con el gerundio correcto:",
                "prompt": "___ (save) money is important.",
                "correct_answer": "Saving",
                "alternative_answers": [],
                "difficulty": "beginner"
            },
        ]
        
        # Unit 10 - SCIENCE (Comparatives & Superlatives)
        unit10 = Unit.query.filter_by(unit_number=10).first()
        unit10_exercises = [
            {
                "grammar_focus": "Comparatives",
                "exercise_type": "build",
                "instruction": "Compara dos cosas usando 'than':",
                "prompt": "Mi casa vs tu casa (grande)",
                "correct_answer": "My house is bigger than yours",
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Comparatives",
                "exercise_type": "fill_blank",
                "instruction": "Completa correctamente:",
                "prompt": "This phone is ___ (expensive) than that one.",
                "correct_answer": "more expensive",
                "alternative_answers": [
                    "more costly"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Superlatives",
                "exercise_type": "build",
                "instruction": "Usa el superlativo para describir:",
                "prompt": "El estudiante más inteligente",
                "correct_answer": "She is the smartest student",
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Superlatives",
                "exercise_type": "build",
                "instruction": "Construye una oración superlativa:",
                "prompt": "La película más emocionante",
                "correct_answer": "This is the most exciting movie",
                "alternative_answers": [
                    "It's the most exciting movie"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Comparatives",
                "exercise_type": "build",
                "instruction": "Compara dos dispositivos usando 'faster than':",
                "prompt": "Teléfono nuevo vs antiguo",
                "correct_answer": "My new phone is faster than my old one",
                "alternative_answers": [
                    "The new phone is faster than the old one"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Superlatives",
                "exercise_type": "fill_blank",
                "instruction": "Completa con el superlativo correcto:",
                "prompt": "This is the ___ (good) app on my phone.",
                "correct_answer": "best",
                "alternative_answers": [],
                "difficulty": "beginner"
            },
        ]
        
        # Unit 11 - NATURAL WORLD (Passive Voice)
        unit11 = Unit.query.filter_by(unit_number=11).first()
        unit11_exercises = [
            {
                "grammar_focus": "Passive Voice",
                "exercise_type": "build",
                "instruction": "Convierte a voz pasiva:",
                "prompt": "They found plastic in the ocean.",
                "correct_answer": "Plastic was found in the ocean",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Passive Voice",
                "exercise_type": "build",
                "instruction": "Usa voz pasiva para describir:",
                "prompt": "El carro fue lavado (por John)",
                "correct_answer": "The car was washed by John",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Passive Voice",
                "exercise_type": "fill_blank",
                "instruction": "Completa en voz pasiva:",
                "prompt": "The book ___ (write) by the author.",
                "correct_answer": "was written",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "Passive Voice",
                "exercise_type": "build",
                "instruction": "Construye una oración pasiva sobre contaminación:",
                "prompt": "Plástico encontrado en todas partes",
                "correct_answer": "Plastic is found everywhere",
                "alternative_answers": [
                    "Plastic is found all over the world"
                ],
                "difficulty": "beginner"
            },
            {
                "grammar_focus": "Passive Voice",
                "exercise_type": "build",
                "instruction": "Convierte a voz pasiva:",
                "prompt": "People recycle bottles every day.",
                "correct_answer": "Bottles are recycled every day",
                "alternative_answers": [
                    "Bottles are recycled daily"
                ],
                "difficulty": "intermediate"
            },
        ]
        
        # Unit 12 - CITIES (Mix review)
        unit12 = Unit.query.filter_by(unit_number=12).first()
        unit12_exercises = [
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Construye una oración describiendo tu ciudad:",
                "prompt": "Usa comparativos o superlativos",
                "correct_answer": "My city is bigger than yours",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Describe algo que solías hacer en tu ciudad:",
                "prompt": "Usa 'used to'",
                "correct_answer": "I used to walk in the park",
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Expresa una situación hipotética sobre ciudades:",
                "prompt": "Usa Second Conditional",
                "correct_answer": "If I lived in a big city I would use public transport",
                "difficulty": "advanced"
            },
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Construye una oración sobre inmigración en voz pasiva:",
                "prompt": "Muchas personas afectadas",
                "correct_answer": "Many people are affected by immigration",
                "alternative_answers": [
                    "Many people are affected by migration"
                ],
                "difficulty": "advanced"
            },
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Usa un comparativo para describir tu barrio:",
                "prompt": "Más tranquilo que el centro",
                "correct_answer": "My neighborhood is quieter than downtown",
                "alternative_answers": [
                    "My neighborhood is quieter than the city center"
                ],
                "difficulty": "intermediate"
            },
            {
                "grammar_focus": "General Review",
                "exercise_type": "build",
                "instruction": "Usa 'used to' para hablar de tu comunidad:",
                "prompt": "Antes era más pequeña",
                "correct_answer": "My community used to be smaller",
                "alternative_answers": [
                    "My town used to be smaller"
                ],
                "difficulty": "intermediate"
            },
        ]
        
        # Diccionario de ejercicios por unidad
        exercises_by_unit = {
            unit7: unit7_exercises,
            unit8: unit8_exercises,
            unit9: unit9_exercises,
            unit10: unit10_exercises,
            unit11: unit11_exercises,
            unit12: unit12_exercises,
        }
        
        # Agregar ejercicios
        for unit, exercises_list in exercises_by_unit.items():
            if unit:
                for idx, ex_data in enumerate(exercises_list, start=1):
                    # Verificar si el ejercicio ya existe
                    existing = SentenceExercise.query.filter_by(
                        unit_id=unit.id,
                        prompt=ex_data.get("prompt", "")
                    ).first()
                    
                    if not existing:
                        exercise = SentenceExercise(
                            unit_id=unit.id,
                            grammar_focus=ex_data["grammar_focus"],
                            exercise_type=ex_data["exercise_type"],
                            instruction=ex_data["instruction"],
                            prompt=ex_data.get("prompt"),
                            correct_answer=ex_data["correct_answer"],
                            alternative_answers=ex_data.get("alternative_answers", []),
                            options=ex_data.get("options"),
                            difficulty=ex_data.get("difficulty", "beginner"),
                            order=idx,
                            is_active=True
                        )
                        db.session.add(exercise)
                        print(f"✓ Ejercicio agregado: {ex_data['grammar_focus']} - Unit {unit.unit_number}")
                    else:
                        print(f"- Ejercicio ya existe: {ex_data['grammar_focus']} - Unit {unit.unit_number}")
                        
        db.session.commit()
        
        print("\n" + "=" * 70)
        print("✅ ¡EJERCICIOS DE ORACIONES AGREGADOS EXITOSAMENTE!")
        print("=" * 70)

if __name__ == "__main__":
    add_sentence_exercises()
