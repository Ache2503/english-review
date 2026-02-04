from flask import Blueprint, render_template, abort, request, session, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import UserSentence, SentenceLike, Verb, GrammarExerciseResult
from datetime import datetime
from sqlalchemy import func
import random

grammar_bp = Blueprint('grammar', __name__, url_prefix='/grammar')

# ============================================================================
# BASE DE DATOS DE TEMAS GRAMATICALES
# ============================================================================

grammar_topics = {
    # =========================================================================
    # NIVEL BÁSICO - BEGINNER
    # =========================================================================
    'verb-to-be': {
        'title': 'The Verb "To Be"',
        'subtitle': 'El verbo más importante del inglés',
        'icon': '🔵',
        'level': 'Beginner',
        'category': 'Verbs',
        'description': 'Aprende a usar el verbo TO BE para describir personas, lugares y cosas.',
        'estimated_time': '15 min',
        'sections': [
            {
                'title': '¿Qué es el verbo TO BE?',
                'type': 'explanation',
                'content': '''
                    El verbo <strong>TO BE</strong> significa "ser" o "estar" en español. 
                    Es el verbo más usado en inglés y se usa para:
                    <ul>
                        <li>Describir personas y cosas</li>
                        <li>Hablar de profesiones</li>
                        <li>Indicar ubicación</li>
                        <li>Expresar sentimientos</li>
                        <li>Hablar de la edad</li>
                    </ul>
                '''
            },
            {
                'title': 'Conjugación en Presente',
                'type': 'table',
                'headers': ['Pronombre', 'Verbo', 'Contracción', 'Ejemplo'],
                'rows': [
                    ['I', 'am', "I'm", "I'm a student. (Soy estudiante)"],
                    ['You', 'are', "You're", "You're smart. (Eres inteligente)"],
                    ['He', 'is', "He's", "He's tall. (Él es alto)"],
                    ['She', 'is', "She's", "She's a doctor. (Ella es doctora)"],
                    ['It', 'is', "It's", "It's hot. (Está caliente)"],
                    ['We', 'are', "We're", "We're friends. (Somos amigos)"],
                    ['They', 'are', "They're", "They're happy. (Ellos están felices)"],
                ],
                'highlight_column': 1
            },
            {
                'title': 'Forma Negativa',
                'type': 'table',
                'headers': ['Afirmativo', 'Negativo', 'Contracción', 'Ejemplo'],
                'rows': [
                    ['I am', 'I am not', "I'm not", "I'm not tired. (No estoy cansado)"],
                    ['You are', 'You are not', "You aren't / You're not", "You aren't late. (No llegas tarde)"],
                    ['He is', 'He is not', "He isn't / He's not", "He isn't here. (Él no está aquí)"],
                    ['She is', 'She is not', "She isn't / She's not", "She isn't sad. (Ella no está triste)"],
                    ['It is', 'It is not', "It isn't / It's not", "It isn't cold. (No está frío)"],
                    ['We are', 'We are not', "We aren't / We're not", "We aren't ready. (No estamos listos)"],
                    ['They are', 'They are not', "They aren't / They're not", "They aren't home. (No están en casa)"],
                ],
                'highlight_column': 2
            },
            {
                'title': 'Forma Interrogativa',
                'type': 'table',
                'headers': ['Pregunta', 'Respuesta Corta (+)', 'Respuesta Corta (-)'],
                'rows': [
                    ['Am I late?', 'Yes, you are.', 'No, you aren\'t.'],
                    ['Are you ready?', 'Yes, I am.', 'No, I\'m not.'],
                    ['Is he a teacher?', 'Yes, he is.', 'No, he isn\'t.'],
                    ['Is she happy?', 'Yes, she is.', 'No, she isn\'t.'],
                    ['Is it expensive?', 'Yes, it is.', 'No, it isn\'t.'],
                    ['Are we late?', 'Yes, we are.', 'No, we aren\'t.'],
                    ['Are they students?', 'Yes, they are.', 'No, they aren\'t.'],
                ],
                'note': '💡 En las preguntas, el verbo TO BE va al inicio de la oración.'
            },
            {
                'title': 'Usos Comunes',
                'type': 'examples',
                'examples': [
                    {'english': "I am 25 years old.", 'spanish': "Tengo 25 años.", 'note': "Edad"},
                    {'english': "She is from Mexico.", 'spanish': "Ella es de México.", 'note': "Origen"},
                    {'english': "We are at the park.", 'spanish': "Estamos en el parque.", 'note': "Ubicación"},
                    {'english': "He is a doctor.", 'spanish': "Él es doctor.", 'note': "Profesión"},
                    {'english': "It is sunny today.", 'spanish': "Está soleado hoy.", 'note': "Clima"},
                    {'english': "They are hungry.", 'spanish': "Ellos tienen hambre.", 'note': "Estado"},
                ]
            },
            {
                'title': 'Practica con Estos Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con la forma correcta de TO BE (am, is, are):',
                'questions': [
                    {'sentence': 'I ___ a student.', 'answer': 'am', 'hint': 'I + ?'},
                    {'sentence': 'She ___ very beautiful.', 'answer': 'is', 'hint': 'She + ?'},
                    {'sentence': 'We ___ friends.', 'answer': 'are', 'hint': 'We + ?'},
                    {'sentence': 'They ___ at home.', 'answer': 'are', 'hint': 'They + ?'},
                    {'sentence': 'It ___ cold today.', 'answer': 'is', 'hint': 'It + ?'},
                    {'sentence': 'You ___ my best friend.', 'answer': 'are', 'hint': 'You + ?'},
                    {'sentence': 'He ___ not here.', 'answer': 'is', 'hint': 'He + ?'},
                    {'sentence': 'I ___ not tired.', 'answer': 'am', 'hint': 'I + ?'},
                ]
            }
        ],
        'tips': [
            'Las contracciones son muy comunes en el habla informal.',
            'Recuerda: I AM es la única forma que no tiene contracción negativa con "not" (I amn\'t NO existe).',
            'En inglés, la edad se expresa con TO BE, no con "tener" como en español.',
        ],
        'common_mistakes': [
            {'wrong': 'I have 20 years old.', 'correct': 'I am 20 years old.', 'explanation': 'La edad usa TO BE, no HAVE.'},
            {'wrong': 'She is have a car.', 'correct': 'She has a car.', 'explanation': 'No se combinan TO BE y HAVE así.'},
            {'wrong': 'He is agree.', 'correct': 'He agrees.', 'explanation': 'Agree es un verbo normal, no usa TO BE.'},
        ]
    },
    
    'articles': {
        'title': 'Articles: A, An, The',
        'subtitle': 'Los artículos en inglés',
        'icon': '📝',
        'level': 'Beginner',
        'category': 'Grammar Basics',
        'description': 'Aprende cuándo usar A, AN y THE correctamente.',
        'estimated_time': '12 min',
        'sections': [
            {
                'title': '¿Qué son los artículos?',
                'type': 'explanation',
                'content': '''
                    Los artículos son palabras que van antes de los sustantivos. En inglés hay:
                    <ul>
                        <li><strong>A / AN</strong> - Artículos indefinidos (un, una)</li>
                        <li><strong>THE</strong> - Artículo definido (el, la, los, las)</li>
                    </ul>
                '''
            },
            {
                'title': 'A vs AN',
                'type': 'comparison',
                'left': {
                    'title': 'A',
                    'description': 'Se usa antes de sonidos CONSONANTES',
                    'examples': ['a book', 'a car', 'a university', 'a European'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'AN',
                    'description': 'Se usa antes de sonidos VOCALES',
                    'examples': ['an apple', 'an hour', 'an honest man', 'an umbrella'],
                    'color': 'success'
                },
                'note': '⚠️ ¡Importante! Se basa en el SONIDO, no en la letra. "Hour" empieza con sonido vocal, "University" empieza con sonido consonante.'
            },
            {
                'title': 'Cuándo usar A/AN',
                'type': 'table',
                'headers': ['Uso', 'Ejemplo', 'Explicación'],
                'rows': [
                    ['Primera mención', 'I saw a dog.', 'No sabemos qué perro específico'],
                    ['Profesiones', 'She is a teacher.', 'Siempre con profesiones'],
                    ['Uno de muchos', 'Give me a pen.', 'Cualquier pluma sirve'],
                    ['Con "what" exclamativo', 'What a beautiful day!', 'En exclamaciones'],
                    ['Frecuencia', 'twice a week', 'Significa "por" o "cada"'],
                ]
            },
            {
                'title': 'Cuándo usar THE',
                'type': 'table',
                'headers': ['Uso', 'Ejemplo', 'Explicación'],
                'rows': [
                    ['Algo específico', 'The book on the table.', 'Sabemos exactamente cuál'],
                    ['Único en el mundo', 'The sun, the moon', 'Solo hay uno'],
                    ['Segunda mención', 'I saw a dog. The dog was big.', 'Ya lo mencionamos antes'],
                    ['Superlativos', 'The best, the biggest', 'Con superlativos siempre'],
                    ['Instrumentos', 'I play the guitar.', 'Instrumentos musicales'],
                    ['Países plurales', 'The United States', 'Países con plural o "kingdom"'],
                ]
            },
            {
                'title': 'Cuándo NO usar artículos',
                'type': 'list',
                'items': [
                    {'text': 'Nombres propios', 'example': 'Maria is nice. (NO: The Maria)'},
                    {'text': 'Países singulares', 'example': 'I live in Mexico. (NO: the Mexico)'},
                    {'text': 'Comidas en general', 'example': 'I like pizza. (NO: the pizza)'},
                    {'text': 'Deportes', 'example': 'I play soccer. (NO: the soccer)'},
                    {'text': 'Idiomas', 'example': 'I speak English. (NO: the English)'},
                    {'text': 'Días y meses', 'example': 'See you on Monday. (NO: the Monday)'},
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con A, AN, THE o deja vacío (—) si no se necesita:',
                'questions': [
                    {'sentence': 'I have ___ apple.', 'answer': 'an', 'hint': 'Sonido vocal'},
                    {'sentence': 'She is ___ doctor.', 'answer': 'a', 'hint': 'Profesión'},
                    {'sentence': '___ sun is very hot today.', 'answer': 'The', 'hint': 'Único'},
                    {'sentence': 'I live in ___ Japan.', 'answer': '—', 'hint': 'País singular'},
                    {'sentence': 'I need ___ hour to finish.', 'answer': 'an', 'hint': 'Sonido de "hour"'},
                    {'sentence': 'This is ___ best movie ever!', 'answer': 'the', 'hint': 'Superlativo'},
                ]
            }
        ],
        'tips': [
            '"A" y "AN" solo se usan con sustantivos SINGULARES contables.',
            'Practica escuchando el sonido inicial de la palabra, no mirando la letra.',
            '"THE" es el mismo para singular, plural, masculino y femenino.',
        ],
        'common_mistakes': [
            {'wrong': 'I play the soccer.', 'correct': 'I play soccer.', 'explanation': 'Los deportes no llevan artículo.'},
            {'wrong': 'She is teacher.', 'correct': 'She is a teacher.', 'explanation': 'Las profesiones necesitan A/AN.'},
            {'wrong': 'I have a informations.', 'correct': 'I have information.', 'explanation': 'Information es incontable.'},
        ]
    },
    
    'present-simple': {
        'title': 'Present Simple',
        'subtitle': 'El tiempo presente simple',
        'icon': '⏰',
        'level': 'Beginner',
        'category': 'Tenses',
        'description': 'Aprende a hablar de rutinas, hábitos y verdades generales.',
        'estimated_time': '20 min',
        'sections': [
            {
                'title': '¿Cuándo se usa?',
                'type': 'explanation',
                'content': '''
                    El Present Simple se usa para:
                    <ul>
                        <li><strong>Rutinas y hábitos:</strong> I wake up at 7 AM.</li>
                        <li><strong>Verdades generales:</strong> Water boils at 100°C.</li>
                        <li><strong>Horarios fijos:</strong> The train leaves at 6 PM.</li>
                        <li><strong>Estados permanentes:</strong> She lives in New York.</li>
                        <li><strong>Gustos y preferencias:</strong> I love chocolate.</li>
                    </ul>
                '''
            },
            {
                'title': 'Conjugación Afirmativa',
                'type': 'table',
                'headers': ['Pronombre', 'Verbo', 'Ejemplo'],
                'rows': [
                    ['I', 'work', 'I work every day.'],
                    ['You', 'work', 'You work at home.'],
                    ['He', 'works ⭐', 'He works in an office.'],
                    ['She', 'works ⭐', 'She works very hard.'],
                    ['It', 'works ⭐', 'It works perfectly.'],
                    ['We', 'work', 'We work together.'],
                    ['They', 'work', 'They work on weekends.'],
                ],
                'note': '⭐ He/She/It añaden -S, -ES, o -IES al verbo.'
            },
            {
                'title': 'Reglas para He/She/It',
                'type': 'table',
                'headers': ['Regla', 'Verbo Base', 'Con He/She/It', 'Ejemplo'],
                'rows': [
                    ['Mayoría de verbos', 'work', 'works', 'She works.'],
                    ['Verbos en -s, -sh, -ch, -x, -o', 'go, watch', 'goes, watches', 'He goes. She watches.'],
                    ['Verbos en consonante + y', 'study, try', 'studies, tries', 'He studies. She tries.'],
                    ['Verbos en vocal + y', 'play, say', 'plays, says', 'He plays. She says.'],
                    ['Verbo HAVE', 'have', 'has', 'She has a car.'],
                ],
                'highlight_column': 2
            },
            {
                'title': 'Forma Negativa',
                'type': 'table',
                'headers': ['Sujeto', 'Negativo', 'Contracción', 'Ejemplo'],
                'rows': [
                    ['I / You / We / They', 'do not + verbo', "don't + verbo", "I don't like coffee."],
                    ['He / She / It', 'does not + verbo', "doesn't + verbo", "She doesn't eat meat."],
                ],
                'note': '⚠️ Con DOES, el verbo vuelve a su forma base (sin -s). She doesn\'t workS ❌ → She doesn\'t work ✅'
            },
            {
                'title': 'Forma Interrogativa',
                'type': 'table',
                'headers': ['Pregunta', 'Respuesta (+)', 'Respuesta (-)'],
                'rows': [
                    ['Do you like pizza?', 'Yes, I do.', 'No, I don\'t.'],
                    ['Do they work here?', 'Yes, they do.', 'No, they don\'t.'],
                    ['Does he speak English?', 'Yes, he does.', 'No, he doesn\'t.'],
                    ['Does she live here?', 'Yes, she does.', 'No, she doesn\'t.'],
                ],
                'note': '💡 Estructura: DO/DOES + sujeto + verbo base + ?'
            },
            {
                'title': 'Palabras Clave (Time Expressions)',
                'type': 'chips',
                'items': [
                    {'text': 'always', 'translation': 'siempre'},
                    {'text': 'usually', 'translation': 'usualmente'},
                    {'text': 'often', 'translation': 'a menudo'},
                    {'text': 'sometimes', 'translation': 'a veces'},
                    {'text': 'rarely', 'translation': 'raramente'},
                    {'text': 'never', 'translation': 'nunca'},
                    {'text': 'every day', 'translation': 'todos los días'},
                    {'text': 'once a week', 'translation': 'una vez a la semana'},
                    {'text': 'on Mondays', 'translation': 'los lunes'},
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con la forma correcta del verbo entre paréntesis:',
                'questions': [
                    {'sentence': 'She ___ (work) in a hospital.', 'answer': 'works', 'hint': 'She + -s'},
                    {'sentence': 'They ___ (play) soccer every Sunday.', 'answer': 'play', 'hint': 'They = forma base'},
                    {'sentence': 'He ___ (not/like) vegetables.', 'answer': "doesn't like", 'hint': 'He negativo'},
                    {'sentence': '___ you ___ (speak) French?', 'answer': 'Do, speak', 'hint': 'Pregunta con you'},
                    {'sentence': 'The store ___ (close) at 9 PM.', 'answer': 'closes', 'hint': 'It + -s'},
                    {'sentence': 'I always ___ (drink) coffee in the morning.', 'answer': 'drink', 'hint': 'I = forma base'},
                ]
            }
        ],
        'tips': [
            'Los adverbios de frecuencia van ANTES del verbo principal pero DESPUÉS de TO BE.',
            'Recuerda: después de DOES (negativo o pregunta), el verbo NO lleva -s.',
            'El Present Simple NO se usa para acciones que están pasando ahora mismo.',
        ],
        'common_mistakes': [
            {'wrong': 'She work every day.', 'correct': 'She works every day.', 'explanation': 'He/She/It necesita -s.'},
            {'wrong': 'He doesn\'t works here.', 'correct': 'He doesn\'t work here.', 'explanation': 'Con DOES, el verbo es base.'},
            {'wrong': 'I am work now.', 'correct': 'I am working now.', 'explanation': 'Para ahora mismo, usa Present Continuous.'},
        ]
    },
    
    'possessives': {
        'title': 'Possessive Adjectives & Pronouns',
        'subtitle': 'Adjetivos y pronombres posesivos',
        'icon': '👤',
        'level': 'Beginner',
        'category': 'Pronouns',
        'description': 'Aprende a expresar posesión y pertenencia en inglés.',
        'estimated_time': '10 min',
        'sections': [
            {
                'title': 'Adjetivos Posesivos',
                'type': 'table',
                'headers': ['Pronombre', 'Adjetivo Posesivo', 'Ejemplo', 'Traducción'],
                'rows': [
                    ['I', 'my', 'This is my book.', 'Este es mi libro.'],
                    ['You', 'your', 'Is this your car?', '¿Es este tu carro?'],
                    ['He', 'his', 'His name is John.', 'Su nombre es John.'],
                    ['She', 'her', 'Her house is big.', 'Su casa es grande.'],
                    ['It', 'its', 'The cat licks its paw.', 'El gato lame su pata.'],
                    ['We', 'our', 'This is our classroom.', 'Este es nuestro salón.'],
                    ['They', 'their', 'Their children are smart.', 'Sus hijos son inteligentes.'],
                ],
                'note': '💡 Los adjetivos posesivos siempre van ANTES del sustantivo.'
            },
            {
                'title': 'Pronombres Posesivos',
                'type': 'table',
                'headers': ['Adjetivo', 'Pronombre', 'Ejemplo', 'Traducción'],
                'rows': [
                    ['my', 'mine', 'This book is mine.', 'Este libro es mío.'],
                    ['your', 'yours', 'Is this car yours?', '¿Es este carro tuyo?'],
                    ['his', 'his', 'The blue one is his.', 'El azul es suyo (de él).'],
                    ['her', 'hers', 'The bag is hers.', 'La bolsa es suya (de ella).'],
                    ['its', '—', '(no se usa)', '—'],
                    ['our', 'ours', 'The house is ours.', 'La casa es nuestra.'],
                    ['their', 'theirs', 'The dog is theirs.', 'El perro es de ellos.'],
                ],
                'note': '💡 Los pronombres posesivos reemplazan al sustantivo. Van SOLOS, sin sustantivo después.'
            },
            {
                'title': 'Diferencia Clave',
                'type': 'comparison',
                'left': {
                    'title': 'Adjetivo Posesivo',
                    'description': 'VA ANTES del sustantivo',
                    'examples': ['This is MY car.', 'I like YOUR house.', 'HIS phone is new.'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'Pronombre Posesivo',
                    'description': 'REEMPLAZA al sustantivo',
                    'examples': ['This car is MINE.', 'The big house is YOURS.', 'The new phone is HIS.'],
                    'color': 'success'
                }
            },
            {
                'title': 'Its vs It\'s',
                'type': 'comparison',
                'left': {
                    'title': 'ITS (sin apóstrofe)',
                    'description': 'Posesivo de "it"',
                    'examples': ['The dog wagged its tail.', 'The company changed its name.'],
                    'color': 'warning'
                },
                'right': {
                    'title': "IT'S (con apóstrofe)",
                    'description': 'Contracción de "it is"',
                    'examples': ["It's raining.", "It's a beautiful day."],
                    'color': 'danger'
                },
                'note': '⚠️ Este es un error muy común. Recuerda: ITS = posesivo, IT\'S = it is'
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con el posesivo correcto:',
                'questions': [
                    {'sentence': 'I love ___ family. (my/mine)', 'answer': 'my', 'hint': 'Antes de sustantivo'},
                    {'sentence': 'This phone is ___. (her/hers)', 'answer': 'hers', 'hint': 'Sin sustantivo después'},
                    {'sentence': 'Is this ___ book? (your/yours)', 'answer': 'your', 'hint': 'Antes de "book"'},
                    {'sentence': 'The red car is ___. (our/ours)', 'answer': 'ours', 'hint': 'Reemplaza "our car"'},
                    {'sentence': 'The cat is cleaning ___ fur.', 'answer': 'its', 'hint': 'Posesivo de "it"'},
                    {'sentence': '___ raining outside.', 'answer': "It's", 'hint': 'It + is'},
                ]
            }
        ],
        'tips': [
            'Los posesivos en inglés NO cambian por género (his = su/suyo para masculino).',
            'Nunca uses apóstrofe en los pronombres posesivos (yours, hers, ours - NO your\'s).',
            'Para animales, se puede usar HIS/HER si conocemos el género, o ITS si no.',
        ],
        'common_mistakes': [
            {'wrong': "The book is her's.", 'correct': 'The book is hers.', 'explanation': 'Los pronombres posesivos nunca llevan apóstrofe.'},
            {'wrong': "It's tail is long.", 'correct': 'Its tail is long.', 'explanation': "It's = it is. Its = posesivo."},
            {'wrong': 'This is the mine.', 'correct': 'This is mine.', 'explanation': 'Los pronombres posesivos no llevan "the".'},
        ]
    },
    
    'there-is-are': {
        'title': 'There is / There are',
        'subtitle': 'Expresar existencia y cantidad',
        'icon': '📍',
        'level': 'Beginner',
        'category': 'Grammar Basics',
        'description': 'Aprende a decir que algo existe o hay algo en un lugar.',
        'estimated_time': '10 min',
        'sections': [
            {
                'title': '¿Cuándo se usan?',
                'type': 'explanation',
                'content': '''
                    Usamos <strong>THERE IS / THERE ARE</strong> para:
                    <ul>
                        <li>Decir que algo <strong>existe</strong></li>
                        <li>Describir qué <strong>hay en un lugar</strong></li>
                        <li>Hablar de <strong>cantidades</strong></li>
                    </ul>
                    Equivale a "hay" en español.
                '''
            },
            {
                'title': 'Regla Principal',
                'type': 'comparison',
                'left': {
                    'title': 'THERE IS',
                    'description': 'Con sustantivos SINGULARES o INCONTABLES',
                    'examples': ['There is a book.', 'There is water.', 'There is a problem.'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'THERE ARE',
                    'description': 'Con sustantivos PLURALES',
                    'examples': ['There are books.', 'There are 5 people.', 'There are many problems.'],
                    'color': 'success'
                }
            },
            {
                'title': 'Formas Completas',
                'type': 'table',
                'headers': ['Forma', 'Singular', 'Plural'],
                'rows': [
                    ['Afirmativa', "There is (There's) a cat.", 'There are (There\'re) cats.'],
                    ['Negativa', "There is not (isn't) a cat.", 'There are not (aren\'t) cats.'],
                    ['Pregunta', 'Is there a cat?', 'Are there cats?'],
                    ['Respuesta +', 'Yes, there is.', 'Yes, there are.'],
                    ['Respuesta -', 'No, there isn\'t.', 'No, there aren\'t.'],
                ]
            },
            {
                'title': 'Con Cuantificadores',
                'type': 'table',
                'headers': ['Cuantificador', 'There is/are', 'Ejemplo'],
                'rows': [
                    ['a / an', 'There is', 'There is a car outside.'],
                    ['some', 'There are', 'There are some cookies.'],
                    ['any (negativo)', 'There aren\'t', 'There aren\'t any problems.'],
                    ['many', 'There are', 'There are many students.'],
                    ['much', 'There is', 'There isn\'t much time.'],
                    ['a lot of', 'There is/are', 'There are a lot of people.'],
                    ['no', 'There is/are', 'There is no milk. = There isn\'t any milk.'],
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con THERE IS o THERE ARE:',
                'questions': [
                    {'sentence': '___ a book on the table.', 'answer': 'There is', 'hint': 'a book = singular'},
                    {'sentence': '___ many students in the class.', 'answer': 'There are', 'hint': 'students = plural'},
                    {'sentence': '___ any milk in the fridge?', 'answer': 'Is there', 'hint': 'milk = incontable, pregunta'},
                    {'sentence': '___ three apples.', 'answer': 'There are', 'hint': 'three = plural'},
                    {'sentence': '___ not a problem.', 'answer': 'There is', 'hint': 'a problem = singular'},
                    {'sentence': 'How many chairs ___ ?', 'answer': 'are there', 'hint': 'chairs = plural, pregunta'},
                ]
            }
        ],
        'tips': [
            'En conversación informal, "There\'s" se usa a veces con plurales: "There\'s a lot of people".',
            '"There" no se traduce - solo indica existencia.',
            'Con "no", es más fuerte que con "not any": "There is no water" = "There isn\'t any water".',
        ],
        'common_mistakes': [
            {'wrong': 'Have a book on the table.', 'correct': 'There is a book on the table.', 'explanation': 'Usa "There is", no "Have" para existencia.'},
            {'wrong': 'There is many people.', 'correct': 'There are many people.', 'explanation': 'People es plural, usa ARE.'},
            {'wrong': 'Are there a problem?', 'correct': 'Is there a problem?', 'explanation': 'A problem es singular, usa IS.'},
        ]
    },
    
    # =========================================================================
    # NIVEL INTERMEDIO
    # =========================================================================
    'modal-can': {
        'title': 'Modal Verb: CAN',
        'subtitle': 'Habilidad, permiso y posibilidad',
        'icon': '💪',
        'level': 'Beginner',
        'category': 'Modals',
        'description': 'Aprende a expresar habilidad, pedir permiso y hablar de posibilidades.',
        'estimated_time': '15 min',
        'sections': [
            {
                'title': '¿Qué es CAN?',
                'type': 'explanation',
                'content': '''
                    <strong>CAN</strong> es un verbo modal que expresa:
                    <ul>
                        <li><strong>Habilidad:</strong> I can swim. (Sé nadar)</li>
                        <li><strong>Permiso:</strong> Can I go? (¿Puedo ir?)</li>
                        <li><strong>Posibilidad:</strong> It can rain. (Puede llover)</li>
                        <li><strong>Peticiones:</strong> Can you help me? (¿Puedes ayudarme?)</li>
                    </ul>
                '''
            },
            {
                'title': 'Estructura',
                'type': 'table',
                'headers': ['Forma', 'Estructura', 'Ejemplo'],
                'rows': [
                    ['Afirmativa', 'Sujeto + CAN + verbo base', 'She can speak English.'],
                    ['Negativa', 'Sujeto + CANNOT/CAN\'T + verbo base', 'I can\'t drive.'],
                    ['Pregunta', 'CAN + sujeto + verbo base?', 'Can you swim?'],
                    ['Respuesta +', 'Yes, + sujeto + can.', 'Yes, I can.'],
                    ['Respuesta -', 'No, + sujeto + can\'t.', 'No, I can\'t.'],
                ],
                'note': '💡 CAN nunca cambia. No hay "cans" ni "caning". Siempre es CAN.'
            },
            {
                'title': 'CAN vs COULD (Pasado)',
                'type': 'comparison',
                'left': {
                    'title': 'CAN (Presente)',
                    'description': 'Habilidad o posibilidad AHORA',
                    'examples': ['I can run fast.', 'She can cook well.', 'We can see the ocean.'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'COULD (Pasado)',
                    'description': 'Habilidad o posibilidad ANTES',
                    'examples': ['I could run fast when I was young.', 'She could cook well.', 'We could see the ocean yesterday.'],
                    'color': 'secondary'
                }
            },
            {
                'title': 'Usos de CAN',
                'type': 'examples',
                'examples': [
                    {'english': 'I can play guitar.', 'spanish': 'Sé tocar guitarra.', 'note': 'Habilidad'},
                    {'english': 'Can I use your phone?', 'spanish': '¿Puedo usar tu teléfono?', 'note': 'Permiso'},
                    {'english': 'It can be difficult.', 'spanish': 'Puede ser difícil.', 'note': 'Posibilidad'},
                    {'english': 'Can you close the door?', 'spanish': '¿Puedes cerrar la puerta?', 'note': 'Petición'},
                    {'english': 'You can go now.', 'spanish': 'Puedes irte ahora.', 'note': 'Permiso dado'},
                ]
            },
            {
                'title': 'CAN vs BE ABLE TO',
                'type': 'table',
                'headers': ['Tiempo', 'CAN', 'BE ABLE TO'],
                'rows': [
                    ['Presente', 'I can swim.', 'I am able to swim.'],
                    ['Pasado', 'I could swim.', 'I was able to swim.'],
                    ['Futuro', '— (no existe)', 'I will be able to swim.'],
                    ['Perfecto', '— (no existe)', 'I have been able to swim.'],
                ],
                'note': '💡 Para tiempos que CAN no tiene, usamos BE ABLE TO.'
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con CAN, CAN\'T, COULD o COULDN\'T:',
                'questions': [
                    {'sentence': 'Birds ___ fly.', 'answer': 'can', 'hint': 'Habilidad general'},
                    {'sentence': 'I ___ swim when I was 5.', 'answer': "couldn't", 'hint': 'Pasado negativo'},
                    {'sentence': '___ you help me, please?', 'answer': 'Can', 'hint': 'Petición presente'},
                    {'sentence': 'She ___ speak three languages.', 'answer': 'can', 'hint': 'Habilidad presente'},
                    {'sentence': 'We ___ see the stars last night.', 'answer': 'could', 'hint': 'Pasado afirmativo'},
                    {'sentence': 'He ___ come to the party. He is busy.', 'answer': "can't", 'hint': 'Imposibilidad presente'},
                ]
            }
        ],
        'tips': [
            'CAN es igual para todos los sujetos (I can, she can, they can).',
            'Después de CAN siempre va el verbo en forma base (sin TO).',
            'Para el futuro, usa "will be able to" en lugar de CAN.',
        ],
        'common_mistakes': [
            {'wrong': 'She can to swim.', 'correct': 'She can swim.', 'explanation': 'Después de CAN no va TO.'},
            {'wrong': 'He cans play.', 'correct': 'He can play.', 'explanation': 'CAN nunca cambia, no existe "cans".'},
            {'wrong': 'I will can go.', 'correct': 'I will be able to go.', 'explanation': 'CAN no se combina con WILL.'},
        ]
    },
    
    'need-want': {
        'title': 'Need vs Want',
        'subtitle': 'Necesitar y querer',
        'icon': '🎯',
        'level': 'Beginner',
        'category': 'Verbs',
        'description': 'Aprende a expresar necesidades y deseos correctamente.',
        'estimated_time': '12 min',
        'sections': [
            {
                'title': 'NEED (Necesitar)',
                'type': 'explanation',
                'content': '''
                    <strong>NEED</strong> expresa algo que es <strong>necesario</strong> o <strong>requerido</strong>.
                    <br><br>
                    Se puede usar de dos formas:
                    <ul>
                        <li><strong>NEED + sustantivo:</strong> I need water.</li>
                        <li><strong>NEED + TO + verbo:</strong> I need to study.</li>
                    </ul>
                '''
            },
            {
                'title': 'Estructuras de NEED',
                'type': 'table',
                'headers': ['Forma', 'Con Sustantivo', 'Con Verbo'],
                'rows': [
                    ['Afirmativa', 'I need a pen.', 'I need to go.'],
                    ['Negativa', 'I don\'t need a pen.', 'I don\'t need to go.'],
                    ['Pregunta', 'Do you need a pen?', 'Do you need to go?'],
                    ['He/She', 'She needs help.', 'He needs to work.'],
                ]
            },
            {
                'title': 'WANT (Querer)',
                'type': 'explanation',
                'content': '''
                    <strong>WANT</strong> expresa un <strong>deseo</strong> o <strong>preferencia</strong>.
                    <br><br>
                    Se puede usar de varias formas:
                    <ul>
                        <li><strong>WANT + sustantivo:</strong> I want pizza.</li>
                        <li><strong>WANT + TO + verbo:</strong> I want to eat.</li>
                        <li><strong>WANT + persona + TO + verbo:</strong> I want you to come.</li>
                    </ul>
                '''
            },
            {
                'title': 'Estructuras de WANT',
                'type': 'table',
                'headers': ['Forma', 'Con Sustantivo', 'Con Verbo'],
                'rows': [
                    ['Afirmativa', 'I want a coffee.', 'I want to sleep.'],
                    ['Negativa', 'I don\'t want coffee.', 'I don\'t want to go.'],
                    ['Pregunta', 'Do you want coffee?', 'Do you want to come?'],
                    ['He/She', 'She wants a car.', 'He wants to travel.'],
                ],
                'note': '💡 Recuerda: He/She/It → wants (con -s)'
            },
            {
                'title': 'NEED vs WANT - Diferencia',
                'type': 'comparison',
                'left': {
                    'title': 'NEED (Necesidad)',
                    'description': 'Algo es NECESARIO, no es opcional',
                    'examples': ['I need water to survive.', 'You need a passport to travel.', 'She needs medicine.'],
                    'color': 'danger'
                },
                'right': {
                    'title': 'WANT (Deseo)',
                    'description': 'Es un DESEO, es opcional',
                    'examples': ['I want a new phone.', 'She wants to go shopping.', 'They want pizza.'],
                    'color': 'success'
                }
            },
            {
                'title': 'Would Like (Forma Más Educada)',
                'type': 'table',
                'headers': ['Want (Directo)', 'Would Like (Educado)', 'Uso'],
                'rows': [
                    ['I want coffee.', 'I would like coffee.', 'Más formal'],
                    ['Do you want to come?', 'Would you like to come?', 'Invitación educada'],
                    ['I want to go.', 'I\'d like to go.', 'Expresar deseo cortés'],
                ],
                'note': '💡 "Would like" es más educado, especialmente en restaurantes, tiendas, etc.'
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con NEED, NEEDS, WANT, WANTS o WOULD LIKE:',
                'questions': [
                    {'sentence': 'I ___ to buy new shoes.', 'answer': 'need', 'hint': 'Las mías están rotas - necesidad'},
                    {'sentence': 'She ___ a new car. (deseo)', 'answer': 'wants', 'hint': 'Deseo + she'},
                    {'sentence': 'You ___ to study for the exam.', 'answer': 'need', 'hint': 'Es necesario'},
                    {'sentence': 'I ___ a coffee, please. (educado)', 'answer': 'would like', 'hint': 'Forma educada'},
                    {'sentence': 'He ___ to be a doctor.', 'answer': 'wants', 'hint': 'Es su sueño'},
                    {'sentence': 'The plant ___ water.', 'answer': 'needs', 'hint': 'Necesidad + it'},
                ]
            }
        ],
        'tips': [
            'NEED implica algo importante o necesario; WANT es solo un deseo.',
            'En situaciones formales, usa "would like" en lugar de "want".',
            'Ambos verbos usan TO antes de otro verbo (need TO go, want TO eat).',
        ],
        'common_mistakes': [
            {'wrong': 'I need go.', 'correct': 'I need to go.', 'explanation': 'Después de NEED/WANT + verbo, siempre va TO.'},
            {'wrong': 'She want a coffee.', 'correct': 'She wants a coffee.', 'explanation': 'He/She/It llevan -s.'},
            {'wrong': 'I am need help.', 'correct': 'I need help.', 'explanation': 'NEED no usa TO BE.'},
        ]
    },
    
    'describing-things': {
        'title': 'Describing Things',
        'subtitle': 'Cómo describir objetos, personas y lugares',
        'icon': '🎨',
        'level': 'Beginner',
        'category': 'Vocabulary',
        'description': 'Aprende a usar adjetivos para describir todo lo que te rodea.',
        'estimated_time': '18 min',
        'sections': [
            {
                'title': 'Orden de los Adjetivos',
                'type': 'explanation',
                'content': '''
                    En inglés, cuando usamos varios adjetivos, siguen un orden específico:
                    <br><br>
                    <strong>OSASCOMP</strong>
                    <ol>
                        <li><strong>O</strong>pinión: beautiful, ugly, nice</li>
                        <li><strong>S</strong>ize: big, small, tall</li>
                        <li><strong>A</strong>ge: old, new, young</li>
                        <li><strong>S</strong>hape: round, square, flat</li>
                        <li><strong>C</strong>olor: red, blue, green</li>
                        <li><strong>O</strong>rigin: American, Mexican, Japanese</li>
                        <li><strong>M</strong>aterial: wooden, plastic, metal</li>
                        <li><strong>P</strong>urpose: cooking (pot), sleeping (bag)</li>
                    </ol>
                '''
            },
            {
                'title': 'Ejemplos del Orden',
                'type': 'examples',
                'examples': [
                    {'english': 'A beautiful big old house', 'spanish': 'Una casa vieja grande hermosa', 'note': 'Opinión → Tamaño → Edad'},
                    {'english': 'A small round wooden table', 'spanish': 'Una mesa de madera redonda pequeña', 'note': 'Tamaño → Forma → Material'},
                    {'english': 'An expensive new Japanese car', 'spanish': 'Un carro japonés nuevo caro', 'note': 'Opinión → Edad → Origen'},
                    {'english': 'A lovely little old Italian restaurant', 'spanish': 'Un encantador pequeño viejo restaurante italiano', 'note': 'Opinión → Tamaño → Edad → Origen'},
                ]
            },
            {
                'title': 'Adjetivos de Tamaño',
                'type': 'chips',
                'items': [
                    {'text': 'big', 'translation': 'grande'},
                    {'text': 'small', 'translation': 'pequeño'},
                    {'text': 'tall', 'translation': 'alto'},
                    {'text': 'short', 'translation': 'bajo/corto'},
                    {'text': 'long', 'translation': 'largo'},
                    {'text': 'wide', 'translation': 'ancho'},
                    {'text': 'narrow', 'translation': 'angosto'},
                    {'text': 'thick', 'translation': 'grueso'},
                    {'text': 'thin', 'translation': 'delgado'},
                    {'text': 'huge', 'translation': 'enorme'},
                    {'text': 'tiny', 'translation': 'diminuto'},
                ]
            },
            {
                'title': 'Adjetivos de Forma',
                'type': 'chips',
                'items': [
                    {'text': 'round', 'translation': 'redondo'},
                    {'text': 'square', 'translation': 'cuadrado'},
                    {'text': 'rectangular', 'translation': 'rectangular'},
                    {'text': 'triangular', 'translation': 'triangular'},
                    {'text': 'flat', 'translation': 'plano'},
                    {'text': 'curved', 'translation': 'curvo'},
                    {'text': 'straight', 'translation': 'recto'},
                    {'text': 'oval', 'translation': 'ovalado'},
                ]
            },
            {
                'title': 'Adjetivos de Apariencia/Opinión',
                'type': 'table',
                'headers': ['Positivo', 'Traducción', 'Negativo', 'Traducción'],
                'rows': [
                    ['beautiful', 'hermoso', 'ugly', 'feo'],
                    ['pretty', 'bonito', 'plain', 'simple'],
                    ['handsome', 'guapo', 'unattractive', 'poco atractivo'],
                    ['elegant', 'elegante', 'tacky', 'de mal gusto'],
                    ['clean', 'limpio', 'dirty', 'sucio'],
                    ['modern', 'moderno', 'old-fashioned', 'anticuado'],
                    ['nice', 'agradable', 'awful', 'horrible'],
                ]
            },
            {
                'title': 'Describiendo con TO BE',
                'type': 'table',
                'headers': ['Estructura', 'Ejemplo', 'Traducción'],
                'rows': [
                    ['Sujeto + is/are + adjetivo', 'The house is big.', 'La casa es grande.'],
                    ['It is + a/an + adj + noun', 'It is a beautiful day.', 'Es un día hermoso.'],
                    ['Sujeto + looks + adj', 'She looks happy.', 'Ella se ve feliz.'],
                    ['Sujeto + seems + adj', 'It seems difficult.', 'Parece difícil.'],
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'order',
                'instructions': 'Ordena los adjetivos correctamente:',
                'questions': [
                    {'words': ['wooden', 'old', 'beautiful', 'table'], 'answer': 'beautiful old wooden table', 'hint': 'Opinión → Edad → Material'},
                    {'words': ['Japanese', 'new', 'small', 'car'], 'answer': 'small new Japanese car', 'hint': 'Tamaño → Edad → Origen'},
                    {'words': ['round', 'big', 'red', 'ball'], 'answer': 'big round red ball', 'hint': 'Tamaño → Forma → Color'},
                    {'words': ['Italian', 'delicious', 'fresh', 'pizza'], 'answer': 'delicious fresh Italian pizza', 'hint': 'Opinión → Edad → Origen'},
                ]
            }
        ],
        'tips': [
            'No es común usar más de 3 adjetivos juntos en una oración.',
            'Los adjetivos en inglés NO cambian por género o número (big house, big houses).',
            'Practica el orden OSASCOMP hasta que sea natural.',
        ],
        'common_mistakes': [
            {'wrong': 'A wooden old table', 'correct': 'An old wooden table', 'explanation': 'Edad va antes de Material.'},
            {'wrong': 'She is a woman beautiful.', 'correct': 'She is a beautiful woman.', 'explanation': 'El adjetivo va ANTES del sustantivo.'},
            {'wrong': 'The cars reds', 'correct': 'The red cars', 'explanation': 'Los adjetivos no tienen plural.'},
        ]
    },
    
    'comparatives-superlatives': {
        'title': 'Comparatives & Superlatives',
        'subtitle': 'Comparar personas, lugares y cosas',
        'icon': '📊',
        'level': 'Intermediate',
        'category': 'Grammar',
        'description': 'Aprende a hacer comparaciones y expresar grados máximos.',
        'estimated_time': '20 min',
        'sections': [
            {
                'title': '¿Qué son?',
                'type': 'explanation',
                'content': '''
                    <ul>
                        <li><strong>Comparativo:</strong> Compara DOS cosas (más... que)</li>
                        <li><strong>Superlativo:</strong> Expresa el grado MÁXIMO (el más...)</li>
                    </ul>
                '''
            },
            {
                'title': 'Reglas para Formar Comparativos',
                'type': 'table',
                'headers': ['Tipo de Adjetivo', 'Regla', 'Ejemplo'],
                'rows': [
                    ['1 sílaba', '+ ER', 'tall → taller'],
                    ['1 sílaba terminada en -e', '+ R', 'nice → nicer'],
                    ['1 sílaba: consonante + vocal + consonante', 'doblar consonante + ER', 'big → bigger'],
                    ['2 sílabas terminadas en -y', 'cambiar y → IER', 'happy → happier'],
                    ['2+ sílabas', 'MORE + adjetivo', 'beautiful → more beautiful'],
                    ['Irregulares', 'forma especial', 'good → better'],
                ],
                'highlight_column': 2
            },
            {
                'title': 'Reglas para Formar Superlativos',
                'type': 'table',
                'headers': ['Tipo de Adjetivo', 'Regla', 'Ejemplo'],
                'rows': [
                    ['1 sílaba', 'THE + adj + EST', 'tall → the tallest'],
                    ['1 sílaba terminada en -e', 'THE + adj + ST', 'nice → the nicest'],
                    ['1 sílaba: CVC', 'THE + doblar cons + EST', 'big → the biggest'],
                    ['2 sílabas terminadas en -y', 'THE + cambiar y → IEST', 'happy → the happiest'],
                    ['2+ sílabas', 'THE MOST + adjetivo', 'beautiful → the most beautiful'],
                    ['Irregulares', 'forma especial', 'good → the best'],
                ],
                'highlight_column': 2
            },
            {
                'title': 'Adjetivos Irregulares',
                'type': 'table',
                'headers': ['Adjetivo', 'Comparativo', 'Superlativo'],
                'rows': [
                    ['good (bueno)', 'better', 'the best'],
                    ['bad (malo)', 'worse', 'the worst'],
                    ['far (lejos)', 'farther/further', 'the farthest/furthest'],
                    ['little (poco)', 'less', 'the least'],
                    ['much/many (mucho)', 'more', 'the most'],
                    ['old (viejo)', 'older/elder', 'the oldest/eldest'],
                ],
                'note': '⭐ Estos son MUY importantes. ¡Memorízalos!'
            },
            {
                'title': 'Estructuras de Comparación',
                'type': 'table',
                'headers': ['Estructura', 'Uso', 'Ejemplo'],
                'rows': [
                    ['A is + comparativo + THAN + B', 'Comparar dos cosas', 'She is taller than me.'],
                    ['A is THE + superlativo', 'El máximo grado', 'She is the tallest.'],
                    ['A is AS + adjetivo + AS + B', 'Igualdad', 'She is as tall as me.'],
                    ['A is NOT AS + adj + AS + B', 'No igualdad', 'I\'m not as tall as her.'],
                    ['LESS + adj + THAN', 'Menos que', 'This is less expensive than that.'],
                    ['THE LEAST + adj', 'El menos', 'This is the least expensive.'],
                ]
            },
            {
                'title': 'Ejemplos en Contexto',
                'type': 'examples',
                'examples': [
                    {'english': 'My house is bigger than yours.', 'spanish': 'Mi casa es más grande que la tuya.', 'note': 'Comparativo'},
                    {'english': 'This is the most beautiful city.', 'spanish': 'Esta es la ciudad más hermosa.', 'note': 'Superlativo'},
                    {'english': 'She runs faster than me.', 'spanish': 'Ella corre más rápido que yo.', 'note': 'Comparativo'},
                    {'english': 'He is the best player.', 'spanish': 'Él es el mejor jugador.', 'note': 'Superlativo irregular'},
                    {'english': 'This test is as hard as the last one.', 'spanish': 'Este examen es tan difícil como el anterior.', 'note': 'Igualdad'},
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con el comparativo o superlativo correcto:',
                'questions': [
                    {'sentence': 'My car is ___ (fast) than yours.', 'answer': 'faster', 'hint': 'Comparativo de fast'},
                    {'sentence': 'She is ___ (intelligent) student in class.', 'answer': 'the most intelligent', 'hint': 'Superlativo + 3 sílabas'},
                    {'sentence': 'This book is ___ (good) than that one.', 'answer': 'better', 'hint': 'Irregular'},
                    {'sentence': 'He is ___ (tall) boy in school.', 'answer': 'the tallest', 'hint': 'Superlativo'},
                    {'sentence': 'Today is ___ (hot) than yesterday.', 'answer': 'hotter', 'hint': 'Doblar la t'},
                    {'sentence': 'This is ___ (bad) movie I\'ve ever seen.', 'answer': 'the worst', 'hint': 'Superlativo de bad'},
                ]
            }
        ],
        'tips': [
            'Siempre usa THE antes del superlativo.',
            'Después de THAN puede ir un pronombre objeto (than me/him/her).',
            'Los adjetivos de 2 sílabas pueden usar -ER o MORE (clever → cleverer/more clever).',
        ],
        'common_mistakes': [
            {'wrong': 'She is more tall than me.', 'correct': 'She is taller than me.', 'explanation': 'Tall es de 1 sílaba, usa -ER.'},
            {'wrong': 'He is the more intelligent.', 'correct': 'He is the most intelligent.', 'explanation': 'Superlativo usa MOST, no MORE.'},
            {'wrong': 'This is the most good.', 'correct': 'This is the best.', 'explanation': 'Good es irregular.'},
        ]
    },
    
    'present-continuous': {
        'title': 'Present Continuous',
        'subtitle': 'Acciones en progreso',
        'icon': '🔄',
        'level': 'Beginner',
        'category': 'Tenses',
        'description': 'Aprende a hablar de lo que está pasando ahora mismo.',
        'estimated_time': '15 min',
        'sections': [
            {
                'title': '¿Cuándo se usa?',
                'type': 'explanation',
                'content': '''
                    El Present Continuous se usa para:
                    <ul>
                        <li><strong>Acciones que pasan AHORA:</strong> I am reading.</li>
                        <li><strong>Situaciones temporales:</strong> I am living in Paris this month.</li>
                        <li><strong>Planes futuros confirmados:</strong> I am meeting John tomorrow.</li>
                        <li><strong>Tendencias actuales:</strong> More people are working from home.</li>
                    </ul>
                '''
            },
            {
                'title': 'Estructura',
                'type': 'table',
                'headers': ['Forma', 'Estructura', 'Ejemplo'],
                'rows': [
                    ['Afirmativa', 'Sujeto + AM/IS/ARE + verbo-ING', 'She is working.'],
                    ['Negativa', 'Sujeto + AM/IS/ARE + NOT + verbo-ING', 'She is not (isn\'t) working.'],
                    ['Pregunta', 'AM/IS/ARE + sujeto + verbo-ING?', 'Is she working?'],
                    ['Respuesta +', 'Yes, + sujeto + am/is/are.', 'Yes, she is.'],
                    ['Respuesta -', 'No, + sujeto + am/is/are + not.', 'No, she isn\'t.'],
                ]
            },
            {
                'title': 'Cómo Formar -ING',
                'type': 'table',
                'headers': ['Regla', 'Verbo Base', 'Con -ING'],
                'rows': [
                    ['Mayoría de verbos', 'work, play', 'working, playing'],
                    ['Terminan en -e muda', 'make, write', 'making, writing'],
                    ['Terminan en -ie', 'die, lie', 'dying, lying'],
                    ['CVC (1 sílaba)', 'run, sit', 'running, sitting'],
                    ['CVC (2 sílabas, acento final)', 'begin, prefer', 'beginning, preferring'],
                    ['Terminan en -c', 'picnic, panic', 'picnicking, panicking'],
                ],
                'note': '💡 CVC = Consonante + Vocal + Consonante'
            },
            {
                'title': 'Palabras Clave',
                'type': 'chips',
                'items': [
                    {'text': 'now', 'translation': 'ahora'},
                    {'text': 'right now', 'translation': 'ahora mismo'},
                    {'text': 'at the moment', 'translation': 'en este momento'},
                    {'text': 'currently', 'translation': 'actualmente'},
                    {'text': 'today', 'translation': 'hoy'},
                    {'text': 'this week', 'translation': 'esta semana'},
                    {'text': 'these days', 'translation': 'estos días'},
                    {'text': 'Look!', 'translation': '¡Mira!'},
                    {'text': 'Listen!', 'translation': '¡Escucha!'},
                ]
            },
            {
                'title': 'Verbos que NO se usan en Continuous',
                'type': 'list',
                'items': [
                    {'text': 'Verbos de estado mental', 'example': 'know, believe, understand, remember, forget'},
                    {'text': 'Verbos de emoción', 'example': 'love, hate, like, want, need, prefer'},
                    {'text': 'Verbos de posesión', 'example': 'have, own, belong, possess'},
                    {'text': 'Verbos de percepción', 'example': 'see, hear, smell, taste, feel'},
                    {'text': 'Otros', 'example': 'seem, appear, mean, cost'},
                ],
                'note': '❌ I am knowing ❌ → ✅ I know ✅'
            },
            {
                'title': 'Present Simple vs Present Continuous',
                'type': 'comparison',
                'left': {
                    'title': 'Present Simple',
                    'description': 'Rutinas, hábitos, verdades',
                    'examples': ['I work every day.', 'She lives in Paris.', 'Water boils at 100°C.'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'Present Continuous',
                    'description': 'Acciones ahora, temporales',
                    'examples': ['I am working now.', 'She is living in Paris this year.', 'The water is boiling!'],
                    'color': 'success'
                }
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con Present Simple o Present Continuous:',
                'questions': [
                    {'sentence': 'She ___ (read) a book right now.', 'answer': 'is reading', 'hint': 'Ahora mismo'},
                    {'sentence': 'I ___ (go) to work every day.', 'answer': 'go', 'hint': 'Rutina'},
                    {'sentence': 'Look! The baby ___ (sleep).', 'answer': 'is sleeping', 'hint': 'Acción en progreso'},
                    {'sentence': 'He usually ___ (drink) coffee.', 'answer': 'drinks', 'hint': 'Hábito'},
                    {'sentence': 'They ___ (not/work) today.', 'answer': 'are not working', 'hint': 'Hoy - temporal'},
                    {'sentence': 'I ___ (love) chocolate.', 'answer': 'love', 'hint': 'Verbo de emoción'},
                ]
            }
        ],
        'tips': [
            'Recuerda: TO BE + verbo-ING es la estructura clave.',
            'Los verbos de estado (stative verbs) generalmente no usan -ING.',
            'Para planes futuros, el Present Continuous suena más natural que "will".',
        ],
        'common_mistakes': [
            {'wrong': 'She working now.', 'correct': 'She is working now.', 'explanation': 'Falta el verbo TO BE.'},
            {'wrong': 'I am liking this.', 'correct': 'I like this.', 'explanation': 'LIKE es un verbo de estado.'},
            {'wrong': 'He is play tennis.', 'correct': 'He is playing tennis.', 'explanation': 'Falta -ING en el verbo.'},
        ]
    },
    
    'past-simple': {
        'title': 'Past Simple',
        'subtitle': 'El tiempo pasado simple',
        'icon': '⏮️',
        'level': 'Intermediate',
        'category': 'Tenses',
        'description': 'Aprende a hablar de acciones completadas en el pasado.',
        'estimated_time': '20 min',
        'sections': [
            {
                'title': '¿Cuándo se usa?',
                'type': 'explanation',
                'content': '''
                    El Past Simple se usa para:
                    <ul>
                        <li><strong>Acciones completadas:</strong> I visited Paris last year.</li>
                        <li><strong>Secuencia de eventos:</strong> I woke up, took a shower, and had breakfast.</li>
                        <li><strong>Estados pasados:</strong> She was happy yesterday.</li>
                        <li><strong>Hábitos pasados:</strong> When I was a child, I played a lot.</li>
                    </ul>
                '''
            },
            {
                'title': 'Verbos Regulares',
                'type': 'table',
                'headers': ['Regla', 'Verbo Base', 'Pasado', 'Ejemplo'],
                'rows': [
                    ['Mayoría', 'work', 'worked', 'I worked yesterday.'],
                    ['Terminan en -e', 'live', 'lived', 'She lived in London.'],
                    ['Consonante + y', 'study', 'studied', 'He studied English.'],
                    ['Vocal + y', 'play', 'played', 'They played soccer.'],
                    ['CVC (1 sílaba)', 'stop', 'stopped', 'The car stopped.'],
                ],
                'note': '💡 Todos los verbos regulares terminan en -ED en pasado.'
            },
            {
                'title': 'Verbos Irregulares Comunes',
                'type': 'table',
                'headers': ['Base', 'Pasado', 'Significado'],
                'rows': [
                    ['go', 'went', 'ir'],
                    ['come', 'came', 'venir'],
                    ['see', 'saw', 'ver'],
                    ['have', 'had', 'tener'],
                    ['make', 'made', 'hacer'],
                    ['take', 'took', 'tomar'],
                    ['get', 'got', 'obtener'],
                    ['give', 'gave', 'dar'],
                    ['know', 'knew', 'saber'],
                    ['think', 'thought', 'pensar'],
                    ['say', 'said', 'decir'],
                    ['eat', 'ate', 'comer'],
                    ['drink', 'drank', 'beber'],
                    ['buy', 'bought', 'comprar'],
                    ['write', 'wrote', 'escribir'],
                ],
                'note': '⭐ Los verbos irregulares deben memorizarse.'
            },
            {
                'title': 'Estructura',
                'type': 'table',
                'headers': ['Forma', 'Estructura', 'Ejemplo'],
                'rows': [
                    ['Afirmativa', 'Sujeto + verbo pasado', 'She worked yesterday.'],
                    ['Negativa', 'Sujeto + DID NOT + verbo base', 'She didn\'t work yesterday.'],
                    ['Pregunta', 'DID + sujeto + verbo base?', 'Did she work yesterday?'],
                    ['Respuesta +', 'Yes, + sujeto + did.', 'Yes, she did.'],
                    ['Respuesta -', 'No, + sujeto + didn\'t.', 'No, she didn\'t.'],
                ],
                'note': '⚠️ Con DID, el verbo VUELVE a su forma base.'
            },
            {
                'title': 'TO BE en Pasado',
                'type': 'table',
                'headers': ['Presente', 'Pasado', 'Ejemplo'],
                'rows': [
                    ['I am', 'I was', 'I was tired.'],
                    ['You are', 'You were', 'You were late.'],
                    ['He/She/It is', 'He/She/It was', 'She was happy.'],
                    ['We are', 'We were', 'We were friends.'],
                    ['They are', 'They were', 'They were at home.'],
                ],
                'note': '💡 TO BE es especial: WAS (singular) y WERE (plural + you)'
            },
            {
                'title': 'Palabras Clave',
                'type': 'chips',
                'items': [
                    {'text': 'yesterday', 'translation': 'ayer'},
                    {'text': 'last week/month/year', 'translation': 'la semana/mes/año pasado'},
                    {'text': 'ago', 'translation': 'hace'},
                    {'text': 'in 2020', 'translation': 'en 2020'},
                    {'text': 'when I was young', 'translation': 'cuando era joven'},
                    {'text': 'the other day', 'translation': 'el otro día'},
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'fill-blank',
                'instructions': 'Completa con el Past Simple:',
                'questions': [
                    {'sentence': 'I ___ (go) to the park yesterday.', 'answer': 'went', 'hint': 'Irregular'},
                    {'sentence': 'She ___ (not/eat) breakfast.', 'answer': "didn't eat", 'hint': 'Negativo'},
                    {'sentence': '___ you ___ (see) the movie?', 'answer': 'Did, see', 'hint': 'Pregunta'},
                    {'sentence': 'They ___ (be) very happy.', 'answer': 'were', 'hint': 'They + be'},
                    {'sentence': 'He ___ (study) all night.', 'answer': 'studied', 'hint': 'Regular -y'},
                    {'sentence': 'We ___ (buy) a new car last month.', 'answer': 'bought', 'hint': 'Irregular'},
                ]
            }
        ],
        'tips': [
            'DID se usa igual para todos los sujetos.',
            'Memoriza los verbos irregulares más comunes - son muy frecuentes.',
            'En pasado, el verbo ES IGUAL para todos los sujetos (I/he/they worked).',
        ],
        'common_mistakes': [
            {'wrong': 'She didn\'t went.', 'correct': 'She didn\'t go.', 'explanation': 'Con DID, el verbo es BASE.'},
            {'wrong': 'I was go yesterday.', 'correct': 'I went yesterday.', 'explanation': 'No mezcles WAS con otro verbo pasado.'},
            {'wrong': 'Did you went?', 'correct': 'Did you go?', 'explanation': 'Con DID, el verbo es BASE.'},
        ]
    },
    
    'future-will-going': {
        'title': 'Future: Will vs Going to',
        'subtitle': 'Expresar el futuro en inglés',
        'icon': '🔮',
        'level': 'Intermediate',
        'category': 'Tenses',
        'description': 'Aprende las dos formas principales de hablar del futuro.',
        'estimated_time': '18 min',
        'sections': [
            {
                'title': 'Dos Formas de Futuro',
                'type': 'explanation',
                'content': '''
                    En inglés hay dos formas principales de hablar del futuro:
                    <ul>
                        <li><strong>WILL:</strong> Decisiones espontáneas, predicciones, promesas</li>
                        <li><strong>GOING TO:</strong> Planes ya decididos, intenciones, predicciones con evidencia</li>
                    </ul>
                '''
            },
            {
                'title': 'Estructura de WILL',
                'type': 'table',
                'headers': ['Forma', 'Estructura', 'Ejemplo'],
                'rows': [
                    ['Afirmativa', 'Sujeto + WILL + verbo base', 'I will help you.'],
                    ['Contracción', "Sujeto + 'LL + verbo base", "I'll help you."],
                    ['Negativa', 'Sujeto + WILL NOT + verbo base', 'I will not (won\'t) go.'],
                    ['Pregunta', 'WILL + sujeto + verbo base?', 'Will you come?'],
                ]
            },
            {
                'title': 'Estructura de GOING TO',
                'type': 'table',
                'headers': ['Forma', 'Estructura', 'Ejemplo'],
                'rows': [
                    ['Afirmativa', 'Sujeto + AM/IS/ARE + GOING TO + verbo', 'I am going to travel.'],
                    ['Contracción', "Sujeto + 'M/'S/'RE + gonna (informal)", "I'm gonna travel."],
                    ['Negativa', 'Sujeto + AM/IS/ARE + NOT + GOING TO + verbo', 'I\'m not going to go.'],
                    ['Pregunta', 'AM/IS/ARE + sujeto + GOING TO + verbo?', 'Are you going to come?'],
                ]
            },
            {
                'title': 'Cuándo Usar Cada Uno',
                'type': 'comparison',
                'left': {
                    'title': 'WILL',
                    'description': 'Decisiones del momento, predicciones sin evidencia, promesas',
                    'examples': ['I\'ll answer the phone.', 'It will rain tomorrow (I think).', 'I\'ll always love you.'],
                    'color': 'primary'
                },
                'right': {
                    'title': 'GOING TO',
                    'description': 'Planes ya hechos, intenciones, predicciones con evidencia',
                    'examples': ['I\'m going to visit Paris next month.', 'Look at those clouds! It\'s going to rain.', 'She\'s going to have a baby.'],
                    'color': 'success'
                }
            },
            {
                'title': 'Ejemplos Comparativos',
                'type': 'examples',
                'examples': [
                    {'english': 'I\'ll have the pizza. (Deciding now)', 'spanish': 'Tomaré la pizza. (Decidiendo ahora)', 'note': 'WILL - decisión espontánea'},
                    {'english': 'I\'m going to order pizza. (Already decided)', 'spanish': 'Voy a pedir pizza. (Ya decidido)', 'note': 'GOING TO - plan previo'},
                    {'english': 'I think she will pass.', 'spanish': 'Creo que ella pasará.', 'note': 'WILL - predicción/opinión'},
                    {'english': 'She\'s studied a lot. She\'s going to pass!', 'spanish': 'Ha estudiado mucho. ¡Va a pasar!', 'note': 'GOING TO - evidencia'},
                ]
            },
            {
                'title': 'Expresiones con WILL',
                'type': 'chips',
                'items': [
                    {'text': 'I think...', 'translation': 'Creo que...'},
                    {'text': 'I hope...', 'translation': 'Espero que...'},
                    {'text': 'probably', 'translation': 'probablemente'},
                    {'text': 'maybe', 'translation': 'quizás'},
                    {'text': 'I promise', 'translation': 'Prometo'},
                    {'text': 'I\'ll try', 'translation': 'Lo intentaré'},
                ]
            },
            {
                'title': 'Ejercicios',
                'type': 'exercise',
                'exercise_type': 'choose',
                'instructions': 'Elige WILL o GOING TO según el contexto:',
                'questions': [
                    {'sentence': 'The phone is ringing. I ___ answer it.', 'answer': "'ll (will)", 'hint': 'Decisión ahora'},
                    {'sentence': 'I\'ve bought the tickets. We ___ to Paris!', 'answer': 'are going', 'hint': 'Plan ya hecho'},
                    {'sentence': 'Look at those dark clouds. It ___ rain.', 'answer': 'is going to', 'hint': 'Evidencia'},
                    {'sentence': 'I think Brazil ___ win the World Cup.', 'answer': 'will', 'hint': 'Predicción/opinión'},
                    {'sentence': 'I ___ study medicine. I\'ve already enrolled.', 'answer': 'am going to', 'hint': 'Intención/plan'},
                ]
            }
        ],
        'tips': [
            '"Gonna" (going to) es muy común en habla informal.',
            'Ambas formas son correctas para predicciones, pero con evidencia usa GOING TO.',
            'Para ofertas y promesas espontáneas, siempre WILL.',
        ],
        'common_mistakes': [
            {'wrong': 'I will going to travel.', 'correct': 'I am going to travel. / I will travel.', 'explanation': 'No combines WILL y GOING TO.'},
            {'wrong': 'I\'m going to help you! (offering now)', 'correct': 'I\'ll help you!', 'explanation': 'Ofertas espontáneas usan WILL.'},
            {'wrong': 'She will to come.', 'correct': 'She will come.', 'explanation': 'Después de WILL no va TO.'},
        ]
    },
}

# ============================================================================
# RUTAS
# ============================================================================

@grammar_bp.route('/')
def index():
    """Lista todos los temas gramaticales"""
    # Organizar por nivel y categoría
    levels = {'Beginner': [], 'Intermediate': [], 'Advanced': []}
    
    for key, topic in grammar_topics.items():
        level = topic.get('level', 'Beginner')
        levels[level].append({
            'key': key,
            **topic
        })
    
    return render_template(
        'grammar/index.html',
        levels=levels,
        total_topics=len(grammar_topics)
    )


@grammar_bp.route('/<topic_key>')
def topic_detail(topic_key):
    """Muestra un tema gramatical específico"""
    if topic_key not in grammar_topics:
        abort(404)
    
    topic = grammar_topics[topic_key]
    
    # Encontrar temas relacionados
    related = []
    current_category = topic.get('category', '')
    for key, t in grammar_topics.items():
        if key != topic_key and t.get('category') == current_category:
            related.append({'key': key, **t})
            if len(related) >= 3:
                break
    
    # Navegación: anterior y siguiente
    topics_list = list(grammar_topics.keys())
    current_index = topics_list.index(topic_key)
    prev_topic = topics_list[current_index - 1] if current_index > 0 else None
    next_topic = topics_list[current_index + 1] if current_index < len(topics_list) - 1 else None
    
    return render_template(
        'grammar/topic.html',
        topic=topic,
        topic_key=topic_key,
        related=related,
        prev_topic=prev_topic,
        next_topic=next_topic,
        prev_title=grammar_topics.get(prev_topic, {}).get('title') if prev_topic else None,
        next_title=grammar_topics.get(next_topic, {}).get('title') if next_topic else None
    )


@grammar_bp.route('/check-exercise', methods=['POST'])
def check_exercise():
    """Verificar respuesta de ejercicio (AJAX)"""
    data = request.get_json()
    user_answer = data.get('answer', '').strip().lower()
    correct_answer = data.get('correct', '').strip().lower()
    
    # Verificar similitud
    is_correct = user_answer == correct_answer
    
    # Para respuestas con múltiples opciones válidas
    if not is_correct and '/' in correct_answer:
        alternatives = [a.strip() for a in correct_answer.split('/')]
        is_correct = user_answer in alternatives
    
    return jsonify({
        'correct': is_correct,
        'expected': correct_answer
    })


# ============================================================================
# RUTAS PARA ORACIONES DE USUARIOS
# ============================================================================

@grammar_bp.route('/<topic_key>/sentences')
def topic_sentences(topic_key):
    """Ver oraciones de la comunidad para un tema"""
    if topic_key not in grammar_topics:
        abort(404)
    
    topic = grammar_topics[topic_key]
    
    # Obtener oraciones aprobadas para este tema
    sentences = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_approved=True
    ).order_by(UserSentence.likes_count.desc()).limit(50).all()
    
    # Obtener oraciones destacadas
    featured = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_featured=True
    ).limit(5).all()
    
    return render_template(
        'grammar/sentences.html',
        topic=topic,
        topic_key=topic_key,
        sentences=sentences,
        featured=featured
    )


@grammar_bp.route('/submit-sentence', methods=['POST'])
@login_required
def submit_sentence():
    """Enviar una oración para revisión"""
    data = request.get_json()
    topic_key = data.get('topic')
    sentence = data.get('sentence', '').strip()
    translation = data.get('translation', '').strip()
    
    if not topic_key or topic_key not in grammar_topics:
        return jsonify({'success': False, 'error': 'Tema inválido'})
    
    if not sentence or len(sentence) < 3:
        return jsonify({'success': False, 'error': 'La oración es muy corta'})
    
    if len(sentence) > 500:
        return jsonify({'success': False, 'error': 'La oración es muy larga (máx 500 caracteres)'})
    
    # Crear la oración
    new_sentence = UserSentence(
        user_id=current_user.id,
        grammar_topic=topic_key,
        original_sentence=sentence,
        spanish_translation=translation if translation else None,
        difficulty=grammar_topics[topic_key].get('level', 'beginner').lower()
    )
    
    db.session.add(new_sentence)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': '¡Oración enviada! Será revisada pronto.',
        'sentence_id': new_sentence.id
    })


@grammar_bp.route('/correct-sentence', methods=['POST'])
@login_required  
def correct_sentence():
    """Corregir una oración (auto-corrección básica)"""
    data = request.get_json()
    sentence_id = data.get('sentence_id')
    corrected_text = data.get('corrected_text', '').strip()
    correction_notes = data.get('notes', '').strip()
    
    sentence = UserSentence.query.get_or_404(sentence_id)
    
    # Solo el autor o admin puede corregir
    if sentence.user_id != current_user.id and not getattr(current_user, 'is_admin', False):
        return jsonify({'success': False, 'error': 'No tienes permiso'})
    
    if corrected_text:
        sentence.corrected_sentence = corrected_text
        sentence.is_correct = (corrected_text.lower() == sentence.original_sentence.lower())
    
    if correction_notes:
        sentence.correction_notes = correction_notes
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Corrección guardada'
    })


@grammar_bp.route('/approve-sentence/<int:sentence_id>', methods=['POST'])
@login_required
def approve_sentence(sentence_id):
    """Aprobar una oración para mostrar a la comunidad"""
    if not getattr(current_user, 'is_admin', False):
        return jsonify({'success': False, 'error': 'Solo administradores'})
    
    sentence = UserSentence.query.get_or_404(sentence_id)
    sentence.is_approved = True
    db.session.commit()
    
    return jsonify({'success': True})


@grammar_bp.route('/like-sentence/<int:sentence_id>', methods=['POST'])
@login_required
def like_sentence(sentence_id):
    """Dar like a una oración"""
    sentence = UserSentence.query.get_or_404(sentence_id)
    
    # Verificar si ya dio like
    existing = SentenceLike.query.filter_by(
        user_id=current_user.id,
        sentence_id=sentence_id
    ).first()
    
    if existing:
        # Quitar like
        db.session.delete(existing)
        sentence.likes_count = max(0, sentence.likes_count - 1)
        liked = False
    else:
        # Agregar like
        like = SentenceLike(user_id=current_user.id, sentence_id=sentence_id)
        db.session.add(like)
        sentence.likes_count += 1
        liked = True
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'liked': liked,
        'likes_count': sentence.likes_count
    })


@grammar_bp.route('/random-sentence/<topic_key>')
def random_sentence(topic_key):
    """Obtener una oración aleatoria aprobada para ejercicios"""
    sentences = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_approved=True,
        is_correct=True
    ).all()
    
    if not sentences:
        return jsonify({'success': False, 'error': 'No hay oraciones disponibles'})
    
    sentence = random.choice(sentences)
    sentence.used_in_exercises += 1
    db.session.commit()
    
    return jsonify({
        'success': True,
        'sentence': {
            'id': sentence.id,
            'text': sentence.corrected_sentence or sentence.original_sentence,
            'translation': sentence.spanish_translation,
            'author': sentence.user.username if sentence.user else 'Anónimo'
        }
    })


@grammar_bp.route('/my-sentences')
@login_required
def my_sentences():
    """Ver mis oraciones enviadas"""
    sentences = UserSentence.query.filter_by(
        user_id=current_user.id
    ).order_by(UserSentence.created_at.desc()).all()
    
    stats = {
        'total': len(sentences),
        'approved': sum(1 for s in sentences if s.is_approved),
        'featured': sum(1 for s in sentences if s.is_featured),
        'total_likes': sum(s.likes_count for s in sentences)
    }
    
    return render_template(
        'grammar/my_sentences.html',
        sentences=sentences,
        stats=stats
    )


# ============================================================================
# BUSCADOR DE VERBOS
# ============================================================================

@grammar_bp.route('/verbs')
def verbs_index():
    """Página principal del buscador de verbos"""
    # Estadísticas
    stats = {
        'total': Verb.query.count(),
        'irregular': Verb.query.filter_by(is_irregular=True).count(),
        'regular': Verb.query.filter_by(is_irregular=False).count(),
        'modal': Verb.query.filter_by(is_modal=True).count()
    }
    
    # Verbos destacados (top 20 por frecuencia)
    featured_verbs = Verb.query.filter(
        Verb.frequency_rank != None
    ).order_by(Verb.frequency_rank).limit(20).all()
    
    # Categorías disponibles
    categories = db.session.query(Verb.category).distinct().filter(
        Verb.category != None
    ).all()
    categories = [c[0] for c in categories]
    
    return render_template(
        'grammar/verbs.html',
        stats=stats,
        featured_verbs=featured_verbs,
        categories=categories
    )


@grammar_bp.route('/verbs/search')
def search_verbs():
    """Buscar verbos (API)"""
    query = request.args.get('q', '').strip().lower()
    filter_type = request.args.get('type', 'all')  # all, irregular, regular, modal
    category = request.args.get('category', '')
    limit = min(int(request.args.get('limit', 20)), 100)
    
    # Base query
    verbs_query = Verb.query
    
    # Filtrar por búsqueda
    if query:
        verbs_query = verbs_query.filter(
            db.or_(
                Verb.infinitive.ilike(f'%{query}%'),
                Verb.spanish_translation.ilike(f'%{query}%'),
                Verb.past_simple.ilike(f'%{query}%'),
                Verb.past_participle.ilike(f'%{query}%')
            )
        )
    
    # Filtrar por tipo
    if filter_type == 'irregular':
        verbs_query = verbs_query.filter_by(is_irregular=True)
    elif filter_type == 'regular':
        verbs_query = verbs_query.filter_by(is_irregular=False)
    elif filter_type == 'modal':
        verbs_query = verbs_query.filter_by(is_modal=True)
    
    # Filtrar por categoría
    if category:
        verbs_query = verbs_query.filter_by(category=category)
    
    # Ordenar
    verbs_query = verbs_query.order_by(Verb.frequency_rank.nullslast())
    
    # Ejecutar
    verbs = verbs_query.limit(limit).all()
    
    return jsonify({
        'success': True,
        'count': len(verbs),
        'verbs': [{
            'id': v.id,
            'infinitive': v.infinitive,
            'past_simple': v.past_simple,
            'past_participle': v.past_participle,
            'present_participle': v.present_participle,
            'third_person': v.third_person,
            'spanish': v.spanish_translation,
            'is_irregular': v.is_irregular,
            'is_modal': v.is_modal,
            'category': v.category,
            'example': v.example_sentence,
            'example_translation': v.example_translation,
            'notes': v.notes
        } for v in verbs]
    })


@grammar_bp.route('/verbs/<infinitive>')
def verb_detail(infinitive):
    """Detalle de un verbo específico"""
    verb = Verb.query.filter(
        func.lower(Verb.infinitive) == infinitive.lower()
    ).first_or_404()
    
    # Verbos similares (misma categoría)
    similar = Verb.query.filter(
        Verb.category == verb.category,
        Verb.id != verb.id
    ).limit(5).all()
    
    return render_template(
        'grammar/verb_detail.html',
        verb=verb,
        similar=similar
    )


@grammar_bp.route('/verbs/random')
def random_verb():
    """Obtener un verbo aleatorio para practicar"""
    verb_type = request.args.get('type', 'all')
    
    query = Verb.query
    if verb_type == 'irregular':
        query = query.filter_by(is_irregular=True)
    elif verb_type == 'regular':
        query = query.filter_by(is_irregular=False)
    
    verbs = query.all()
    if not verbs:
        return jsonify({'success': False})
    
    verb = random.choice(verbs)
    
    return jsonify({
        'success': True,
        'verb': {
            'infinitive': verb.infinitive,
            'past_simple': verb.past_simple,
            'past_participle': verb.past_participle,
            'spanish': verb.spanish_translation,
            'is_irregular': verb.is_irregular
        }
    })


# ============================================================================
# GUARDAR RESULTADOS DE EJERCICIOS
# ============================================================================

@grammar_bp.route('/save-exercise-result', methods=['POST'])
@login_required
def save_exercise_result():
    """Guardar resultado de ejercicios de gramática"""
    data = request.get_json()
    
    result = GrammarExerciseResult(
        user_id=current_user.id,
        grammar_topic=data.get('topic'),
        exercise_type=data.get('exercise_type', 'fill_blank'),
        total_questions=data.get('total', 0),
        correct_answers=data.get('correct', 0),
        score_percentage=data.get('score', 0.0),
        time_spent_seconds=data.get('time_seconds')
    )
    
    db.session.add(result)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'result_id': result.id
    })


