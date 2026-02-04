#!/usr/bin/env python
"""
Script para poblar los desafíos de unidades con preguntas variadas.
Cada desafío tiene preguntas de gramática, vocabulario y comprensión.
"""

from app import create_app
from app.extensions import db
from app.models import Unit, UnitChallenge, ChallengeQuestion, GrammarRule, VocabularyCategory

def create_challenges():
    """Crear desafíos para todas las unidades"""
    app = create_app()
    
    with app.app_context():
        # Crear tablas si no existen
        db.create_all()
        
        units = Unit.query.order_by(Unit.unit_number).all()
        
        print("=" * 60)
        print("🎯 CREANDO DESAFÍOS DE UNIDADES")
        print("=" * 60)
        
        for unit in units:
            # Verificar si ya existe un desafío
            existing = UnitChallenge.query.filter_by(unit_id=unit.id).first()
            if existing:
                print(f"⏭️  Unit {unit.unit_number}: ya tiene desafío")
                continue
            
            # Crear el desafío
            challenge = UnitChallenge(
                unit_id=unit.id,
                title=f"Desafío de {unit.title}",
                description=f"Demuestra tu conocimiento de la Unidad {unit.unit_number}. Necesitas al menos 70% para aprobar.",
                passing_score=70.0,
                time_limit=20,  # 20 minutos
                max_attempts=3
            )
            db.session.add(challenge)
            db.session.flush()  # Para obtener el ID
            
            # Crear preguntas basadas en el nivel
            questions = generate_questions_for_unit(unit, challenge.id)
            
            for q in questions:
                db.session.add(q)
            
            print(f"✅ Unit {unit.unit_number}: {len(questions)} preguntas creadas")
        
        db.session.commit()
        
        print("\n" + "=" * 60)
        print("✅ DESAFÍOS CREADOS EXITOSAMENTE")
        print("=" * 60)


def generate_questions_for_unit(unit, challenge_id):
    """Generar preguntas variadas para una unidad"""
    questions = []
    order = 1
    
    # Determinar nivel basado en el número de unidad
    if unit.unit_number <= 12:
        level = 'A1'
        difficulty = 'easy'
    elif unit.unit_number <= 24:
        level = 'A2'
        difficulty = 'easy'
    elif unit.unit_number <= 36:
        level = 'B1'
        difficulty = 'medium'
    elif unit.unit_number <= 48:
        level = 'B2'
        difficulty = 'medium'
    elif unit.unit_number <= 60:
        level = 'C1'
        difficulty = 'hard'
    else:
        level = 'C2'
        difficulty = 'hard'
    
    # Obtener reglas gramaticales de la unidad
    grammar_rules = GrammarRule.query.filter_by(unit_id=unit.id).all()
    
    # Obtener categorías de vocabulario
    vocab_categories = VocabularyCategory.query.filter_by(unit_id=unit.id).all()
    
    # Banco de preguntas por nivel
    question_bank = get_question_bank(level, unit.unit_number)
    
    for q_data in question_bank:
        question = ChallengeQuestion(
            challenge_id=challenge_id,
            question_type=q_data['type'],
            question_text=q_data['question'],
            correct_answer=q_data['answer'],
            options=q_data.get('options'),
            explanation=q_data.get('explanation', ''),
            points=q_data.get('points', 10),
            difficulty=q_data.get('difficulty', difficulty),
            skill_tested=q_data.get('skill', 'grammar'),
            order=order
        )
        questions.append(question)
        order += 1
    
    return questions


