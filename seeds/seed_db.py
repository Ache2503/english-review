from app import create_app, db
from app.models import Unit, Topic, GrammarRule, VocabularyCategory, VocabularyItem, WritingPractice, UnitExtra, Quiz, QuizQuestion, QuizOption
import json
import os

app = create_app('development')

# Datos de las unidades desde tu contexto (fallback si no existe seeds/units_data.json)
UNITS_DATA_FALLBACK = [
    {
        "unit_number": 7,
        "title": "MIND (La Mente)",
        "topics": ["Felicidad", "Internet y el cerebro", "Inteligencia"],
        "grammar": [
            {
                "topic": "Articles (a/an/the/no article)",
                "rule": "Cuándo usar 'the' y cuándo no. (Ej: I go to school = soy estudiante; I go to the school = voy al edificio)."
            },
            {
                "topic": "Used to",
                "rule": "Para hábitos en el pasado que ya no ocurren (I used to sleep late)."
            }
        ],
        "vocabulary_categories": ["Sentimientos", "Verbos frasales (phrasal verbs)"],
        "practice_writing": "In the past, I used to think that money was the only way to find happiness. I felt an emptiness inside. However, I read an article about the human brain and realized that simple things matter. Now, I focus on positive feelings. Going to school (para estudiar) helps me keep my mind active, but going to the school (el edificio) just to meet friends makes me even happier."
    },
    {
        "unit_number": 8,
        "title": "ART (Arte)",
        "topics": ["Gustos musicales", "Arte inusual", "Películas y libros"],
        "grammar": [
            {
                "topic": "Reflexive Pronouns",
                "rule": "(myself, yourself, himself). Cuando el sujeto y el objeto son el mismo."
            },
            {
                "topic": "Infinitive of Purpose",
                "rule": "Usar 'to' para explicar para qué haces algo (I went to the gallery to see art)."
            },
            {
                "topic": "First Conditional",
                "rule": "Situaciones reales y posibles (If + Present, Will + Verb)."
            }
        ],
        "vocabulary_categories": ["Géneros de música", "Cine"],
        "practice_writing": "I bought a ticket to see the new abstract art exhibition. I told myself that I needed to be open-minded. If the exhibition is interesting, I will write a review about it. I love horror movies, but this time I want to explore painting. If I learn enough, maybe I will paint something myself one day."
    },
    {
        "unit_number": 9,
        "title": "MONEY (Dinero)",
        "topics": ["Gastos", "Filantropía", "Habilidades"],
        "grammar": [
            {
                "topic": "Second Conditional",
                "rule": "Situaciones hipotéticas o imaginarias (If I had money, I would travel)."
            },
            {
                "topic": "Gerunds",
                "rule": "Verbos terminados en -ing actuando como sustantivos (Spending money is easy)."
            },
            {
                "topic": "Essential Adjective Clauses",
                "rule": "Frases con who/which/that que definen al sujeto."
            }
        ],
        "vocabulary_categories": ["Make vs Do", "Frases de dinero"],
        "practice_writing": "Spending money responsibly is difficult. If I won the lottery, I would give half to charity. There are people who need help everywhere. I want to do good things for my community, but first I need to make enough money. Bartering (intercambiar bienes) is also a good option when you don't have cash."
    },
    {
        "unit_number": 10,
        "title": "SCIENCE AND TECHNOLOGY (Ciencia y Tecnología)",
        "topics": ["Dispositivos", "Tipos de tecnología", "El espacio"],
        "grammar": [
            {
                "topic": "Comparatives & Superlatives",
                "rule": "Faster than, the most expensive."
            },
            {
                "topic": "Need to",
                "rule": "Obligación o necesidad."
            }
        ],
        "vocabulary_categories": ["Dispositivos electrónicos", "Colocaciones de ciencia"],
        "practice_writing": "My new smartphone is faster than my old tablet. It is the most useful device I own. However, technology changes quickly, so we need to update our skills constantly. Doing research on the internet is easier now than it was ten years ago. I think working in space would be the most exciting job in the world."
    },
    {
        "unit_number": 11,
        "title": "NATURAL WORLD (Mundo Natural)",
        "topics": ["Maravillas naturales", "Fotografía de vida salvaje", "Contaminación plástica"],
        "grammar": [
            {
                "topic": "Passive Voice",
                "rule": "Cuando la acción es más importante que quien la hace (Plastic is found in the ocean)."
            },
            {
                "topic": "Adjective + Infinitive",
                "rule": "It is hard to believe."
            },
            {
                "topic": "Words with -where",
                "rule": "Somewhere, nowhere, everywhere."
            }
        ],
        "vocabulary_categories": ["Animales", "Características naturales"],
        "practice_writing": "Plastic pollution is found everywhere, even in the deepest oceans. It is sad to see animals suffering because of our waste. Many photos were taken by wildlife photographers to show this problem. We must do something before there is nowhere safe for these animals to live. It is important to protect our natural wonders."
    },
    {
        "unit_number": 12,
        "title": "MEDIA (Medios de Comunicación)",
        "topics": ["Noticias online", "Hábitos de TV", "Publicidad"],
        "grammar": [
            {
                "topic": "Reported Speech",
                "rule": "Contar lo que otro dijo. (Directo: 'I like TV' -> Indirecto: He said he liked TV)."
            },
            {
                "topic": "Past Perfect",
                "rule": "Una acción en el pasado que ocurrió antes que otra (When I turned on the TV, the show had already started)."
            },
            {
                "topic": "Should",
                "rule": "Recomendaciones."
            }
        ],
        "vocabulary_categories": ["Expresiones de noticias", "Publicidad"],
        "practice_writing": "The journalist said that fake news had become a big problem. He told us that we should check the sources before sharing. Last night, I wanted to watch the news, but when I arrived home, the program had finished. So, I watched a documentary about advertising instead. People say that binge-watching TV series is addictive."
    }
]

