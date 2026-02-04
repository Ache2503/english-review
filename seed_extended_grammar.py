"""
Script para agregar temas gramaticales extensos y detallados
============================================================
Incluye explicaciones completas, ejemplos, errores comunes y excepciones.
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import GrammarRule, Unit

app = create_app()

# Definición de temas gramaticales extensos organizados por nivel CEFR
GRAMMAR_TOPICS = {
    # ==================== NIVEL A1 ====================
    'A1': [
        {
            'topic': 'Verb TO BE - Complete Guide',
            'rules': [
                {
                    'rule': 'Affirmative forms: I am, You are, He/She/It is, We are, They are',
                    'detailed_explanation': '''El verbo TO BE es el más importante en inglés. Se usa para:
1. Identificar personas y cosas: "I am a student"
2. Describir cualidades: "She is tall"
3. Expresar estados: "We are happy"
4. Indicar ubicación: "They are at home"
5. Expresar edad: "He is 25 years old"
6. Hablar del clima: "It is cold today"''',
                    'example': 'I am a teacher. She is my friend. We are from Mexico.',
                    'correct_usage': 'She is beautiful. They are students.',
                    'incorrect_usage': 'She are beautiful. ❌ They is students. ❌',
                    'common_errors': 'Confundir "is" con "are" según el sujeto. Olvidar usar contracciones en habla informal.',
                    'exceptions': 'En preguntas de confirmación (tag questions): "You are coming, aren\'t you?"'
                },
                {
                    'rule': 'Negative forms: am not, is not (isn\'t), are not (aren\'t)',
                    'detailed_explanation': '''Para formar negativos con TO BE:
1. I am not (I'm not) - NUNCA "I amn't"
2. He/She/It is not (isn't)
3. You/We/They are not (aren't)

Uso de contracciones:
- Informal: I'm not, he isn't, they aren't
- Formal: I am not, he is not, they are not''',
                    'example': 'I am not tired. She isn\'t here. We aren\'t ready.',
                    'correct_usage': 'He isn\'t a doctor. They aren\'t coming.',
                    'incorrect_usage': 'He not is a doctor. ❌ They not are coming. ❌',
                    'common_errors': 'Poner "not" antes del verbo en lugar de después.',
                    'exceptions': '"I\'m not" es la única forma - no existe "I amn\'t"'
                },
                {
                    'rule': 'Questions with TO BE: Am I...? Is he...? Are they...?',
                    'detailed_explanation': '''Para formar preguntas, invertimos el orden sujeto-verbo:
Afirmativo: She is happy.
Pregunta: Is she happy?

Estructura: BE + Subject + Complement + ?
- Am I late?
- Is he your brother?
- Are they students?''',
                    'example': 'Are you ready? Is this your book? Am I on time?',
                    'correct_usage': 'Is she a teacher? Are they from Spain?',
                    'incorrect_usage': 'She is a teacher? ❌ (falta inversión)',
                    'common_errors': 'Olvidar invertir el verbo y sujeto en preguntas.',
                    'exceptions': 'En preguntas indirectas no se invierte: "I wonder if she is happy"'
                }
            ]
        },
        {
            'topic': 'Articles A/AN/THE - Complete Guide',
            'rules': [
                {
                    'rule': 'A vs AN: Use "a" before consonant sounds, "an" before vowel sounds',
                    'detailed_explanation': '''La elección entre A y AN depende del SONIDO, no de la letra:

Usa AN antes de sonidos vocálicos:
- an apple, an elephant, an idea, an orange, an umbrella
- an hour (la H es muda), an honest person
- an MBA (se pronuncia "em-bi-ei")

Usa A antes de sonidos consonánticos:
- a book, a car, a dog
- a university (suena "yu-"), a European (suena "yu-")
- a one-way street (suena "wun")''',
                    'example': 'I need an umbrella. She is a university student.',
                    'correct_usage': 'an hour, a hotel, an honest answer, a house',
                    'incorrect_usage': 'a hour ❌, an university ❌, a honest ❌',
                    'common_errors': 'Guiarse por la letra en lugar del sonido.',
                    'exceptions': 'Palabras que empiezan con "h" muda: an hour, an heir, an honor'
                },
                {
                    'rule': 'THE - Definite article for specific things',
                    'detailed_explanation': '''Usa THE cuando:
1. Algo es único: the sun, the moon, the Earth
2. Ya mencionaste algo: "I saw a cat. The cat was black."
3. Es específico por contexto: "Close the door" (sabemos cuál)
4. Con superlativos: the best, the tallest
5. Con ordinales: the first, the second
6. Instrumentos musicales: play the piano
7. Países plurales/unidos: the USA, the Netherlands

NO uses THE con:
- Nombres propios: Maria (no "the Maria")
- Países singulares: Spain, Mexico, Japan
- Comidas en general: I like pizza
- Deportes: play football''',
                    'example': 'The Eiffel Tower is in France. I love the ocean.',
                    'correct_usage': 'The moon is bright. She plays the guitar.',
                    'incorrect_usage': 'I like the pizza. ❌ (en general)',
                    'common_errors': 'Usar "the" con nombres propios o cosas en general.',
                    'exceptions': 'The + adjetivo = grupo de personas: the rich, the poor, the elderly'
                },
                {
                    'rule': 'Zero Article - When to use no article',
                    'detailed_explanation': '''NO uses artículo con:
1. Nombres propios: John, Paris, Microsoft
2. Idiomas: I speak English
3. Comidas/bebidas en general: I like coffee
4. Deportes y juegos: play tennis, play chess
5. Días y meses: on Monday, in January
6. Transporte después de BY: by car, by plane
7. Lugares con propósito específico:
   - go to school (como estudiante)
   - go to church (para rezar)
   - go to bed (para dormir)

Compara:
- "He is in prison" (es prisionero)
- "He is in the prison" (está visitando)''',
                    'example': 'I go to school by bus. She speaks French.',
                    'correct_usage': 'Life is beautiful. I love music.',
                    'incorrect_usage': 'The life is beautiful. ❌ I love the music. ❌',
                    'common_errors': 'Usar artículos con conceptos abstractos generales.',
                    'exceptions': 'Si es específico, usa THE: The music at the party was great.'
                }
            ]
        },
        {
            'topic': 'Present Simple - Complete Guide',
            'rules': [
                {
                    'rule': 'Form: I/You/We/They + base verb, He/She/It + verb + s/es',
                    'detailed_explanation': '''El Present Simple describe:
1. Hábitos y rutinas: I wake up at 7 AM
2. Verdades generales: Water boils at 100°C
3. Estados permanentes: She lives in London
4. Horarios fijos: The train leaves at 9:00

Formación:
- I/You/We/They: verbo base (work, eat, study)
- He/She/It: verbo + s/es (works, eats, studies)

Reglas para -s/-es:
- Mayoría: +s (plays, works, eats)
- Verbos en -s, -sh, -ch, -x, -o: +es (watches, goes, fixes)
- Verbos en consonante + y: y → ies (studies, carries)''',
                    'example': 'She works in a bank. They play tennis every Sunday.',
                    'correct_usage': 'He watches TV. She studies medicine.',
                    'incorrect_usage': 'He watch TV. ❌ She studys medicine. ❌',
                    'common_errors': 'Olvidar la -s con tercera persona. Escribir "studys" en lugar de "studies".',
                    'exceptions': 'El verbo "have" cambia a "has": She has a car.'
                },
                {
                    'rule': 'Negative: do not (don\'t) / does not (doesn\'t) + base verb',
                    'detailed_explanation': '''Para formar negativos:
- I/You/We/They + do not (don't) + verbo base
- He/She/It + does not (doesn't) + verbo base

IMPORTANTE: El verbo principal va en forma base (sin -s)

Ejemplos:
✓ He doesn't work here. (correcto)
✗ He doesn't works here. (incorrecto)''',
                    'example': 'I don\'t like coffee. She doesn\'t speak French.',
                    'correct_usage': 'He doesn\'t eat meat. They don\'t live here.',
                    'incorrect_usage': 'He doesn\'t eats meat. ❌ She not speaks English. ❌',
                    'common_errors': 'Añadir -s al verbo después de doesn\'t. Usar "not" sin auxiliar.',
                    'exceptions': 'Con "have to": She doesn\'t have to work today.'
                },
                {
                    'rule': 'Questions: Do/Does + subject + base verb?',
                    'detailed_explanation': '''Para formar preguntas:
- Do + I/you/we/they + verbo base?
- Does + he/she/it + verbo base?

Estructura: DO/DOES + Sujeto + Verbo base + Complemento?

Respuestas cortas:
- Yes, I do. / No, I don't.
- Yes, she does. / No, she doesn't.''',
                    'example': 'Do you speak English? Does she work here?',
                    'correct_usage': 'Does he like pizza? Do they live nearby?',
                    'incorrect_usage': 'Does he likes pizza? ❌ Do she work? ❌',
                    'common_errors': 'Añadir -s al verbo en preguntas. Usar "do" con tercera persona.',
                    'exceptions': 'Who/What como sujeto no necesitan "do": Who works here?'
                }
            ]
        },
        {
            'topic': 'Possessive Adjectives and Pronouns',
            'rules': [
                {
                    'rule': 'Possessive Adjectives: my, your, his, her, its, our, their',
                    'detailed_explanation': '''Los adjetivos posesivos van ANTES del sustantivo:
- my book (mi libro)
- your car (tu carro)
- his phone (su teléfono - de él)
- her bag (su bolsa - de ella)
- its tail (su cola - de animal/cosa)
- our house (nuestra casa)
- their children (sus hijos - de ellos)

IMPORTANTE:
- No cambian con plural: my book / my books
- "Its" (posesivo) vs "It's" (it is)''',
                    'example': 'This is my pen. Their house is big. Its color is blue.',
                    'correct_usage': 'She loves her job. We enjoy our weekends.',
                    'incorrect_usage': 'She loves she\'s job. ❌ This is mine book. ❌',
                    'common_errors': 'Confundir "its" con "it\'s". Usar pronombres en lugar de adjetivos.',
                    'exceptions': 'Con partes del cuerpo se usa THE en algunas expresiones: He hit me on the arm.'
                },
                {
                    'rule': 'Possessive Pronouns: mine, yours, his, hers, ours, theirs',
                    'detailed_explanation': '''Los pronombres posesivos REEMPLAZAN sustantivo + adjetivo posesivo:
- This book is mine. (= This is my book)
- The car is yours. (= It is your car)
- That phone is his.
- The bag is hers.
- The house is ours.
- Those keys are theirs.

NOTA: "its" no tiene forma de pronombre posesivo
Van solos, nunca con sustantivo después''',
                    'example': 'Is this pen yours? No, it\'s hers. Mine is blue.',
                    'correct_usage': 'This car is ours. That decision was theirs.',
                    'incorrect_usage': 'This is mine book. ❌ That is her\'s. ❌',
                    'common_errors': 'Agregar sustantivo después del pronombre. Escribir "your\'s" con apóstrofe.',
                    'exceptions': 'Expresiones idiomáticas: "A friend of mine" (un amigo mío)'
                }
            ]
        },
        {
            'topic': 'Prepositions of Time - IN, ON, AT',
            'rules': [
                {
                    'rule': 'AT for specific times: at 5 o\'clock, at noon, at midnight',
                    'detailed_explanation': '''Usa AT para:
1. Horas específicas: at 3:00, at 7:30 PM
2. Momentos del día: at noon, at midnight, at dawn, at sunset
3. Fines de semana (British): at the weekend
4. Festividades: at Christmas, at Easter
5. Expresiones: at the moment, at present, at the same time

Frases comunes:
- at night (pero: in the morning/afternoon/evening)
- at the beginning/end
- at first''',
                    'example': 'I wake up at 6 AM. The meeting is at noon.',
                    'correct_usage': 'at midnight, at Christmas, at the moment',
                    'incorrect_usage': 'in 5 o\'clock ❌, on noon ❌',
                    'common_errors': 'Usar "in" o "on" con horas específicas.',
                    'exceptions': 'at night pero in the evening'
                },
                {
                    'rule': 'ON for days and dates: on Monday, on July 4th',
                    'detailed_explanation': '''Usa ON para:
1. Días de la semana: on Monday, on Fridays
2. Fechas: on July 4th, on December 25th
3. Días especiales: on my birthday, on Christmas Day
4. Días + parte del día: on Monday morning

Expresiones:
- on time (puntual)
- on the weekend (American English)
- on vacation (American English)''',
                    'example': 'The party is on Saturday. I was born on March 15th.',
                    'correct_usage': 'on Tuesday, on New Year\'s Day, on my wedding day',
                    'incorrect_usage': 'in Monday ❌, at July 4th ❌',
                    'common_errors': 'Usar "in" con días de la semana.',
                    'exceptions': 'Sin preposición con "this/next/last": I\'ll see you next Monday.'
                },
                {
                    'rule': 'IN for longer periods: in January, in 2024, in the morning',
                    'detailed_explanation': '''Usa IN para:
1. Meses: in January, in December
2. Años: in 2024, in 1990
3. Estaciones: in summer, in winter
4. Partes del día: in the morning, in the afternoon, in the evening
5. Períodos: in the 21st century, in the 1980s
6. Tiempo futuro: in 5 minutes, in 2 weeks

PERO: at night (no "in the night")''',
                    'example': 'She was born in 1995. We\'ll meet in the afternoon.',
                    'correct_usage': 'in March, in the evening, in 10 minutes',
                    'incorrect_usage': 'on 2024 ❌, at the morning ❌',
                    'common_errors': 'Usar "at" con partes del día excepto "night".',
                    'exceptions': 'in time (con tiempo de sobra) vs on time (puntual)'
                }
            ]
        },
        {
            'topic': 'Prepositions of Place - IN, ON, AT',
            'rules': [
                {
                    'rule': 'IN for enclosed spaces: in the room, in the box, in the city',
                    'detailed_explanation': '''Usa IN para:
1. Espacios cerrados: in the room, in the building
2. Países y ciudades: in Mexico, in Paris
3. Vehículos pequeños: in the car, in a taxi
4. Agua: in the pool, in the sea
5. Contenedores: in the box, in my pocket
6. Líneas/filas: in a row, in line

Expresiones:
- in bed
- in hospital (British)
- in the sky
- in a book/newspaper''',
                    'example': 'She lives in London. The keys are in my bag.',
                    'correct_usage': 'in the kitchen, in Spain, in the water',
                    'incorrect_usage': 'on the room ❌, at Paris ❌',
                    'common_errors': 'Usar "on" para países o ciudades.',
                    'exceptions': 'on the bus/train/plane (transporte público grande)'
                },
                {
                    'rule': 'ON for surfaces: on the table, on the wall, on the floor',
                    'detailed_explanation': '''Usa ON para:
1. Superficies: on the table, on the floor, on the wall
2. Transporte público: on the bus, on the train, on the plane
3. Calles: on Main Street, on Fifth Avenue
4. Islas pequeñas: on an island
5. Pisos de edificios: on the second floor
6. Tecnología: on TV, on the radio, on the internet

Expresiones:
- on the left/right
- on the way
- on foot''',
                    'example': 'The book is on the table. I saw it on TV.',
                    'correct_usage': 'on the bus, on the first floor, on the beach',
                    'incorrect_usage': 'in the table ❌, in the bus ❌',
                    'common_errors': 'Usar "in" para transporte público grande.',
                    'exceptions': 'in the car (vehículo pequeño) vs on the bus (grande)'
                },
                {
                    'rule': 'AT for specific points: at the door, at the bus stop, at home',
                    'detailed_explanation': '''Usa AT para:
1. Puntos específicos: at the door, at the corner
2. Direcciones: at 123 Main Street
3. Lugares comunes: at home, at work, at school
4. Eventos: at a party, at a concert
5. Edificios como puntos: at the bank, at the supermarket

Expresiones:
- at the top/bottom
- at the end
- at the beginning
- at someone\'s house: at John\'s''',
                    'example': 'Wait for me at the entrance. She\'s at work.',
                    'correct_usage': 'at the bus stop, at home, at the restaurant',
                    'incorrect_usage': 'in home ❌, on the bus stop ❌',
                    'common_errors': 'Decir "in home" en lugar de "at home".',
                    'exceptions': 'in the office (dentro) vs at the office (el lugar en general)'
                }
            ]
        },
        {
            'topic': 'Plurals - Regular and Irregular',
            'rules': [
                {
                    'rule': 'Regular plurals: add -s or -es',
                    'detailed_explanation': '''Reglas para plurales regulares:

1. Mayoría de sustantivos: +s
   cat → cats, dog → dogs, book → books

2. Palabras terminadas en -s, -ss, -sh, -ch, -x, -z: +es
   bus → buses, glass → glasses, box → boxes
   watch → watches, brush → brushes

3. Palabras terminadas en consonante + y: y → ies
   baby → babies, city → cities, story → stories
   PERO vocal + y: +s (boy → boys, key → keys)

4. Palabras terminadas en -f/-fe: f → ves
   knife → knives, wife → wives, leaf → leaves
   PERO algunos: roof → roofs, chef → chefs

5. Palabras terminadas en -o: +es (generalmente)
   potato → potatoes, tomato → tomatoes
   PERO: photo → photos, piano → pianos''',
                    'example': 'One cat, two cats. One box, three boxes.',
                    'correct_usage': 'babies, cities, watches, leaves',
                    'incorrect_usage': 'babys ❌, citys ❌, watchs ❌',
                    'common_errors': 'Olvidar cambiar -y a -ies o -f a -ves.',
                    'exceptions': 'Palabras extranjeras mantienen su plural: criterion → criteria'
                },
                {
                    'rule': 'Irregular plurals: complete list',
                    'detailed_explanation': '''Plurales irregulares comunes:

Cambio de vocal:
- man → men, woman → women
- foot → feet, tooth → teeth
- goose → geese, mouse → mice

Sin cambio:
- sheep → sheep, fish → fish
- deer → deer, aircraft → aircraft

Terminaciones especiales:
- child → children
- person → people (o persons formal)
- ox → oxen

Del latín/griego:
- analysis → analyses
- crisis → crises
- phenomenon → phenomena
- criterion → criteria
- cactus → cacti/cactuses
- focus → foci/focuses''',
                    'example': 'One child, many children. One foot, two feet.',
                    'correct_usage': 'men, women, children, mice, teeth',
                    'incorrect_usage': 'childs ❌, foots ❌, mouses ❌',
                    'common_errors': 'Aplicar reglas regulares a irregulares.',
                    'exceptions': 'Algunos aceptan ambas formas: fish/fishes (especies diferentes)'
                }
            ]
        },
        {
            'topic': 'Numbers and Counting',
            'rules': [
                {
                    'rule': 'Cardinal numbers: one, two, three... hundred, thousand',
                    'detailed_explanation': '''Números cardinales:
0 - zero/oh
1-10: one, two, three, four, five, six, seven, eight, nine, ten
11-19: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
20-90: twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
21-99: twenty-one, thirty-five, ninety-nine (con guión)

Grandes números:
100 - a/one hundred
1,000 - a/one thousand
1,000,000 - a/one million
1,000,000,000 - a/one billion

IMPORTANTE: hundred/thousand/million NO llevan -s cuando siguen a un número:
- two hundred (NO "two hundreds")
- five thousand (NO "five thousands")''',
                    'example': 'I have twenty-five books. The city has three million people.',
                    'correct_usage': 'two hundred people, five thousand dollars',
                    'incorrect_usage': 'two hundreds people ❌, five thousands dollars ❌',
                    'common_errors': 'Añadir -s a hundred/thousand después de números.',
                    'exceptions': 'hundreds of people, thousands of books (sin número específico)'
                },
                {
                    'rule': 'Ordinal numbers: first, second, third... for order and dates',
                    'detailed_explanation': '''Números ordinales (para orden y fechas):

1st - first, 2nd - second, 3rd - third
4th - fourth, 5th - fifth
6th - sixth, 7th - seventh, 8th - eighth
9th - ninth, 10th - tenth
11th - eleventh, 12th - twelfth
13th - thirteenth, 20th - twentieth
21st - twenty-first, 22nd - twenty-second
30th - thirtieth, 100th - hundredth

Uso:
- Fechas: January 1st (se dice "January first")
- Pisos: the 3rd floor
- Posición: She came first in the race
- Fracciones: one third, two fifths''',
                    'example': 'Today is March 15th. She lives on the 10th floor.',
                    'correct_usage': 'the first time, my second child, the twenty-first century',
                    'incorrect_usage': 'the one time ❌, March 15 ❌ (hablado)',
                    'common_errors': 'Usar cardinales donde se necesitan ordinales.',
                    'exceptions': 'En fechas escritas, cardinal es aceptable: March 15, 2024'
                }
            ]
        }
    ],
    
    # ==================== NIVEL A2 ====================
    'A2': [
        {
            'topic': 'Past Simple - Complete Guide',
            'rules': [
                {
                    'rule': 'Regular verbs: add -ed (worked, played, studied)',
                    'detailed_explanation': '''Formación de verbos regulares en pasado:

1. Mayoría: +ed
   work → worked, play → played, want → wanted

2. Verbos terminados en -e: +d
   live → lived, like → liked, arrive → arrived

3. Verbos terminados en consonante + y: y → ied
   study → studied, try → tried, carry → carried

4. Verbos de una sílaba (CVC): doblar consonante + ed
   stop → stopped, plan → planned, drop → dropped

Pronunciación de -ed:
- /t/ después de sonidos sordos: worked, helped, watched
- /d/ después de sonidos sonoros: played, lived, called
- /ɪd/ después de t/d: wanted, needed, decided''',
                    'example': 'She worked yesterday. They played football.',
                    'correct_usage': 'studied, stopped, lived, wanted',
                    'incorrect_usage': 'studyed ❌, stoped ❌, plaied ❌',
                    'common_errors': 'Olvidar doblar consonante o cambiar y→i.',
                    'exceptions': 'travel → traveled (US) / travelled (UK)'
                },
                {
                    'rule': 'Irregular verbs: memorize common patterns',
                    'detailed_explanation': '''Verbos irregulares más comunes:

Sin cambio: cut-cut, put-put, shut-shut, hit-hit

Cambio de vocal:
- i → a → u: swim-swam-swum, sing-sang-sung, drink-drank-drunk
- ee → e: meet-met, feed-fed, bleed-bled
- ow → ew → own: know-knew-known, grow-grew-grown, throw-threw-thrown
- eak → oke → oken: speak-spoke-spoken, break-broke-broken

Otros patrones:
- go-went-gone, do-did-done, have-had-had
- see-saw-seen, be-was/were-been
- make-made-made, say-said-said
- come-came-come, become-became-become''',
                    'example': 'I went to the store. She saw a movie.',
                    'correct_usage': 'He ate breakfast. They made a cake.',
                    'incorrect_usage': 'He eated breakfast. ❌ They maked a cake. ❌',
                    'common_errors': 'Añadir -ed a verbos irregulares.',
                    'exceptions': 'Algunos verbos tienen dos formas: dreamed/dreamt, learned/learnt'
                },
                {
                    'rule': 'Negative and questions: did not (didn\'t) + base form',
                    'detailed_explanation': '''Para negativos y preguntas en pasado:

Negativo: Subject + didn\'t + verb (base form)
- I didn\'t go (NO "I didn\'t went")
- She didn\'t eat (NO "She didn\'t ate")

Preguntas: Did + subject + verb (base form)?
- Did you see it? (NO "Did you saw it?")
- Did she work? (NO "Did she worked?")

Respuestas cortas:
- Yes, I did. / No, I didn\'t.

CLAVE: El auxiliar DID lleva la marca de pasado, así que el verbo principal va en forma base.''',
                    'example': 'Did you eat lunch? I didn\'t see him yesterday.',
                    'correct_usage': 'She didn\'t know. Did they arrive?',
                    'incorrect_usage': 'She didn\'t knew. ❌ Did they arrived? ❌',
                    'common_errors': 'Usar el verbo en pasado después de did/didn\'t.',
                    'exceptions': 'Con el verbo BE no se usa did: Was she there? She wasn\'t home.'
                }
            ]
        },
        {
            'topic': 'Past Continuous - Complete Guide',
            'rules': [
                {
                    'rule': 'Form: was/were + verb-ing',
                    'detailed_explanation': '''Formación del pasado continuo:

Afirmativo:
- I/He/She/It was + verb-ing
- You/We/They were + verb-ing

Negativo:
- wasn\'t / weren\'t + verb-ing

Pregunta:
- Was/Were + subject + verb-ing?

Uso principal:
1. Acción en progreso en un momento pasado
2. Contexto/escena para otra acción
3. Dos acciones simultáneas en el pasado''',
                    'example': 'I was sleeping when you called. They were watching TV.',
                    'correct_usage': 'She was working. Were you listening?',
                    'incorrect_usage': 'She was work. ❌ She were working. ❌',
                    'common_errors': 'Olvidar -ing o usar was/were incorrectamente.',
                    'exceptions': 'Verbos de estado generalmente no usan continuo: I was knowing ❌'
                },
                {
                    'rule': 'Past Simple vs Past Continuous: interrupted actions',
                    'detailed_explanation': '''Combinación de tiempos:

WHEN + Past Simple (acción corta que interrumpe)
WHILE + Past Continuous (acción larga de fondo)

Estructura común:
"I was doing X when Y happened"
- Past Continuous = acción larga/de fondo
- Past Simple = acción corta/interrupción

Ejemplos:
- I was taking a shower when the phone rang.
- While she was cooking, he arrived.
- They were playing when it started to rain.

Dos acciones simultáneas (ambas largas):
- While I was cooking, she was cleaning.''',
                    'example': 'I was reading when the lights went out.',
                    'correct_usage': 'While I was walking, I saw an accident.',
                    'incorrect_usage': 'While I walked, I was seeing an accident. ❌',
                    'common_errors': 'Invertir los tiempos verbales.',
                    'exceptions': 'Si ambas acciones son breves, usa Past Simple para ambas.'
                }
            ]
        },
        {
            'topic': 'Comparatives and Superlatives - Complete Guide',
            'rules': [
                {
                    'rule': 'Short adjectives (1 syllable): add -er/-est',
                    'detailed_explanation': '''Adjetivos cortos (1 sílaba):

Comparativo: adj + er + than
Superlativo: the + adj + est

Ejemplos:
- tall → taller → the tallest
- old → older → the oldest
- fast → faster → the fastest

Reglas de ortografía:
1. Terminados en -e: +r/+st (nice → nicer → nicest)
2. CVC cortos: doblar + er/est (big → bigger → biggest)
3. Terminados en -y: y → ier/iest (happy → happier → happiest)''',
                    'example': 'She is taller than me. He is the tallest in class.',
                    'correct_usage': 'bigger, happier, the fastest, the nicest',
                    'incorrect_usage': 'more tall ❌, the most fast ❌, biger ❌',
                    'common_errors': 'Usar more/most con adjetivos cortos u olvidar doblar consonantes.',
                    'exceptions': 'Algunos de 2 sílabas pueden usar ambas formas: cleverer/more clever'
                },
                {
                    'rule': 'Long adjectives (2+ syllables): use more/most',
                    'detailed_explanation': '''Adjetivos largos (2+ sílabas):

Comparativo: more + adj + than
Superlativo: the most + adj

Ejemplos:
- beautiful → more beautiful → the most beautiful
- interesting → more interesting → the most interesting
- expensive → more expensive → the most expensive

Menos:
- less + adj + than (comparativo)
- the least + adj (superlativo)

Ejemplo: This is less expensive than that.''',
                    'example': 'This book is more interesting than that one.',
                    'correct_usage': 'more comfortable, the most important',
                    'incorrect_usage': 'interestinger ❌, beautifulest ❌',
                    'common_errors': 'Añadir -er/-est a adjetivos largos.',
                    'exceptions': 'quiet, simple, clever pueden usar ambas formas'
                },
                {
                    'rule': 'Irregular comparatives and superlatives',
                    'detailed_explanation': '''Formas irregulares (memorizar):

good → better → the best
bad → worse → the worst
far → farther/further → the farthest/furthest
little → less → the least
much/many → more → the most
old → older/elder → the oldest/eldest

Notas:
- farther = distancia física
- further = distancia física O abstracta (further information)
- elder/eldest = solo para familia (my elder brother)''',
                    'example': 'This is better than that. She is the best student.',
                    'correct_usage': 'worse than, the worst, further information',
                    'incorrect_usage': 'more good ❌, badder ❌, the most bad ❌',
                    'common_errors': 'Aplicar reglas regulares a irregulares.',
                    'exceptions': 'old puede ser older (general) o elder (familia)'
                }
            ]
        },
        {
            'topic': 'Future with WILL and GOING TO',
            'rules': [
                {
                    'rule': 'WILL: spontaneous decisions, predictions, promises',
                    'detailed_explanation': '''Uso de WILL:

1. Decisiones espontáneas (en el momento):
   - The phone is ringing. I\'ll answer it.
   - It\'s cold. I\'ll close the window.

2. Predicciones basadas en opinión:
   - I think it will rain tomorrow.
   - She\'ll probably be late.

3. Promesas y ofertas:
   - I\'ll help you with that.
   - I won\'t tell anyone.

4. Hechos futuros:
   - The sun will rise at 6:30.
   - He\'ll be 30 next year.

Forma: will + base verb (won\'t para negativo)''',
                    'example': 'I\'ll call you later. She won\'t come to the party.',
                    'correct_usage': 'I think it will be sunny. I\'ll help you.',
                    'incorrect_usage': 'I\'ll to help you. ❌ I will going. ❌',
                    'common_errors': 'Añadir "to" después de will.',
                    'exceptions': 'En condicionales tipo 1: If it rains, I will stay home.'
                },
                {
                    'rule': 'GOING TO: plans and evidence-based predictions',
                    'detailed_explanation': '''Uso de GOING TO:

1. Planes e intenciones (decididos antes):
   - I\'m going to study medicine.
   - We\'re going to visit Paris next month.

2. Predicciones basadas en evidencia presente:
   - Look at those clouds! It\'s going to rain.
   - She\'s going to have a baby. (está embarazada)

Forma: am/is/are + going to + base verb

Comparación:
- WILL: decisión ahora → I\'ll have the pizza.
- GOING TO: decisión anterior → I\'m going to have the pizza. (ya lo decidí)''',
                    'example': 'I\'m going to buy a new car. Look out! You\'re going to fall!',
                    'correct_usage': 'We\'re going to travel. She\'s going to be a doctor.',
                    'incorrect_usage': 'I going to study. ❌ She going buy. ❌',
                    'common_errors': 'Olvidar am/is/are o la palabra "to".',
                    'exceptions': 'Informal: I\'m gonna go (spoken English)'
                },
                {
                    'rule': 'Present Continuous for fixed future arrangements',
                    'detailed_explanation': '''Present Continuous para futuro:

Para planes CONFIRMADOS con hora/lugar específico:
- I\'m meeting John at 3 PM. (cita confirmada)
- We\'re flying to London tomorrow. (boletos comprados)
- She\'s starting her new job on Monday.

Diferencia con GOING TO:
- GOING TO: intención (I\'m going to meet John)
- Present Continuous: arreglo confirmado (I\'m meeting John at 3)

Normalmente con verbos de movimiento/actividad:
come, go, leave, arrive, meet, have, start, fly, etc.''',
                    'example': 'I\'m having dinner with my parents tonight.',
                    'correct_usage': 'We\'re leaving at 8 AM. She\'s arriving tomorrow.',
                    'incorrect_usage': 'I\'m know the answer tomorrow. ❌',
                    'common_errors': 'Usar verbos de estado en continuo para futuro.',
                    'exceptions': 'Siempre necesita expresión de tiempo futuro para contexto.'
                }
            ]
        },
        {
            'topic': 'Modal Verbs - Can, Could, Should, Must',
            'rules': [
                {
                    'rule': 'CAN/CAN\'T for ability and permission',
                    'detailed_explanation': '''Usos de CAN:

1. Habilidad (poder hacer algo):
   - I can swim.
   - She can speak three languages.
   - Can you drive?

2. Permiso (informal):
   - Can I use your phone?
   - You can leave now.
   - You can\'t park here.

3. Posibilidad:
   - It can be very cold in winter.
   - Accidents can happen to anyone.

Forma: can + base verb (sin "to")
Negativo: cannot / can\'t''',
                    'example': 'I can play the piano. Can I borrow your pen?',
                    'correct_usage': 'She can\'t come. Can you help me?',
                    'incorrect_usage': 'I can to swim. ❌ She cans speak. ❌',
                    'common_errors': 'Añadir "to" o conjugar can con -s.',
                    'exceptions': 'Para habilidad pasada: could (I could swim when I was 5)'
                },
                {
                    'rule': 'COULD for past ability and polite requests',
                    'detailed_explanation': '''Usos de COULD:

1. Habilidad pasada:
   - I could run fast when I was young.
   - She could play the violin as a child.

2. Peticiones corteses:
   - Could you help me? (más formal que can)
   - Could I have some water, please?

3. Posibilidad (menos seguro que can):
   - It could rain later.
   - That could be true.

4. Sugerencias:
   - We could go to the cinema.
   - You could try calling him.''',
                    'example': 'Could you open the window? I could speak French as a child.',
                    'correct_usage': 'Could I ask a question? It could be expensive.',
                    'incorrect_usage': 'Could you to help? ❌ She could to swim. ❌',
                    'common_errors': 'Añadir "to" después de could.',
                    'exceptions': 'Para habilidad en una ocasión específica: was able to (I was able to escape)'
                },
                {
                    'rule': 'SHOULD/SHOULDN\'T for advice',
                    'detailed_explanation': '''Usos de SHOULD:

1. Consejos y recomendaciones:
   - You should see a doctor.
   - She shouldn\'t eat so much sugar.
   - Should I call him?

2. Obligación moral (más suave que must):
   - You should help your parents.
   - We should respect the environment.

3. Expectativas:
   - The package should arrive tomorrow.
   - He should be here by now.

Forma: should + base verb
Es más suave/educado que "must" o "have to"''',
                    'example': 'You should exercise more. You shouldn\'t smoke.',
                    'correct_usage': 'Should I bring anything? You should try this.',
                    'incorrect_usage': 'You should to study. ❌ She shoulds go. ❌',
                    'common_errors': 'Añadir "to" o conjugar should.',
                    'exceptions': 'Para arrepentimiento pasado: should have + past participle'
                },
                {
                    'rule': 'MUST/MUSTN\'T for obligation and prohibition',
                    'detailed_explanation': '''Usos de MUST:

1. Obligación fuerte (reglas, leyes):
   - You must wear a seatbelt.
   - Students must attend all classes.

2. Prohibición (mustn\'t):
   - You mustn\'t smoke here.
   - You mustn\'t tell anyone.

3. Deducción lógica (casi seguro):
   - She must be tired. (estoy seguro)
   - He must be at home. (es la única explicación)

MUST vs HAVE TO:
- must = obligación interna/del hablante
- have to = obligación externa/reglas''',
                    'example': 'You must be quiet in the library. You mustn\'t be late.',
                    'correct_usage': 'I must finish this. She must be hungry.',
                    'incorrect_usage': 'You must to go. ❌ She musts work. ❌',
                    'common_errors': 'Confundir mustn\'t (prohibición) con don\'t have to (no es necesario).',
                    'exceptions': 'Pasado de must (obligación) = had to'
                }
            ]
        },
        {
            'topic': 'Adverbs of Frequency',
            'rules': [
                {
                    'rule': 'Position: before main verb, after BE',
                    'detailed_explanation': '''Adverbios de frecuencia comunes:
always (100%), usually (80%), often (60%), sometimes (40%), 
rarely/seldom (20%), hardly ever (10%), never (0%)

Posición:
1. ANTES del verbo principal:
   - I always eat breakfast.
   - She never drinks coffee.

2. DESPUÉS del verbo BE:
   - He is always late.
   - They are never here.

3. CON auxiliares, entre auxiliar y verbo:
   - I have never seen that movie.
   - She can always help.''',
                    'example': 'I usually wake up at 7. She is always happy.',
                    'correct_usage': 'They often go there. He has never been to Paris.',
                    'incorrect_usage': 'I eat always breakfast. ❌ She late is always. ❌',
                    'common_errors': 'Poner el adverbio después del verbo principal o antes de BE.',
                    'exceptions': 'Sometimes/Usually pueden ir al inicio: Sometimes I work late.'
                },
                {
                    'rule': 'Expressions of frequency with time words',
                    'detailed_explanation': '''Expresiones de frecuencia (van al final):

Cada + tiempo:
- every day/week/month/year
- every Monday/morning

Una vez, dos veces, etc.:
- once a week
- twice a month
- three times a year

Otros:
- once in a while
- from time to time
- now and then

Posición: generalmente al FINAL de la oración
- I go to the gym three times a week.
- She visits her parents once a month.''',
                    'example': 'I exercise every day. We meet twice a week.',
                    'correct_usage': 'once a day, three times a month, every year',
                    'incorrect_usage': 'I every day exercise. ❌ twice the week ❌',
                    'common_errors': 'Poner la expresión en medio de la oración.',
                    'exceptions': 'Para énfasis pueden ir al inicio: Every day, I practice English.'
                }
            ]
        }
    ],
    
    # ==================== NIVEL B1 ====================
    'B1': [
        {
            'topic': 'Present Perfect - Complete Guide',
            'rules': [
                {
                    'rule': 'Form: have/has + past participle',
                    'detailed_explanation': '''Formación del Present Perfect:

Afirmativo:
- I/You/We/They have + past participle
- He/She/It has + past participle

Negativo: haven\'t / hasn\'t + past participle
Pregunta: Have/Has + subject + past participle?

Past Participle:
- Regulares: verb + ed (worked, played)
- Irregulares: tercera columna (gone, seen, eaten)

Contracciones: I\'ve, you\'ve, he\'s, she\'s, we\'ve, they\'ve''',
                    'example': 'I have finished my homework. She has lived here for 5 years.',
                    'correct_usage': 'Have you seen this movie? She\'s never been to Japan.',
                    'incorrect_usage': 'I have finish. ❌ She has went. ❌',
                    'common_errors': 'Usar infinitivo o pasado simple en lugar del participio.',
                    'exceptions': 'He\'s can ser "he is" o "he has" - el contexto aclara.'
                },
                {
                    'rule': 'Use 1: Life experiences (ever/never)',
                    'detailed_explanation': '''Present Perfect para experiencias de vida:

Preguntamos sobre experiencias usando EVER:
- Have you ever been to Paris?
- Has she ever eaten sushi?

Respondemos con NEVER para experiencias que no hemos tenido:
- I have never seen snow.
- She has never driven a car.

NUNCA usamos tiempo específico (yesterday, last year) con PP.
- I have been to Paris. ✓
- I have been to Paris last year. ❌ (usa Past Simple)''',
                    'example': 'Have you ever tried Thai food? I\'ve never met a celebrity.',
                    'correct_usage': 'I have visited 10 countries. She\'s never flown.',
                    'incorrect_usage': 'Have you ever went? ❌ I never have seen. ❌',
                    'common_errors': 'Usar Past Simple con ever/never o poner never después del verbo.',
                    'exceptions': 'This is the best pizza I have ever eaten. (superlativo + ever)'
                },
                {
                    'rule': 'Use 2: Actions with present result (just, already, yet)',
                    'detailed_explanation': '''Present Perfect para acciones recientes con resultado presente:

JUST = acabar de (reciente)
- I have just finished. (acabo de terminar)
- She\'s just arrived.

ALREADY = ya (antes de lo esperado, afirmativo)
- I have already done it.
- She\'s already left.

YET = ya/todavía (preguntas y negativos, al final)
- Have you finished yet? (¿Ya terminaste?)
- I haven\'t eaten yet. (Todavía no he comido)

Posición:
- just/already: entre have y el participio
- yet: al final de la oración''',
                    'example': 'I\'ve just woken up. Have you called her yet?',
                    'correct_usage': 'She has already eaten. They haven\'t arrived yet.',
                    'incorrect_usage': 'I have finished just. ❌ Have you yet called? ❌',
                    'common_errors': 'Posición incorrecta de just/already/yet.',
                    'exceptions': 'Already puede ir al final para énfasis: You\'ve finished already?!'
                },
                {
                    'rule': 'Use 3: Unfinished time with FOR and SINCE',
                    'detailed_explanation': '''Present Perfect para situaciones que continúan:

FOR + duración (cuánto tiempo)
- I have lived here for 5 years.
- She has worked here for 2 months.
- for a long time, for ages, for centuries

SINCE + punto de inicio (desde cuándo)
- I have lived here since 2019.
- She has worked here since January.
- since yesterday, since I was a child

Pregunta: How long have you...?
- How long have you lived here?
- How long have you known him?

CLAVE: La acción empezó en el pasado y continúa hasta ahora.''',
                    'example': 'I have known her since 2015. He has been sick for a week.',
                    'correct_usage': 'for 3 hours, since Monday, since we met',
                    'incorrect_usage': 'I have lived here since 5 years. ❌ for 2019 ❌',
                    'common_errors': 'Confundir for/since o usar Past Simple.',
                    'exceptions': 'It\'s been 5 years since I saw him. (= I haven\'t seen him for 5 years)'
                }
            ]
        },
        {
            'topic': 'First and Second Conditionals',
            'rules': [
                {
                    'rule': 'First Conditional: If + present, will + base verb',
                    'detailed_explanation': '''Primer Condicional - Situaciones reales/posibles:

Estructura:
IF + Present Simple, WILL + base verb
- If it rains, I will stay home.
- I will call you if I have time.

Uso: situaciones futuras reales o probables
- If you study, you will pass.
- If she comes, we will go together.

Otras combinaciones:
- If + present, can/may/might + verb
- If + present, imperative
  "If you see him, tell him to call me."

La cláusula IF puede ir primero o segundo:
- If I see her, I\'ll tell her.
- I\'ll tell her if I see her.''',
                    'example': 'If you don\'t hurry, you will miss the bus.',
                    'correct_usage': 'If it snows, we\'ll build a snowman.',
                    'incorrect_usage': 'If it will rain, I will stay. ❌',
                    'common_errors': 'Usar will en la cláusula IF.',
                    'exceptions': 'Will puede usarse en IF para peticiones corteses: If you will wait here...'
                },
                {
                    'rule': 'Second Conditional: If + past, would + base verb',
                    'detailed_explanation': '''Segundo Condicional - Situaciones hipotéticas/irreales:

Estructura:
IF + Past Simple, WOULD + base verb
- If I had money, I would travel.
- If she knew, she would tell us.

Uso: situaciones imaginarias o improbables
- If I were rich, I would buy a yacht.
- If I could fly, I would go everywhere.

WERE vs WAS:
En lenguaje formal, usamos WERE para todos los sujetos:
- If I were you, I would accept.
- If she were here, she would help.

En informal, "was" es aceptable con I/he/she/it.''',
                    'example': 'If I won the lottery, I would quit my job.',
                    'correct_usage': 'If I were you, I would apologize.',
                    'incorrect_usage': 'If I would have money, I would travel. ❌',
                    'common_errors': 'Usar would en la cláusula IF.',
                    'exceptions': 'Could/might pueden reemplazar would: If I had time, I could/might help.'
                },
                {
                    'rule': 'First vs Second Conditional: real vs unreal',
                    'detailed_explanation': '''Comparación de condicionales:

FIRST CONDITIONAL (real/posible):
- If I have time tomorrow, I will visit you.
  (Es posible que tenga tiempo)

SECOND CONDITIONAL (irreal/hipotético):
- If I had time, I would visit you.
  (No tengo tiempo, es imaginario)

Ejemplos comparados:
- If it rains (probable), I will take an umbrella.
- If it rained in the Sahara (improbable), people would be surprised.

- If I see her (posible), I\'ll tell her.
- If I saw a ghost (hipotético), I would scream.''',
                    'example': 'If I have money (maybe I will), I\'ll buy it. If I had a million (I don\'t), I\'d travel.',
                    'correct_usage': 'Use 1st for realistic future, 2nd for imagination.',
                    'incorrect_usage': 'If I will have time... ❌ If I would be rich... ❌',
                    'common_errors': 'Elegir el condicional incorrecto para la situación.',
                    'exceptions': 'Some situations can use either depending on speaker\'s perspective.'
                }
            ]
        },
        {
            'topic': 'Relative Clauses - Who, Which, That, Where, When',
            'rules': [
                {
                    'rule': 'WHO for people, WHICH for things, THAT for both',
                    'detailed_explanation': '''Pronombres relativos básicos:

WHO = para personas
- The man who called is my uncle.
- I met a woman who works at Google.

WHICH = para cosas y animales
- The book which I bought is interesting.
- I have a cat which loves to play.

THAT = para personas O cosas (informal)
- The man that called is my uncle.
- The book that I bought is interesting.

WHOSE = posesión (de quien)
- The woman whose car was stolen is upset.
- That\'s the author whose books I love.''',
                    'example': 'The teacher who taught me is retiring. The car which I want is expensive.',
                    'correct_usage': 'The girl who/that won is my sister. The movie which/that we saw was great.',
                    'incorrect_usage': 'The man which called... ❌ The book who I read... ❌',
                    'common_errors': 'Usar who para cosas o which para personas.',
                    'exceptions': 'Who/which no se pueden omitir cuando son sujeto de la cláusula.'
                },
                {
                    'rule': 'WHERE for places, WHEN for times, WHY for reasons',
                    'detailed_explanation': '''Adverbios relativos:

WHERE = para lugares
- This is the restaurant where we met.
- The city where I was born is beautiful.

WHEN = para tiempos
- I remember the day when we first met.
- The 1990s was a time when music was great.

WHY = para razones (solo con "reason")
- That\'s the reason why I left.
- Tell me the reason why you\'re upset.

Estos pueden omitirse en inglés informal:
- This is the restaurant (where) we met.
- I remember the day (when) we met.''',
                    'example': 'Paris is the city where I want to live. Summer is when I feel happiest.',
                    'correct_usage': 'The hotel where we stayed was lovely. The moment when I realized...',
                    'incorrect_usage': 'The place when we met. ❌ The time where it happened. ❌',
                    'common_errors': 'Confundir where y when.',
                    'exceptions': 'Where puede usarse con abstractos: a situation where...'
                },
                {
                    'rule': 'Defining vs Non-defining relative clauses',
                    'detailed_explanation': '''DEFINING (especificativa) - sin comas:
- Identifica de qué/quién hablamos
- Información esencial
- THAT puede usarse
- El pronombre puede omitirse si es objeto

"The woman who lives next door is nice."
(¿Cuál mujer? La que vive al lado)

NON-DEFINING (explicativa) - CON comas:
- Añade información extra
- Información no esencial
- THAT no puede usarse
- El pronombre NUNCA se omite

"My mother, who is 60, still works."
(Ya sabemos quién es, añadimos info)''',
                    'example': 'The car that I bought is red. (defining) My car, which is red, is fast. (non-defining)',
                    'correct_usage': 'Paris, which is in France, is beautiful. The book I read was good.',
                    'incorrect_usage': 'My mother that is 60... ❌ Paris that is in France... ❌',
                    'common_errors': 'Usar THAT en non-defining u olvidar las comas.',
                    'exceptions': 'Los pronombres relativos como objeto pueden omitirse en defining clauses.'
                }
            ]
        },
        {
            'topic': 'Passive Voice - Present and Past',
            'rules': [
                {
                    'rule': 'Form: BE + past participle',
                    'detailed_explanation': '''Formación de la voz pasiva:

Activa → Pasiva:
Subject + Verb + Object → Object + BE + Past Participle (+ by + Agent)

PRESENTE SIMPLE:
- Active: They make cars in Japan.
- Passive: Cars are made in Japan.

PASADO SIMPLE:
- Active: Someone stole my bike.
- Passive: My bike was stolen.

PRESENTE PERFECTO:
- Active: They have finished the project.
- Passive: The project has been finished.

FUTURO:
- Active: They will announce the winner.
- Passive: The winner will be announced.''',
                    'example': 'English is spoken here. The window was broken by the ball.',
                    'correct_usage': 'The letter was written yesterday. These phones are made in China.',
                    'incorrect_usage': 'The book was wrote. ❌ Spanish is speak here. ❌',
                    'common_errors': 'Usar el infinitivo o pasado simple en lugar del participio.',
                    'exceptions': 'GET + past participle es más informal: He got fired.'
                },
                {
                    'rule': 'When to use passive voice',
                    'detailed_explanation': '''Cuándo usar la voz pasiva:

1. El agente es desconocido:
   - My car was stolen. (no sé quién)
   
2. El agente es obvio o no importante:
   - The criminal was arrested. (obviamente la policía)
   
3. Para enfatizar la acción o el objeto:
   - The Mona Lisa was painted by Da Vinci.
   - The new iPhone was released yesterday.

4. En textos formales/científicos/periodísticos:
   - The experiment was conducted in 2023.
   - Three people were injured in the accident.

5. Para ser diplomático/evitar culpar:
   - Mistakes were made. (evita decir quién)''',
                    'example': 'The pyramids were built thousands of years ago. The package will be delivered tomorrow.',
                    'correct_usage': 'The meeting has been cancelled. The house is being renovated.',
                    'incorrect_usage': 'The report writes every week. ❌',
                    'common_errors': 'Usar pasiva cuando la activa es más natural y directa.',
                    'exceptions': 'BY + agente solo se incluye si es importante o inesperado.'
                }
            ]
        },
        {
            'topic': 'Reported Speech - Statements and Questions',
            'rules': [
                {
                    'rule': 'Reporting statements: tense shift',
                    'detailed_explanation': '''Cambio de tiempos al reportar:

PRESENTE → PASADO
- "I am happy" → She said she was happy.
- "I work here" → He said he worked there.

PASADO → PASADO PERFECTO
- "I saw him" → She said she had seen him.
- "I went home" → He said he had gone home.

PRESENTE PERFECTO → PASADO PERFECTO
- "I have finished" → She said she had finished.

WILL → WOULD
- "I will come" → He said he would come.

CAN → COULD
- "I can swim" → She said she could swim.

MUST → HAD TO
- "I must go" → He said he had to go.''',
                    'example': '"I love you" → He said he loved me. "I will help" → She said she would help.',
                    'correct_usage': 'He said he was tired. She told me she had seen the movie.',
                    'incorrect_usage': 'He said he is tired. ❌ She told me she has seen. ❌',
                    'common_errors': 'No hacer el cambio de tiempo o confundir said/told.',
                    'exceptions': 'Si es verdad general, el cambio es opcional: He said the Earth is/was round.'
                },
                {
                    'rule': 'Reporting questions: word order changes',
                    'detailed_explanation': '''Reportar preguntas:

1. Usa IF/WHETHER para preguntas sí/no:
   - "Do you like coffee?" → She asked if I liked coffee.
   - "Are you coming?" → He asked whether I was coming.

2. Mantén la palabra WH para preguntas abiertas:
   - "Where do you live?" → She asked where I lived.
   - "What is your name?" → He asked what my name was.

IMPORTANTE: Cambia a orden afirmativo (sin do/does/did)
- "Where do you work?" → She asked where I worked.
   (NO: She asked where did I work ❌)

Cambios adicionales:
- this → that, here → there, now → then
- today → that day, tomorrow → the next day''',
                    'example': '"Where is the station?" → He asked where the station was.',
                    'correct_usage': 'She asked if I was hungry. He asked what time it was.',
                    'incorrect_usage': 'She asked if was I hungry. ❌ He asked what time was it. ❌',
                    'common_errors': 'Mantener el orden de pregunta o usar signos de interrogación.',
                    'exceptions': 'Con verbos como wonder, el orden siempre es afirmativo.'
                },
                {
                    'rule': 'SAY vs TELL: when to use each',
                    'detailed_explanation': '''Diferencia entre SAY y TELL:

SAY = no necesita persona (o + to + person)
- She said she was tired.
- She said to me that she was tired.

TELL = siempre necesita persona (sin to)
- She told me she was tired.
- He told the children a story.

Expresiones fijas con TELL:
- tell the truth / tell a lie
- tell a story / tell a joke
- tell the time / tell the difference
- tell someone\'s fortune

Expresiones fijas con SAY:
- say hello / say goodbye
- say yes / say no
- say a prayer / say a few words''',
                    'example': 'She said she was happy. She told me she was happy.',
                    'correct_usage': 'He told me the news. She said it was late.',
                    'incorrect_usage': 'He said me the news. ❌ She told it was late. ❌',
                    'common_errors': 'Usar TELL sin persona o SAY con persona directa.',
                    'exceptions': 'Tell puede usarse sin persona en: tell the truth, tell a story'
                }
            ]
        }
    ],
    
    # ==================== NIVEL B2 ====================
    'B2': [
        {
            'topic': 'Third Conditional and Mixed Conditionals',
            'rules': [
                {
                    'rule': 'Third Conditional: If + past perfect, would have + past participle',
                    'detailed_explanation': '''Tercer Condicional - Situaciones pasadas irreales:

Estructura:
IF + Past Perfect, WOULD HAVE + Past Participle
- If I had studied, I would have passed.
- If she had known, she would have helped.

Uso: imaginar un pasado diferente
- If I had woken up earlier, I wouldn\'t have missed the bus.
  (Pero no me desperté temprano, y perdí el bus)

Contracciones:
- If I\'d known, I\'d have told you.
- If she hadn\'t left, she would\'ve seen him.

El tercer condicional expresa arrepentimiento o reflexión sobre el pasado.''',
                    'example': 'If I had known you were sick, I would have visited you.',
                    'correct_usage': 'If they had arrived earlier, they would have caught the train.',
                    'incorrect_usage': 'If I would have studied, I would have passed. ❌',
                    'common_errors': 'Usar would have en la cláusula IF.',
                    'exceptions': 'Could/might pueden reemplazar would: If I\'d known, I might have helped.'
                },
                {
                    'rule': 'Mixed Conditionals: combining different time references',
                    'detailed_explanation': '''Condicionales Mixtos - Mezclando tiempos:

TIPO 1: Pasado irreal → Presente irreal
If + Past Perfect, would + base verb
- If I had studied medicine, I would be a doctor now.
  (No estudié medicina, así que no soy médico)

TIPO 2: Presente irreal → Pasado irreal  
If + Past Simple, would have + past participle
- If I were rich, I would have bought that house.
  (No soy rico, así que no la compré)

Estos se usan cuando la condición y el resultado son de diferentes tiempos.''',
                    'example': 'If I had saved money, I would be traveling now. If I spoke Chinese, I would have taken that job.',
                    'correct_usage': 'If she hadn\'t moved, she would still live here.',
                    'incorrect_usage': 'If I would be rich, I would have bought it. ❌',
                    'common_errors': 'Confundir qué parte es pasada y cuál es presente.',
                    'exceptions': 'El contexto temporal debe estar claro por la situación o adverbios.'
                }
            ]
        },
        {
            'topic': 'Future Perfect and Future Continuous',
            'rules': [
                {
                    'rule': 'Future Perfect: will have + past participle',
                    'detailed_explanation': '''Future Perfect - Acciones completadas antes de un punto futuro:

Estructura: will have + past participle
- By next year, I will have graduated.
- By 6 PM, she will have finished work.

Uso: ver el futuro desde un punto aún más futuro
- By 2030, we will have moved to a new house.
- By the time you arrive, I will have cooked dinner.

Marcadores de tiempo:
- by + tiempo futuro (by tomorrow, by next week)
- by the time + present clause
- in + período (in 5 years, in a decade)''',
                    'example': 'By December, I will have worked here for 10 years.',
                    'correct_usage': 'By tonight, I\'ll have read the whole book.',
                    'incorrect_usage': 'I will have finish by tomorrow. ❌',
                    'common_errors': 'Usar infinitivo en lugar del participio pasado.',
                    'exceptions': 'Negativo: will not have (won\'t have) + past participle'
                },
                {
                    'rule': 'Future Continuous: will be + verb-ing',
                    'detailed_explanation': '''Future Continuous - Acciones en progreso en el futuro:

Estructura: will be + verb-ing
- At 8 PM, I will be watching TV.
- This time tomorrow, she will be flying to Paris.

Usos:
1. Acción en progreso en un momento futuro:
   - At midnight, everyone will be celebrating.

2. Planes/arreglos futuros (formal):
   - I will be meeting the client at 3 PM.

3. Preguntas corteses sobre planes:
   - Will you be using the car tonight?

4. Predicciones sobre el presente:
   - She will be sleeping now. (I imagine)''',
                    'example': 'This time next week, I\'ll be lying on a beach.',
                    'correct_usage': 'At 10 AM, we\'ll be having the meeting.',
                    'incorrect_usage': 'I will be watch TV at 8. ❌',
                    'common_errors': 'Olvidar -ing en el verbo principal.',
                    'exceptions': 'También expresa certeza cortés: You\'ll be hearing from us soon.'
                }
            ]
        },
        {
            'topic': 'Wish and If Only',
            'rules': [
                {
                    'rule': 'Wish/If only + past simple for present regrets',
                    'detailed_explanation': '''Deseos sobre el presente (situación irreal ahora):

WISH/IF ONLY + Past Simple
- I wish I had more money. (no tengo suficiente)
- If only I knew the answer. (no lo sé)
- I wish I could help. (no puedo)

Con BE, usamos WERE (formal) para todos:
- I wish I were taller.
- If only she were here.

Esto expresa insatisfacción con el presente:
- I wish my apartment were bigger.
  = I\'m not happy because my apartment is small.''',
                    'example': 'I wish I spoke French. If only I had a car.',
                    'correct_usage': 'I wish I knew her name. If only he were more patient.',
                    'incorrect_usage': 'I wish I have more time. ❌ I wish I can swim. ❌',
                    'common_errors': 'Usar presente en lugar de pasado con wish.',
                    'exceptions': 'Was es aceptable en inglés informal: I wish I was there.'
                },
                {
                    'rule': 'Wish/If only + past perfect for past regrets',
                    'detailed_explanation': '''Deseos/arrepentimientos sobre el pasado:

WISH/IF ONLY + Past Perfect
- I wish I had studied harder. (no estudié)
- If only I hadn\'t said that. (lo dije)
- I wish I had listened to you. (no escuché)

Esto expresa arrepentimiento - quisieras haber hecho algo diferente:
- I wish I had bought that house.
  = I regret not buying that house.

- If only I hadn\'t eaten so much.
  = I regret eating so much.''',
                    'example': 'I wish I had accepted the job offer. If only I\'d known earlier.',
                    'correct_usage': 'She wishes she had traveled more when young.',
                    'incorrect_usage': 'I wish I studied harder. ❌ (para el pasado)',
                    'common_errors': 'Usar past simple para arrepentimientos pasados.',
                    'exceptions': 'If only es más enfático/emocional que wish.'
                },
                {
                    'rule': 'Wish + would for complaints and requests',
                    'detailed_explanation': '''Deseos sobre acciones de otros (queja/petición):

WISH + Subject + WOULD + base verb
- I wish you would listen to me. (no me escuchas)
- I wish it would stop raining. (sigue lloviendo)
- If only he would call. (no llama)

Uso:
1. Quejas sobre comportamiento repetido:
   - I wish she wouldn\'t smoke inside.
   
2. Deseo de que algo cambie:
   - I wish they would fix the road.

NUNCA: I wish I would...
(usamos wish + past simple para nosotros mismos)''',
                    'example': 'I wish you would be quiet. If only the neighbors would turn down the music.',
                    'correct_usage': 'I wish he would stop complaining.',
                    'incorrect_usage': 'I wish I would be taller. ❌',
                    'common_errors': 'Usar wish + would con uno mismo.',
                    'exceptions': 'Para eventos naturales/incontrolables: I wish it would rain.'
                }
            ]
        },
        {
            'topic': 'Inversion for Emphasis',
            'rules': [
                {
                    'rule': 'Negative adverbs at the beginning: Never have I...',
                    'detailed_explanation': '''Inversión con adverbios negativos:

Cuando ponemos adverbios negativos al inicio, invertimos sujeto y auxiliar:

NEVER + aux + subject + verb
- Never have I seen such a thing.
- Never had she felt so happy.

RARELY/SELDOM + aux + subject + verb
- Rarely do we see such talent.
- Seldom have I met someone so kind.

HARDLY/BARELY/SCARCELY + aux + subject + verb
- Hardly had I arrived when the phone rang.
- Scarcely had she finished when...

NO SOONER...THAN
- No sooner had I left than it started raining.''',
                    'example': 'Never have I been so embarrassed. Rarely does he make mistakes.',
                    'correct_usage': 'Seldom do they visit. Hardly had we begun when...',
                    'incorrect_usage': 'Never I have seen... ❌ Rarely he does... ❌',
                    'common_errors': 'Mantener el orden normal después de adverbio negativo.',
                    'exceptions': 'Esto es formal/literario; en conversación normal se evita.'
                },
                {
                    'rule': 'Only + time/after/when: Only then did I realize...',
                    'detailed_explanation': '''Inversión con ONLY + expresiones:

ONLY + time expression + aux + subject
- Only yesterday did I hear the news.
- Only later did she understand.

ONLY + after/when + normal clause, + inverted clause
- Only after the meeting did we discuss it.
- Only when I saw him did I believe it.

ONLY + by + -ing + aux + subject
- Only by working hard can you succeed.

NOT ONLY...BUT ALSO (inversión en la primera parte)
- Not only did he win, but he also broke the record.''',
                    'example': 'Only then did I understand. Not only is she smart, but also kind.',
                    'correct_usage': 'Only after reading it did I see the error.',
                    'incorrect_usage': 'Only then I understood. ❌',
                    'common_errors': 'Olvidar invertir después de "only + expression".',
                    'exceptions': 'Sin expresión, "only" no causa inversión: I only saw her once.'
                }
            ]
        },
        {
            'topic': 'Cleft Sentences for Emphasis',
            'rules': [
                {
                    'rule': 'IT + BE + focus + that/who clause',
                    'detailed_explanation': '''Oraciones hendidas con IT:

Estructura: It + BE + elemento enfatizado + that/who + resto

Original: John broke the window.

Enfatizando diferentes elementos:
- It was JOHN who broke the window. (quién)
- It was THE WINDOW that John broke. (qué)
- It was YESTERDAY that John broke the window. (cuándo)

Usos:
- Contrastar información
- Corregir malentendidos
- Dar información sorprendente

"It wasn\'t me who ate the cake, it was Tom!"''',
                    'example': 'It was in Paris that they first met. It\'s the noise that bothers me.',
                    'correct_usage': 'It was Mary who told me. It\'s this song that I love.',
                    'incorrect_usage': 'It was John what broke it. ❌',
                    'common_errors': 'Usar what en lugar de that/who.',
                    'exceptions': 'Con personas, who es preferible pero that es aceptable.'
                },
                {
                    'rule': 'What clause + BE + focus',
                    'detailed_explanation': '''Oraciones hendidas con WHAT (pseudo-cleft):

Estructura: What + clause + BE + elemento enfatizado

Original: I need a vacation.
Énfasis: What I need is a vacation.

Original: She said something strange.
Énfasis: What she said was strange.

Variaciones:
- What I want is peace.
- What happened was terrible.
- What you should do is apologize.

THE THING THAT... también funciona:
- The thing that annoys me is his attitude.
- The reason why I left was the noise.''',
                    'example': 'What I like most is the view. What she needs is rest.',
                    'correct_usage': 'What bothers me is the price. What he said was rude.',
                    'incorrect_usage': 'What I need are money. ❌',
                    'common_errors': 'Problemas de concordancia con el verbo BE.',
                    'exceptions': 'Con plurales: What I bought were books. (formal)'
                }
            ]
        }
    ],
    
    # ==================== NIVEL C1-C2 ====================
    'C1': [
        {
            'topic': 'Advanced Modal Verbs',
            'rules': [
                {
                    'rule': 'Modals of deduction: must/can\'t/might + have + past participle',
                    'detailed_explanation': '''Deducciones sobre el pasado:

MUST HAVE + PP = casi seguro que pasó
- He must have forgotten. (Estoy casi seguro)
- They must have left early.

CAN\'T/COULDN\'T HAVE + PP = imposible que pasó
- She can\'t have said that. (Es imposible)
- He couldn\'t have known.

MAY/MIGHT/COULD HAVE + PP = posiblemente pasó
- She might have missed the train.
- They could have gotten lost.

SHOULD HAVE / OUGHT TO HAVE + PP = era esperado pero no pasó
- He should have called by now.
- They ought to have arrived.''',
                    'example': 'She must have been tired. He can\'t have known the answer.',
                    'correct_usage': 'They might have forgotten. You shouldn\'t have worried.',
                    'incorrect_usage': 'He must forgot. ❌ She can\'t said that. ❌',
                    'common_errors': 'Olvidar "have" o usar el infinitivo en lugar del participio.',
                    'exceptions': 'Needn\'t have = no era necesario pero se hizo: You needn\'t have bought flowers.'
                },
                {
                    'rule': 'Would for past habits vs Used to',
                    'detailed_explanation': '''WOULD vs USED TO para hábitos pasados:

USED TO: hábitos Y estados pasados
- I used to live in Paris. (estado)
- I used to play tennis. (hábito)

WOULD: solo hábitos pasados (no estados)
- Every summer, we would go to the beach.
- She would always bring me coffee.

NO se puede usar WOULD con:
- Estados: I would live in Paris ❌
- Verbos de estado: She would know him ❌

WOULD suena más nostálgico/narrativo:
"When I was young, I would spend hours reading..."''',
                    'example': 'We would visit grandma every Sunday. I used to be afraid of dogs.',
                    'correct_usage': 'She would always make us laugh. I used to have a cat.',
                    'incorrect_usage': 'I would live in London (as a state). ❌',
                    'common_errors': 'Usar would con verbos de estado o para situaciones no habituales.',
                    'exceptions': 'Would también expresa voluntad pasada: He wouldn\'t listen to me.'
                }
            ]
        },
        {
            'topic': 'Subjunctive Mood',
            'rules': [
                {
                    'rule': 'Formal subjunctive after verbs of suggestion/demand',
                    'detailed_explanation': '''El subjuntivo formal (base form) después de ciertos verbos:

Verbos que requieren subjuntivo:
suggest, recommend, demand, insist, request, require, propose, ask

Estructura: Verb + (that) + subject + BASE FORM
- I suggest (that) he leave now.
- They demanded (that) she be present.
- It is essential (that) everyone attend.

NOTA: usamos la forma base para todos los sujetos:
- I suggest he GO (no "goes")
- She insisted I BE there (no "am/was")

En inglés británico, "should" es alternativa:
- I suggest he should leave.''',
                    'example': 'The doctor recommended that she take more rest. It\'s vital that he be informed.',
                    'correct_usage': 'I insisted that he pay me back. It\'s important that this be done.',
                    'incorrect_usage': 'I suggest that he leaves. ❌ (en formal)',
                    'common_errors': 'Usar formas conjugadas en lugar de la base.',
                    'exceptions': 'El subjuntivo es más común en inglés americano formal.'
                },
                {
                    'rule': 'Subjunctive in fixed expressions',
                    'detailed_explanation': '''Subjuntivo en expresiones fijas:

Expresiones comunes con subjuntivo:
- God bless you!
- God forbid!
- Long live the king!
- Heaven help us!
- Be that as it may...
- Come what may...
- Suffice it to say...
- Be it known that...
- Far be it from me to...
- If need be...

También en condicionales formales:
- If I were you... (were, no was)
- If it be necessary... (muy formal)
- Were I to know... (inversión formal)''',
                    'example': 'Be that as it may, we must continue. Far be it from me to criticize.',
                    'correct_usage': 'Long live the queen! Come what may, I\'ll be there.',
                    'incorrect_usage': 'God blesses you! ❌',
                    'common_errors': 'No reconocer estas expresiones como subjuntivo.',
                    'exceptions': 'Muchas de estas expresiones son arcaicas pero aún se usan.'
                }
            ]
        },
        {
            'topic': 'Participle Clauses',
            'rules': [
                {
                    'rule': 'Present participle (-ing) for simultaneous or causal actions',
                    'detailed_explanation': '''Cláusulas de participio presente:

Acciones simultáneas:
- Walking down the street, I saw an old friend.
  (= While I was walking...)

Causa/razón:
- Being tired, she went to bed early.
  (= Because she was tired...)

Después de conjunciones:
- After finishing dinner, we watched a movie.
- Before leaving, check your pockets.
- While waiting, I read a book.

El sujeto debe ser el mismo en ambas partes:
✓ Seeing the rain, I took an umbrella. (I saw, I took)
✗ Seeing the rain, the umbrella was taken. (misplaced modifier)''',
                    'example': 'Having finished work, she went home. Not knowing what to do, he called for help.',
                    'correct_usage': 'Standing at the window, I noticed a strange car.',
                    'incorrect_usage': 'Walking to school, the rain started. ❌',
                    'common_errors': 'Participio colgante (dangling modifier) - sujetos diferentes.',
                    'exceptions': 'Algunos participios colgantes son aceptables: Generally speaking, Considering...'
                },
                {
                    'rule': 'Past participle for passive meaning',
                    'detailed_explanation': '''Cláusulas de participio pasado (sentido pasivo):

Estructura: Past Participle + (by agent), main clause

Ejemplos:
- Written in 1605, the play is still popular.
  (= The play, which was written in 1605...)
  
- Exhausted by the journey, they fell asleep immediately.
  (= Because they were exhausted...)

- Shocked by the news, she couldn\'t speak.
  (= She was shocked by the news, so...)

Puede ir al principio o después del sujeto:
- The painting, discovered in 1920, is priceless.
- Discovered in 1920, the painting is priceless.''',
                    'example': 'Built in 1920, the house is now a museum. Surprised by the question, he hesitated.',
                    'correct_usage': 'Seen from above, the city looks beautiful.',
                    'incorrect_usage': 'Seeing from above, the city... ❌ (la ciudad no ve)',
                    'common_errors': 'Confundir cuándo usar -ing (activo) vs -ed (pasivo).',
                    'exceptions': 'Algunos participios funcionan como adjetivos: concerned, interested.'
                },
                {
                    'rule': 'Perfect participle for prior actions',
                    'detailed_explanation': '''Participio perfecto para acciones anteriores:

HAVING + Past Participle = después de / porque antes

- Having finished the exam, she left.
  (= After she had finished...)
  
- Having lived in Japan, he speaks Japanese.
  (= Because he has lived...)

Versión negativa: NOT HAVING + PP
- Not having heard the news, I was surprised.

Versión pasiva: HAVING BEEN + PP
- Having been warned, he was careful.
- Having been rejected twice, she gave up.''',
                    'example': 'Having eaten, we continued our journey. Having been invited, I felt I should go.',
                    'correct_usage': 'Not having slept well, I was tired all day.',
                    'incorrect_usage': 'Having finished, the work was good. ❌',
                    'common_errors': 'Usar having + base form o having + past tense.',
                    'exceptions': 'Having said that = dicho esto (expresión fija)'
                }
            ]
        }
    ]
}


def seed_extended_grammar():
    """Poblar la base de datos con temas gramaticales extensos"""
    with app.app_context():
        print("=" * 60)
        print("🎓 AGREGANDO TEMAS GRAMATICALES EXTENSOS")
        print("=" * 60)
        
        total_topics = 0
        total_rules = 0
        
        for level, topics in GRAMMAR_TOPICS.items():
            print(f"\n📚 Procesando nivel {level}...")
            
            # Buscar unidades de este nivel
            units = Unit.query.filter(Unit.title.like(f'%{level}%')).order_by(Unit.unit_number).all()
            
            if not units:
                print(f"  ⚠️ No se encontraron unidades para {level}")
                continue
            
            for topic_data in topics:
                topic_name = topic_data['topic']
                
                # Distribuir entre las unidades del nivel
                unit_index = total_topics % len(units)
                target_unit = units[unit_index]
                
                print(f"  📖 {topic_name} → Unit {target_unit.unit_number}")
                
                for i, rule_data in enumerate(topic_data['rules']):
                    # Verificar si ya existe
                    existing = GrammarRule.query.filter_by(
                        unit_id=target_unit.id,
                        topic=topic_name,
                        rule=rule_data['rule']
                    ).first()
                    
                    if existing:
                        continue
                    
                    grammar_rule = GrammarRule(
                        unit_id=target_unit.id,
                        topic=topic_name,
                        rule=rule_data['rule'],
                        detailed_explanation=rule_data.get('detailed_explanation', ''),
                        example=rule_data.get('example', ''),
                        correct_usage=rule_data.get('correct_usage', ''),
                        incorrect_usage=rule_data.get('incorrect_usage', ''),
                        common_errors=rule_data.get('common_errors', ''),
                        exceptions=rule_data.get('exceptions', ''),
                        order=i + 1
                    )
                    db.session.add(grammar_rule)
                    total_rules += 1
                
                total_topics += 1
        
        db.session.commit()
        
        print("\n" + "=" * 60)
        print(f"✅ RESUMEN:")
        print(f"   📚 Temas agregados: {total_topics}")
        print(f"   📝 Reglas agregadas: {total_rules}")
        print("=" * 60)
        
        # Contar total
        total = GrammarRule.query.count()
        print(f"\n📊 Total de reglas gramaticales en la base de datos: {total}")


if __name__ == '__main__':
    seed_extended_grammar()
