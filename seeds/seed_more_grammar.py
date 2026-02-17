"""
Script para agregar más temas gramaticales - Parte 2
=====================================================
Más temas avanzados y especializados.
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import GrammarRule, Unit

app = create_app()

# Más temas gramaticales
ADDITIONAL_GRAMMAR = {
    'A1': [
        {
            'topic': 'There is / There are',
            'rules': [
                {
                    'rule': 'THERE IS for singular, THERE ARE for plural',
                    'detailed_explanation': '''Uso de There is/are para expresar existencia:

THERE IS + singular/uncountable:
- There is a book on the table.
- There is some water in the glass.
- There is a problem.

THERE ARE + plural:
- There are two cats in the garden.
- There are many people here.
- There are some books on the shelf.

Contracciones:
- There\'s = There is (muy común)
- There\'re = There are (menos común, informal)

Negativo: There isn\'t / There aren\'t
Pregunta: Is there...? / Are there...?''',
                    'example': 'There is a bank near here. There are 30 students in the class.',
                    'correct_usage': 'There\'s a cat outside. There are many options.',
                    'incorrect_usage': 'There are a book. ❌ It has a bank near here. ❌',
                    'common_errors': 'Usar "It is" o "Have" para expresar existencia.',
                    'exceptions': 'Informal: "There\'s" se usa a veces con plurales: There\'s two reasons.'
                },
                {
                    'rule': 'Questions and short answers with There is/are',
                    'detailed_explanation': '''Preguntas con There is/are:

Preguntas Sí/No:
- Is there a bathroom here?
  Yes, there is. / No, there isn\'t.
- Are there any restaurants nearby?
  Yes, there are. / No, there aren\'t.

Preguntas con HOW MANY (contables):
- How many chairs are there?
  There are six chairs.

Preguntas con HOW MUCH (incontables):
- How much milk is there?
  There\'s a little milk.

Con ANY (preguntas y negativos):
- Is there any coffee?
- There aren\'t any shops.

Con SOME (afirmativo):
- There are some cookies.''',
                    'example': 'Is there a gym in this hotel? How many bedrooms are there?',
                    'correct_usage': 'Are there any questions? There isn\'t any sugar.',
                    'incorrect_usage': 'Have there any coffee? ❌ Is there any books? ❌',
                    'common_errors': 'Confundir some/any o usar singular/plural incorrectamente.',
                    'exceptions': 'Some en preguntas cuando ofreces: Would you like some tea?'
                }
            ]
        },
        {
            'topic': 'Demonstratives - This, That, These, Those',
            'rules': [
                {
                    'rule': 'THIS/THESE for near, THAT/THOSE for far',
                    'detailed_explanation': '''Demostrativos según distancia:

CERCA del hablante:
- THIS (singular): This is my book.
- THESE (plural): These are my friends.

LEJOS del hablante:
- THAT (singular): That is your house.
- THOSE (plural): Those are his shoes.

También para tiempo:
- THIS = ahora/presente: this week, this year
- THAT = pasado/futuro: that day, that summer

Como adjetivos (antes de sustantivo):
- This car is fast.
- Those people are nice.

Como pronombres (solos):
- This is delicious!
- I don\'t like those.''',
                    'example': 'This is my phone. That building is very tall. These cookies are good.',
                    'correct_usage': 'Is this your bag? Who are those people over there?',
                    'incorrect_usage': 'This books ❌ (these books). That are my friends. ❌',
                    'common_errors': 'No concordar singular/plural con el sustantivo.',
                    'exceptions': 'En el teléfono: "This is John" (presentarse), "Who is this?"'
                }
            ]
        },
        {
            'topic': 'Object Pronouns - Me, You, Him, Her, It, Us, Them',
            'rules': [
                {
                    'rule': 'Object pronouns come after verbs and prepositions',
                    'detailed_explanation': '''Pronombres de objeto:

Subject → Object:
I → me
you → you
he → him
she → her
it → it
we → us
they → them

Posición: después del verbo o preposición
- She loves me. (después del verbo)
- This is for you. (después de preposición)
- Tell him the truth.
- Give her the book.
- I saw them yesterday.

NUNCA como sujeto:
✓ She and I went. (sujeto)
✗ Me and her went. (incorrecto)''',
                    'example': 'Call me later. I gave it to her. They saw us at the park.',
                    'correct_usage': 'Listen to me. He told them a story. Wait for us.',
                    'incorrect_usage': 'She loves I. ❌ Give the book to she. ❌',
                    'common_errors': 'Usar pronombres de sujeto como objeto.',
                    'exceptions': 'Informal: "It\'s me" es común, aunque "It is I" es gramaticalmente correcto.'
                }
            ]
        },
        {
            'topic': 'Basic Question Words - What, Where, When, Who, Why, How',
            'rules': [
                {
                    'rule': 'WH-Questions structure and meaning',
                    'detailed_explanation': '''Palabras interrogativas:

WHAT = qué (cosas, acciones)
- What is your name?
- What do you do?

WHERE = dónde (lugar)
- Where do you live?
- Where is the station?

WHEN = cuándo (tiempo)
- When is your birthday?
- When does the class start?

WHO = quién (personas)
- Who is that man?
- Who called you?

WHY = por qué (razón)
- Why are you late?
- Why did you leave?

HOW = cómo (manera, estado)
- How are you?
- How do you spell it?

Estructura: WH-word + auxiliary + subject + verb''',
                    'example': 'What time is it? Where does she work? Who is your teacher?',
                    'correct_usage': 'When does the movie start? How do you get there?',
                    'incorrect_usage': 'What you want? ❌ Where he lives? ❌',
                    'common_errors': 'Olvidar el auxiliar en preguntas.',
                    'exceptions': 'Who/What como sujeto no necesitan auxiliar: Who wants coffee?'
                },
                {
                    'rule': 'HOW + adjective/adverb for degree questions',
                    'detailed_explanation': '''HOW + adjetivo/adverbio:

HOW + adjective:
- How old are you? (edad)
- How tall is he? (altura)
- How big is your house? (tamaño)
- How long is the movie? (duración/longitud)
- How far is the airport? (distancia)

HOW + adverb:
- How often do you exercise? (frecuencia)
- How well do you speak English? (calidad)
- How fast can you run? (velocidad)

Otras expresiones:
- How much? (cantidad incontable/precio)
- How many? (cantidad contable)
- How come? = Why? (informal)''',
                    'example': 'How old is your sister? How far is the beach? How often do you travel?',
                    'correct_usage': 'How much does it cost? How many languages do you speak?',
                    'incorrect_usage': 'How many water? ❌ How much people? ❌',
                    'common_errors': 'Confundir how much/how many.',
                    'exceptions': 'How come no invierte: How come you\'re late? (no "How come are you late?")'
                }
            ]
        },
        {
            'topic': 'Can for Ability and Requests',
            'rules': [
                {
                    'rule': 'CAN + base verb for present ability',
                    'detailed_explanation': '''CAN para habilidad presente:

Afirmativo: Subject + can + base verb
- I can swim.
- She can speak French.
- They can play the piano.

Negativo: Subject + can\'t/cannot + base verb
- I can\'t drive.
- He can\'t cook.

Pregunta: Can + subject + base verb?
- Can you dance?
- Can she come to the party?

IMPORTANTE:
- Sin "to": I can swim ✓ (I can to swim ❌)
- Sin -s: She can swim ✓ (She cans swim ❌)
- Mismo forma para todos: I/you/he/she/it/we/they CAN''',
                    'example': 'I can ride a bike. She can\'t sing well. Can you help me?',
                    'correct_usage': 'He can run very fast. We can\'t understand him.',
                    'incorrect_usage': 'She can to dance. ❌ He cans play guitar. ❌',
                    'common_errors': 'Añadir "to" o conjugar can.',
                    'exceptions': 'Para habilidad pasada usa "could": I could swim when I was 5.'
                },
                {
                    'rule': 'CAN/COULD for polite requests',
                    'detailed_explanation': '''CAN/COULD para peticiones:

CAN (menos formal):
- Can I borrow your pen?
- Can you open the window?
- Can we sit here?

COULD (más formal/cortés):
- Could I use your phone?
- Could you help me, please?
- Could we have the bill?

Respuestas:
- Yes, of course. / Sure. / No problem.
- I\'m sorry, I can\'t. / I\'m afraid not.

Para pedir permiso:
- Can I go to the bathroom?
- Could I leave early today?''',
                    'example': 'Can I ask you a question? Could you repeat that, please?',
                    'correct_usage': 'Can I have some water? Could you speak more slowly?',
                    'incorrect_usage': 'Can I to go? ❌ Could you to help me? ❌',
                    'common_errors': 'Añadir "to" después de can/could.',
                    'exceptions': 'May I es aún más formal: May I come in?'
                }
            ]
        },
        {
            'topic': 'Telling the Time',
            'rules': [
                {
                    'rule': 'O\'clock, half past, quarter past/to',
                    'detailed_explanation': '''Formas de decir la hora:

Hora exacta: O\'CLOCK
- 3:00 = three o\'clock
- 9:00 = nine o\'clock

Media hora: HALF PAST
- 3:30 = half past three
- 9:30 = half past nine

Cuartos: QUARTER PAST / QUARTER TO
- 3:15 = quarter past three
- 3:45 = quarter to four

Minutos: PAST (hasta :30) / TO (después de :30)
- 3:10 = ten past three
- 3:50 = ten to four
- 3:25 = twenty-five past three

AM/PM o uso de 24h:
- 3:00 PM = three o\'clock in the afternoon
- 15:00 = fifteen hundred (formal)''',
                    'example': 'It\'s half past two. The meeting is at quarter to nine.',
                    'correct_usage': 'It\'s ten past eight. We leave at quarter past seven.',
                    'incorrect_usage': 'It\'s three and half. ❌ It\'s fifteen to. ❌',
                    'common_errors': 'Olvidar especificar la hora con "to".',
                    'exceptions': 'Digital style: It\'s three thirty (3:30), four forty-five (4:45)'
                }
            ]
        },
        {
            'topic': 'Days, Months, and Seasons',
            'rules': [
                {
                    'rule': 'Days of the week with ON, months with IN',
                    'detailed_explanation': '''Días de la semana (siempre con mayúscula):
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

Preposición ON:
- I work on Monday.
- We meet on Fridays. (cada viernes)
- The party is on Saturday night.

Meses del año (siempre con mayúscula):
January, February, March, April, May, June,
July, August, September, October, November, December

Preposición IN:
- My birthday is in March.
- We travel in July.
- Christmas is in December.

Estaciones:
spring, summer, fall/autumn, winter
- In summer, it\'s hot.
- I love spring.''',
                    'example': 'I have English on Tuesdays. Her birthday is in April.',
                    'correct_usage': 'We go skiing in winter. The concert is on Friday.',
                    'incorrect_usage': 'on April ❌, in Monday ❌, on summer ❌',
                    'common_errors': 'Confundir on/in con días y meses.',
                    'exceptions': 'Sin preposición con this/next/last: I\'ll see you next Monday.'
                }
            ]
        },
        {
            'topic': 'Likes and Dislikes',
            'rules': [
                {
                    'rule': 'Like/Love/Hate + noun or -ing form',
                    'detailed_explanation': '''Expresar gustos:

VERBOS + sustantivo:
- I like pizza.
- She loves music.
- They hate traffic.

VERBOS + verb-ing:
- I like reading.
- She loves dancing.
- He hates waiting.

Escala de preferencia:
love > really like > like > don\'t mind > don\'t like > hate

Preguntas:
- Do you like coffee?
- Does she like swimming?

Respuestas:
- Yes, I love it!
- No, I don\'t like it at all.
- It\'s okay. / I don\'t mind it.''',
                    'example': 'I love cooking. She doesn\'t like getting up early.',
                    'correct_usage': 'Do you like watching movies? I really like Italian food.',
                    'incorrect_usage': 'I like read books. ❌ She like dancing. ❌',
                    'common_errors': 'Usar infinitivo sin "to" o olvidar -s en tercera persona.',
                    'exceptions': 'Like + to infinitive también existe: I like to read before bed.'
                }
            ]
        }
    ],
    
    'A2': [
        {
            'topic': 'Present Continuous for Now and Future',
            'rules': [
                {
                    'rule': 'Form: am/is/are + verb-ing for actions happening now',
                    'detailed_explanation': '''Present Continuous para acciones en progreso:

Estructura: am/is/are + verb-ing

Afirmativo:
- I am working.
- She is sleeping.
- They are playing.

Negativo: am not / isn\'t / aren\'t + verb-ing
- I\'m not watching TV.
- He isn\'t listening.

Pregunta: Am/Is/Are + subject + verb-ing?
- Are you coming?
- Is she studying?

Ortografía del -ing:
- Mayoría: + ing (playing, eating)
- Terminados en -e: quitar e + ing (making, having)
- CVC cortos: doblar + ing (running, swimming)
- -ie: ie → y + ing (dying, lying)''',
                    'example': 'I\'m writing an email right now. Look! It\'s raining.',
                    'correct_usage': 'She\'s having breakfast. They aren\'t working today.',
                    'incorrect_usage': 'She working now. ❌ He is make dinner. ❌',
                    'common_errors': 'Olvidar be o no añadir -ing.',
                    'exceptions': 'Verbos de estado no usan continuo: I\'m knowing ❌'
                },
                {
                    'rule': 'Present Continuous for future arrangements',
                    'detailed_explanation': '''Present Continuous para planes futuros:

Para planes CONFIRMADOS con hora/lugar:
- I\'m meeting John tomorrow at 3.
- We\'re flying to Paris next week.
- She\'s starting a new job on Monday.

Diferencia con GOING TO:
- Going to = intención general
- Present Continuous = plan confirmado con detalles

Ejemplos:
- I\'m going to travel more this year. (intención)
- I\'m traveling to Japan next month. (boleto comprado)

Verbos comunes para futuro:
come, go, leave, arrive, meet, have, start, fly, visit''',
                    'example': 'I\'m having dinner with my parents tonight. We\'re leaving at 8 AM.',
                    'correct_usage': 'Are you working tomorrow? She\'s arriving on Friday.',
                    'incorrect_usage': 'I\'m travel next week. ❌ (sin arreglo confirmado)',
                    'common_errors': 'Usar para intenciones sin plan confirmado.',
                    'exceptions': 'Siempre necesita expresión de tiempo futuro para claridad.'
                }
            ]
        },
        {
            'topic': 'Some, Any, No, Every Compounds',
            'rules': [
                {
                    'rule': 'SOME- for affirmative, ANY- for negative/questions',
                    'detailed_explanation': '''Compuestos con some/any/no/every:

SOME- (afirmativo):
- someone/somebody = alguien
- something = algo
- somewhere = en algún lugar
- I saw someone at the door.

ANY- (negativo/preguntas):
- anyone/anybody = alguien/nadie
- anything = algo/nada
- anywhere = en algún lugar/ningún lugar
- Did you see anyone? I didn\'t hear anything.

NO- (negativo fuerte):
- no one/nobody = nadie
- nothing = nada
- nowhere = en ningún lugar
- Nobody knows the answer.

EVERY- (todos):
- everyone/everybody = todos
- everything = todo
- everywhere = en todas partes
- Everyone is here.''',
                    'example': 'There\'s something in my bag. Is anyone home? Nobody answered.',
                    'correct_usage': 'I didn\'t see anybody. Everything is ready.',
                    'incorrect_usage': 'I saw anyone. ❌ Nobody didn\'t come. ❌',
                    'common_errors': 'Usar any- en afirmativo o doble negación.',
                    'exceptions': 'Any- en afirmativo = cualquiera: Anyone can do it.'
                },
                {
                    'rule': 'Grammar with compound pronouns',
                    'detailed_explanation': '''Gramática de pronombres compuestos:

Todos son SINGULARES (aunque signifiquen "todos"):
- Everyone IS here. (no "are")
- Nobody KNOWS. (no "know")
- Something HAS happened. (no "have")

ELSE después de compuestos:
- someone else = otra persona
- anywhere else = en otro lugar
- nothing else = nada más
- Would you like something else?

Con preposiciones (al final):
- I need someone to talk to.
- There\'s nothing to worry about.
- Do you have anywhere to stay?''',
                    'example': 'Somebody has taken my pen. Is there anywhere else to go?',
                    'correct_usage': 'Everyone wants something different. Nothing lasts forever.',
                    'incorrect_usage': 'Everyone are happy. ❌ Something have changed. ❌',
                    'common_errors': 'Usar verbo plural con pronombres compuestos.',
                    'exceptions': 'En inglés informal: "Everyone brought their books" (their como género neutro)'
                }
            ]
        },
        {
            'topic': 'Too and Enough',
            'rules': [
                {
                    'rule': 'TOO + adjective = more than necessary (negative)',
                    'detailed_explanation': '''TOO antes del adjetivo (exceso negativo):

TOO + adjective:
- It\'s too hot. (demasiado calor)
- He\'s too young to drive.
- This is too expensive for me.

TOO + adverb:
- You speak too fast.
- She arrived too late.

TOO MUCH + uncountable noun:
- There\'s too much sugar.
- You have too much work.

TOO MANY + countable noun:
- There are too many people.
- I have too many emails.

TOO + adj/adv + TO + infinitive:
- It\'s too cold to swim.
- He was too tired to continue.''',
                    'example': 'The music is too loud. I have too much homework.',
                    'correct_usage': 'It\'s too late to call. There are too many mistakes.',
                    'incorrect_usage': 'It\'s too much cold. ❌ Too people. ❌',
                    'common_errors': 'Confundir too much/too many.',
                    'exceptions': 'Too también puede ser "también": I\'m tired too.'
                },
                {
                    'rule': 'ENOUGH + noun / adjective + ENOUGH = sufficient',
                    'detailed_explanation': '''ENOUGH para cantidad suficiente:

ENOUGH + noun (antes):
- I have enough money.
- There isn\'t enough time.
- Do we have enough food?

Adjective + ENOUGH (después):
- She\'s old enough to vote.
- Is it warm enough?
- The coffee isn\'t hot enough.

Adverb + ENOUGH:
- She doesn\'t speak clearly enough.
- Did you sleep well enough?

Adj/Adv + ENOUGH + TO + infinitive:
- He\'s tall enough to play basketball.
- She\'s not fast enough to win.

ENOUGH + noun + TO:
- I have enough time to finish.''',
                    'example': 'Is this box big enough? I don\'t have enough experience.',
                    'correct_usage': 'She\'s smart enough to understand. There\'s enough space.',
                    'incorrect_usage': 'She\'s enough old. ❌ Enough big. ❌',
                    'common_errors': 'Posición incorrecta de enough.',
                    'exceptions': 'Funnily enough = curiosamente (expresión fija)'
                }
            ]
        },
        {
            'topic': 'Make vs Do',
            'rules': [
                {
                    'rule': 'MAKE for creating/producing, DO for actions/tasks',
                    'detailed_explanation': '''MAKE = crear, producir, causar:

Expresiones con MAKE:
- make breakfast/lunch/dinner
- make coffee/tea
- make a decision/choice
- make a mistake
- make money
- make friends
- make a phone call
- make plans
- make progress
- make an effort
- make a promise
- make noise
- make someone happy/sad/angry

MAKE + object + adjective:
- The news made me happy.
- You make me laugh.''',
                    'example': 'I\'m making dinner. She made a mistake. Don\'t make noise!',
                    'correct_usage': 'He makes good coffee. They made a decision.',
                    'incorrect_usage': 'I\'m doing dinner. ❌ She did a mistake. ❌',
                    'common_errors': 'Usar do con expresiones que llevan make.',
                    'exceptions': 'Make the bed (aunque no creas la cama)'
                },
                {
                    'rule': 'DO for activities, duties, work',
                    'detailed_explanation': '''DO = realizar actividades, deberes:

Expresiones con DO:
- do homework/housework
- do the dishes/laundry
- do exercise/sport
- do a job/work
- do business
- do your best
- do a favor
- do damage/harm
- do well/badly
- do an exam/test
- do research

DO con actividades indefinidas:
- What are you doing?
- I have nothing to do.
- What do you do? (trabajo)

DO como auxiliar:
- Do you like it?
- I don\'t know.''',
                    'example': 'I need to do my homework. She does exercise every day.',
                    'correct_usage': 'Can you do me a favor? He did well on the test.',
                    'incorrect_usage': 'I need to make my homework. ❌ She makes exercise. ❌',
                    'common_errors': 'Usar make con expresiones que llevan do.',
                    'exceptions': 'Do your hair/makeup (arreglarse)'
                }
            ]
        },
        {
            'topic': 'Phrasal Verbs Basics',
            'rules': [
                {
                    'rule': 'Verb + particle changes meaning',
                    'detailed_explanation': '''Phrasal verbs comunes:

LOOK:
- look for = buscar (I\'m looking for my keys)
- look after = cuidar (She looks after her grandmother)
- look forward to = esperar con ilusión

GET:
- get up = levantarse
- get on/off = subir/bajar (transporte)
- get along = llevarse bien

TURN:
- turn on/off = encender/apagar
- turn up/down = subir/bajar (volumen)
- turn around = darse vuelta

TAKE:
- take off = despegar/quitarse ropa
- take out = sacar
- take care of = cuidar''',
                    'example': 'Please turn off the light. I\'m looking for a job.',
                    'correct_usage': 'She gets up at 7 AM. The plane took off on time.',
                    'incorrect_usage': 'Please off turn the light. ❌',
                    'common_errors': 'Separar incorrectamente o usar la partícula equivocada.',
                    'exceptions': 'Algunos phrasal verbs son separables: turn it off / turn off the TV'
                },
                {
                    'rule': 'Separable vs inseparable phrasal verbs',
                    'detailed_explanation': '''Phrasal verbs separables e inseparables:

SEPARABLES (el objeto puede ir en medio):
- turn on the TV = turn the TV on = turn it on
- pick up the book = pick the book up = pick it up
- put on your coat = put your coat on = put it on

⚠️ Con pronombres, DEBE separarse:
- Turn it on. ✓
- Turn on it. ✗

INSEPARABLES (el objeto va después):
- look after the baby ✓ (look the baby after ✗)
- get on the bus ✓ (get the bus on ✗)
- look for my keys ✓ (look my keys for ✗)

Inseparables comunes: look after, look for, get on, get off, come across, run into''',
                    'example': 'I need to look after my sister. Please pick it up.',
                    'correct_usage': 'She takes after her mother. Turn it off, please.',
                    'incorrect_usage': 'Look the children after. ❌ Turn on it. ❌',
                    'common_errors': 'Separar inseparables o no separar con pronombres.',
                    'exceptions': 'Algunos pueden ser ambos según el significado.'
                }
            ]
        }
    ],
    
    'B1': [
        {
            'topic': 'Used to vs Would for Past Habits',
            'rules': [
                {
                    'rule': 'USED TO for past states and habits',
                    'detailed_explanation': '''USED TO = solía (ya no es así):

Para hábitos pasados:
- I used to play tennis. (ya no juego)
- She used to smoke. (ya no fuma)

Para estados pasados:
- I used to live in Paris. (ya no vivo)
- He used to be thin. (ya no es)

Negativo: didn\'t use to
- I didn\'t use to like coffee.
- She didn\'t use to exercise.

Pregunta: Did + subject + use to...?
- Did you use to play sports?
- Where did she use to work?

Implica CAMBIO: la situación ya no existe.''',
                    'example': 'I used to have long hair. We didn\'t use to have smartphones.',
                    'correct_usage': 'Did you use to live here? She used to be a teacher.',
                    'incorrect_usage': 'I use to play. ❌ I used to playing. ❌',
                    'common_errors': 'Olvidar "d" en afirmativo o añadir "d" en negativo/pregunta.',
                    'exceptions': 'BE USED TO + -ing = estar acostumbrado: I\'m used to waking up early.'
                },
                {
                    'rule': 'WOULD for repeated past actions only',
                    'detailed_explanation': '''WOULD para acciones habituales pasadas:

Solo para acciones repetidas (NO estados):
- Every summer, we would go to the beach.
- She would always bring me coffee.
- They would play chess every evening.

NO usar WOULD con:
- Estados: I would live in Paris. ❌ (use "used to")
- Verbos de estado: She would know him. ❌
- Situaciones no repetidas

WOULD suena más nostálgico y literario:
"When I was young, I would spend hours playing outside.
My grandmother would tell us stories by the fire."

Necesita contexto temporal:
- When I was a child, I would... ✓
- I would go there. (sin contexto) ?''',
                    'example': 'My father would read to us every night. We would go fishing on Sundays.',
                    'correct_usage': 'She would always laugh at his jokes.',
                    'incorrect_usage': 'I would be a student. ❌ (estado)',
                    'common_errors': 'Usar would con verbos de estado o sin contexto.',
                    'exceptions': 'Would también expresa voluntad pasada: He wouldn\'t listen to me.'
                }
            ]
        },
        {
            'topic': 'Gerunds and Infinitives',
            'rules': [
                {
                    'rule': 'Verbs followed by gerund (-ing)',
                    'detailed_explanation': '''Verbos + gerundio (-ing):

ENJOY + -ing:
- I enjoy reading.
- She enjoys traveling.

AVOID + -ing:
- Avoid eating too much sugar.
- He avoids talking about it.

Otros verbos + gerundio:
- finish: I finished working at 6.
- keep (on): Keep trying!
- mind: Do you mind waiting?
- suggest: I suggest leaving now.
- consider: She\'s considering moving.
- practice: Practice speaking English.
- miss: I miss living there.
- admit: He admitted stealing.
- deny: She denied knowing him.
- imagine: Imagine living on Mars!''',
                    'example': 'I enjoy cooking. She avoids eating meat. Have you finished studying?',
                    'correct_usage': 'I don\'t mind helping. Consider applying for the job.',
                    'incorrect_usage': 'I enjoy to cook. ❌ She avoids to eat. ❌',
                    'common_errors': 'Usar infinitivo con verbos que requieren gerundio.',
                    'exceptions': 'Go + -ing para actividades: go swimming, go shopping'
                },
                {
                    'rule': 'Verbs followed by infinitive (to + verb)',
                    'detailed_explanation': '''Verbos + infinitivo (to + verb):

WANT + to:
- I want to learn Spanish.
- She wants to travel.

DECIDE + to:
- I decided to quit.
- They decided to stay.

Otros verbos + infinitivo:
- hope: I hope to see you soon.
- expect: I expect to finish today.
- plan: We plan to visit London.
- promise: She promised to help.
- agree: He agreed to come.
- refuse: They refused to pay.
- learn: I\'m learning to drive.
- seem: She seems to be happy.
- pretend: He pretended to sleep.
- afford: I can\'t afford to buy it.
- manage: She managed to escape.''',
                    'example': 'I want to travel. She promised to call me. They agreed to help.',
                    'correct_usage': 'He hopes to get the job. I can\'t afford to go.',
                    'incorrect_usage': 'I want traveling. ❌ She promised calling. ❌',
                    'common_errors': 'Usar gerundio con verbos que requieren infinitivo.',
                    'exceptions': 'Help puede usar ambos: Help me (to) carry this.'
                },
                {
                    'rule': 'Verbs that take both with different meanings',
                    'detailed_explanation': '''Verbos que cambian significado:

STOP:
- stop doing = dejar de hacer
  I stopped smoking. (ya no fumo)
- stop to do = detenerse para hacer
  I stopped to smoke. (me detuve para fumar)

REMEMBER:
- remember doing = recordar haber hecho
  I remember meeting her. (recuerdo el encuentro)
- remember to do = acordarse de hacer
  Remember to call me. (no olvides)

FORGET:
- forget doing = olvidar haber hecho
  I\'ll never forget seeing the Alps.
- forget to do = olvidar hacer
  I forgot to lock the door.

TRY:
- try doing = experimentar
  Try eating less sugar.
- try to do = intentar/esforzarse
  I\'m trying to learn Chinese.''',
                    'example': 'I stopped eating meat. (quit) I stopped to eat. (paused to eat)',
                    'correct_usage': 'Remember to buy milk. I remember buying milk yesterday.',
                    'incorrect_usage': 'Confundir los significados.',
                    'common_errors': 'No distinguir entre los dos significados.',
                    'exceptions': 'El contexto ayuda a aclarar el significado.'
                }
            ]
        },
        {
            'topic': 'Present Perfect Continuous',
            'rules': [
                {
                    'rule': 'Form: have/has been + verb-ing',
                    'detailed_explanation': '''Formación del Present Perfect Continuous:

Estructura: have/has + been + verb-ing

Afirmativo:
- I have been working.
- She has been studying.
- They have been waiting.

Negativo: haven\'t/hasn\'t been + verb-ing
- I haven\'t been sleeping well.
- He hasn\'t been feeling well.

Pregunta: Have/Has + subject + been + verb-ing?
- Have you been exercising?
- How long has she been living here?

Contracción: I\'ve been, she\'s been, they\'ve been''',
                    'example': 'I\'ve been learning English for 3 years. She\'s been working all day.',
                    'correct_usage': 'Have you been waiting long? It\'s been raining since morning.',
                    'incorrect_usage': 'I have been work. ❌ She has being waiting. ❌',
                    'common_errors': 'Olvidar been o -ing.',
                    'exceptions': 'Verbos de estado usan Present Perfect Simple: I\'ve known him for years.'
                },
                {
                    'rule': 'Use for duration and recent activities',
                    'detailed_explanation': '''Usos del Present Perfect Continuous:

1. Acciones que empezaron en el pasado y continúan:
   - I\'ve been studying since 8 AM.
   - She\'s been living here for 5 years.

2. Acciones recientes con resultado visible:
   - You\'re wet! Have you been swimming?
   - My eyes hurt. I\'ve been reading.

3. Énfasis en la duración o continuidad:
   - I\'ve been waiting for an hour!
   - How long have you been learning English?

Diferencia con Present Perfect Simple:
- Simple: enfatiza resultado/cantidad
  I\'ve written 3 emails. (resultado)
- Continuous: enfatiza duración/proceso
  I\'ve been writing emails. (actividad)''',
                    'example': 'Why are you tired? I\'ve been working out. How long have you been waiting?',
                    'correct_usage': 'It\'s been snowing all day. She\'s been teaching for 20 years.',
                    'incorrect_usage': 'I\'ve been knowing him for years. ❌',
                    'common_errors': 'Usar con verbos de estado.',
                    'exceptions': 'Live/work pueden usar ambos: I\'ve lived/been living here for 5 years.'
                }
            ]
        }
    ],
    
    'B2': [
        {
            'topic': 'Have/Get Something Done (Causative)',
            'rules': [
                {
                    'rule': 'HAVE/GET + object + past participle for services',
                    'detailed_explanation': '''Causativo: alguien hace algo por ti:

HAVE + object + past participle (más común):
- I had my hair cut. (someone cut my hair)
- She\'s having her car repaired.
- We had our house painted.

GET + object + past participle (más informal):
- I got my phone fixed.
- She\'s getting her nails done.
- We got the windows cleaned.

Tiempos verbales:
- Present: I have/get my car washed every week.
- Past: I had my car washed yesterday.
- Future: I\'ll have it done tomorrow.
- Present Perfect: I\'ve had it repaired.

Con agente (menos común):
- I had my hair cut by a new stylist.''',
                    'example': 'I need to have my eyes tested. She got her dress cleaned.',
                    'correct_usage': 'We\'re having the kitchen remodeled. I got my photo taken.',
                    'incorrect_usage': 'I had cut my hair. ❌ I had someone cut my hair. (also correct, but different)',
                    'common_errors': 'Confundir con el pasado perfecto.',
                    'exceptions': 'GET + object + to infinitive = hacer que alguien haga algo: I got him to help me.'
                },
                {
                    'rule': 'MAKE vs LET vs HAVE + object + bare infinitive',
                    'detailed_explanation': '''Estructuras causativas con infinitivo sin TO:

MAKE + object + bare infinitive (forzar/obligar):
- She made me wait.
- They made him apologize.
- The movie made me cry.

LET + object + bare infinitive (permitir):
- Let me help you.
- She let him go.
- My parents let me stay out late.

HAVE + object + bare infinitive (hacer que, organizar):
- I\'ll have someone call you.
- He had his assistant book the flight.

En pasivo, MAKE usa TO:
- I was made to wait.
- He was made to apologize.''',
                    'example': 'Don\'t make me laugh. Let me explain. I\'ll have the secretary send it.',
                    'correct_usage': 'She made him clean his room. They let us leave early.',
                    'incorrect_usage': 'She made him to clean. ❌ Let me to help. ❌',
                    'common_errors': 'Añadir "to" después de make/let.',
                    'exceptions': 'Allow usa to: She allowed him to leave.'
                }
            ]
        },
        {
            'topic': 'Narrative Tenses',
            'rules': [
                {
                    'rule': 'Combining Past Simple, Continuous, and Perfect',
                    'detailed_explanation': '''Tiempos narrativos para contar historias:

PAST SIMPLE: acciones principales de la historia
- I walked into the room. She saw me.

PAST CONTINUOUS: contexto/escena de fondo
- The sun was shining. People were walking.

PAST PERFECT: acciones anteriores a la historia
- I realized I had left my keys.
- She was upset because he had lied.

Combinación típica:
"I was walking (background) down the street when I saw (main action) my ex-boyfriend. He was talking (background) to a woman I had never seen (earlier) before."

Marcadores:
- When = Past Simple después
- While = Past Continuous después
- After/Before = Past Perfect posible''',
                    'example': 'I was sleeping when the phone rang. I had forgotten to set my alarm.',
                    'correct_usage': 'She realized she had made a mistake.',
                    'incorrect_usage': 'I walked when the phone was ringing. ❌',
                    'common_errors': 'No usar Past Perfect para la acción anterior.',
                    'exceptions': 'En narrativa informal, Past Simple puede reemplazar Past Perfect.'
                },
                {
                    'rule': 'Past Perfect Continuous for background activities',
                    'detailed_explanation': '''Past Perfect Continuous para duración anterior:

Estructura: had been + verb-ing

Uso: acción en progreso ANTES de otra acción pasada
- I had been waiting for an hour when she arrived.
- She was tired because she had been working all night.
- They had been living there for 10 years before they moved.

Énfasis en duración hasta un punto pasado:
- How long had you been learning English before you moved?
- He had been smoking for 20 years when he finally quit.

Señales visibles de actividad reciente (en pasado):
- His eyes were red. He had been crying.
- The ground was wet. It had been raining.''',
                    'example': 'I had been studying for hours when you called. She had been running—that\'s why she was out of breath.',
                    'correct_usage': 'They had been dating for 2 years before they got engaged.',
                    'incorrect_usage': 'I had been wait for an hour. ❌',
                    'common_errors': 'Olvidar "been" o "-ing".',
                    'exceptions': 'Verbos de estado usan Past Perfect Simple: I had known him for years.'
                }
            ]
        },
        {
            'topic': 'Articles - Advanced Usage',
            'rules': [
                {
                    'rule': 'THE with unique, specific, or previously mentioned nouns',
                    'detailed_explanation': '''THE - usos avanzados:

Cosas únicas:
- the sun, the moon, the Earth, the universe
- the President (of this country), the government

Con superlativos y ordinales:
- the best, the worst, the first, the last

Países/lugares específicos:
- the USA, the UK, the Netherlands (plurales/unidos)
- the Amazon, the Nile (ríos)
- the Pacific, the Atlantic (océanos)
- the Alps, the Andes (cordilleras)

Con adjetivos sustantivados (grupos):
- the rich, the poor, the elderly, the unemployed

Instituciones en contexto:
- I\'m going to the bank/the doctor/the movies.''',
                    'example': 'The elderly need special care. We visited the Alps.',
                    'correct_usage': 'The first time I saw the Eiffel Tower, I was amazed.',
                    'incorrect_usage': 'I\'m going to bank. ❌ I visited Alps. ❌',
                    'common_errors': 'Omitir THE donde es necesario.',
                    'exceptions': 'Países singulares sin the: France, Japan, Mexico'
                },
                {
                    'rule': 'Zero article for general statements and abstracts',
                    'detailed_explanation': '''Sin artículo (zero article):

Conceptos generales/abstractos:
- Life is beautiful. (la vida en general)
- Love conquers all.
- Time flies.

Plural general:
- Dogs are loyal. (perros en general)
- Children need love.
- Teachers work hard.

Actividades/deportes:
- play tennis/football/chess
- do yoga/exercise

Comidas del día:
- have breakfast/lunch/dinner
- after breakfast, before lunch

Transporte con BY:
- by car, by bus, by plane

Lugares con propósito:
- go to school (como estudiante)
- go to bed (para dormir)
- go to church (para rezar)''',
                    'example': 'Happiness is important. I love music. We had dinner at 7.',
                    'correct_usage': 'Children need education. I go to work by bus.',
                    'incorrect_usage': 'The life is beautiful. ❌ I play the tennis. ❌',
                    'common_errors': 'Añadir artículos innecesarios.',
                    'exceptions': 'Si es específico, usa THE: The children in this school are smart.'
                }
            ]
        }
    ]
}


def seed_additional_grammar():
    """Poblar la base de datos con más temas gramaticales"""
    with app.app_context():
        print("=" * 60)
        print("🎓 AGREGANDO MÁS TEMAS GRAMATICALES")
        print("=" * 60)
        
        total_topics = 0
        total_rules = 0
        
        for level, topics in ADDITIONAL_GRAMMAR.items():
            print(f"\n📚 Procesando nivel {level}...")
            
            # Buscar unidades de este nivel
            units = Unit.query.filter(Unit.title.like(f'%{level}%')).order_by(Unit.unit_number).all()
            
            if not units:
                print(f"  ⚠️ No se encontraron unidades para {level}")
                continue
            
            for topic_data in topics:
                topic_name = topic_data['topic']
                
                # Distribuir entre las unidades del nivel
                unit_index = (total_topics + 5) % len(units)  # Offset para no repetir
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
        unique_topics = db.session.execute(db.text(
            'SELECT COUNT(DISTINCT topic) FROM grammar_rules'
        )).scalar()
        
        print(f"\n📊 ESTADÍSTICAS TOTALES:")
        print(f"   Temas únicos: {unique_topics}")
        print(f"   Reglas totales: {total}")


if __name__ == '__main__':
    seed_additional_grammar()