def load_units_data() -> list:
    here = os.path.dirname(os.path.abspath(__file__))
    # Preferir el nuevo esquema: unit_data.json
    preferred_path = os.path.join(here, 'unit_data.json')
    legacy_path = os.path.join(here, 'units_data.json')
    for data_path in (preferred_path, legacy_path):
        if os.path.exists(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
                print(f"Cargando datos desde {data_path}...")
                return json.load(f)
    print("Usando datos embebidos de fallback...")
    return UNITS_DATA_FALLBACK

def seed_database(clean=True):
    """Cargar datos iniciales en la base de datos
    
    Args:
        clean: Si True, limpia la base de datos antes de cargar. 
               Si False, solo agrega datos que no existen.
    """
    with app.app_context():
        if clean:
            # Limpiar datos existentes
            print("Limpiando base de datos...")
            db.drop_all()
            db.create_all()
            db.session.commit()
        else:
            # Solo crear tablas si no existen
            print("Verificando estructura de tablas...")
            db.create_all()
            db.session.commit()
            
        print("Cargando unidades...")
        units_data = load_units_data()
        for unit_data in units_data:
            # Crear unidad
            unit = Unit(
                unit_number=unit_data['unit_number'],
                title=unit_data['title'],
                description=f"Unit {unit_data['unit_number']}: {unit_data['title']}"
            )
            db.session.add(unit)
            db.session.flush()
            
            # Agregar tópicos
            for idx, topic_title in enumerate(unit_data['topics']):
                topic = Topic(
                    unit_id=unit.id,
                    title=topic_title,
                    order=idx
                )
                db.session.add(topic)
            
            # Agregar reglas gramaticales (soporta 'topic' o 'title')
            for idx, grammar in enumerate(unit_data['grammar']):
                rule = GrammarRule(
                    unit_id=unit.id,
                    topic=grammar.get('topic') or grammar.get('title', ''),
                    rule=grammar.get('rule', ''),
                    example=grammar.get('example', ''),
                    order=idx
                )
                db.session.add(rule)
            
            # Agregar categorías de vocabulario (soporta 'vocabulary_categories' o 'vocabulary')
            vocab_source = unit_data.get('vocabulary_categories') or unit_data.get('vocabulary') or []
            for idx, vocab_cat in enumerate(vocab_source):
                vocab_category = VocabularyCategory(
                    unit_id=unit.id,
                    category_name=vocab_cat,
                    order=idx
                )
                db.session.add(vocab_category)
            
            # Agregar ejercicio de escritura
            # Agregar ejercicio de escritura (acepta dict o string)
            pw_raw = unit_data.get('practice_writing', {})
            if isinstance(pw_raw, dict):
                instructions = pw_raw.get('instructions', "Escribe un párrafo de práctica.")
                example = pw_raw.get('example_text', '')
            else:
                instructions = "Escribe un párrafo de práctica."
                example = pw_raw if isinstance(pw_raw, str) else ''
            writing = WritingPractice(
                unit_id=unit.id,
                title=f"Writing Practice - Unit {unit_data['unit_number']}",
                instructions=instructions,
                example_text=example,
                difficulty='intermediate',
                order=0
            )
            db.session.add(writing)
            
            print(f"✓ Unit {unit_data['unit_number']}: {unit_data['title']}")

            # Guardar actividades/tips/prompts en UnitExtra (JSON)
            # Guardar actividades/tips/prompts en UnitExtra (JSON)
            extras = {}
            for key in ('activities', 'tips', 'prompts'):
                if key in unit_data and unit_data[key]:
                    extras[key] = unit_data[key]
            if extras:
                extra = UnitExtra(unit_id=unit.id, data=extras)
                db.session.add(extra)

            # Create a simple grammar quiz per unit
            quiz = Quiz(
                unit_id=unit.id,
                title=f"Grammar Check - Unit {unit_data['unit_number']}",
                description="Quiz sobre gramática clave de la unidad"
            )
            db.session.add(quiz)
            db.session.flush()

            # Define 2-3 questions per unit based on grammar topics
            # Q1: Identify correct form/pattern
            g1_topic = unit_data['grammar'][0].get('topic') or unit_data['grammar'][0].get('title', '')
            q1 = QuizQuestion(quiz_id=quiz.id, prompt=f"Selecciona la opción que mejor aplica a: {g1_topic}", order=1)
            db.session.add(q1)
            db.session.flush()
            db.session.add_all([
                QuizOption(question_id=q1.id, text="I go to school to study.", is_correct=True, order=1),
                QuizOption(question_id=q1.id, text="I go to the school to be student.", is_correct=False, order=2),
                QuizOption(question_id=q1.id, text="I go school the.", is_correct=False, order=3),
            ])

            # Q2: Another grammar topic if present
            if len(unit_data['grammar']) > 1:
                g2 = unit_data['grammar'][1].get('topic') or unit_data['grammar'][1].get('title', '')
                q2 = QuizQuestion(quiz_id=quiz.id, prompt=f"Elige la oración correcta usando: {g2}", order=2)
                db.session.add(q2)
                db.session.flush()
                if unit_data['unit_number'] == 8:
                    db.session.add_all([
                        QuizOption(question_id=q2.id, text="I told myself to be open-minded.", is_correct=True, order=1),
                        QuizOption(question_id=q2.id, text="I told me to be open-minded.", is_correct=False, order=2),
                        QuizOption(question_id=q2.id, text="I told myself be open-minded.", is_correct=False, order=3),
                    ])
                elif unit_data['unit_number'] == 9:
                    db.session.add_all([
                        QuizOption(question_id=q2.id, text="If I had more time, I would volunteer.", is_correct=True, order=1),
                        QuizOption(question_id=q2.id, text="If I have more time, I would volunteer.", is_correct=False, order=2),
                        QuizOption(question_id=q2.id, text="If I had more time, I will volunteer.", is_correct=False, order=3),
                    ])
                elif unit_data['unit_number'] == 10:
                    db.session.add_all([
                        QuizOption(question_id=q2.id, text="This laptop is more powerful than my phone.", is_correct=True, order=1),
                        QuizOption(question_id=q2.id, text="This laptop is powerfull than my phone.", is_correct=False, order=2),
                        QuizOption(question_id=q2.id, text="This laptop is the more powerful than my phone.", is_correct=False, order=3),
                    ])
                elif unit_data['unit_number'] == 11:
                    db.session.add_all([
                        QuizOption(question_id=q2.id, text="Plastic is found everywhere.", is_correct=True, order=1),
                        QuizOption(question_id=q2.id, text="Plastic found is everywhere.", is_correct=False, order=2),
                        QuizOption(question_id=q2.id, text="Plastic is finding everywhere.", is_correct=False, order=3),
                    ])
                elif unit_data['unit_number'] == 12:
                    db.session.add_all([
                        QuizOption(question_id=q2.id, text="He said that we should check the source.", is_correct=True, order=1),
                        QuizOption(question_id=q2.id, text="He said we should to check the source.", is_correct=False, order=2),
                        QuizOption(question_id=q2.id, text="He told that we should check the source.", is_correct=False, order=3),
                    ])
        
        db.session.commit()
        print("\n✓ Base de datos cargada exitosamente!")

if __name__ == '__main__':
    import sys
    clean = '--no-clean' not in sys.argv
    if not clean:
        print("Modo --no-clean: No se eliminarán datos existentes")
    seed_database(clean=clean)