def get_question_bank(level, unit_number):
    """Obtener banco de preguntas según el nivel"""
    
    # Preguntas específicas por unidad para hacerlas más relevantes
    question_banks = {
        # A1 - Beginner (Units 1-12)
        1: [  # Hello! Nice to Meet You
            {
                'type': 'multiple_choice',
                'question': 'Complete: "Hello, my name _____ Maria."',
                'answer': 'is',
                'options': ['is', 'am', 'are', 'be'],
                'explanation': 'Usamos "is" con tercera persona singular (my name).',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': 'What is the correct greeting for the morning?',
                'answer': 'Good morning',
                'options': ['Good morning', 'Good evening', 'Good night', 'Good afternoon'],
                'explanation': 'Good morning se usa antes del mediodía.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'Complete: "Nice to _____ you!"',
                'answer': 'meet',
                'explanation': '"Nice to meet you" es una expresión común para conocer a alguien.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"I _____ from Mexico."',
                'answer': 'am',
                'options': ['am', 'is', 'are', 'be'],
                'explanation': 'Usamos "am" con "I".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "¿Cómo te llamas?"',
                'answer': 'What is your name?|What\'s your name?',
                'explanation': '"What is your name?" es la forma correcta de preguntar el nombre.',
                'skill': 'translation',
                'points': 15
            }
        ],
        2: [  # My Family
            {
                'type': 'multiple_choice',
                'question': 'My mother\'s mother is my _____.',
                'answer': 'grandmother',
                'options': ['grandmother', 'aunt', 'sister', 'cousin'],
                'explanation': 'Grandmother = abuela (madre de tu madre o padre).',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"She _____ two brothers."',
                'answer': 'has',
                'options': ['has', 'have', 'is', 'are'],
                'explanation': 'Con tercera persona singular (she) usamos "has".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'My father\'s sister is my _____.',
                'answer': 'aunt',
                'explanation': 'Aunt = tía (hermana de tu padre o madre).',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"_____ they your parents?"',
                'answer': 'Are',
                'options': ['Are', 'Is', 'Do', 'Does'],
                'explanation': 'Usamos "Are" para preguntas con "they".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Tengo dos hermanos."',
                'answer': 'I have two brothers.|I\'ve got two brothers.',
                'explanation': '"I have" es la forma de indicar posesión.',
                'skill': 'translation',
                'points': 15
            }
        ],
        3: [  # My Home
            {
                'type': 'multiple_choice',
                'question': 'Where do you sleep?',
                'answer': 'In the bedroom',
                'options': ['In the bedroom', 'In the kitchen', 'In the bathroom', 'In the living room'],
                'explanation': 'Bedroom = dormitorio, donde dormimos.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"There _____ a table in the kitchen."',
                'answer': 'is',
                'options': ['is', 'are', 'be', 'have'],
                'explanation': 'Usamos "There is" con sustantivos singulares.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'I cook food in the _____.',
                'answer': 'kitchen',
                'explanation': 'Kitchen = cocina, donde cocinamos.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"There _____ three chairs."',
                'answer': 'are',
                'options': ['are', 'is', 'be', 'have'],
                'explanation': 'Usamos "There are" con sustantivos plurales.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Hay un sofá en la sala."',
                'answer': 'There is a sofa in the living room.|There\'s a sofa in the living room.',
                'explanation': '"There is" se usa para indicar existencia de algo.',
                'skill': 'translation',
                'points': 15
            }
        ],
        4: [  # Daily Routine
            {
                'type': 'multiple_choice',
                'question': 'What time do you usually wake up?',
                'answer': 'At 7 o\'clock',
                'options': ['At 7 o\'clock', 'On 7 o\'clock', 'In 7 o\'clock', 'By 7 o\'clock'],
                'explanation': 'Usamos "at" con horas específicas.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"She _____ breakfast at 8 AM."',
                'answer': 'has',
                'options': ['has', 'have', 'eat', 'is'],
                'explanation': 'Con tercera persona singular usamos "has" (have breakfast).',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'I _____ my teeth every morning.',
                'answer': 'brush',
                'explanation': 'Brush my teeth = cepillarme los dientes.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"He _____ to work by bus."',
                'answer': 'goes',
                'options': ['goes', 'go', 'going', 'gone'],
                'explanation': 'Con tercera persona singular (he) añadimos -es a "go".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Me despierto a las 6 de la mañana."',
                'answer': 'I wake up at 6 in the morning.|I wake up at 6 AM.|I get up at 6 in the morning.',
                'explanation': '"Wake up" significa despertarse.',
                'skill': 'translation',
                'points': 15
            }
        ],
        5: [  # Food and Drinks
            {
                'type': 'multiple_choice',
                'question': 'Which is a vegetable?',
                'answer': 'Carrot',
                'options': ['Carrot', 'Apple', 'Chicken', 'Bread'],
                'explanation': 'Carrot (zanahoria) es un vegetal.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"I would like _____ coffee, please."',
                'answer': 'some',
                'options': ['some', 'a', 'an', 'many'],
                'explanation': 'Usamos "some" con sustantivos incontables como coffee.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'I drink _____ in the morning (hot drink with milk).',
                'answer': 'coffee|tea',
                'explanation': 'Coffee y tea son bebidas calientes populares en la mañana.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"Do you like _____?"',
                'answer': 'pizza',
                'options': ['pizza', 'a pizza', 'the pizza', 'pizzas'],
                'explanation': 'Con "Do you like" usamos el sustantivo en general sin artículo.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "¿Quieres un poco de agua?"',
                'answer': 'Do you want some water?|Would you like some water?',
                'explanation': '"Some water" se usa para ofrecer agua.',
                'skill': 'translation',
                'points': 15
            }
        ]
    }
    
    # Si no hay preguntas específicas, usar preguntas genéricas del nivel
    if unit_number not in question_banks:
        return get_generic_questions(level, unit_number)
    
    return question_banks[unit_number]