@grammar_bp.route('/my-progress')
@login_required
def grammar_progress():
    """Ver progreso en gramática"""
    # Obtener resultados agrupados por tema
    results = db.session.query(
        GrammarExerciseResult.grammar_topic,
        func.count(GrammarExerciseResult.id).label('attempts'),
        func.avg(GrammarExerciseResult.score_percentage).label('avg_score'),
        func.max(GrammarExerciseResult.score_percentage).label('best_score')
    ).filter_by(user_id=current_user.id).group_by(
        GrammarExerciseResult.grammar_topic
    ).all()
    
    progress = []
    for r in results:
        topic_info = grammar_topics.get(r.grammar_topic, {})
        progress.append({
            'topic_key': r.grammar_topic,
            'title': topic_info.get('title', r.grammar_topic),
            'icon': topic_info.get('icon', '📚'),
            'attempts': r.attempts,
            'avg_score': round(r.avg_score or 0, 1),
            'best_score': round(r.best_score or 0, 1)
        })
    
    # Estadísticas generales
    total_exercises = GrammarExerciseResult.query.filter_by(
        user_id=current_user.id
    ).count()
    
    avg_overall = db.session.query(
        func.avg(GrammarExerciseResult.score_percentage)
    ).filter_by(user_id=current_user.id).scalar() or 0
    
    return render_template(
        'grammar/progress.html',
        progress=progress,
        total_exercises=total_exercises,
        avg_overall=round(avg_overall, 1),
        grammar_topics=grammar_topics
    )