def get_generic_questions(level, unit_number):
    """Preguntas genéricas cuando no hay específicas para la unidad"""
    
    generic_banks = {
        'A1': [
            {
                'type': 'multiple_choice',
                'question': '"She _____ a student."',
                'answer': 'is',
                'options': ['is', 'am', 'are', 'be'],
                'explanation': 'Usamos "is" con tercera persona singular.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"_____ you like coffee?"',
                'answer': 'Do',
                'options': ['Do', 'Does', 'Are', 'Is'],
                'explanation': 'Usamos "Do" para preguntas con "you".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'The opposite of "big" is _____.',
                'answer': 'small|little',
                'explanation': 'Small/little son antónimos de big.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"I _____ to school every day."',
                'answer': 'go',
                'options': ['go', 'goes', 'going', 'went'],
                'explanation': 'Con "I" usamos la forma base del verbo.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Ella tiene un gato."',
                'answer': 'She has a cat.|She\'s got a cat.',
                'explanation': '"Has" se usa con tercera persona singular.',
                'skill': 'translation',
                'points': 15
            }
        ],
        'A2': [
            {
                'type': 'multiple_choice',
                'question': '"I _____ to Paris last year."',
                'answer': 'went',
                'options': ['went', 'go', 'gone', 'going'],
                'explanation': '"Went" es el pasado de "go".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"She is _____ than her brother."',
                'answer': 'taller',
                'options': ['taller', 'more tall', 'tallest', 'tall'],
                'explanation': 'Usamos -er para comparativos de adjetivos cortos.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'I _____ TV last night for 2 hours.',
                'answer': 'watched',
                'explanation': 'Watch → watched (pasado regular).',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"_____ you ever been to London?"',
                'answer': 'Have',
                'options': ['Have', 'Did', 'Were', 'Are'],
                'explanation': 'Present Perfect: Have + you + ever + past participle.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Ayer fui al cine."',
                'answer': 'Yesterday I went to the cinema.|I went to the cinema yesterday.|I went to the movies yesterday.',
                'explanation': 'Pasado simple de "go" es "went".',
                'skill': 'translation',
                'points': 15
            }
        ],
        'B1': [
            {
                'type': 'multiple_choice',
                'question': '"If I _____ rich, I would travel the world."',
                'answer': 'were',
                'options': ['were', 'am', 'was', 'be'],
                'explanation': 'En el segundo condicional usamos "were" para todas las personas.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"She said she _____ come tomorrow."',
                'answer': 'would',
                'options': ['would', 'will', 'can', 'is'],
                'explanation': 'En reported speech, "will" cambia a "would".',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'I wish I _____ speak French fluently.',
                'answer': 'could',
                'explanation': 'Wish + could para deseos sobre habilidades.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"The book _____ by millions of people."',
                'answer': 'has been read',
                'options': ['has been read', 'has read', 'is reading', 'reads'],
                'explanation': 'Voz pasiva: has been + past participle.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Si tuviera más tiempo, estudiaría más."',
                'answer': 'If I had more time, I would study more.|If I had more time, I\'d study more.',
                'explanation': 'Segundo condicional: If + past simple, would + verb.',
                'skill': 'translation',
                'points': 15
            }
        ],
        'B2': [
            {
                'type': 'multiple_choice',
                'question': '"By the time she arrives, we _____ dinner."',
                'answer': 'will have finished',
                'options': ['will have finished', 'will finish', 'finished', 'have finished'],
                'explanation': 'Future Perfect: will have + past participle.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"I wish I _____ that mistake."',
                'answer': 'hadn\'t made',
                'options': ['hadn\'t made', 'didn\'t make', 'don\'t make', 'won\'t make'],
                'explanation': 'Wish + past perfect para arrepentimientos del pasado.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'He _____ to tell her the truth, but he was too scared.',
                'answer': 'ought|should have',
                'explanation': 'Ought to / should have indica obligación moral pasada.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"_____ having worked all day, she wasn\'t tired."',
                'answer': 'Despite',
                'options': ['Despite', 'Although', 'However', 'Because'],
                'explanation': 'Despite + gerund para contrastar ideas.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "No solo estudia, sino que también trabaja."',
                'answer': 'Not only does she study, but she also works.|She not only studies but also works.',
                'explanation': 'Not only... but also para énfasis.',
                'skill': 'translation',
                'points': 15
            }
        ],
        'C1': [
            {
                'type': 'multiple_choice',
                'question': '"_____ she known about the problem, she would have acted differently."',
                'answer': 'Had',
                'options': ['Had', 'If', 'Would', 'Should'],
                'explanation': 'Inversión en tercer condicional: Had + subject...',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"It\'s high time you _____ looking for a job."',
                'answer': 'started',
                'options': ['started', 'start', 'would start', 'have started'],
                'explanation': 'It\'s high time + past simple para expresar urgencia.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'The proposal was rejected, _____ surprised everyone.',
                'answer': 'which',
                'explanation': 'Which se refiere a toda la cláusula anterior.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"_____ no circumstances should you reveal this information."',
                'answer': 'Under',
                'options': ['Under', 'In', 'At', 'By'],
                'explanation': 'Under no circumstances = nunca, bajo ninguna circunstancia.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "De haber sabido, habría venido antes."',
                'answer': 'Had I known, I would have come earlier.|If I had known, I would have come earlier.',
                'explanation': 'Tercer condicional con inversión o forma estándar.',
                'skill': 'translation',
                'points': 15
            }
        ],
        'C2': [
            {
                'type': 'multiple_choice',
                'question': '"_____ it not for his support, I would have failed."',
                'answer': 'Were',
                'options': ['Were', 'Was', 'If', 'Should'],
                'explanation': 'Were it not for = Si no fuera por (formal/literario).',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': '"He speaks as _____ he were an expert."',
                'answer': 'though',
                'options': ['though', 'if', 'when', 'while'],
                'explanation': 'As though/as if + subjuntivo para situaciones hipotéticas.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'fill_blank',
                'question': 'Her argument, _____ cogent, failed to convince the jury.',
                'answer': 'however|though',
                'explanation': 'However/though como concesión formal.',
                'skill': 'grammar',
                'points': 10
            },
            {
                'type': 'multiple_choice',
                'question': 'Which word means "extremely angry"?',
                'answer': 'Furious',
                'options': ['Furious', 'Annoyed', 'Upset', 'Frustrated'],
                'explanation': 'Furious = extremadamente enojado.',
                'skill': 'vocabulary',
                'points': 10
            },
            {
                'type': 'translation',
                'question': 'Translate: "Por muy inteligente que sea, comete errores."',
                'answer': 'However intelligent he may be, he makes mistakes.|No matter how intelligent he is, he makes mistakes.',
                'explanation': 'However + adjective o No matter how para concesión.',
                'skill': 'translation',
                'points': 15
            }
        ]
    }
    
    return generic_banks.get(level, generic_banks['A1'])


if __name__ == '__main__':
    create_challenges()
