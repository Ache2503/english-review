"""
Sistema de Estudio Intensivo - Contenido Educativo Completo

Contenido detallado para preparación de exámenes con:
- Explicaciones claras
- Reglas y estructuras
- Ejemplos prácticos
- Errores comunes
- Tips y trucos de memoria
- Ejercicios interactivos
"""

STUDY_TOPICS = {
    'comparative-superlative': {
        'title': 'Comparative & Superlative',
        'icon': '📊',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Aprende a comparar cosas y expresar superlativos correctamente.',
        
        'theory': {
            'introduction': '''
Los **comparativos** se usan para comparar DOS cosas o personas.
Los **superlativos** se usan para comparar UNA cosa con un GRUPO (3 o más).
''',
            'rules': [
                {
                    'title': '📏 Adjetivos Cortos (1 sílaba)',
                    'rule': 'Agregar -ER para comparativo, -EST para superlativo',
                    'formula': 'Adj + ER / THE + Adj + EST',
                    'examples': [
                        {'adj': 'tall', 'comparative': 'taller', 'superlative': 'the tallest', 
                         'sentence_comp': 'John is **taller** than Peter.', 
                         'sentence_super': 'John is **the tallest** in the class.'},
                        {'adj': 'fast', 'comparative': 'faster', 'superlative': 'the fastest',
                         'sentence_comp': 'A car is **faster** than a bicycle.',
                         'sentence_super': 'The cheetah is **the fastest** animal.'},
                        {'adj': 'old', 'comparative': 'older', 'superlative': 'the oldest',
                         'sentence_comp': 'My brother is **older** than me.',
                         'sentence_super': 'She is **the oldest** person in town.'},
                    ],
                    'spelling_rules': [
                        '🔤 Si termina en **-e**: solo agregar -R/-ST → large → larger → largest',
                        '🔤 Si termina en **consonante + vocal + consonante**: doblar última consonante → big → bigger → biggest',
                        '🔤 Si termina en **-y**: cambiar Y por I → dry → drier → driest',
                    ]
                },
                {
                    'title': '📐 Adjetivos Largos (2+ sílabas)',
                    'rule': 'Usar MORE para comparativo, THE MOST para superlativo',
                    'formula': 'MORE + Adj / THE MOST + Adj',
                    'examples': [
                        {'adj': 'beautiful', 'comparative': 'more beautiful', 'superlative': 'the most beautiful',
                         'sentence_comp': 'Paris is **more beautiful** than London.',
                         'sentence_super': 'Venice is **the most beautiful** city I\'ve visited.'},
                        {'adj': 'expensive', 'comparative': 'more expensive', 'superlative': 'the most expensive',
                         'sentence_comp': 'Gold is **more expensive** than silver.',
                         'sentence_super': 'Diamonds are **the most expensive** gems.'},
                        {'adj': 'interesting', 'comparative': 'more interesting', 'superlative': 'the most interesting',
                         'sentence_comp': 'This book is **more interesting** than the movie.',
                         'sentence_super': 'It was **the most interesting** documentary ever.'},
                    ]
                },
                {
                    'title': '⚠️ Adjetivos Irregulares (MEMORIZAR)',
                    'rule': 'Estos NO siguen las reglas normales',
                    'formula': 'Memorizar cada uno',
                    'examples': [
                        {'adj': 'good', 'comparative': 'better', 'superlative': 'the best',
                         'sentence_comp': 'Your idea is **better** than mine.',
                         'sentence_super': 'This is **the best** pizza I\'ve ever had!'},
                        {'adj': 'bad', 'comparative': 'worse', 'superlative': 'the worst',
                         'sentence_comp': 'Monday was **worse** than Tuesday.',
                         'sentence_super': 'It was **the worst** day of my life.'},
                        {'adj': 'far', 'comparative': 'farther/further', 'superlative': 'the farthest/furthest',
                         'sentence_comp': 'The store is **farther** than the bank.',
                         'sentence_super': 'Pluto is **the farthest** planet from the Sun.'},
                        {'adj': 'little', 'comparative': 'less', 'superlative': 'the least',
                         'sentence_comp': 'I have **less** money than you.',
                         'sentence_super': 'He did **the least** work.'},
                        {'adj': 'much/many', 'comparative': 'more', 'superlative': 'the most',
                         'sentence_comp': 'She has **more** friends than me.',
                         'sentence_super': 'He scored **the most** points.'},
                    ]
                },
                {
                    'title': '📝 Adjetivos de 2 sílabas terminados en -Y',
                    'rule': 'Cambiar -Y por -IER / -IEST',
                    'formula': 'Adj(-y) → -ier / -iest',
                    'examples': [
                        {'adj': 'happy', 'comparative': 'happier', 'superlative': 'the happiest',
                         'sentence_comp': 'I am **happier** now than before.',
                         'sentence_super': 'Today is **the happiest** day!'},
                        {'adj': 'easy', 'comparative': 'easier', 'superlative': 'the easiest',
                         'sentence_comp': 'English is **easier** than Chinese.',
                         'sentence_super': 'This is **the easiest** question.'},
                        {'adj': 'funny', 'comparative': 'funnier', 'superlative': 'the funniest',
                         'sentence_comp': 'Jim Carrey is **funnier** than Adam Sandler.',
                         'sentence_super': 'He is **the funniest** comedian.'},
                    ]
                }
            ],
            'structures': [
                {
                    'name': 'Comparativo con THAN',
                    'structure': 'Subject + BE + comparative + THAN + object',
                    'example': 'My house is **bigger than** yours.',
                    'note': 'THAN es obligatorio cuando comparas directamente'
                },
                {
                    'name': 'Superlativo con IN/OF',
                    'structure': 'Subject + BE + THE + superlative + IN/OF + group',
                    'example': 'She is **the smartest** student **in** the class.',
                    'note': 'IN para lugares/grupos, OF para períodos de tiempo'
                },
                {
                    'name': 'As...as (igualdad)',
                    'structure': 'Subject + BE + AS + adjective + AS + object',
                    'example': 'My car is **as fast as** yours.',
                    'note': 'Para decir que dos cosas son iguales'
                },
                {
                    'name': 'Not as...as (desigualdad)',
                    'structure': 'Subject + BE + NOT AS + adjective + AS + object',
                    'example': 'Monday is **not as busy as** Friday.',
                    'note': 'Para decir que algo es MENOS que otra cosa'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She is more prettier than her sister.',
                'correct': 'She is prettier than her sister.',
                'explanation': '❌ No uses MORE con adjetivos cortos. "Pretty" → "prettier"'
            },
            {
                'wrong': 'This is the most biggest house.',
                'correct': 'This is the biggest house.',
                'explanation': '❌ No uses MOST con adjetivos cortos. "Big" → "biggest"'
            },
            {
                'wrong': 'He is more better than me.',
                'correct': 'He is better than me.',
                'explanation': '❌ "Good" es irregular. Comparativo = "better" (no "more better")'
            },
            {
                'wrong': 'She is the more intelligent student.',
                'correct': 'She is the most intelligent student.',
                'explanation': '❌ Superlativo de adjetivos largos usa THE MOST, no THE MORE'
            },
            {
                'wrong': 'He is taller that me.',
                'correct': 'He is taller than me.',
                'explanation': '❌ Siempre usa THAN, no THAT en comparativos'
            },
            {
                'wrong': 'This is the best city of the world.',
                'correct': 'This is the best city in the world.',
                'explanation': '❌ Usa IN para lugares, OF para grupos/períodos'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'Cuenta las sílabas',
                'content': '1 sílaba = -er/-est. 2+ sílabas = more/most. Así de simple.'
            },
            {
                'icon': '🧠',
                'title': 'Memoriza los 5 irregulares',
                'content': 'GOOD-BETTER-BEST, BAD-WORSE-WORST, FAR-FARTHER-FARTHEST, LITTLE-LESS-LEAST, MUCH/MANY-MORE-MOST'
            },
            {
                'icon': '✍️',
                'title': 'Regla del CVC',
                'content': 'Consonante-Vocal-Consonante al final = doblar: big→bigger, hot→hotter, thin→thinner'
            },
            {
                'icon': '📍',
                'title': 'IN vs OF',
                'content': 'IN = lugares (in the class, in the world). OF = períodos (of all time, of the year)'
            },
            {
                'icon': '⚡',
                'title': 'Truco rápido',
                'content': '¿Puedes decirlo en 1 respiración? → -er/-est. ¿Es largo? → more/most'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la forma correcta del adjetivo entre paréntesis.',
                'questions': [
                    {'prompt': 'My sister is ___ than me. (tall)', 'answer': 'taller', 'hint': '1 sílaba = -er'},
                    {'prompt': 'This is ___ movie I\'ve ever seen. (good)', 'answer': 'the best', 'hint': 'Irregular: good-better-best'},
                    {'prompt': 'Gold is ___ than silver. (expensive)', 'answer': 'more expensive', 'hint': '3 sílabas = more'},
                    {'prompt': 'Today is ___ day of the year. (hot)', 'answer': 'the hottest', 'hint': 'CVC = doblar la t'},
                    {'prompt': 'This test is ___ than the last one. (easy)', 'answer': 'easier', 'hint': '-y → -ier'},
                    {'prompt': 'She is ___ student in our class. (intelligent)', 'answer': 'the most intelligent', 'hint': '4 sílabas = the most'},
                    {'prompt': 'Your idea is ___ than mine. (bad)', 'answer': 'worse', 'hint': 'Irregular: bad-worse-worst'},
                    {'prompt': 'Mount Everest is ___ mountain in the world. (high)', 'answer': 'the highest', 'hint': '1 sílaba = -est'},
                    {'prompt': 'I feel ___ today than yesterday. (happy)', 'answer': 'happier', 'hint': '-y → -ier'},
                    {'prompt': 'This is ___ book I\'ve read. (interesting)', 'answer': 'the most interesting', 'hint': '4 sílabas = the most'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'My car is ___ yours.',
                        'options': ['faster than', 'more fast than', 'fastest than', 'more faster than'],
                        'answer': 'faster than',
                        'explanation': 'Fast = 1 sílaba → faster'
                    },
                    {
                        'prompt': 'She is ___ person I know.',
                        'options': ['the more kind', 'the kindest', 'the most kind', 'kinder'],
                        'answer': 'the kindest',
                        'explanation': 'Kind = 1 sílaba → kindest (superlativo)'
                    },
                    {
                        'prompt': 'This problem is ___ I thought.',
                        'options': ['difficulter than', 'more difficult than', 'most difficult than', 'the difficultest'],
                        'answer': 'more difficult than',
                        'explanation': 'Difficult = 3 sílabas → more difficult'
                    },
                    {
                        'prompt': 'Today was ___ day of my life.',
                        'options': ['the worse', 'the baddest', 'the worst', 'worse'],
                        'answer': 'the worst',
                        'explanation': 'Bad es irregular: bad-worse-worst'
                    },
                    {
                        'prompt': 'Your English is as ___ mine.',
                        'options': ['good as', 'better as', 'best as', 'gooder as'],
                        'answer': 'good as',
                        'explanation': 'as...as usa el adjetivo base, no comparativo'
                    }
                ]
            },
            {
                'type': 'error_correction',
                'instruction': 'Encuentra y corrige el error en cada oración.',
                'questions': [
                    {'prompt': 'She is more taller than her brother.', 'answer': 'She is taller than her brother.', 'error': 'more taller → taller'},
                    {'prompt': 'This is the most easiest test.', 'answer': 'This is the easiest test.', 'error': 'most easiest → easiest'},
                    {'prompt': 'He runs more faster that me.', 'answer': 'He runs faster than me.', 'error': 'more faster that → faster than'},
                    {'prompt': 'Today is more hot than yesterday.', 'answer': 'Today is hotter than yesterday.', 'error': 'more hot → hotter'},
                    {'prompt': 'This is the goodest pizza ever.', 'answer': 'This is the best pizza ever.', 'error': 'goodest → best (irregular)'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Comparativos (-ER / MORE)
| Tipo | Regla | Ejemplo |
|------|-------|---------|
| 1 sílaba | +er | tall → tall**er** |
| 1 sílaba CVC | doblar +er | big → bigg**er** |
| 2 síl. en -y | -ier | happy → happ**ier** |
| 2+ sílabas | more + adj | more beautiful |
| Irregulares | memorizar | good → better |

### Superlativos (-EST / MOST)
| Tipo | Regla | Ejemplo |
|------|-------|---------|
| 1 sílaba | the +est | the tall**est** |
| 1 sílaba CVC | the + doblar +est | the bigg**est** |
| 2 síl. en -y | the -iest | the happ**iest** |
| 2+ sílabas | the most + adj | the most beautiful |
| Irregulares | memorizar | good → the best |

### Irregulares (¡MEMORIZAR!)
| Base | Comparativo | Superlativo |
|------|-------------|-------------|
| good | better | the best |
| bad | worse | the worst |
| far | farther/further | the farthest/furthest |
| little | less | the least |
| much/many | more | the most |
'''
    },
    
    'need-to': {
        'title': 'Need To',
        'icon': '❗',
        'difficulty': 'beginner',
        'estimated_time': '15 min',
        'description': 'Expresa necesidad y obligación con "need to".',
        
        'theory': {
            'introduction': '''
**NEED TO** se usa para expresar **necesidad** u **obligación**. 
Es similar a "have to" pero menos fuerte. Indica que algo es necesario o importante hacer.
''',
            'rules': [
                {
                    'title': '✅ Afirmativo',
                    'rule': 'Sujeto + NEED + TO + verbo base',
                    'formula': 'S + need/needs + to + verb',
                    'examples': [
                        {'sentence': 'I **need to** study for my exam.', 'translation': 'Necesito estudiar para mi examen.'},
                        {'sentence': 'She **needs to** call her mother.', 'translation': 'Ella necesita llamar a su madre.'},
                        {'sentence': 'We **need to** leave now.', 'translation': 'Necesitamos irnos ahora.'},
                        {'sentence': 'He **needs to** finish his homework.', 'translation': 'Él necesita terminar su tarea.'},
                        {'sentence': 'They **need to** buy groceries.', 'translation': 'Ellos necesitan comprar comida.'},
                    ],
                    'note': '⚠️ Con he/she/it → NEEDS (con S)'
                },
                {
                    'title': '❌ Negativo',
                    'rule': 'Sujeto + DO/DOES + NOT + NEED + TO + verbo',
                    'formula': 'S + don\'t/doesn\'t + need + to + verb',
                    'examples': [
                        {'sentence': 'You **don\'t need to** worry.', 'translation': 'No necesitas preocuparte.'},
                        {'sentence': 'She **doesn\'t need to** come early.', 'translation': 'Ella no necesita venir temprano.'},
                        {'sentence': 'We **don\'t need to** hurry.', 'translation': 'No necesitamos apurarnos.'},
                        {'sentence': 'He **doesn\'t need to** pay today.', 'translation': 'Él no necesita pagar hoy.'},
                    ],
                    'note': '"Don\'t need to" = No es necesario (no hay obligación)'
                },
                {
                    'title': '❓ Interrogativo',
                    'rule': 'DO/DOES + sujeto + NEED + TO + verbo?',
                    'formula': 'Do/Does + S + need + to + verb?',
                    'examples': [
                        {'sentence': '**Do** you **need to** leave now?', 'translation': '¿Necesitas irte ahora?'},
                        {'sentence': '**Does** she **need to** bring anything?', 'translation': '¿Necesita ella traer algo?'},
                        {'sentence': '**Do** we **need to** register?', 'translation': '¿Necesitamos registrarnos?'},
                        {'sentence': '**Does** he **need to** wear a suit?', 'translation': '¿Necesita él usar traje?'},
                    ]
                }
            ],
            'structures': [
                {
                    'name': 'Need to vs Have to',
                    'structure': 'Comparación de uso',
                    'example': '''
- **Need to** = Necesidad personal/recomendación suave
- **Have to** = Obligación más fuerte/externa
                    ''',
                    'note': '"I need to exercise" (sé que debo) vs "I have to work tomorrow" (obligación)'
                },
                {
                    'name': 'Need + -ing (pasiva)',
                    'structure': 'Something + needs + verb-ing',
                    'example': 'The car **needs washing**. (= needs to be washed)',
                    'note': 'Forma pasiva: algo necesita que le hagan algo'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She need to go home.',
                'correct': 'She needs to go home.',
                'explanation': '❌ Con he/she/it debes usar NEEDS (con S)'
            },
            {
                'wrong': 'I don\'t need go to the store.',
                'correct': 'I don\'t need to go to the store.',
                'explanation': '❌ Siempre necesitas TO después de need'
            },
            {
                'wrong': 'Do she needs to come?',
                'correct': 'Does she need to come?',
                'explanation': '❌ Con DOES el verbo va sin S (need, no needs)'
            },
            {
                'wrong': 'He needs study more.',
                'correct': 'He needs to study more.',
                'explanation': '❌ Falta TO entre needs y el verbo'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'La regla de la S',
                'content': 'He/She/It NEEDS (con S). I/You/We/They NEED (sin S). Igual que todos los verbos en presente.'
            },
            {
                'icon': '🔗',
                'title': 'Siempre con TO',
                'content': 'NEED + TO + VERBO. Nunca olvides el TO en el medio.'
            },
            {
                'icon': '💡',
                'title': 'Don\'t need to = No es necesario',
                'content': '"You don\'t need to pay" = No tienes que pagar (puedes, pero no es obligatorio).'
            },
            {
                'icon': '⚡',
                'title': 'Truco para negativo',
                'content': 'Si usas DO/DOES, el NEED pierde la S. "She doesn\'t need" (no "doesn\'t needs")'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la forma correcta de NEED TO.',
                'questions': [
                    {'prompt': 'She ___ (need) study harder.', 'answer': 'needs to', 'hint': 'She = tercera persona'},
                    {'prompt': 'I ___ (not/need) go to work tomorrow.', 'answer': "don't need to", 'hint': 'I = primera persona, negativo'},
                    {'prompt': '___ you ___ (need) any help?', 'answer': 'Do...need to', 'hint': 'Pregunta con you'},
                    {'prompt': 'He ___ (need) see a doctor.', 'answer': 'needs to', 'hint': 'He = tercera persona'},
                    {'prompt': 'We ___ (not/need) bring food.', 'answer': "don't need to", 'hint': 'We = plural, negativo'},
                    {'prompt': '___ she ___ (need) call you back?', 'answer': 'Does...need to', 'hint': 'Pregunta con she'},
                    {'prompt': 'They ___ (need) finish by Friday.', 'answer': 'need to', 'hint': 'They = plural'},
                    {'prompt': 'The car ___ (need) washing.', 'answer': 'needs', 'hint': 'Forma pasiva: needs + -ing'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': '___ John ___ to leave early?',
                        'options': ['Do...need', 'Does...need', 'Does...needs', 'Do...needs'],
                        'answer': 'Does...need',
                        'explanation': 'Con Does, el verbo va sin S'
                    },
                    {
                        'prompt': 'She ___ to study tonight.',
                        'options': ['need', 'needs', 'needing', 'needed'],
                        'answer': 'needs',
                        'explanation': 'She = tercera persona = needs (con S)'
                    },
                    {
                        'prompt': 'You ___ worry about it.',
                        'options': ["don't need to", "doesn't need to", "don't need", "not need to"],
                        'answer': "don't need to",
                        'explanation': 'You = don\'t + need + to'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura
| Forma | Estructura | Ejemplo |
|-------|-----------|---------|
| ✅ Afirmativo | S + need(s) + to + verb | I need to go |
| ❌ Negativo | S + don't/doesn't + need + to + verb | She doesn't need to come |
| ❓ Pregunta | Do/Does + S + need + to + verb? | Do you need to leave? |

### Conjugación
| Persona | Afirmativo | Negativo |
|---------|-----------|----------|
| I/You/We/They | need to | don't need to |
| He/She/It | needs to | doesn't need to |

### Recuerda
- ✅ need/needs + **TO** + verbo
- ✅ He/She/It → need**S**
- ✅ Con do/does → need (sin S)
'''
    },
    
    'adjectives-infinitives': {
        'title': 'Adjectives + Infinitives',
        'icon': '🔗',
        'difficulty': 'intermediate',
        'estimated_time': '20 min',
        'description': 'Combina adjetivos con infinitivos para expresar reacciones y sentimientos.',
        
        'theory': {
            'introduction': '''
**Adjectives + Infinitives** es una estructura que combina un adjetivo con un verbo en infinitivo (TO + verbo).
Se usa principalmente para expresar **reacciones**, **sentimientos** y **evaluaciones**.
''',
            'rules': [
                {
                    'title': '😊 Sentimientos/Reacciones',
                    'rule': 'Sujeto + BE + Adjetivo + TO + Verbo',
                    'formula': 'S + be + adj + to + verb',
                    'examples': [
                        {'sentence': 'I am **happy to** meet you.', 'translation': 'Estoy feliz de conocerte.'},
                        {'sentence': 'She was **surprised to** see him.', 'translation': 'Ella estaba sorprendida de verlo.'},
                        {'sentence': 'We are **excited to** travel.', 'translation': 'Estamos emocionados de viajar.'},
                        {'sentence': 'He is **afraid to** fly.', 'translation': 'Él tiene miedo de volar.'},
                        {'sentence': 'They were **sad to** leave.', 'translation': 'Estaban tristes de irse.'},
                    ],
                    'common_adjectives': ['happy', 'sad', 'surprised', 'excited', 'afraid', 'glad', 'sorry', 'proud', 'ashamed', 'relieved']
                },
                {
                    'title': '📊 Evaluaciones',
                    'rule': 'IT + BE + Adjetivo + TO + Verbo',
                    'formula': 'It is/was + adj + to + verb',
                    'examples': [
                        {'sentence': 'It is **easy to** learn.', 'translation': 'Es fácil de aprender.'},
                        {'sentence': 'It is **important to** study.', 'translation': 'Es importante estudiar.'},
                        {'sentence': 'It was **difficult to** understand.', 'translation': 'Era difícil de entender.'},
                        {'sentence': 'It is **nice to** meet you.', 'translation': 'Es un placer conocerte.'},
                        {'sentence': 'It is **impossible to** finish today.', 'translation': 'Es imposible terminar hoy.'},
                    ],
                    'common_adjectives': ['easy', 'difficult', 'hard', 'important', 'necessary', 'possible', 'impossible', 'nice', 'good', 'bad']
                },
                {
                    'title': '👤 Con FOR + Persona',
                    'rule': 'IT + BE + Adjetivo + FOR + Persona + TO + Verbo',
                    'formula': 'It is + adj + for + person + to + verb',
                    'examples': [
                        {'sentence': 'It is **easy for me to** understand.', 'translation': 'Es fácil para mí entender.'},
                        {'sentence': 'It is **important for students to** study.', 'translation': 'Es importante que los estudiantes estudien.'},
                        {'sentence': 'It was **hard for him to** accept.', 'translation': 'Fue difícil para él aceptar.'},
                        {'sentence': 'It is **necessary for us to** leave.', 'translation': 'Es necesario que nos vayamos.'},
                    ],
                    'note': 'FOR indica QUIÉN realiza la acción'
                },
                {
                    'title': '📏 Adjetivo + ENOUGH + TO',
                    'rule': 'Adjetivo + ENOUGH + TO + Verbo',
                    'formula': 'adj + enough + to + verb',
                    'examples': [
                        {'sentence': 'She is **old enough to** drive.', 'translation': 'Ella es suficientemente mayor para manejar.'},
                        {'sentence': 'He is **strong enough to** lift it.', 'translation': 'Él es suficientemente fuerte para levantarlo.'},
                        {'sentence': 'It is **good enough to** eat.', 'translation': 'Está suficientemente bueno para comer.'},
                    ],
                    'note': 'ENOUGH va DESPUÉS del adjetivo'
                },
                {
                    'title': '📏 TOO + Adjetivo + TO',
                    'rule': 'TOO + Adjetivo + TO + Verbo',
                    'formula': 'too + adj + to + verb',
                    'examples': [
                        {'sentence': 'She is **too young to** vote.', 'translation': 'Ella es demasiado joven para votar.'},
                        {'sentence': 'It is **too expensive to** buy.', 'translation': 'Es demasiado caro para comprar.'},
                        {'sentence': 'He was **too tired to** continue.', 'translation': 'Él estaba demasiado cansado para continuar.'},
                    ],
                    'note': 'TOO indica exceso (demasiado)'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I am happy for meet you.',
                'correct': 'I am happy to meet you.',
                'explanation': '❌ Después del adjetivo de sentimiento usa TO, no FOR'
            },
            {
                'wrong': 'It is easy for understand.',
                'correct': 'It is easy to understand.',
                'explanation': '❌ Sin persona específica, usa solo TO (no FOR)'
            },
            {
                'wrong': 'She is enough old to drive.',
                'correct': 'She is old enough to drive.',
                'explanation': '❌ ENOUGH va DESPUÉS del adjetivo, no antes'
            },
            {
                'wrong': 'He is too tired for work.',
                'correct': 'He is too tired to work.',
                'explanation': '❌ Usa TO + verbo (infinitivo), no FOR + verbo'
            },
            {
                'wrong': 'I am happy to meeting you.',
                'correct': 'I am happy to meet you.',
                'explanation': '❌ TO + verbo BASE (meet), no gerundio (meeting)'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'Estructura básica',
                'content': 'BE + ADJETIVO + TO + VERBO. Siempre infinitivo (to + verbo base).'
            },
            {
                'icon': '👥',
                'title': 'FOR = Persona específica',
                'content': 'Usa FOR cuando quieras especificar QUIÉN hace la acción: "It is hard FOR ME to..."'
            },
            {
                'icon': '⚖️',
                'title': 'TOO vs ENOUGH',
                'content': 'TOO = demasiado (negativo). ENOUGH = suficiente (positivo). TOO va antes, ENOUGH después.'
            },
            {
                'icon': '💡',
                'title': 'Sentimientos comunes',
                'content': 'happy/glad/sad/surprised/excited/afraid + TO + verbo para expresar reacciones'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa las oraciones.',
                'questions': [
                    {'prompt': 'I am happy ___ you. (meet)', 'answer': 'to meet', 'hint': 'Adjetivo de sentimiento + to + verbo'},
                    {'prompt': 'It is important ___ on time. (arrive)', 'answer': 'to arrive', 'hint': 'It is + adj + to + verbo'},
                    {'prompt': 'She is old ___ to drive. (enough)', 'answer': 'enough', 'hint': 'Adj + ENOUGH + to'},
                    {'prompt': 'It is ___ hot to go outside. (too)', 'answer': 'too', 'hint': 'TOO + adj + to'},
                    {'prompt': 'It is easy ___ him to solve. (for)', 'answer': 'for', 'hint': 'FOR indica quién hace la acción'},
                    {'prompt': 'We were surprised ___ the news. (hear)', 'answer': 'to hear', 'hint': 'Adjetivo + to + verbo'},
                    {'prompt': 'The box is ___ heavy ___ carry. (too)', 'answer': 'too...to', 'hint': 'too + adj + to + verbo'},
                    {'prompt': 'He is strong ___ ___ lift it. (enough)', 'answer': 'enough to', 'hint': 'adj + enough + to + verbo'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'It is important ___ healthy.',
                        'options': ['eating', 'to eat', 'for eat', 'eat'],
                        'answer': 'to eat',
                        'explanation': 'It is + adj + TO + verbo'
                    },
                    {
                        'prompt': 'She is ___ young to drink alcohol.',
                        'options': ['enough', 'too', 'very', 'so'],
                        'answer': 'too',
                        'explanation': 'TOO indica exceso/impedimento'
                    },
                    {
                        'prompt': 'He is rich ___ to buy a Ferrari.',
                        'options': ['too', 'enough', 'very', 'so'],
                        'answer': 'enough',
                        'explanation': 'ENOUGH = suficiente para poder hacer algo'
                    },
                    {
                        'prompt': 'It is difficult ___ me ___ understand.',
                        'options': ['for...to', 'to...for', 'for...for', 'to...to'],
                        'answer': 'for...to',
                        'explanation': 'It is adj + FOR persona + TO verbo'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructuras Principales
| Patrón | Ejemplo |
|--------|---------|
| BE + adj + to + verb | I am **happy to help** |
| It is + adj + to + verb | It is **easy to learn** |
| It is + adj + FOR + person + to | It is **hard for me to understand** |
| adj + ENOUGH + to | old **enough to drive** |
| TOO + adj + to | **too tired to** work |

### Adjetivos Comunes
| Sentimientos | Evaluaciones |
|--------------|--------------|
| happy, sad, surprised | easy, difficult, hard |
| excited, afraid, glad | important, necessary |
| proud, ashamed, sorry | possible, impossible |

### Recuerda
- ✅ TO + verbo BASE (to meet, NOT to meeting)
- ✅ ENOUGH va DESPUÉS del adjetivo
- ✅ TOO va ANTES del adjetivo
- ✅ FOR + persona cuando especificas quién
'''
    },
    
    'used-to': {
        'title': 'Used To',
        'icon': '⏰',
        'difficulty': 'intermediate',
        'estimated_time': '20 min',
        'description': 'Habla sobre hábitos y situaciones del pasado que ya no existen.',
        
        'theory': {
            'introduction': '''
**USED TO** se usa para hablar de **hábitos** o **situaciones** en el pasado que **ya no son verdad** ahora.

Indica un **contraste** entre el pasado y el presente:
- Antes hacía algo → Ahora ya no lo hago
- Antes era de cierta manera → Ahora ya no es así
''',
            'rules': [
                {
                    'title': '✅ Afirmativo',
                    'rule': 'Sujeto + USED TO + verbo base',
                    'formula': 'S + used to + verb (base form)',
                    'examples': [
                        {'sentence': 'I **used to** play soccer every weekend.', 
                         'translation': 'Yo solía jugar fútbol cada fin de semana.',
                         'now': '(Ya no lo hago)'},
                        {'sentence': 'She **used to** live in Paris.', 
                         'translation': 'Ella solía vivir en París.',
                         'now': '(Ya no vive allí)'},
                        {'sentence': 'We **used to** be best friends.', 
                         'translation': 'Solíamos ser mejores amigos.',
                         'now': '(Ya no lo somos)'},
                        {'sentence': 'He **used to** smoke.', 
                         'translation': 'Él solía fumar.',
                         'now': '(Ya no fuma)'},
                        {'sentence': 'They **used to** work here.', 
                         'translation': 'Ellos solían trabajar aquí.',
                         'now': '(Ya no trabajan aquí)'},
                    ],
                    'note': '⚠️ "Used to" es IGUAL para TODAS las personas (I, you, he, she, etc.)'
                },
                {
                    'title': '❌ Negativo',
                    'rule': 'Sujeto + DID NOT + USE TO + verbo',
                    'formula': 'S + didn\'t + use to + verb',
                    'examples': [
                        {'sentence': 'I **didn\'t use to** like vegetables.', 
                         'translation': 'No solía gustarme las verduras.',
                         'now': '(Ahora sí me gustan)'},
                        {'sentence': 'She **didn\'t use to** exercise.', 
                         'translation': 'Ella no solía hacer ejercicio.',
                         'now': '(Ahora sí lo hace)'},
                        {'sentence': 'He **didn\'t use to** be so tall.', 
                         'translation': 'Él no solía ser tan alto.',
                         'now': '(Ahora es alto)'},
                    ],
                    'note': '⚠️ Con DIDN\'T → USE TO (sin D al final)'
                },
                {
                    'title': '❓ Interrogativo',
                    'rule': 'DID + Sujeto + USE TO + verbo?',
                    'formula': 'Did + S + use to + verb?',
                    'examples': [
                        {'sentence': '**Did** you **use to** play any sports?', 
                         'translation': '¿Solías practicar algún deporte?'},
                        {'sentence': '**Did** she **use to** work here?', 
                         'translation': '¿Ella solía trabajar aquí?'},
                        {'sentence': '**Did** they **use to** live together?', 
                         'translation': '¿Solían vivir juntos?'},
                    ],
                    'note': '⚠️ Con DID → USE TO (sin D al final)'
                }
            ],
            'structures': [
                {
                    'name': 'USED TO vs BE USED TO',
                    'structure': 'Diferencia importante',
                    'example': '''
- **USED TO + verb** = Hábito pasado (ya no existe)
  → "I used to smoke" = Fumaba antes (ya no fumo)
  
- **BE USED TO + noun/verb-ing** = Estar acostumbrado a
  → "I am used to smoking" = Estoy acostumbrado a fumar (todavía lo hago)
                    ''',
                    'note': '¡Son estructuras DIFERENTES con significados DIFERENTES!'
                },
                {
                    'name': 'USED TO vs Past Simple',
                    'structure': 'Cuándo usar cada uno',
                    'example': '''
- **USED TO** = Hábitos repetidos o estados permanentes del pasado
  → "I used to walk to school" (todos los días)
  
- **PAST SIMPLE** = Acciones específicas del pasado
  → "I walked to school yesterday" (una vez)
                    ''',
                    'note': 'USED TO enfatiza la repetición o duración'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I use to play soccer.',
                'correct': 'I used to play soccer.',
                'explanation': '❌ En afirmativo siempre es USED TO (con D)'
            },
            {
                'wrong': 'She didn\'t used to smoke.',
                'correct': 'She didn\'t use to smoke.',
                'explanation': '❌ Con DIDN\'T → USE TO (sin D porque DID ya indica pasado)'
            },
            {
                'wrong': 'Did you used to live here?',
                'correct': 'Did you use to live here?',
                'explanation': '❌ Con DID → USE TO (sin D porque DID ya indica pasado)'
            },
            {
                'wrong': 'I used to lived in Spain.',
                'correct': 'I used to live in Spain.',
                'explanation': '❌ Después de USED TO va el verbo BASE (live, no lived)'
            },
            {
                'wrong': 'I am used to play guitar.',
                'correct': 'I used to play guitar.',
                'explanation': '❌ "Am used to" = estar acostumbrado. Para hábito pasado: "used to" (sin BE)'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'La regla de la D',
                'content': 'Afirmativo = USED TO (con D). Con DID/DIDN\'T = USE TO (sin D, porque DID ya es pasado).'
            },
            {
                'icon': '🔄',
                'title': 'Contraste pasado-presente',
                'content': 'Siempre implica: "Antes SÍ/NO... pero ahora NO/SÍ". Hay un cambio.'
            },
            {
                'icon': '⚠️',
                'title': 'USED TO ≠ BE USED TO',
                'content': '"I used to smoke" = Fumaba antes. "I am used to the cold" = Estoy acostumbrado al frío.'
            },
            {
                'icon': '💡',
                'title': 'Verbo siempre BASE',
                'content': 'Después de USED TO / USE TO siempre va el verbo en forma base: play, live, work (no played, lived).'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con USED TO o USE TO.',
                'questions': [
                    {'prompt': 'I ___ play tennis when I was young.', 'answer': 'used to', 'hint': 'Afirmativo'},
                    {'prompt': 'She didn\'t ___ like coffee.', 'answer': 'use to', 'hint': 'Con didn\'t, sin D'},
                    {'prompt': 'Did you ___ live in London?', 'answer': 'use to', 'hint': 'Con did, sin D'},
                    {'prompt': 'We ___ go to the beach every summer.', 'answer': 'used to', 'hint': 'Afirmativo'},
                    {'prompt': 'He didn\'t ___ be so quiet.', 'answer': 'use to', 'hint': 'Con didn\'t, sin D'},
                    {'prompt': 'They ___ work together.', 'answer': 'used to', 'hint': 'Afirmativo'},
                    {'prompt': 'Did she ___ study here?', 'answer': 'use to', 'hint': 'Con did, sin D'},
                    {'prompt': 'I ___ hate vegetables, but now I love them.', 'answer': 'used to', 'hint': 'Afirmativo + contraste'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'When I was a child, I ___ play outside every day.',
                        'options': ['used to', 'use to', 'was used to', 'using to'],
                        'answer': 'used to',
                        'explanation': 'Afirmativo = USED TO (con D)'
                    },
                    {
                        'prompt': 'She didn\'t ___ speak English.',
                        'options': ['used to', 'use to', 'uses to', 'using to'],
                        'answer': 'use to',
                        'explanation': 'Con didn\'t = USE TO (sin D)'
                    },
                    {
                        'prompt': '___ you ___ have long hair?',
                        'options': ['Did...use to', 'Did...used to', 'Do...use to', 'Were...used to'],
                        'answer': 'Did...use to',
                        'explanation': 'Pregunta en pasado: Did + use to'
                    },
                    {
                        'prompt': 'He used to ___ very shy.',
                        'options': ['be', 'being', 'was', 'been'],
                        'answer': 'be',
                        'explanation': 'Después de used to = verbo BASE'
                    }
                ]
            },
            {
                'type': 'transformation',
                'instruction': 'Reescribe usando USED TO.',
                'questions': [
                    {'prompt': 'I played football in high school. (Now I don\'t)', 'answer': 'I used to play football in high school.'},
                    {'prompt': 'She didn\'t like pizza. (Now she does)', 'answer': "She didn't use to like pizza."},
                    {'prompt': 'Did you smoke? (In the past)', 'answer': 'Did you use to smoke?'},
                    {'prompt': 'We lived in New York. (Now we don\'t)', 'answer': 'We used to live in New York.'},
                    {'prompt': 'They were neighbors. (Not anymore)', 'answer': 'They used to be neighbors.'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura
| Forma | Estructura | Ejemplo |
|-------|-----------|---------|
| ✅ Afirmativo | S + **used to** + verb | I **used to** play |
| ❌ Negativo | S + didn't + **use to** + verb | I didn't **use to** play |
| ❓ Pregunta | Did + S + **use to** + verb? | Did you **use to** play? |

### La Regla de la D
| Situación | Forma | Porque |
|-----------|-------|--------|
| Afirmativo | used to | Es la forma pasada |
| Con didn't | use to | DID ya indica pasado |
| Con did | use to | DID ya indica pasado |

### USED TO vs BE USED TO
| Estructura | Significado | Ejemplo |
|------------|-------------|---------|
| used to + verb | Hábito pasado | I **used to smoke** (ya no) |
| be used to + noun/-ing | Estar acostumbrado | I **am used to** the cold |

### Recuerda
- ✅ "Used to" implica CAMBIO (antes ≠ ahora)
- ✅ Verbo siempre en forma BASE después
- ✅ Con DID/DIDN'T → sin la D
'''
    },
    
    'present-tenses': {
        'title': 'The Present (Simple & Continuous)',
        'icon': '🕐',
        'difficulty': 'beginner',
        'estimated_time': '30 min',
        'description': 'Domina los dos tiempos presentes: Simple y Continuo.',
        
        'theory': {
            'introduction': '''
El inglés tiene dos formas principales de presente:
- **Present Simple**: Para hábitos, hechos y rutinas
- **Present Continuous**: Para acciones en progreso ahora mismo
''',
            'rules': [
                {
                    'title': '📅 Present Simple - Formación',
                    'rule': 'Verbo base (+ -s/-es para he/she/it)',
                    'formula': 'S + verb (+ s/es) | S + don\'t/doesn\'t + verb',
                    'examples': [
                        {'sentence': 'I **work** every day.', 'translation': 'Trabajo todos los días.'},
                        {'sentence': 'She **works** at a bank.', 'translation': 'Ella trabaja en un banco.'},
                        {'sentence': 'They **don\'t** like coffee.', 'translation': 'A ellos no les gusta el café.'},
                        {'sentence': 'He **doesn\'t** speak French.', 'translation': 'Él no habla francés.'},
                        {'sentence': '**Do** you **live** here?', 'translation': '¿Vives aquí?'},
                        {'sentence': '**Does** she **play** tennis?', 'translation': '¿Ella juega tenis?'},
                    ],
                    'uses': [
                        '✓ Hábitos y rutinas: I wake up at 7 AM.',
                        '✓ Hechos generales: Water boils at 100°C.',
                        '✓ Horarios fijos: The train leaves at 9.',
                        '✓ Estados permanentes: She lives in Madrid.',
                    ]
                },
                {
                    'title': '🔄 Present Continuous - Formación',
                    'rule': 'Sujeto + BE + verbo-ING',
                    'formula': 'S + am/is/are + verb-ing',
                    'examples': [
                        {'sentence': 'I **am working** now.', 'translation': 'Estoy trabajando ahora.'},
                        {'sentence': 'She **is cooking** dinner.', 'translation': 'Ella está cocinando la cena.'},
                        {'sentence': 'They **are not watching** TV.', 'translation': 'Ellos no están viendo TV.'},
                        {'sentence': '**Is** he **sleeping**?', 'translation': '¿Él está durmiendo?'},
                        {'sentence': 'We **are studying** English.', 'translation': 'Estamos estudiando inglés.'},
                    ],
                    'uses': [
                        '✓ Acciones en progreso AHORA: I am reading.',
                        '✓ Situaciones temporales: She is staying with us.',
                        '✓ Planes futuros definidos: I am meeting John tomorrow.',
                        '✓ Cambios en desarrollo: The weather is getting colder.',
                    ]
                },
                {
                    'title': '⚖️ Simple vs Continuous - Diferencia Clave',
                    'rule': 'Simple = general/habitual. Continuous = ahora/temporal',
                    'formula': 'Pregunta: ¿Es siempre o es ahora mismo?',
                    'examples': [
                        {'simple': 'I **drink** coffee every morning.', 
                         'continuous': 'I **am drinking** coffee right now.',
                         'explanation': 'Siempre vs ahora mismo'},
                        {'simple': 'She **works** at Google.', 
                         'continuous': 'She **is working** from home today.',
                         'explanation': 'Permanente vs temporal'},
                        {'simple': 'They **play** football on Sundays.', 
                         'continuous': 'They **are playing** football at the moment.',
                         'explanation': 'Hábito vs en progreso'},
                    ]
                },
                {
                    'title': '🚫 Stative Verbs (NO usan Continuous)',
                    'rule': 'Verbos de estado: emociones, sentidos, posesión, pensamiento',
                    'formula': 'Estos verbos NO van con -ing normalmente',
                    'examples': [
                        {'wrong': 'I am loving this movie.', 'correct': 'I love this movie.', 'verb': 'love'},
                        {'wrong': 'She is knowing the answer.', 'correct': 'She knows the answer.', 'verb': 'know'},
                        {'wrong': 'He is having a car.', 'correct': 'He has a car.', 'verb': 'have (posesión)'},
                        {'wrong': 'They are understanding now.', 'correct': 'They understand now.', 'verb': 'understand'},
                    ],
                    'stative_verbs': [
                        '❤️ Emociones: love, hate, like, want, need, prefer',
                        '🧠 Pensamiento: know, believe, think*, understand, remember',
                        '👁️ Sentidos: see, hear, smell, taste, feel*',
                        '📦 Posesión: have*, own, belong, possess',
                        '🔗 Otros: be*, seem, appear, mean, cost, contain',
                    ],
                    'note': '*Algunos pueden usarse con -ing cuando cambian de significado'
                }
            ],
            'structures': [
                {
                    'name': 'Palabras Clave - Simple',
                    'structure': 'Indicadores de frecuencia',
                    'example': 'always, usually, often, sometimes, rarely, never, every day, on Mondays',
                    'note': 'Si ves estas palabras → usa Present Simple'
                },
                {
                    'name': 'Palabras Clave - Continuous',
                    'structure': 'Indicadores de "ahora"',
                    'example': 'now, right now, at the moment, currently, today, this week',
                    'note': 'Si ves estas palabras → usa Present Continuous'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She work at a hospital.',
                'correct': 'She works at a hospital.',
                'explanation': '❌ He/She/It necesitan -S en Present Simple'
            },
            {
                'wrong': 'I am work now.',
                'correct': 'I am working now.',
                'explanation': '❌ Present Continuous necesita verbo + ING'
            },
            {
                'wrong': 'He doesn\'t works here.',
                'correct': 'He doesn\'t work here.',
                'explanation': '❌ Con doesn\'t el verbo va SIN -S'
            },
            {
                'wrong': 'I am loving this song.',
                'correct': 'I love this song.',
                'explanation': '❌ LOVE es stative verb, no usa -ing'
            },
            {
                'wrong': 'What you are doing?',
                'correct': 'What are you doing?',
                'explanation': '❌ En preguntas: BE + sujeto + verbo-ing'
            },
            {
                'wrong': 'She is work from home today.',
                'correct': 'She is working from home today.',
                'explanation': '❌ AM/IS/ARE + verbo-ING (no verbo base)'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'La pregunta mágica',
                'content': '¿Es algo que pasa SIEMPRE o AHORA MISMO? Siempre = Simple. Ahora = Continuous.'
            },
            {
                'icon': '📝',
                'title': 'Regla de la S',
                'content': 'He/She/It → verbo + S (works, plays, goes). Con do/does → sin S.'
            },
            {
                'icon': '🚫',
                'title': 'Stative Verbs',
                'content': 'Verbos de emoción/pensamiento/sentidos = NO -ing. "I know" (no "I am knowing").'
            },
            {
                'icon': '📅',
                'title': 'Palabras clave',
                'content': 'Always, usually, every day = Simple. Now, at the moment = Continuous.'
            },
            {
                'icon': '✍️',
                'title': 'Spelling -ing',
                'content': 'Termina en -e → quitar e + ing (make→making). CVC → doblar (run→running).'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con Present Simple o Present Continuous.',
                'questions': [
                    {'prompt': 'She usually ___ (wake up) at 7 AM.', 'answer': 'wakes up', 'hint': 'Usually = hábito = Simple'},
                    {'prompt': 'Look! The baby ___ (sleep).', 'answer': 'is sleeping', 'hint': 'Look! = ahora = Continuous'},
                    {'prompt': 'I ___ (not/like) coffee.', 'answer': "don't like", 'hint': 'Like = stative verb = Simple'},
                    {'prompt': 'What ___ you ___ (do) right now?', 'answer': 'are...doing', 'hint': 'Right now = Continuous'},
                    {'prompt': 'Water ___ (boil) at 100°C.', 'answer': 'boils', 'hint': 'Hecho científico = Simple'},
                    {'prompt': 'He ___ (work) from home today.', 'answer': 'is working', 'hint': 'Today (temporal) = Continuous'},
                    {'prompt': 'They ___ (play) football every Sunday.', 'answer': 'play', 'hint': 'Every Sunday = hábito = Simple'},
                    {'prompt': 'Shh! The teacher ___ (explain) something.', 'answer': 'is explaining', 'hint': 'Shh! = en este momento = Continuous'},
                    {'prompt': '___ she ___ (know) the answer?', 'answer': 'Does...know', 'hint': 'Know = stative verb = Simple'},
                    {'prompt': 'I ___ (think) about changing jobs.', 'answer': 'am thinking', 'hint': 'Think about = considerar = puede ser Continuous'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'She ___ TV every evening.',
                        'options': ['watches', 'is watching', 'watch', 'watching'],
                        'answer': 'watches',
                        'explanation': 'Every evening = hábito = Present Simple + S'
                    },
                    {
                        'prompt': 'Be quiet! The baby ___.',
                        'options': ['sleeps', 'is sleeping', 'sleep', 'sleeping'],
                        'answer': 'is sleeping',
                        'explanation': 'Be quiet! = ahora mismo = Present Continuous'
                    },
                    {
                        'prompt': 'I ___ you are right.',
                        'options': ['think', 'am thinking', 'thinks', 'thinking'],
                        'answer': 'think',
                        'explanation': 'Think (opinión) = stative = Simple'
                    },
                    {
                        'prompt': '___ he ___ to work every day?',
                        'options': ['Does...drive', 'Is...driving', 'Do...drives', 'Does...drives'],
                        'answer': 'Does...drive',
                        'explanation': 'Every day = Simple. Does + verbo sin S'
                    }
                ]
            },
            {
                'type': 'error_correction',
                'instruction': 'Corrige los errores.',
                'questions': [
                    {'prompt': 'She don\'t like pizza.', 'answer': "She doesn't like pizza.", 'error': "don't → doesn't (she)"},
                    {'prompt': 'I am understand the problem.', 'answer': 'I understand the problem.', 'error': 'understand = stative (no -ing)'},
                    {'prompt': 'What you are doing?', 'answer': 'What are you doing?', 'error': 'Orden: What + are + you'},
                    {'prompt': 'He work at Google.', 'answer': 'He works at Google.', 'error': 'He → works (con S)'},
                    {'prompt': 'They is playing football.', 'answer': 'They are playing football.', 'error': 'They → are (no is)'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Present Simple
| Persona | Afirmativo | Negativo | Pregunta |
|---------|-----------|----------|----------|
| I/You/We/They | work | don't work | Do...work? |
| He/She/It | work**s** | doesn't work | Does...work? |

**Usa para:** Hábitos, hechos, horarios, estados permanentes

### Present Continuous
| Persona | Afirmativo | Negativo | Pregunta |
|---------|-----------|----------|----------|
| I | am working | am not working | Am I working? |
| He/She/It | is working | isn't working | Is...working? |
| You/We/They | are working | aren't working | Are...working? |

**Usa para:** Ahora mismo, temporal, planes, cambios

### Stative Verbs (NO continuous)
- ❤️ love, hate, like, want, need
- 🧠 know, believe, understand, remember
- 👁️ see, hear, smell (sentidos)
- 📦 have (posesión), own, belong

### Palabras Clave
| Simple | Continuous |
|--------|------------|
| always, usually | now, right now |
| every day/week | at the moment |
| often, sometimes | currently |
| on Mondays | today (temporal) |
'''
    },
    
    'articles': {
        'title': 'A, An, The or No Article',
        'icon': '📖',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Domina el uso de artículos en inglés: a, an, the y cuándo no usar ninguno.',
        
        'theory': {
            'introduction': '''
Los artículos en inglés son pequeñas palabras que van antes de sustantivos:
- **A/AN** = Artículos indefinidos (algo no específico)
- **THE** = Artículo definido (algo específico/conocido)
- **Ø (cero)** = Sin artículo (generalización)
''',
            'rules': [
                {
                    'title': '🅰️ A vs AN',
                    'rule': 'A = antes de consonante SONIDO. AN = antes de vocal SONIDO',
                    'formula': 'Es el SONIDO, no la letra',
                    'examples': [
                        {'article': 'a', 'word': 'book', 'explanation': 'B = sonido consonante'},
                        {'article': 'a', 'word': 'university', 'explanation': 'Suena /yuniversiti/ = consonante Y'},
                        {'article': 'a', 'word': 'European', 'explanation': 'Suena /yurupian/ = consonante Y'},
                        {'article': 'an', 'word': 'apple', 'explanation': 'A = sonido vocal'},
                        {'article': 'an', 'word': 'hour', 'explanation': 'H es muda, suena /aur/ = vocal'},
                        {'article': 'an', 'word': 'honest person', 'explanation': 'H es muda, suena /onest/ = vocal'},
                        {'article': 'an', 'word': 'MBA', 'explanation': 'Suena /em-bi-ei/ = vocal E'},
                    ]
                },
                {
                    'title': '🎯 Cuándo usar A/AN',
                    'rule': 'Primera mención, uno de muchos, profesiones, descripciones',
                    'formula': 'Indefinido = no específico',
                    'examples': [
                        {'sentence': 'I saw **a** dog in the park.', 'use': 'Primera mención (no sabemos cuál)'},
                        {'sentence': 'She is **a** teacher.', 'use': 'Profesión'},
                        {'sentence': 'I need **a** new phone.', 'use': 'Uno de muchos (cualquiera)'},
                        {'sentence': 'What **a** beautiful day!', 'use': 'Exclamaciones'},
                        {'sentence': 'He eats **an** apple every day.', 'use': 'Uno de un tipo'},
                    ]
                },
                {
                    'title': '📍 Cuándo usar THE',
                    'rule': 'Único, ya mencionado, específico, superlativo',
                    'formula': 'Definido = específico/conocido',
                    'examples': [
                        {'sentence': 'I saw a dog. **The** dog was big.', 'use': 'Ya mencionado antes'},
                        {'sentence': '**The** sun is bright today.', 'use': 'Único (solo hay uno)'},
                        {'sentence': 'Pass me **the** salt, please.', 'use': 'Ambos sabemos cuál'},
                        {'sentence': '**The** Eiffel Tower is in Paris.', 'use': 'Lugares famosos específicos'},
                        {'sentence': 'She is **the** best student.', 'use': 'Superlativos'},
                        {'sentence': '**The** rich should help **the** poor.', 'use': 'Grupos de personas'},
                    ]
                },
                {
                    'title': '⭕ Sin Artículo (Zero Article)',
                    'rule': 'Plurales generales, incontables generales, nombres propios',
                    'formula': 'Generalización = sin artículo',
                    'examples': [
                        {'sentence': '**Ø** Dogs are loyal animals.', 'use': 'Generalización (perros en general)'},
                        {'sentence': 'I love **Ø** music.', 'use': 'Incontable general'},
                        {'sentence': '**Ø** Water is essential for life.', 'use': 'Incontable general'},
                        {'sentence': 'I live in **Ø** Mexico.', 'use': 'Países (la mayoría)'},
                        {'sentence': 'She speaks **Ø** Spanish.', 'use': 'Idiomas'},
                        {'sentence': 'I go to **Ø** school every day.', 'use': 'Lugares como propósito'},
                        {'sentence': 'I have **Ø** breakfast at 8.', 'use': 'Comidas'},
                    ]
                },
                {
                    'title': '🏛️ Reglas Especiales con THE',
                    'rule': 'Cuándo SÍ y cuándo NO usar THE',
                    'formula': 'Memorizar patrones',
                    'examples': [
                        {'with_the': '**The** United States', 'without': '**Ø** Mexico', 'rule': 'THE con países plurales/con "of"'},
                        {'with_the': '**The** Pacific Ocean', 'without': '**Ø** Lake Titicaca', 'rule': 'THE con océanos, NO con lagos'},
                        {'with_the': '**The** Alps', 'without': '**Ø** Mount Everest', 'rule': 'THE con cadenas montañosas, NO con montañas individuales'},
                        {'with_the': '**The** Amazon River', 'without': '-', 'rule': 'THE con ríos'},
                        {'with_the': '**The** Smiths', 'without': '**Ø** John Smith', 'rule': 'THE con familias (plural), NO con nombres'},
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She is teacher.',
                'correct': 'She is a teacher.',
                'explanation': '❌ Profesiones necesitan A/AN'
            },
            {
                'wrong': 'I love the music.',
                'correct': 'I love music.',
                'explanation': '❌ Generalización = sin artículo (música en general)'
            },
            {
                'wrong': 'A hour later, he arrived.',
                'correct': 'An hour later, he arrived.',
                'explanation': '❌ "Hour" suena /aur/ (vocal) → AN'
            },
            {
                'wrong': 'I go to the school every day.',
                'correct': 'I go to school every day.',
                'explanation': '❌ "Go to school" (como propósito) = sin artículo'
            },
            {
                'wrong': 'The dogs are loyal.',
                'correct': 'Dogs are loyal.',
                'explanation': '❌ Generalización sobre todos los perros = sin artículo'
            },
            {
                'wrong': 'I visited United States.',
                'correct': 'I visited the United States.',
                'explanation': '❌ Países con "United" o plurales llevan THE'
            }
        ],
        
        'tips': [
            {
                'icon': '👂',
                'title': 'A vs AN = SONIDO',
                'content': 'No es la letra, es cómo suena. "A university" (suena Y), "An hour" (H muda).'
            },
            {
                'icon': '🎯',
                'title': 'THE = Específico',
                'content': 'Si ambos (hablante y oyente) saben exactamente cuál → THE.'
            },
            {
                'icon': '🌍',
                'title': 'Generalización = Ø',
                'content': 'Cuando hablas en GENERAL (toda la categoría): "Cats are cute" (todos los gatos).'
            },
            {
                'icon': '💼',
                'title': 'Profesiones',
                'content': 'Siempre A/AN: "He is A doctor", "She is AN engineer".'
            },
            {
                'icon': '🏔️',
                'title': 'Geografía',
                'content': 'THE: océanos, ríos, cadenas. NO THE: países, lagos, montañas individuales.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con A, AN, THE o Ø (sin artículo).',
                'questions': [
                    {'prompt': 'She is ___ doctor.', 'answer': 'a', 'hint': 'Profesión'},
                    {'prompt': 'I love ___ chocolate.', 'answer': 'Ø', 'hint': 'Generalización'},
                    {'prompt': 'Can you pass me ___ salt?', 'answer': 'the', 'hint': 'Específico (ambos saben cuál)'},
                    {'prompt': 'I waited for ___ hour.', 'answer': 'an', 'hint': '"Hour" suena /aur/'},
                    {'prompt': '___ Nile is the longest river.', 'answer': 'The', 'hint': 'Ríos llevan THE'},
                    {'prompt': 'I have ___ breakfast at 8 AM.', 'answer': 'Ø', 'hint': 'Comidas = sin artículo'},
                    {'prompt': 'She goes to ___ university.', 'answer': 'Ø', 'hint': 'Como propósito/actividad'},
                    {'prompt': 'He is ___ honest man.', 'answer': 'an', 'hint': '"Honest" = H muda'},
                    {'prompt': 'I saw ___ movie yesterday. ___ movie was great.', 'answer': 'a...The', 'hint': 'Primera vez = a, segunda = the'},
                    {'prompt': 'I visited ___ France last year.', 'answer': 'Ø', 'hint': 'Países = sin artículo'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': '___ water is essential for life.',
                        'options': ['A', 'An', 'The', 'Ø (no article)'],
                        'answer': 'Ø (no article)',
                        'explanation': 'Generalización sobre el agua = sin artículo'
                    },
                    {
                        'prompt': 'He is ___ European.',
                        'options': ['a', 'an', 'the', 'no article'],
                        'answer': 'a',
                        'explanation': '"European" suena /yuripian/ (Y = consonante)'
                    },
                    {
                        'prompt': 'I love playing ___ piano.',
                        'options': ['a', 'an', 'the', 'no article'],
                        'answer': 'the',
                        'explanation': 'Instrumentos musicales llevan THE'
                    },
                    {
                        'prompt': '___ Amazon is in South America.',
                        'options': ['A', 'An', 'The', 'No article'],
                        'answer': 'The',
                        'explanation': 'Ríos llevan THE'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### A vs AN (SONIDO, no letra)
| Artículo | Antes de | Ejemplos |
|----------|----------|----------|
| **A** | Sonido consonante | a book, a university, a European |
| **AN** | Sonido vocal | an apple, an hour, an MBA |

### Cuándo usar cada uno
| Artículo | Uso | Ejemplo |
|----------|-----|---------|
| A/AN | Primera mención | I saw **a** cat |
| A/AN | Profesiones | She is **a** nurse |
| A/AN | Uno de muchos | I need **a** pen |
| THE | Ya mencionado | **The** cat was black |
| THE | Único | **The** sun, **the** moon |
| THE | Específico/conocido | Pass **the** salt |
| THE | Superlativos | **The** best, **the** biggest |
| Ø | Plurales generales | **Ø** Dogs are loyal |
| Ø | Incontables generales | **Ø** Water is vital |
| Ø | Países (mayoría) | **Ø** Mexico, **Ø** Spain |
| Ø | Idiomas | **Ø** English, **Ø** Spanish |
| Ø | Comidas | **Ø** breakfast, **Ø** lunch |

### Geografía
| Con THE | Sin THE |
|---------|---------|
| Océanos: The Pacific | Lagos: Lake Titicaca |
| Ríos: The Amazon | Montañas: Mount Everest |
| Cadenas: The Alps | Países: Mexico, Spain |
| Desiertos: The Sahara | Continentes: Africa |
'''
    },
    
    'passive-voice': {
        'title': 'Passive Voice',
        'icon': '🔄',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Transforma oraciones activas a pasivas y entiende cuándo usar cada una.',
        
        'theory': {
            'introduction': '''
La **voz pasiva** cambia el enfoque de QUIÉN hace la acción a QUÉ recibe la acción.

**Activa**: The dog bit the man. (Quién hizo la acción)
**Pasiva**: The man was bitten by the dog. (Quién recibió la acción)

Se usa cuando:
- No sabemos quién hizo la acción
- No importa quién la hizo
- Queremos enfatizar el objeto
''',
            'rules': [
                {
                    'title': '🔨 Fórmula Básica',
                    'rule': 'Sujeto + BE + Participio Pasado (+ BY + agente)',
                    'formula': 'Object → Subject + BE + Past Participle',
                    'examples': [
                        {
                            'active': 'Someone **cleans** the office every day.',
                            'passive': 'The office **is cleaned** every day.',
                            'note': 'Present Simple'
                        },
                        {
                            'active': 'They **are building** a new hospital.',
                            'passive': 'A new hospital **is being built**.',
                            'note': 'Present Continuous'
                        },
                        {
                            'active': 'Shakespeare **wrote** Hamlet.',
                            'passive': 'Hamlet **was written** by Shakespeare.',
                            'note': 'Past Simple'
                        },
                        {
                            'active': 'They **have finished** the project.',
                            'passive': 'The project **has been finished**.',
                            'note': 'Present Perfect'
                        },
                        {
                            'active': 'They **will announce** the results tomorrow.',
                            'passive': 'The results **will be announced** tomorrow.',
                            'note': 'Future Simple'
                        },
                    ]
                },
                {
                    'title': '📊 Pasiva por Tiempo Verbal',
                    'rule': 'El verbo BE cambia según el tiempo, el participio NO cambia',
                    'formula': 'BE (conjugado) + Past Participle',
                    'examples': [
                        {'tense': 'Present Simple', 'be_form': 'am/is/are', 'example': 'The room **is cleaned** daily.'},
                        {'tense': 'Past Simple', 'be_form': 'was/were', 'example': 'The room **was cleaned** yesterday.'},
                        {'tense': 'Present Continuous', 'be_form': 'am/is/are being', 'example': 'The room **is being cleaned** now.'},
                        {'tense': 'Past Continuous', 'be_form': 'was/were being', 'example': 'The room **was being cleaned** when I arrived.'},
                        {'tense': 'Present Perfect', 'be_form': 'have/has been', 'example': 'The room **has been cleaned**.'},
                        {'tense': 'Past Perfect', 'be_form': 'had been', 'example': 'The room **had been cleaned** before we arrived.'},
                        {'tense': 'Future Simple', 'be_form': 'will be', 'example': 'The room **will be cleaned** tomorrow.'},
                        {'tense': 'Modal Verbs', 'be_form': 'modal + be', 'example': 'The room **must be cleaned**.'},
                    ]
                },
                {
                    'title': '🎯 BY + Agente',
                    'rule': 'Usa BY cuando es importante saber QUIÉN hizo la acción',
                    'formula': 'Passive + BY + agent',
                    'examples': [
                        {'sentence': 'The letter was written **by my grandmother**.', 'note': 'Agente importante'},
                        {'sentence': 'The cake was made **by a famous chef**.', 'note': 'Agente importante'},
                        {'sentence': 'The window was broken. (by someone - no importa)', 'note': 'Agente desconocido/no importante'},
                    ],
                    'note': 'Omite BY cuando el agente es obvio, desconocido o no importante'
                }
            ],
            'structures': [
                {
                    'name': 'Cuándo usar PASIVA',
                    'structure': 'Situaciones ideales',
                    'example': '''
✓ No sabemos quién: "My car was stolen." (no sé quién)
✓ Es obvio: "Spanish is spoken in Mexico." (obviamente por mexicanos)
✓ Foco en acción: "The bridge was built in 1990."
✓ Textos formales: "Applications must be submitted by Friday."
                    ''',
                    'note': 'Pasiva es más formal y objetiva'
                },
                {
                    'name': 'Cuándo usar ACTIVA',
                    'structure': 'Es mejor la activa cuando...',
                    'example': '''
✓ Sabes y quieres decir quién: "John fixed my car."
✓ Es más natural/claro: "I love you." (no "You are loved by me")
✓ Conversación informal: La activa es más directa
                    ''',
                    'note': 'La activa es más común en habla cotidiana'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'The car was repair yesterday.',
                'correct': 'The car was repaired yesterday.',
                'explanation': '❌ Necesitas el PARTICIPIO PASADO (repaired, no repair)'
            },
            {
                'wrong': 'English is speak in many countries.',
                'correct': 'English is spoken in many countries.',
                'explanation': '❌ "Speak" es irregular: speak-spoke-SPOKEN'
            },
            {
                'wrong': 'The letter was wrote by John.',
                'correct': 'The letter was written by John.',
                'explanation': '❌ "Write" es irregular: write-wrote-WRITTEN'
            },
            {
                'wrong': 'The project is been finished.',
                'correct': 'The project has been finished.',
                'explanation': '❌ Present Perfect Passive = HAS/HAVE BEEN + participio'
            },
            {
                'wrong': 'The cake was make by my mom.',
                'correct': 'The cake was made by my mom.',
                'explanation': '❌ "Make" es irregular: make-made-MADE'
            }
        ],
        
        'tips': [
            {
                'icon': '🔄',
                'title': 'Transformación paso a paso',
                'content': '1) Objeto → nuevo sujeto. 2) Agregar BE (conjugado). 3) Verbo → participio. 4) BY + sujeto original (opcional).'
            },
            {
                'icon': '📝',
                'title': 'Participios irregulares',
                'content': 'Memoriza los más comunes: written, spoken, made, done, seen, taken, given, broken, stolen.'
            },
            {
                'icon': '🎯',
                'title': '¿Necesito BY?',
                'content': 'Solo si el agente es importante, interesante o inesperado. Si es obvio u desconocido, omítelo.'
            },
            {
                'icon': '⚡',
                'title': 'Truco rápido',
                'content': 'Si puedes agregar "by someone" y tiene sentido → es pasiva correcta.'
            }
        ],
        
        'exercises': [
            {
                'type': 'transformation',
                'instruction': 'Transforma las oraciones a voz pasiva.',
                'questions': [
                    {'active': 'Someone stole my bike.', 'passive': 'My bike was stolen.'},
                    {'active': 'They speak English in Australia.', 'passive': 'English is spoken in Australia.'},
                    {'active': 'Bell invented the telephone.', 'passive': 'The telephone was invented by Bell.'},
                    {'active': 'They are building a new mall.', 'passive': 'A new mall is being built.'},
                    {'active': 'Someone has eaten my sandwich.', 'passive': 'My sandwich has been eaten.'},
                    {'active': 'They will announce the winner tomorrow.', 'passive': 'The winner will be announced tomorrow.'},
                    {'active': 'People must wear masks.', 'passive': 'Masks must be worn.'},
                    {'active': 'Shakespeare wrote Romeo and Juliet.', 'passive': 'Romeo and Juliet was written by Shakespeare.'}
                ]
            },
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la forma pasiva correcta.',
                'questions': [
                    {'prompt': 'English ___ (speak) all over the world.', 'answer': 'is spoken', 'hint': 'Present Simple Passive'},
                    {'prompt': 'The Mona Lisa ___ (paint) by Leonardo da Vinci.', 'answer': 'was painted', 'hint': 'Past Simple Passive'},
                    {'prompt': 'A new school ___ (build) right now.', 'answer': 'is being built', 'hint': 'Present Continuous Passive'},
                    {'prompt': 'The report ___ (finish) by tomorrow.', 'answer': 'will be finished', 'hint': 'Future Passive'},
                    {'prompt': 'The homework ___ already ___ (do).', 'answer': 'has...been done', 'hint': 'Present Perfect Passive'},
                    {'prompt': 'This song ___ (write) in 1985.', 'answer': 'was written', 'hint': 'Past Simple Passive + irregular'},
                    {'prompt': 'The rules must ___ (follow).', 'answer': 'be followed', 'hint': 'Modal Passive'},
                    {'prompt': 'Many books ___ (publish) every year.', 'answer': 'are published', 'hint': 'Present Simple Passive (plural)'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la forma pasiva correcta.',
                'questions': [
                    {
                        'prompt': 'The window ___ yesterday.',
                        'options': ['broke', 'was broke', 'was broken', 'is broken'],
                        'answer': 'was broken',
                        'explanation': 'Past Simple Passive: was/were + participio (broken)'
                    },
                    {
                        'prompt': 'This book ___ by millions of people.',
                        'options': ['has read', 'has been read', 'was been read', 'have been read'],
                        'answer': 'has been read',
                        'explanation': 'Present Perfect Passive: has/have been + participio'
                    },
                    {
                        'prompt': 'The pizza ___ right now.',
                        'options': ['is made', 'is being made', 'was made', 'is been made'],
                        'answer': 'is being made',
                        'explanation': 'Present Continuous Passive: is/are being + participio'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Fórmula General
**Sujeto + BE (conjugado) + Participio Pasado + (by + agente)**

### Pasiva por Tiempo Verbal
| Tiempo | Activa | Pasiva |
|--------|--------|--------|
| Present Simple | clean(s) | am/is/are cleaned |
| Past Simple | cleaned | was/were cleaned |
| Present Continuous | am/is/are cleaning | am/is/are being cleaned |
| Past Continuous | was/were cleaning | was/were being cleaned |
| Present Perfect | have/has cleaned | have/has been cleaned |
| Past Perfect | had cleaned | had been cleaned |
| Future Simple | will clean | will be cleaned |
| Modal | can clean | can be cleaned |

### Participios Irregulares Comunes
| Base | Past | Participio |
|------|------|------------|
| write | wrote | **written** |
| speak | spoke | **spoken** |
| take | took | **taken** |
| make | made | **made** |
| do | did | **done** |
| see | saw | **seen** |
| give | gave | **given** |
| break | broke | **broken** |
| steal | stole | **stolen** |
| eat | ate | **eaten** |
'''
    },
    
    'conditionals': {
        'title': 'First & Second Conditional',
        'icon': '🔀',
        'difficulty': 'intermediate',
        'estimated_time': '30 min',
        'description': 'Expresa condiciones reales (primer condicional) e hipotéticas (segundo condicional).',
        
        'theory': {
            'introduction': '''
Los condicionales expresan situaciones y sus resultados:
- **First Conditional**: Situaciones REALES y POSIBLES en el futuro
- **Second Conditional**: Situaciones HIPOTÉTICAS o IMPROBABLES
''',
            'rules': [
                {
                    'title': '1️⃣ First Conditional (Posible/Real)',
                    'rule': 'IF + Present Simple, WILL + verbo base',
                    'formula': 'If + present simple, will + verb',
                    'examples': [
                        {
                            'sentence': '**If** it **rains**, I **will stay** home.',
                            'translation': 'Si llueve, me quedaré en casa.',
                            'situation': 'Es posible que llueva (situación real)'
                        },
                        {
                            'sentence': '**If** you **study** hard, you **will pass** the exam.',
                            'translation': 'Si estudias duro, aprobarás el examen.',
                            'situation': 'Es posible que estudies'
                        },
                        {
                            'sentence': '**If** she **calls**, I **will tell** her.',
                            'translation': 'Si ella llama, le diré.',
                            'situation': 'Es posible que llame'
                        },
                        {
                            'sentence': 'I **will buy** a car **if** I **get** the job.',
                            'translation': 'Compraré un auto si consigo el trabajo.',
                            'situation': 'La cláusula IF puede ir al final'
                        },
                    ],
                    'uses': [
                        '✓ Predicciones reales: If it snows, schools will close.',
                        '✓ Promesas: If you help me, I will help you.',
                        '✓ Advertencias: If you touch that, you will burn yourself.',
                        '✓ Planes condicionales: If I finish early, I will call you.',
                    ]
                },
                {
                    'title': '2️⃣ Second Conditional (Hipotético/Improbable)',
                    'rule': 'IF + Past Simple, WOULD + verbo base',
                    'formula': 'If + past simple, would + verb',
                    'examples': [
                        {
                            'sentence': '**If** I **had** a million dollars, I **would travel** the world.',
                            'translation': 'Si tuviera un millón de dólares, viajaría por el mundo.',
                            'situation': 'No tengo un millón (hipotético)'
                        },
                        {
                            'sentence': '**If** I **were** you, I **would study** more.',
                            'translation': 'Si yo fuera tú, estudiaría más.',
                            'situation': 'No soy tú (imposible)'
                        },
                        {
                            'sentence': '**If** she **spoke** English, she **would get** the job.',
                            'translation': 'Si ella hablara inglés, conseguiría el trabajo.',
                            'situation': 'Ella no habla inglés (hipotético)'
                        },
                        {
                            'sentence': 'I **would buy** that house **if** it **were** cheaper.',
                            'translation': 'Compraría esa casa si fuera más barata.',
                            'situation': 'La casa no es barata (irreal)'
                        },
                    ],
                    'uses': [
                        '✓ Imaginación: If I could fly, I would visit every country.',
                        '✓ Consejos: If I were you, I would apologize.',
                        '✓ Deseos irreales: If I had more time, I would learn piano.',
                        '✓ Situaciones contrarias: If I lived in Paris, I would eat croissants every day.',
                    ],
                    'note': '⚠️ Con "I/he/she/it" se usa WERE (no was) en inglés formal: "If I were..."'
                },
                {
                    'title': '⚖️ Diferencia Clave',
                    'rule': 'First = posible. Second = hipotético/improbable',
                    'formula': 'Probabilidad real vs imaginación',
                    'examples': [
                        {
                            'first': '**If** I **have** time tomorrow, I **will help** you.',
                            'second': '**If** I **had** time (but I don\'t), I **would help** you.',
                            'explanation': 'First: Mañana podría tener tiempo. Second: No tengo tiempo ahora.'
                        },
                        {
                            'first': '**If** it **rains**, we **will cancel** the picnic.',
                            'second': '**If** it **rained** (but it probably won\'t), we **would cancel**.',
                            'explanation': 'First: Es posible que llueva. Second: Probablemente no lloverá.'
                        },
                    ]
                },
                {
                    'title': '📝 Variaciones y Alternativas',
                    'rule': 'Otras expresiones en lugar de IF y WILL/WOULD',
                    'formula': 'Sinónimos y variantes',
                    'examples': [
                        {'variant': 'UNLESS = If not', 'example': 'I will go **unless** it rains. (= if it doesn\'t rain)'},
                        {'variant': 'IN CASE = por si acaso', 'example': 'Take an umbrella **in case** it rains.'},
                        {'variant': 'CAN/COULD', 'example': 'If you study, you **can** pass. / If I had money, I **could** buy it.'},
                        {'variant': 'MIGHT', 'example': 'If it rains, I **might** stay home. (menos seguro que will)'},
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'If it will rain, I will stay home.',
                'correct': 'If it rains, I will stay home.',
                'explanation': '❌ Después de IF usa PRESENT (rains), no WILL'
            },
            {
                'wrong': 'If I would have money, I would buy it.',
                'correct': 'If I had money, I would buy it.',
                'explanation': '❌ Después de IF usa PAST SIMPLE (had), no WOULD'
            },
            {
                'wrong': 'If I was you, I would study.',
                'correct': 'If I were you, I would study.',
                'explanation': '❌ Con "If I/he/she..." usa WERE (formal)'
            },
            {
                'wrong': 'If you will help me, I will pay you.',
                'correct': 'If you help me, I will pay you.',
                'explanation': '❌ IF + present simple, NO will'
            },
            {
                'wrong': 'If I won the lottery, I will buy a house.',
                'correct': 'If I won the lottery, I would buy a house.',
                'explanation': '❌ Second conditional: If + past, WOULD + verb'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'Regla de oro: NO WILL/WOULD después de IF',
                'content': 'First: If + PRESENT, will... Second: If + PAST, would... NUNCA: "If I will..." o "If I would..."'
            },
            {
                'icon': '🤔',
                'title': '¿Cuál uso?',
                'content': '¿Es posible que pase? → First. ¿Es imaginación/improbable? → Second.'
            },
            {
                'icon': '👑',
                'title': 'IF I WERE (no was)',
                'content': 'En second conditional formal: "If I were rich..." "If she were here..." WERE para todos.'
            },
            {
                'icon': '🔄',
                'title': 'El orden no importa',
                'content': '"If it rains, I will stay" = "I will stay if it rains". Coma solo cuando IF va primero.'
            },
            {
                'icon': '💡',
                'title': 'Truco para Second',
                'content': 'Si puedes agregar "but I\'m not/I don\'t" → es Second. "If I were rich (but I\'m not)..."'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la forma correcta del verbo.',
                'questions': [
                    {'prompt': 'If it ___ (rain) tomorrow, I will stay home.', 'answer': 'rains', 'hint': 'First: If + present'},
                    {'prompt': 'If I ___ (be) you, I would apologize.', 'answer': 'were', 'hint': 'Second: If + were'},
                    {'prompt': 'She will call you if she ___ (have) time.', 'answer': 'has', 'hint': 'First: if + present simple'},
                    {'prompt': 'If I ___ (have) more money, I would buy a bigger house.', 'answer': 'had', 'hint': 'Second: If + past simple'},
                    {'prompt': 'If you ___ (study), you will pass the exam.', 'answer': 'study', 'hint': 'First: If + present'},
                    {'prompt': 'I ___ (travel) the world if I won the lottery.', 'answer': 'would travel', 'hint': 'Second: would + verb'},
                    {'prompt': 'If she ___ (speak) Spanish, she could work in Mexico.', 'answer': 'spoke', 'hint': 'Second: If + past simple'},
                    {'prompt': 'We ___ (go) to the beach if the weather is nice.', 'answer': 'will go', 'hint': 'First: will + verb'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'If I ___ rich, I would donate to charity.',
                        'options': ['am', 'was', 'were', 'will be'],
                        'answer': 'were',
                        'explanation': 'Second conditional: If + were (hipotético)'
                    },
                    {
                        'prompt': 'If you ___ hard, you will succeed.',
                        'options': ['work', 'worked', 'will work', 'would work'],
                        'answer': 'work',
                        'explanation': 'First conditional: If + present simple'
                    },
                    {
                        'prompt': 'She ___ angry if you don\'t call her.',
                        'options': ['would be', 'will be', 'was', 'were'],
                        'answer': 'will be',
                        'explanation': 'First conditional: will + be (posible)'
                    },
                    {
                        'prompt': 'If I ___ you, I would accept the offer.',
                        'options': ['am', 'was', 'were', 'will be'],
                        'answer': 'were',
                        'explanation': 'Second: "If I were you" (hipotético)'
                    },
                    {
                        'prompt': 'What ___ you do if you won the lottery?',
                        'options': ['will', 'would', 'do', 'did'],
                        'answer': 'would',
                        'explanation': 'Second conditional (improbable) → would'
                    }
                ]
            },
            {
                'type': 'classification',
                'instruction': 'Clasifica: ¿First o Second Conditional?',
                'questions': [
                    {'sentence': 'If it rains, I will take an umbrella.', 'answer': 'First', 'reason': 'Posible que llueva'},
                    {'sentence': 'If I were a bird, I would fly away.', 'answer': 'Second', 'reason': 'Imposible ser un pájaro'},
                    {'sentence': 'If you call me, I will help you.', 'answer': 'First', 'reason': 'Es posible que llames'},
                    {'sentence': 'If I had wings, I would fly.', 'answer': 'Second', 'reason': 'No tengo alas (hipotético)'},
                    {'sentence': 'If she studies, she will pass.', 'answer': 'First', 'reason': 'Es posible que estudie'},
                    {'sentence': 'If I lived in Japan, I would learn Japanese.', 'answer': 'Second', 'reason': 'No vivo en Japón'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### First Conditional (Real/Posible)
**If + Present Simple, WILL + verb**

| Ejemplo | Situación |
|---------|-----------|
| If it rains, I will stay home. | Posible que llueva |
| If you study, you will pass. | Posible que estudies |

**Usa para:** Predicciones reales, promesas, advertencias

### Second Conditional (Hipotético/Improbable)
**If + Past Simple, WOULD + verb**

| Ejemplo | Situación |
|---------|-----------|
| If I had money, I would travel. | No tengo dinero |
| If I were you, I would apologize. | No soy tú |

**Usa para:** Imaginación, consejos, deseos irreales

### ⚠️ Reglas Importantes
1. **NUNCA** uses WILL/WOULD después de IF
2. Con "If I/he/she" → usa **WERE** (no was)
3. La cláusula IF puede ir al principio o al final
4. Coma (,) solo cuando IF va primero

### Cuadro Comparativo
| Aspecto | First | Second |
|---------|-------|--------|
| IF + | Present | Past |
| Result | WILL + verb | WOULD + verb |
| Probabilidad | Posible | Hipotético |
| Tiempo | Futuro real | Presente irreal |
'''
    },
    
    'infinitive-purpose': {
        'title': 'Infinitive of Purpose',
        'icon': '🎯',
        'difficulty': 'beginner',
        'estimated_time': '15 min',
        'description': 'Usa el infinitivo para expresar propósito o razón de una acción.',
        
        'theory': {
            'introduction': '''
El **infinitivo de propósito** (TO + verb) se usa para explicar **POR QUÉ** hacemos algo.
Responde a la pregunta: "¿Para qué?" o "¿Con qué fin?"

Es equivalente a "para" o "con el fin de" en español.
''',
            'rules': [
                {
                    'title': '🎯 Estructura Básica',
                    'rule': 'Acción + TO + verbo (propósito)',
                    'formula': 'Subject + verb + TO + infinitive',
                    'examples': [
                        {
                            'sentence': 'I went to the store **to buy** milk.',
                            'translation': 'Fui a la tienda **para comprar** leche.',
                            'question': '¿Para qué fui? → Para comprar leche'
                        },
                        {
                            'sentence': 'She studies hard **to pass** her exams.',
                            'translation': 'Ella estudia duro **para aprobar** sus exámenes.',
                            'question': '¿Para qué estudia? → Para aprobar'
                        },
                        {
                            'sentence': 'He works overtime **to earn** more money.',
                            'translation': 'Él trabaja horas extra **para ganar** más dinero.',
                            'question': '¿Para qué trabaja? → Para ganar más'
                        },
                        {
                            'sentence': 'We use a dictionary **to find** new words.',
                            'translation': 'Usamos un diccionario **para encontrar** palabras nuevas.',
                            'question': '¿Para qué lo usamos? → Para encontrar palabras'
                        },
                    ]
                },
                {
                    'title': '📝 IN ORDER TO (más formal)',
                    'rule': 'IN ORDER TO + verbo = TO + verbo (más enfático)',
                    'formula': 'Subject + verb + IN ORDER TO + infinitive',
                    'examples': [
                        {
                            'informal': 'I wake up early **to catch** the bus.',
                            'formal': 'I wake up early **in order to catch** the bus.',
                            'note': 'Mismo significado, más formal'
                        },
                        {
                            'informal': 'She saved money **to buy** a car.',
                            'formal': 'She saved money **in order to buy** a car.',
                            'note': 'Más usado en escritura formal'
                        },
                    ],
                    'note': 'IN ORDER TO es intercambiable con TO, pero más formal/enfático'
                },
                {
                    'title': '❌ Negativo: IN ORDER NOT TO / SO AS NOT TO',
                    'rule': 'Para propósito negativo',
                    'formula': 'Subject + verb + IN ORDER NOT TO / SO AS NOT TO + infinitive',
                    'examples': [
                        {
                            'sentence': 'I left early **in order not to** be late.',
                            'translation': 'Salí temprano **para no** llegar tarde.',
                        },
                        {
                            'sentence': 'She whispered **so as not to** wake the baby.',
                            'translation': 'Ella susurró **para no** despertar al bebé.',
                        },
                        {
                            'sentence': 'He studied hard **in order not to** fail.',
                            'translation': 'Estudió duro **para no** reprobar.',
                        },
                    ],
                    'note': '⚠️ NO uses "to not" - usa "in order not to" o "so as not to"'
                },
                {
                    'title': '🔧 FOR + Noun/-ING (Propósito con sustantivo)',
                    'rule': 'FOR + noun/gerund para propósito',
                    'formula': 'FOR + noun / FOR + verb-ing',
                    'examples': [
                        {
                            'with_to': 'I use this knife **to cut** vegetables.',
                            'with_for': 'This knife is **for cutting** vegetables.',
                            'note': 'FOR + gerund describe la función'
                        },
                        {
                            'with_to': 'I went to the gym **to exercise**.',
                            'with_for': 'I went to the gym **for a workout**.',
                            'note': 'FOR + noun también expresa propósito'
                        },
                    ]
                }
            ],
            'structures': [
                {
                    'name': 'Preguntas con WHY',
                    'structure': 'La respuesta natural a WHY usa infinitivo de propósito',
                    'example': '''
Q: **Why** did you go to the supermarket?
A: **To buy** groceries.

Q: **Why** is she studying?
A: **To pass** her exam.
                    ''',
                    'note': 'TO + verb es la forma natural de responder "¿Por qué?"'
                },
                {
                    'name': 'Con What...for?',
                    'structure': 'What is this for? → propósito/función',
                    'example': '''
Q: **What** is this tool **for**?
A: It's **for opening** bottles. / **To open** bottles.
                    ''',
                    'note': 'Ambas formas son correctas para describir función'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I came here for to study.',
                'correct': 'I came here to study.',
                'explanation': '❌ NO uses FOR + TO. Solo TO o solo FOR + noun'
            },
            {
                'wrong': 'She exercises for lose weight.',
                'correct': 'She exercises to lose weight.',
                'explanation': '❌ FOR + verbo base es incorrecto. Usa TO + verb'
            },
            {
                'wrong': 'I left early to not be late.',
                'correct': 'I left early in order not to be late.',
                'explanation': '❌ "To not" es incorrecto. Usa "in order not to"'
            },
            {
                'wrong': 'I need a pen for to write.',
                'correct': 'I need a pen to write. / I need a pen for writing.',
                'explanation': '❌ FOR TO es incorrecto. Elige uno: TO + verb o FOR + -ing'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'La pregunta clave',
                'content': 'Si puedes preguntar "¿Para qué?" → la respuesta es TO + verbo.'
            },
            {
                'icon': '❌',
                'title': 'Nunca FOR + TO',
                'content': 'INCORRECTO: "for to study". CORRECTO: "to study" o "for studying".'
            },
            {
                'icon': '📝',
                'title': 'Negativo formal',
                'content': 'Para "para no..." usa "in order not to" o "so as not to" (no "to not").'
            },
            {
                'icon': '🔧',
                'title': 'Función de objetos',
                'content': '"What is it for?" → "It\'s for + verb-ing" describe para qué sirve algo.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con TO o FOR.',
                'questions': [
                    {'prompt': 'I went to the library ___ study.', 'answer': 'to', 'hint': 'Propósito = TO + verbo'},
                    {'prompt': 'This brush is ___ painting.', 'answer': 'for', 'hint': 'Función = FOR + -ing'},
                    {'prompt': 'She called me ___ ask a question.', 'answer': 'to', 'hint': 'Propósito = TO + verbo'},
                    {'prompt': 'I need glasses ___ reading.', 'answer': 'for', 'hint': 'Función = FOR + -ing'},
                    {'prompt': 'He saved money ___ buy a car.', 'answer': 'to', 'hint': 'Propósito = TO + verbo'},
                    {'prompt': 'What is this tool ___?', 'answer': 'for', 'hint': '"What...for?" pregunta función'}
                ]
            },
            {
                'type': 'combine',
                'instruction': 'Une las dos oraciones usando TO (infinitivo de propósito).',
                'questions': [
                    {
                        'sentence1': 'I went to the supermarket.',
                        'sentence2': 'I wanted to buy food.',
                        'answer': 'I went to the supermarket to buy food.'
                    },
                    {
                        'sentence1': 'She studies hard.',
                        'sentence2': 'She wants to pass her exams.',
                        'answer': 'She studies hard to pass her exams.'
                    },
                    {
                        'sentence1': 'He wakes up early.',
                        'sentence2': 'He wants to exercise.',
                        'answer': 'He wakes up early to exercise.'
                    },
                    {
                        'sentence1': 'I turned off my phone.',
                        'sentence2': 'I didn\'t want to be disturbed.',
                        'answer': 'I turned off my phone in order not to be disturbed.'
                    }
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I came here ___ learn English.',
                        'options': ['for', 'to', 'for to', 'in order'],
                        'answer': 'to',
                        'explanation': 'Propósito: TO + verbo (no FOR TO)'
                    },
                    {
                        'prompt': 'This machine is ___ making coffee.',
                        'options': ['to', 'for', 'in order to', 'so as to'],
                        'answer': 'for',
                        'explanation': 'Función de objeto: FOR + -ing'
                    },
                    {
                        'prompt': 'She spoke quietly ___ wake the baby.',
                        'options': ['to not', 'not to', 'in order not to', 'for not'],
                        'answer': 'in order not to',
                        'explanation': 'Propósito negativo: in order not to'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura Principal
**Acción + TO + verbo** = Para + verbo

| Oración | Propósito |
|---------|-----------|
| I study hard **to pass**. | Para aprobar |
| She works **to earn** money. | Para ganar dinero |

### Formas Equivalentes
| Forma | Ejemplo | Formalidad |
|-------|---------|------------|
| TO + verb | to study | Neutral |
| IN ORDER TO + verb | in order to study | Formal |
| SO AS TO + verb | so as to study | Formal |

### Forma Negativa
| Forma | Ejemplo |
|-------|---------|
| ❌ to not | INCORRECTO |
| ✅ in order not to | in order not to be late |
| ✅ so as not to | so as not to wake him |

### FOR + Noun/-ing (Función)
| Estructura | Ejemplo |
|------------|---------|
| FOR + noun | a room **for guests** |
| FOR + -ing | a knife **for cutting** |

### ⚠️ Errores Comunes
- ❌ for to study → ✅ to study
- ❌ for study → ✅ to study / for studying
- ❌ to not be → ✅ in order not to be
'''
    },
    
    'past-simple-continuous': {
        'title': 'Past Simple vs Past Continuous',
        'icon': '⏮️',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Diferencia entre acciones completas y acciones en progreso en el pasado.',
        
        'theory': {
            'introduction': '''
**Past Simple**: Acciones COMPLETAS en el pasado (empezaron y terminaron).
**Past Continuous**: Acciones EN PROGRESO en un momento del pasado.

Frecuentemente se usan JUNTOS para mostrar una acción larga interrumpida por una corta.
''',
            'rules': [
                {
                    'title': '✅ Past Simple - Formación',
                    'rule': 'Verbo + ED (regulares) o segunda columna (irregulares)',
                    'formula': 'S + verb-ed / S + didn\'t + verb / Did + S + verb?',
                    'examples': [
                        {'sentence': 'I **worked** yesterday.', 'translation': 'Trabajé ayer.'},
                        {'sentence': 'She **went** to Paris last year.', 'translation': 'Ella fue a París el año pasado.'},
                        {'sentence': 'They **didn\'t come** to the party.', 'translation': 'Ellos no vinieron a la fiesta.'},
                        {'sentence': '**Did** you **see** that movie?', 'translation': '¿Viste esa película?'},
                    ],
                    'uses': [
                        '✓ Acciones completas: I ate breakfast at 8.',
                        '✓ Secuencia de acciones: I woke up, took a shower, and left.',
                        '✓ Tiempo específico: She called me yesterday.',
                    ]
                },
                {
                    'title': '🔄 Past Continuous - Formación',
                    'rule': 'WAS/WERE + verbo-ING',
                    'formula': 'S + was/were + verb-ing',
                    'examples': [
                        {'sentence': 'I **was working** at 9 PM.', 'translation': 'Estaba trabajando a las 9 PM.'},
                        {'sentence': 'They **were playing** football.', 'translation': 'Ellos estaban jugando fútbol.'},
                        {'sentence': 'She **wasn\'t listening** to me.', 'translation': 'Ella no me estaba escuchando.'},
                        {'sentence': '**Were** you **sleeping** when I called?', 'translation': '¿Estabas durmiendo cuando llamé?'},
                    ],
                    'uses': [
                        '✓ Acción en progreso: At 8 PM, I was studying.',
                        '✓ Acción de fondo: The sun was shining.',
                        '✓ Dos acciones simultáneas: While I was cooking, she was reading.',
                    ]
                },
                {
                    'title': '⚡ WHEN vs WHILE (La clave)',
                    'rule': 'WHEN + Past Simple, WHILE + Past Continuous',
                    'formula': 'When + short action, While + long action',
                    'examples': [
                        {
                            'sentence': 'I **was watching** TV **when** the phone **rang**.',
                            'translation': 'Estaba viendo TV cuando sonó el teléfono.',
                            'explanation': 'Acción larga (watching) interrumpida por corta (rang)'
                        },
                        {
                            'sentence': '**While** I **was walking**, I **saw** an accident.',
                            'translation': 'Mientras caminaba, vi un accidente.',
                            'explanation': 'WHILE + continuous, acción corta en simple'
                        },
                        {
                            'sentence': '**While** she **was cooking**, he **was cleaning**.',
                            'translation': 'Mientras ella cocinaba, él limpiaba.',
                            'explanation': 'Dos acciones simultáneas = ambas continuous'
                        },
                    ]
                }
            ],
            'structures': [
                {
                    'name': 'Patrón de Interrupción',
                    'structure': 'Past Continuous + WHEN + Past Simple',
                    'example': 'I was sleeping WHEN the alarm went off.',
                    'note': 'La acción larga es INTERRUMPIDA por la corta'
                },
                {
                    'name': 'Acciones Paralelas',
                    'structure': 'WHILE + Past Cont., Past Cont.',
                    'example': 'While I was reading, my sister was playing.',
                    'note': 'Dos acciones ocurriendo AL MISMO TIEMPO'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'When I was sleeping, the phone was ringing.',
                'correct': 'When I was sleeping, the phone rang.',
                'explanation': '❌ El teléfono suena una vez (acción corta) = Past Simple'
            },
            {
                'wrong': 'I was see him yesterday.',
                'correct': 'I saw him yesterday.',
                'explanation': '❌ "Yesterday" indica acción completa = Past Simple, no Continuous'
            },
            {
                'wrong': 'While I watched TV, she called.',
                'correct': 'While I was watching TV, she called.',
                'explanation': '❌ WHILE necesita Past Continuous (acción larga)'
            },
            {
                'wrong': 'I was knowing the answer.',
                'correct': 'I knew the answer.',
                'explanation': '❌ "Know" es stative verb - no usa continuous'
            }
        ],
        
        'tips': [
            {
                'icon': '⚡',
                'title': 'WHEN = Interrupción',
                'content': 'WHEN + Past Simple para la acción corta que INTERRUMPE.'
            },
            {
                'icon': '🔄',
                'title': 'WHILE = En progreso',
                'content': 'WHILE + Past Continuous para la acción LARGA de fondo.'
            },
            {
                'icon': '📸',
                'title': 'Piensa en una foto',
                'content': 'Past Continuous = lo que estaba pasando en el "momento" de la foto.'
            },
            {
                'icon': '⏱️',
                'title': 'Tiempo específico',
                'content': '"At 8 PM I was studying" vs "Yesterday I studied" - el momento vs el día completo.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con Past Simple o Past Continuous.',
                'questions': [
                    {'prompt': 'I ___ (watch) TV when the lights ___ (go) out.', 'answer': 'was watching...went', 'hint': 'Continuous + interrupción Simple'},
                    {'prompt': 'While she ___ (cook), the phone ___ (ring).', 'answer': 'was cooking...rang', 'hint': 'While + Continuous, interrupción Simple'},
                    {'prompt': 'They ___ (play) football at 5 PM yesterday.', 'answer': 'were playing', 'hint': 'Momento específico = Continuous'},
                    {'prompt': 'I ___ (meet) John yesterday.', 'answer': 'met', 'hint': 'Acción completa = Simple'},
                    {'prompt': 'What ___ you ___ (do) when I called?', 'answer': 'were...doing', 'hint': 'En ese momento = Continuous'},
                    {'prompt': 'She ___ (not/listen) when the teacher ___ (explain).', 'answer': "wasn't listening...was explaining", 'hint': 'Dos acciones simultáneas'},
                    {'prompt': 'I ___ (see) a car accident while I ___ (drive) home.', 'answer': 'saw...was driving', 'hint': 'Saw = corta, driving = larga'},
                    {'prompt': 'He ___ (break) his leg while he ___ (ski).', 'answer': 'broke...was skiing', 'hint': 'Break = momento, ski = actividad'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I ___ dinner when you called.',
                        'options': ['cooked', 'was cooking', 'am cooking', 'cook'],
                        'answer': 'was cooking',
                        'explanation': 'Acción en progreso interrumpida = Past Continuous'
                    },
                    {
                        'prompt': 'While she ___, the baby started crying.',
                        'options': ['slept', 'was sleeping', 'sleeps', 'is sleeping'],
                        'answer': 'was sleeping',
                        'explanation': 'WHILE + Past Continuous'
                    },
                    {
                        'prompt': 'I ___ to work yesterday.',
                        'options': ['was walking', 'walked', 'walk', 'walking'],
                        'answer': 'walked',
                        'explanation': '"Yesterday" = acción completa = Past Simple'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Past Simple
| Forma | Ejemplo |
|-------|---------|
| ✅ Afirmativo | I **worked** / She **went** |
| ❌ Negativo | I **didn't work** |
| ❓ Pregunta | **Did** you **work**? |

**Usa para:** Acciones COMPLETAS, secuencias, tiempo específico

### Past Continuous
| Forma | Ejemplo |
|-------|---------|
| ✅ Afirmativo | I **was working** / They **were playing** |
| ❌ Negativo | I **wasn't working** |
| ❓ Pregunta | **Were** you **working**? |

**Usa para:** Acciones EN PROGRESO, fondo, simultáneas

### WHEN vs WHILE
| Palabra | + Tiempo | Ejemplo |
|---------|----------|---------|
| WHEN | Past Simple | When the phone **rang**... |
| WHILE | Past Continuous | While I **was sleeping**... |

### Patrón Clave
**Past Continuous + WHEN + Past Simple**
= Acción larga INTERRUMPIDA por acción corta

"I **was studying** WHEN the lights **went** out."
'''
    },
    
    'present-perfect': {
        'title': 'Present Perfect',
        'icon': '✨',
        'difficulty': 'intermediate',
        'estimated_time': '30 min',
        'description': 'Conecta el pasado con el presente usando have/has + participio.',
        
        'theory': {
            'introduction': '''
El **Present Perfect** conecta el PASADO con el PRESENTE.
La acción ocurrió en algún momento del pasado, pero tiene relevancia AHORA.

Estructura: **HAVE/HAS + Past Participle (3ra columna)**
''',
            'rules': [
                {
                    'title': '✅ Formación',
                    'rule': 'HAVE/HAS + Participio Pasado',
                    'formula': 'S + have/has + past participle',
                    'examples': [
                        {'sentence': 'I **have finished** my homework.', 'translation': 'He terminado mi tarea.'},
                        {'sentence': 'She **has lived** here for 5 years.', 'translation': 'Ella ha vivido aquí por 5 años.'},
                        {'sentence': 'They **have been** to Paris.', 'translation': 'Ellos han estado en París.'},
                        {'sentence': 'He **hasn\'t called** me yet.', 'translation': 'Él no me ha llamado todavía.'},
                        {'sentence': '**Have** you **seen** this movie?', 'translation': '¿Has visto esta película?'},
                    ],
                    'note': 'I/You/We/They → HAVE. He/She/It → HAS'
                },
                {
                    'title': '🎯 Usos Principales',
                    'rule': 'Experiencias, cambios recientes, acciones con resultado presente',
                    'formula': 'Pasado indefinido con relevancia presente',
                    'examples': [
                        {'sentence': 'I **have visited** Japan twice.', 'use': 'EXPERIENCIA (alguna vez)'},
                        {'sentence': 'She **has just arrived**.', 'use': 'ACCIÓN RECIENTE (just)'},
                        {'sentence': 'I **have lost** my keys.', 'use': 'RESULTADO PRESENTE (no las tengo ahora)'},
                        {'sentence': 'He **has worked** here since 2010.', 'use': 'DURACIÓN hasta ahora (since/for)'},
                        {'sentence': 'I **have already eaten**.', 'use': 'YA completado (already)'},
                        {'sentence': 'She **hasn\'t finished** yet.', 'use': 'TODAVÍA no (yet)'},
                    ]
                },
                {
                    'title': '📅 Palabras Clave',
                    'rule': 'Palabras que indican Present Perfect',
                    'formula': 'Indicadores temporales',
                    'examples': [
                        {'word': 'EVER', 'example': 'Have you **ever** been to London?', 'meaning': 'Alguna vez (preguntas)'},
                        {'word': 'NEVER', 'example': 'I have **never** seen snow.', 'meaning': 'Nunca (negativo)'},
                        {'word': 'ALREADY', 'example': 'I have **already** finished.', 'meaning': 'Ya (afirmativo)'},
                        {'word': 'YET', 'example': "She hasn't arrived **yet**.", 'meaning': 'Todavía (negativo/pregunta)'},
                        {'word': 'JUST', 'example': 'He has **just** left.', 'meaning': 'Recién, acabar de'},
                        {'word': 'FOR', 'example': 'I have lived here **for** 3 years.', 'meaning': 'Durante (período)'},
                        {'word': 'SINCE', 'example': 'She has worked here **since** 2015.', 'meaning': 'Desde (punto inicio)'},
                    ]
                },
                {
                    'title': '⚖️ Present Perfect vs Past Simple',
                    'rule': 'El tiempo específico determina cuál usar',
                    'formula': 'Tiempo definido = Simple. Indefinido = Perfect.',
                    'examples': [
                        {
                            'perfect': 'I **have been** to Paris.',
                            'simple': 'I **went** to Paris last year.',
                            'explanation': 'Sin tiempo = Perfect. Con "last year" = Simple'
                        },
                        {
                            'perfect': 'She **has lost** her phone.',
                            'simple': 'She **lost** her phone yesterday.',
                            'explanation': 'Resultado presente = Perfect. "Yesterday" = Simple'
                        },
                        {
                            'perfect': 'I **have eaten** already.',
                            'simple': 'I **ate** at 7 PM.',
                            'explanation': '"Already" = Perfect. Hora específica = Simple'
                        },
                    ]
                }
            ],
            'structures': [
                {
                    'name': 'FOR vs SINCE',
                    'structure': 'Diferencia clave',
                    'example': '''
**FOR** = Período de tiempo (duración)
- for 3 hours, for 2 weeks, for a long time

**SINCE** = Punto de inicio
- since Monday, since 2010, since I was a child
                    ''',
                    'note': 'FOR = cuánto tiempo. SINCE = desde cuándo.'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I have seen him yesterday.',
                'correct': 'I saw him yesterday.',
                'explanation': '❌ "Yesterday" = tiempo específico = Past Simple'
            },
            {
                'wrong': 'She has went to the store.',
                'correct': 'She has gone to the store.',
                'explanation': '❌ Usa PARTICIPIO (gone), no pasado simple (went)'
            },
            {
                'wrong': 'I have lived here since 3 years.',
                'correct': 'I have lived here for 3 years.',
                'explanation': '❌ "3 years" es período = FOR. SINCE + punto (2020)'
            },
            {
                'wrong': 'Did you ever visit London?',
                'correct': 'Have you ever visited London?',
                'explanation': '❌ "Ever" (alguna vez) = Present Perfect'
            },
            {
                'wrong': 'I have already ate lunch.',
                'correct': 'I have already eaten lunch.',
                'explanation': '❌ Participio de eat = eaten, no ate'
            }
        ],
        
        'tips': [
            {
                'icon': '🎯',
                'title': 'Sin tiempo = Perfect',
                'content': 'Si NO mencionas CUÁNDO pasó → Present Perfect. Con fecha/hora específica → Past Simple.'
            },
            {
                'icon': '📅',
                'title': 'FOR = Duración, SINCE = Inicio',
                'content': 'FOR + período (for 2 years). SINCE + punto (since 2020, since Monday).'
            },
            {
                'icon': '✨',
                'title': 'Participios irregulares',
                'content': 'Memoriza: go→gone, see→seen, eat→eaten, do→done, write→written, take→taken.'
            },
            {
                'icon': '🔍',
                'title': 'Pregunta clave',
                'content': '¿El resultado importa AHORA? → Perfect. ¿Solo describe el pasado? → Simple.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con Present Perfect o Past Simple.',
                'questions': [
                    {'prompt': 'I ___ (never/eat) sushi.', 'answer': 'have never eaten', 'hint': 'Never = Present Perfect'},
                    {'prompt': 'She ___ (go) to the cinema yesterday.', 'answer': 'went', 'hint': 'Yesterday = Past Simple'},
                    {'prompt': '___ you ___ (finish) your homework yet?', 'answer': 'Have...finished', 'hint': 'Yet = Present Perfect'},
                    {'prompt': 'I ___ (live) here for 10 years.', 'answer': 'have lived', 'hint': 'For + período = Perfect'},
                    {'prompt': 'He ___ (just/arrive).', 'answer': 'has just arrived', 'hint': 'Just = Present Perfect'},
                    {'prompt': 'We ___ (meet) in 2015.', 'answer': 'met', 'hint': '2015 = tiempo específico = Simple'},
                    {'prompt': 'They ___ (already/see) that movie.', 'answer': 'have already seen', 'hint': 'Already = Present Perfect'},
                    {'prompt': 'I ___ (lose) my wallet. I can\'t find it.', 'answer': 'have lost', 'hint': 'Resultado presente = Perfect'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I ___ to London three times.',
                        'options': ['have been', 'was', 'went', 'am'],
                        'answer': 'have been',
                        'explanation': 'Experiencia sin tiempo específico = Present Perfect'
                    },
                    {
                        'prompt': 'She ___ here since 2018.',
                        'options': ['works', 'worked', 'has worked', 'is working'],
                        'answer': 'has worked',
                        'explanation': 'SINCE + punto de inicio = Present Perfect'
                    },
                    {
                        'prompt': 'I ___ him last Monday.',
                        'options': ['have seen', 'saw', 'see', 'have saw'],
                        'answer': 'saw',
                        'explanation': '"Last Monday" = tiempo específico = Past Simple'
                    },
                    {
                        'prompt': '___ you ever ___ Korean food?',
                        'options': ['Did...try', 'Have...tried', 'Do...try', 'Are...trying'],
                        'answer': 'Have...tried',
                        'explanation': 'EVER = alguna vez = Present Perfect'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura
| Forma | Estructura | Ejemplo |
|-------|-----------|---------|
| ✅ Afirmativo | S + have/has + pp | I **have finished** |
| ❌ Negativo | S + haven't/hasn't + pp | She **hasn't called** |
| ❓ Pregunta | Have/Has + S + pp? | **Have** you **seen** it? |

### Palabras Clave
| Palabra | Uso | Ejemplo |
|---------|-----|---------|
| ever | Preguntas | Have you **ever** ...? |
| never | Negativo | I have **never** ... |
| already | Afirmativo | I have **already** ... |
| yet | Neg/Pregunta | ...hasn't ... **yet** |
| just | Reciente | She has **just** left |
| for | Período | for 3 years |
| since | Punto inicio | since 2020 |

### FOR vs SINCE
| FOR | SINCE |
|-----|-------|
| for 2 hours | since 9 AM |
| for a week | since Monday |
| for years | since 2015 |

### Perfect vs Simple
| Present Perfect | Past Simple |
|-----------------|-------------|
| Sin tiempo específico | Con tiempo específico |
| I have visited Paris | I visited Paris in 2020 |
| Relevancia presente | Solo pasado |
'''
    },
    
    'modal-verbs': {
        'title': 'Modal Verbs',
        'icon': '🎭',
        'difficulty': 'intermediate',
        'estimated_time': '30 min',
        'description': 'Domina can, could, must, should, may, might y sus usos.',
        
        'theory': {
            'introduction': '''
Los **verbos modales** expresan posibilidad, habilidad, permiso, obligación, etc.
Son especiales porque:
- NO agregan -S con he/she/it
- Van seguidos de verbo BASE (sin TO)
- NO usan DO/DOES para preguntas y negativos
''',
            'rules': [
                {
                    'title': '💪 CAN / COULD (Habilidad)',
                    'rule': 'Expresan capacidad o habilidad',
                    'formula': 'S + can/could + verb (base)',
                    'examples': [
                        {'sentence': 'I **can swim**.', 'meaning': 'Sé nadar / Puedo nadar (habilidad presente)'},
                        {'sentence': 'She **can\'t drive**.', 'meaning': 'No sabe manejar'},
                        {'sentence': '**Can** you **speak** French?', 'meaning': '¿Sabes hablar francés?'},
                        {'sentence': 'I **could read** at age 4.', 'meaning': 'Podía leer a los 4 años (habilidad pasada)'},
                        {'sentence': '**Could** you **help** me?', 'meaning': '¿Podrías ayudarme? (más cortés que can)'},
                    ]
                },
                {
                    'title': '✅ MUST / HAVE TO (Obligación)',
                    'rule': 'Expresan necesidad u obligación',
                    'formula': 'S + must + verb / S + have to + verb',
                    'examples': [
                        {'sentence': 'You **must wear** a helmet.', 'meaning': 'Debes usar casco (obligación fuerte)'},
                        {'sentence': 'I **have to work** tomorrow.', 'meaning': 'Tengo que trabajar mañana'},
                        {'sentence': 'She **must be** tired.', 'meaning': 'Debe estar cansada (deducción)'},
                        {'sentence': 'You **mustn\'t smoke** here.', 'meaning': 'No debes fumar aquí (prohibición)'},
                        {'sentence': 'You **don\'t have to** come.', 'meaning': 'No tienes que venir (no es necesario)'},
                    ],
                    'note': '⚠️ MUSTN\'T = prohibición. DON\'T HAVE TO = no es necesario (diferente!)'
                },
                {
                    'title': '💡 SHOULD / OUGHT TO (Consejo)',
                    'rule': 'Expresan recomendación o consejo',
                    'formula': 'S + should + verb',
                    'examples': [
                        {'sentence': 'You **should study** more.', 'meaning': 'Deberías estudiar más (consejo)'},
                        {'sentence': 'She **shouldn\'t eat** so much sugar.', 'meaning': 'No debería comer tanta azúcar'},
                        {'sentence': '**Should** I call him?', 'meaning': '¿Debería llamarlo?'},
                        {'sentence': 'You **ought to** apologize.', 'meaning': 'Deberías disculparte (más formal)'},
                    ]
                },
                {
                    'title': '🎲 MAY / MIGHT (Posibilidad)',
                    'rule': 'Expresan posibilidad o permiso',
                    'formula': 'S + may/might + verb',
                    'examples': [
                        {'sentence': 'It **may rain** tomorrow.', 'meaning': 'Puede que llueva mañana (50%)'},
                        {'sentence': 'She **might be** at home.', 'meaning': 'Puede que esté en casa (menos seguro)'},
                        {'sentence': '**May** I use your phone?', 'meaning': '¿Puedo usar tu teléfono? (permiso formal)'},
                        {'sentence': 'He **might not** come.', 'meaning': 'Puede que no venga'},
                    ],
                    'note': 'MAY = más probable (~50%). MIGHT = menos probable (~30%)'
                },
                {
                    'title': '📊 Grados de Certeza',
                    'rule': 'De más a menos seguro',
                    'formula': 'Escala de probabilidad',
                    'examples': [
                        {'modal': 'MUST', 'certainty': '95%', 'example': 'He must be sick. (Casi seguro)'},
                        {'modal': 'SHOULD', 'certainty': '75%', 'example': 'She should arrive soon. (Probablemente)'},
                        {'modal': 'MAY', 'certainty': '50%', 'example': 'It may work. (Quizás)'},
                        {'modal': 'MIGHT', 'certainty': '30%', 'example': 'He might call. (Posiblemente)'},
                        {'modal': 'CAN\'T', 'certainty': '5%', 'example': 'It can\'t be true. (Imposible)'},
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She can to swim.',
                'correct': 'She can swim.',
                'explanation': '❌ Después de modales va verbo BASE, sin TO'
            },
            {
                'wrong': 'He must to go.',
                'correct': 'He must go.',
                'explanation': '❌ MUST + verbo base, sin TO'
            },
            {
                'wrong': 'She cans speak English.',
                'correct': 'She can speak English.',
                'explanation': '❌ Los modales NO agregan -S con he/she/it'
            },
            {
                'wrong': 'You don\'t must smoke here.',
                'correct': 'You mustn\'t smoke here.',
                'explanation': '❌ Negativo de MUST = MUSTN\'T, no "don\'t must"'
            },
            {
                'wrong': 'I must to study yesterday.',
                'correct': 'I had to study yesterday.',
                'explanation': '❌ MUST no tiene pasado. Usa HAD TO para pasado'
            }
        ],
        
        'tips': [
            {
                'icon': '🚫',
                'title': 'Sin TO después de modal',
                'content': 'Can swim, must go, should eat - NUNCA "can to swim".'
            },
            {
                'icon': '👤',
                'title': 'Sin -S',
                'content': 'He CAN (no "cans"), She MUST (no "musts"). Igual para todas las personas.'
            },
            {
                'icon': '⚠️',
                'title': 'Mustn\'t ≠ Don\'t have to',
                'content': 'MUSTN\'T = prohibido. DON\'T HAVE TO = no necesario (puedes si quieres).'
            },
            {
                'icon': '📊',
                'title': 'Escala de certeza',
                'content': 'Must (95%) > Should (75%) > May (50%) > Might (30%) > Can\'t (5%)'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con el modal correcto.',
                'questions': [
                    {'prompt': 'She ___ speak three languages. (ability)', 'answer': 'can', 'hint': 'Habilidad = can'},
                    {'prompt': 'You ___ wear a seatbelt. It\'s the law. (obligation)', 'answer': 'must', 'hint': 'Obligación fuerte = must'},
                    {'prompt': 'You ___ see a doctor. (advice)', 'answer': 'should', 'hint': 'Consejo = should'},
                    {'prompt': 'It ___ rain later. (possibility ~50%)', 'answer': 'may', 'hint': 'Posibilidad 50% = may'},
                    {'prompt': 'You ___ smoke here. It\'s forbidden.', 'answer': "mustn't", 'hint': 'Prohibición = mustn\'t'},
                    {'prompt': 'You ___ come if you don\'t want to. (not necessary)', 'answer': "don't have to", 'hint': 'No necesario = don\'t have to'},
                    {'prompt': '___ you help me, please? (polite request)', 'answer': 'Could', 'hint': 'Petición cortés = Could'},
                    {'prompt': 'She ___ be at home. Her car is there. (95% sure)', 'answer': 'must', 'hint': 'Deducción segura = must'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'You ___ smoke in a hospital.',
                        'options': ["don't have to", "mustn't", "shouldn't", "can't to"],
                        'answer': "mustn't",
                        'explanation': 'Prohibición total = mustn\'t'
                    },
                    {
                        'prompt': 'She ___ play piano when she was 5.',
                        'options': ['can', 'could', 'may', 'must'],
                        'answer': 'could',
                        'explanation': 'Habilidad en el pasado = could'
                    },
                    {
                        'prompt': 'It\'s a holiday. You ___ work tomorrow.',
                        'options': ["mustn't", "don't have to", "can't", "shouldn't"],
                        'answer': "don't have to",
                        'explanation': 'No es necesario (pero puedes si quieres) = don\'t have to'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Reglas Básicas
- ❌ NO -S: He **can** (not "cans")
- ❌ NO TO: She **must go** (not "must to go")
- ❌ NO DO/DOES: **Can** you...? (not "Do you can...?")

### Tabla de Modales
| Modal | Uso | Ejemplo |
|-------|-----|---------|
| **can** | Habilidad presente | I can swim |
| **could** | Habilidad pasada / cortesía | I could read at 5 / Could you help? |
| **must** | Obligación / deducción | You must go / She must be tired |
| **mustn't** | Prohibición | You mustn't smoke |
| **have to** | Obligación | I have to work |
| **don't have to** | No necesario | You don't have to come |
| **should** | Consejo | You should rest |
| **may** | Posibilidad 50% / permiso formal | It may rain / May I...? |
| **might** | Posibilidad 30% | He might call |

### ⚠️ Diferencia Importante
| Mustn't | Don't have to |
|---------|---------------|
| Prohibido | No necesario |
| You mustn't lie | You don't have to pay |
| = NO PUEDES | = No es obligatorio |
'''
    },
    
    'relative-clauses': {
        'title': 'Relative Clauses',
        'icon': '🔗',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Usa who, which, that, where, when y whose para conectar ideas.',
        
        'theory': {
            'introduction': '''
Las **cláusulas relativas** dan información adicional sobre un sustantivo.
Usan pronombres relativos: **WHO, WHICH, THAT, WHERE, WHEN, WHOSE**

Tipos:
- **Defining**: Esencial para entender (sin comas)
- **Non-defining**: Información extra (con comas)
''',
            'rules': [
                {
                    'title': '👤 WHO (Personas)',
                    'rule': 'Usado para referirse a personas',
                    'formula': 'noun (person) + WHO + verb...',
                    'examples': [
                        {'sentence': 'The woman **who lives** next door is a doctor.', 'note': 'WHO = la mujer'},
                        {'sentence': 'I know someone **who can** help you.', 'note': 'WHO = alguien'},
                        {'sentence': 'The teacher **who taught** me was excellent.', 'note': 'WHO = el profesor'},
                    ]
                },
                {
                    'title': '📦 WHICH (Cosas/Animales)',
                    'rule': 'Usado para cosas y animales',
                    'formula': 'noun (thing) + WHICH + verb...',
                    'examples': [
                        {'sentence': 'The book **which I bought** is interesting.', 'note': 'WHICH = el libro'},
                        {'sentence': 'I like the car **which is** parked outside.', 'note': 'WHICH = el auto'},
                        {'sentence': 'The dog **which barks** all night is annoying.', 'note': 'WHICH = el perro'},
                    ]
                },
                {
                    'title': '🎯 THAT (Personas o Cosas)',
                    'rule': 'Puede reemplazar WHO o WHICH en defining clauses',
                    'formula': 'noun + THAT + verb...',
                    'examples': [
                        {'sentence': 'The man **that called** you is here.', 'note': 'THAT = who (persona)'},
                        {'sentence': 'The movie **that we watched** was great.', 'note': 'THAT = which (cosa)'},
                        {'sentence': 'Everything **that happened** was unexpected.', 'note': 'Después de everything/anything = THAT'},
                    ],
                    'note': '⚠️ THAT no se puede usar en non-defining clauses (con comas)'
                },
                {
                    'title': '📍 WHERE (Lugares)',
                    'rule': 'Usado para lugares',
                    'formula': 'place + WHERE + subject + verb...',
                    'examples': [
                        {'sentence': 'This is the restaurant **where we met**.', 'note': 'WHERE = el restaurante'},
                        {'sentence': 'I visited the city **where I was born**.', 'note': 'WHERE = la ciudad'},
                        {'sentence': 'The hotel **where we stayed** was beautiful.', 'note': 'WHERE = el hotel'},
                    ]
                },
                {
                    'title': '⏰ WHEN (Tiempo)',
                    'rule': 'Usado para tiempo',
                    'formula': 'time + WHEN + subject + verb...',
                    'examples': [
                        {'sentence': 'I remember the day **when we first met**.', 'note': 'WHEN = el día'},
                        {'sentence': 'Summer is the time **when I travel**.', 'note': 'WHEN = el tiempo'},
                    ]
                },
                {
                    'title': '👑 WHOSE (Posesión)',
                    'rule': 'Indica posesión (de quién)',
                    'formula': 'noun + WHOSE + noun + verb...',
                    'examples': [
                        {'sentence': 'The boy **whose father** is a doctor won.', 'note': 'WHOSE = del chico'},
                        {'sentence': 'I know the woman **whose car** was stolen.', 'note': 'WHOSE = de la mujer'},
                    ],
                    'note': 'WHOSE = cuyo/cuya'
                },
                {
                    'title': '📝 Defining vs Non-Defining',
                    'rule': 'Con o sin comas',
                    'formula': 'Esencial (sin comas) vs Extra (con comas)',
                    'examples': [
                        {
                            'defining': 'The man **who stole** my wallet was arrested.',
                            'note_def': 'Sin comas - esencial para identificar CUÁL hombre'
                        },
                        {
                            'non_defining': 'My brother, **who lives in London**, is visiting.',
                            'note_non': 'Con comas - información extra, ya sabemos quién es'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'The book who I bought.',
                'correct': 'The book which/that I bought.',
                'explanation': '❌ WHO es para personas. Para cosas usa WHICH o THAT.'
            },
            {
                'wrong': 'The man which called you.',
                'correct': 'The man who/that called you.',
                'explanation': '❌ WHICH es para cosas. Para personas usa WHO o THAT.'
            },
            {
                'wrong': 'My mother, that is a teacher, lives in Madrid.',
                'correct': 'My mother, who is a teacher, lives in Madrid.',
                'explanation': '❌ THAT no se usa en non-defining clauses (con comas)'
            },
            {
                'wrong': 'The city where I visited was beautiful.',
                'correct': 'The city which I visited was beautiful.',
                'explanation': '❌ WHERE = in which. "I visited the city" (sin preposición)'
            },
            {
                'wrong': 'The boy who his father is a doctor.',
                'correct': "The boy whose father is a doctor.",
                'explanation': '❌ Para posesión usa WHOSE, no "who his"'
            }
        ],
        
        'tips': [
            {
                'icon': '👤',
                'title': 'WHO = personas',
                'content': 'The girl WHO called... The doctor WHO helped...'
            },
            {
                'icon': '📦',
                'title': 'WHICH = cosas',
                'content': 'The book WHICH I read... The car WHICH is red...'
            },
            {
                'icon': '🎯',
                'title': 'THAT = comodín',
                'content': 'THAT puede reemplazar WHO o WHICH en defining clauses (sin comas).'
            },
            {
                'icon': '📍',
                'title': 'WHERE = in which',
                'content': 'The place WHERE I work = The place in which I work.'
            },
            {
                'icon': '✏️',
                'title': 'Comas = extra',
                'content': 'Sin comas = esencial. Con comas = información adicional.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con who, which, that, where, when o whose.',
                'questions': [
                    {'prompt': 'The woman ___ lives next door is friendly.', 'answer': 'who', 'hint': 'Persona = who'},
                    {'prompt': 'The book ___ I bought is interesting.', 'answer': 'which', 'hint': 'Cosa = which (o that)'},
                    {'prompt': 'This is the restaurant ___ we had dinner.', 'answer': 'where', 'hint': 'Lugar = where'},
                    {'prompt': 'The boy ___ father is a doctor won the prize.', 'answer': 'whose', 'hint': 'Posesión = whose'},
                    {'prompt': 'I remember the day ___ we first met.', 'answer': 'when', 'hint': 'Tiempo = when'},
                    {'prompt': 'The car ___ is parked outside is mine.', 'answer': 'which', 'hint': 'Cosa = which (o that)'},
                    {'prompt': 'The people ___ work here are friendly.', 'answer': 'who', 'hint': 'Personas = who'},
                    {'prompt': 'She showed me the house ___ she grew up.', 'answer': 'where', 'hint': 'Lugar = where'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'The man ___ called you is waiting.',
                        'options': ['which', 'who', 'where', 'whose'],
                        'answer': 'who',
                        'explanation': 'Persona = who'
                    },
                    {
                        'prompt': 'This is the town ___ I was born.',
                        'options': ['who', 'which', 'where', 'when'],
                        'answer': 'where',
                        'explanation': 'Lugar = where'
                    },
                    {
                        'prompt': 'The girl ___ bag was stolen called the police.',
                        'options': ['who', 'which', 'whose', 'that'],
                        'answer': 'whose',
                        'explanation': 'Posesión (her bag) = whose'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Pronombres Relativos
| Pronombre | Para | Ejemplo |
|-----------|------|---------|
| **who** | Personas | The man **who** called... |
| **which** | Cosas/animales | The book **which** I read... |
| **that** | Ambos (defining) | The person/thing **that**... |
| **where** | Lugares | The city **where** I live... |
| **when** | Tiempo | The day **when** we met... |
| **whose** | Posesión | The boy **whose** father... |

### Defining vs Non-Defining
| Tipo | Comas | Uso |
|------|-------|-----|
| Defining | Sin comas | Esencial para identificar |
| Non-defining | Con comas | Información extra |

**Defining**: The woman **who called** is my sister.
**Non-defining**: My mother, **who is 60**, lives in Paris.

### ⚠️ Recuerda
- THAT no se usa con comas (non-defining)
- WHERE = in which (para lugares)
- WHOSE = posesión (cuyo/cuya)
'''
    },
    
    'question-tags': {
        'title': 'Question Tags',
        'icon': '❓',
        'difficulty': 'intermediate',
        'estimated_time': '20 min',
        'description': 'Aprende a formar preguntas de confirmación: isn\'t it?, don\'t you?, etc.',
        
        'theory': {
            'introduction': '''
Los **Question Tags** son mini-preguntas al final de una oración para confirmar información.
Equivalen a: "¿verdad?", "¿no?", "¿cierto?"

Regla básica:
- Oración positiva → Tag negativo
- Oración negativa → Tag positivo
''',
            'rules': [
                {
                    'title': '➕➖ Regla Principal',
                    'rule': 'Positivo → negativo / Negativo → positivo',
                    'formula': 'Statement (+) → tag (-) / Statement (-) → tag (+)',
                    'examples': [
                        {'sentence': 'You are a student, **aren\'t you**?', 'note': 'Positivo → negativo'},
                        {'sentence': 'She isn\'t here, **is she**?', 'note': 'Negativo → positivo'},
                        {'sentence': 'They can swim, **can\'t they**?', 'note': 'Modal positivo → negativo'},
                        {'sentence': 'He doesn\'t like coffee, **does he**?', 'note': 'Negativo → positivo'},
                    ]
                },
                {
                    'title': '🔧 Con Verbo BE',
                    'rule': 'Usa el mismo verbo BE en el tag',
                    'formula': 'am/is/are/was/were → aren\'t/isn\'t/aren\'t/wasn\'t/weren\'t',
                    'examples': [
                        {'sentence': 'It is cold, **isn\'t it**?', 'verb': 'is → isn\'t'},
                        {'sentence': 'They were late, **weren\'t they**?', 'verb': 'were → weren\'t'},
                        {'sentence': 'You are happy, **aren\'t you**?', 'verb': 'are → aren\'t'},
                        {'sentence': 'I am right, **aren\'t I**?', 'verb': 'am → aren\'t (excepción!)'},
                    ],
                    'note': '⚠️ Con "I am" el tag es "aren\'t I" (no "amn\'t I")'
                },
                {
                    'title': '🔨 Con Auxiliares y Modales',
                    'rule': 'Usa el mismo auxiliar/modal en el tag',
                    'formula': 'have/has/will/can/should... → haven\'t/hasn\'t/won\'t/can\'t/shouldn\'t...',
                    'examples': [
                        {'sentence': 'You have finished, **haven\'t you**?', 'aux': 'have → haven\'t'},
                        {'sentence': 'She will come, **won\'t she**?', 'aux': 'will → won\'t'},
                        {'sentence': 'They can help, **can\'t they**?', 'aux': 'can → can\'t'},
                        {'sentence': 'He should study, **shouldn\'t he**?', 'aux': 'should → shouldn\'t'},
                    ]
                },
                {
                    'title': '📝 Con DO/DOES/DID',
                    'rule': 'Si no hay auxiliar, usa DO/DOES/DID',
                    'formula': 'Present → do/does. Past → did',
                    'examples': [
                        {'sentence': 'You like pizza, **don\'t you**?', 'note': 'Present (you) → don\'t'},
                        {'sentence': 'She works here, **doesn\'t she**?', 'note': 'Present (she) → doesn\'t'},
                        {'sentence': 'They went home, **didn\'t they**?', 'note': 'Past → didn\'t'},
                        {'sentence': 'He called you, **didn\'t he**?', 'note': 'Past → didn\'t'},
                    ]
                },
                {
                    'title': '⚠️ Casos Especiales',
                    'rule': 'Excepciones importantes',
                    'formula': 'Memorizar',
                    'examples': [
                        {'sentence': 'I am late, **aren\'t I**?', 'note': 'I am → aren\'t I (no "amn\'t")'},
                        {'sentence': 'Let\'s go, **shall we**?', 'note': 'Let\'s → shall we'},
                        {'sentence': 'Don\'t touch that, **will you**?', 'note': 'Imperativo negativo → will you'},
                        {'sentence': 'Open the door, **will you**?', 'note': 'Imperativo → will you'},
                        {'sentence': 'There is a problem, **isn\'t there**?', 'note': 'There is → isn\'t there'},
                        {'sentence': 'Nobody came, **did they**?', 'note': 'Nobody/nothing (neg) → positivo'},
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She likes pizza, doesn\'t she?',
                'correct': 'She likes pizza, doesn\'t she?',
                'explanation': '✅ Correcto! Likes (positivo) → doesn\'t she (negativo)'
            },
            {
                'wrong': 'You are coming, are you?',
                'correct': 'You are coming, aren\'t you?',
                'explanation': '❌ Positivo necesita tag NEGATIVO'
            },
            {
                'wrong': 'I am right, amn\'t I?',
                'correct': "I am right, aren't I?",
                'explanation': '❌ "Amn\'t" no existe. Usa "aren\'t I"'
            },
            {
                'wrong': 'Let\'s eat, don\'t we?',
                'correct': "Let's eat, shall we?",
                'explanation': '❌ Let\'s siempre usa "shall we"'
            },
            {
                'wrong': 'Nobody knows, don\'t they?',
                'correct': 'Nobody knows, do they?',
                'explanation': '❌ Nobody es negativo, entonces tag positivo'
            }
        ],
        
        'tips': [
            {
                'icon': '↔️',
                'title': 'Regla de oro',
                'content': 'Positivo → Negativo. Negativo → Positivo. Siempre opuestos.'
            },
            {
                'icon': '🔍',
                'title': 'Busca el auxiliar',
                'content': 'Usa el MISMO auxiliar de la oración. Sin auxiliar → usa DO/DOES/DID.'
            },
            {
                'icon': '⚠️',
                'title': 'I am → aren\'t I',
                'content': '"I am right, aren\'t I?" No existe "amn\'t".'
            },
            {
                'icon': '👥',
                'title': 'Nobody/Nothing = negativo',
                'content': 'Nobody, nothing, never son negativos. El tag debe ser positivo.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con el question tag correcto.',
                'questions': [
                    {'prompt': 'You are tired, ___?', 'answer': "aren't you", 'hint': 'are (positivo) → aren\'t (negativo)'},
                    {'prompt': 'She doesn\'t like fish, ___?', 'answer': 'does she', 'hint': 'doesn\'t (negativo) → does (positivo)'},
                    {'prompt': 'They can swim, ___?', 'answer': "can't they", 'hint': 'can (positivo) → can\'t (negativo)'},
                    {'prompt': 'He went home, ___?', 'answer': "didn't he", 'hint': 'went (past, positivo) → didn\'t (negativo)'},
                    {'prompt': 'I am right, ___?', 'answer': "aren't I", 'hint': 'I am → aren\'t I (especial)'},
                    {'prompt': 'Let\'s go, ___?', 'answer': 'shall we', 'hint': 'Let\'s → shall we (especial)'},
                    {'prompt': 'She will come, ___?', 'answer': "won't she", 'hint': 'will → won\'t'},
                    {'prompt': 'Nobody called, ___?', 'answer': 'did they', 'hint': 'Nobody (negativo) → positivo'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'You like coffee, ___?',
                        'options': ["don't you", "do you", "aren't you", "like you"],
                        'answer': "don't you",
                        'explanation': 'Like (positivo, sin auxiliar) → don\'t you'
                    },
                    {
                        'prompt': 'She hasn\'t arrived, ___?',
                        'options': ["hasn't she", "has she", "is she", "does she"],
                        'answer': 'has she',
                        'explanation': 'Hasn\'t (negativo) → has (positivo)'
                    },
                    {
                        'prompt': 'There are many people, ___?',
                        'options': ["aren't there", "are there", "isn't it", "don't they"],
                        'answer': "aren't there",
                        'explanation': 'There are → aren\'t there'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Regla Principal
| Oración | Tag |
|---------|-----|
| ➕ Positiva | ➖ Negativo |
| ➖ Negativa | ➕ Positivo |

### Ejemplos por Tipo
| Oración | Tag |
|---------|-----|
| You **are** happy | **aren't** you? |
| She **isn't** here | **is** she? |
| They **can** swim | **can't** they? |
| He **doesn't** work | **does** he? |
| You **like** pizza | **don't** you? |
| She **works** here | **doesn't** she? |
| They **went** home | **didn't** they? |

### Casos Especiales
| Oración | Tag |
|---------|-----|
| I am right | **aren't I**? |
| Let's go | **shall we**? |
| Open the door | **will you**? |
| Nobody came | **did they**? |
| There is... | **isn't there**? |

### ⚠️ Recuerda
- Mismo tiempo verbal
- Mismo auxiliar/modal
- Sin auxiliar → DO/DOES/DID
- I am → aren't I
'''
    },
    
    'third-conditional': {
        'title': 'Third Conditional',
        'icon': '🔮',
        'difficulty': 'advanced',
        'estimated_time': '25 min',
        'description': 'Habla sobre situaciones hipotéticas en el pasado que NO ocurrieron.',
        
        'theory': {
            'introduction': '''
El **Third Conditional** habla de situaciones IRREALES en el PASADO.
Son cosas que NO pasaron y ya no pueden cambiar.

Estructura: **If + Past Perfect, would have + past participle**

Equivale a: "Si hubiera... habría..."
''',
            'rules': [
                {
                    'title': '📐 Estructura',
                    'rule': 'If + Past Perfect, would have + participio',
                    'formula': 'If + had + PP, would have + PP',
                    'examples': [
                        {
                            'sentence': 'If I **had studied**, I **would have passed**.',
                            'translation': 'Si hubiera estudiado, habría aprobado.',
                            'reality': 'Realidad: No estudié, no aprobé'
                        },
                        {
                            'sentence': 'If she **had left** earlier, she **wouldn\'t have missed** the train.',
                            'translation': 'Si hubiera salido antes, no habría perdido el tren.',
                            'reality': 'Realidad: Salió tarde, perdió el tren'
                        },
                        {
                            'sentence': 'If they **had known**, they **would have helped**.',
                            'translation': 'Si hubieran sabido, habrían ayudado.',
                            'reality': 'Realidad: No sabían, no ayudaron'
                        },
                    ]
                },
                {
                    'title': '❓ Preguntas',
                    'rule': 'What would you have done if...?',
                    'formula': 'What/Where/Why + would + S + have + PP + if + had + PP?',
                    'examples': [
                        {'sentence': '**Would** you **have gone** if I had invited you?', 'translation': '¿Habrías ido si te hubiera invitado?'},
                        {'sentence': 'What **would** you **have done** if you had won?', 'translation': '¿Qué habrías hecho si hubieras ganado?'},
                        {'sentence': 'Where **would** she **have lived** if she had moved?', 'translation': '¿Dónde habría vivido si se hubiera mudado?'},
                    ]
                },
                {
                    'title': '🔄 Variaciones con Could/Might',
                    'rule': 'Puedes usar could have o might have en lugar de would have',
                    'formula': 'If + had + PP, could/might have + PP',
                    'examples': [
                        {
                            'sentence': 'If I had known, I **could have helped**.',
                            'meaning': 'Habría tenido la posibilidad de ayudar'
                        },
                        {
                            'sentence': 'If she had applied, she **might have gotten** the job.',
                            'meaning': 'Quizás habría conseguido el trabajo (menos seguro)'
                        },
                    ],
                    'note': 'Would have = resultado seguro. Could have = posibilidad. Might have = menos probable.'
                },
                {
                    'title': '⚖️ Comparación de Condicionales',
                    'rule': 'First, Second, Third Conditional',
                    'formula': 'Cada uno para diferente situación',
                    'examples': [
                        {
                            'type': 'First',
                            'example': 'If I study, I **will pass**.',
                            'time': 'Futuro - posible'
                        },
                        {
                            'type': 'Second',
                            'example': 'If I studied, I **would pass**.',
                            'time': 'Presente/Futuro - hipotético'
                        },
                        {
                            'type': 'Third',
                            'example': 'If I had studied, I **would have passed**.',
                            'time': 'Pasado - imposible cambiar'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'If I would have studied, I would have passed.',
                'correct': 'If I had studied, I would have passed.',
                'explanation': '❌ NUNCA uses "would" en la cláusula IF. Usa "had".'
            },
            {
                'wrong': 'If she had known, she would helped.',
                'correct': 'If she had known, she would have helped.',
                'explanation': '❌ Falta "HAVE" después de would.'
            },
            {
                'wrong': 'If I had studied, I passed.',
                'correct': 'If I had studied, I would have passed.',
                'explanation': '❌ El resultado necesita "would have + participio".'
            },
            {
                'wrong': 'If I have studied harder, I would have passed.',
                'correct': 'If I had studied harder, I would have passed.',
                'explanation': '❌ La cláusula IF necesita Past Perfect (HAD + participio).'
            }
        ],
        
        'tips': [
            {
                'icon': '🚫',
                'title': 'No "would" en IF',
                'content': 'NUNCA digas "If I would have...". Siempre "If I HAD..."'
            },
            {
                'icon': '⏰',
                'title': 'Pasado irreal',
                'content': 'Third conditional = situaciones que YA NO pueden cambiar.'
            },
            {
                'icon': '🔢',
                'title': 'Doble "had" y "have"',
                'content': 'If I HAD studied, I would HAVE passed. Dos perfectos.'
            },
            {
                'icon': '😔',
                'title': 'Arrepentimientos',
                'content': 'Úsalo para expresar arrepentimientos: "If only I had known..."'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con Third Conditional.',
                'questions': [
                    {'prompt': 'If I ___ (know), I ___ (tell) you.', 'answer': 'had known...would have told', 'hint': 'Past Perfect + would have + PP'},
                    {'prompt': 'If she ___ (study), she ___ (pass) the exam.', 'answer': 'had studied...would have passed', 'hint': 'Past Perfect + would have + PP'},
                    {'prompt': 'If they ___ (not/leave) late, they ___ (not/miss) the flight.', 'answer': "hadn't left...wouldn't have missed", 'hint': 'Negativo en ambas partes'},
                    {'prompt': 'What ___ you ___ (do) if you ___ (win) the lottery?', 'answer': 'would...have done...had won', 'hint': 'Pregunta: Would + S + have + PP'},
                    {'prompt': 'If I ___ (be) you, I ___ (accept) the offer.', 'answer': 'had been...would have accepted', 'hint': 'Past Perfect + would have + PP'},
                    {'prompt': 'She ___ (not/get) hurt if she ___ (wear) her seatbelt.', 'answer': "wouldn't have got...had worn", 'hint': 'Resultado negativo + condición positiva'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'If I ___ the news, I would have called you.',
                        'options': ['knew', 'had known', 'would know', 'have known'],
                        'answer': 'had known',
                        'explanation': 'If + Past Perfect (had known)'
                    },
                    {
                        'prompt': 'If she had asked, I ___ her.',
                        'options': ['helped', 'would help', 'would have helped', 'had helped'],
                        'answer': 'would have helped',
                        'explanation': 'Resultado = would have + participio'
                    },
                    {
                        'prompt': 'What would you have done if you ___ in my situation?',
                        'options': ['were', 'are', 'had been', 'would be'],
                        'answer': 'had been',
                        'explanation': 'If clause = Past Perfect'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura
| Parte | Forma | Ejemplo |
|-------|-------|---------|
| IF clause | If + Past Perfect | If I **had studied**... |
| Result | would have + PP | ...I **would have passed**. |

### Fórmula
```
If + had + participio, would have + participio
```

### ⚠️ Regla de Oro
| ❌ Incorrecto | ✅ Correcto |
|---------------|-------------|
| If I **would have** known | If I **had** known |
| ...I would passed | ...I would **have** passed |

### Comparación
| Condicional | Estructura | Tiempo |
|-------------|------------|--------|
| First | If + present, will + verb | Futuro real |
| Second | If + past, would + verb | Presente irreal |
| Third | If + had PP, would have PP | Pasado irreal |

### Uso
Para hablar de:
- Situaciones pasadas que NO ocurrieron
- Arrepentimientos
- Resultados diferentes en el pasado
'''
    },
    
    'reported-speech': {
        'title': 'Reported Speech',
        'icon': '💬',
        'difficulty': 'advanced',
        'estimated_time': '30 min',
        'description': 'Reporta lo que alguien dijo: "He said that..."',
        
        'theory': {
            'introduction': '''
El **Reported Speech** (discurso indirecto) se usa para contar lo que alguien dijo.
En lugar de citar directamente, "cambiamos" las palabras.

Regla principal: El tiempo verbal "retrocede" un paso al pasado.
''',
            'rules': [
                {
                    'title': '🔄 Cambios de Tiempo Verbal',
                    'rule': 'Cada tiempo retrocede un paso',
                    'formula': 'Direct → Reported (un tiempo atrás)',
                    'examples': [
                        {
                            'direct': '"I **am** tired."',
                            'reported': 'He said he **was** tired.',
                            'change': 'Present Simple → Past Simple'
                        },
                        {
                            'direct': '"I **am working**."',
                            'reported': 'She said she **was working**.',
                            'change': 'Present Continuous → Past Continuous'
                        },
                        {
                            'direct': '"I **have finished**."',
                            'reported': 'He said he **had finished**.',
                            'change': 'Present Perfect → Past Perfect'
                        },
                        {
                            'direct': '"I **will call** you."',
                            'reported': 'She said she **would call** me.',
                            'change': 'Will → Would'
                        },
                        {
                            'direct': '"I **can swim**."',
                            'reported': 'He said he **could swim**.',
                            'change': 'Can → Could'
                        },
                    ]
                },
                {
                    'title': '📅 Cambios de Tiempo y Lugar',
                    'rule': 'Las referencias de tiempo y lugar también cambian',
                    'formula': 'Ajustar perspectiva',
                    'examples': [
                        {'direct': 'today', 'reported': 'that day'},
                        {'direct': 'tomorrow', 'reported': 'the next day / the following day'},
                        {'direct': 'yesterday', 'reported': 'the day before / the previous day'},
                        {'direct': 'now', 'reported': 'then'},
                        {'direct': 'here', 'reported': 'there'},
                        {'direct': 'this', 'reported': 'that'},
                        {'direct': 'these', 'reported': 'those'},
                        {'direct': 'ago', 'reported': 'before'},
                    ]
                },
                {
                    'title': '👤 Cambios de Pronombres',
                    'rule': 'Ajustar pronombres según contexto',
                    'formula': 'Cambiar perspectiva',
                    'examples': [
                        {
                            'direct': '"**I** love **my** job."',
                            'reported': 'She said **she** loved **her** job.',
                            'change': 'I → she, my → her'
                        },
                        {
                            'direct': '"**You** are late."',
                            'reported': 'He told **me** I was late.',
                            'change': 'You → I/me (depende del contexto)'
                        },
                    ]
                },
                {
                    'title': '❓ Preguntas en Reported Speech',
                    'rule': 'Usa asked + orden de afirmación',
                    'formula': 'asked + if/what/where... + S + V (sin inversión)',
                    'examples': [
                        {
                            'direct': '"**Are** you coming?"',
                            'reported': 'She **asked if** I was coming.',
                            'note': 'Yes/No question → asked if'
                        },
                        {
                            'direct': '"**Where** do you live?"',
                            'reported': 'He **asked where** I lived.',
                            'note': 'WH-question → asked + WH + S + V'
                        },
                        {
                            'direct': '"**What** are you doing?"',
                            'reported': 'She **asked what** I was doing.',
                            'note': 'Sin inversión en reported'
                        },
                    ],
                    'note': '⚠️ En reported questions NO hay inversión (no "where was I")'
                },
                {
                    'title': '📢 Órdenes y Peticiones',
                    'rule': 'Usa told/asked + person + to + verb',
                    'formula': 'told/asked + object + (not) to + infinitive',
                    'examples': [
                        {
                            'direct': '"Close the door."',
                            'reported': 'He **told me to close** the door.',
                            'type': 'Orden'
                        },
                        {
                            'direct': '"Please help me."',
                            'reported': 'She **asked me to help** her.',
                            'type': 'Petición'
                        },
                        {
                            'direct': '"Don\'t be late."',
                            'reported': 'He **told me not to be** late.',
                            'type': 'Negativo = not to'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'She said that she is tired.',
                'correct': 'She said that she was tired.',
                'explanation': '❌ Present Simple → Past Simple en reported speech'
            },
            {
                'wrong': 'He asked where do I live.',
                'correct': 'He asked where I lived.',
                'explanation': '❌ Sin inversión en reported questions'
            },
            {
                'wrong': 'She said me that...',
                'correct': 'She told me that... / She said that...',
                'explanation': '❌ SAY no lleva objeto directo. Use TELL + person'
            },
            {
                'wrong': 'He told that he was happy.',
                'correct': 'He said that he was happy. / He told me that he was happy.',
                'explanation': '❌ TELL siempre necesita objeto (told ME/HIM/HER)'
            },
            {
                'wrong': 'He asked me to don\'t be late.',
                'correct': "He asked me not to be late.",
                'explanation': '❌ Negativo = NOT TO + infinitive, no "to don\'t"'
            }
        ],
        
        'tips': [
            {
                'icon': '⏰',
                'title': 'Un paso atrás',
                'content': 'Cada tiempo retrocede: am→was, will→would, can→could.'
            },
            {
                'icon': '💬',
                'title': 'SAY vs TELL',
                'content': 'SAY (no persona): He said that... TELL (+ persona): He told ME that...'
            },
            {
                'icon': '❓',
                'title': 'Questions sin inversión',
                'content': '"Where do you live?" → He asked where I lived (NO "where did I live")'
            },
            {
                'icon': '📍',
                'title': 'Cambia perspectiva',
                'content': 'today→that day, here→there, tomorrow→the next day'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Convierte a Reported Speech.',
                'questions': [
                    {'prompt': '"I am happy." → She said she ___ happy.', 'answer': 'was', 'hint': 'am → was'},
                    {'prompt': '"I will help you." → He said he ___ help me.', 'answer': 'would', 'hint': 'will → would'},
                    {'prompt': '"Where do you live?" → She asked where I ___.', 'answer': 'lived', 'hint': 'do live → lived, sin inversión'},
                    {'prompt': '"Close the window." → He told me ___ the window.', 'answer': 'to close', 'hint': 'Orden = told + to + infinitive'},
                    {'prompt': '"I have finished." → She said she ___ finished.', 'answer': 'had', 'hint': 'have → had'},
                    {'prompt': '"Don\'t touch that." → He told me ___ touch that.', 'answer': 'not to', 'hint': 'Negativo = not to + infinitive'},
                    {'prompt': '"Are you coming?" → She asked ___ I was coming.', 'answer': 'if', 'hint': 'Yes/No question → asked if'},
                    {'prompt': '"I can swim." → He said he ___ swim.', 'answer': 'could', 'hint': 'can → could'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'She said that she ___ tired.',
                        'options': ['is', 'was', 'be', 'been'],
                        'answer': 'was',
                        'explanation': 'Present → Past en reported speech'
                    },
                    {
                        'prompt': 'He asked me where I ___.',
                        'options': ['do work', 'worked', 'working', 'did work'],
                        'answer': 'worked',
                        'explanation': 'Questions: sin inversión, tiempo pasado'
                    },
                    {
                        'prompt': 'She told me ___ late.',
                        'options': ["to don't be", 'not to be', 'not be', 'to not be'],
                        'answer': 'not to be',
                        'explanation': 'Negativo = not to + infinitive'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Cambios de Tiempo
| Directo | Reportado |
|---------|-----------|
| am/is/are | was/were |
| have/has | had |
| will | would |
| can | could |
| may | might |
| must | had to |

### Cambios de Tiempo/Lugar
| Directo | Reportado |
|---------|-----------|
| today | that day |
| tomorrow | the next day |
| yesterday | the day before |
| now | then |
| here | there |
| this/these | that/those |

### SAY vs TELL
| SAY | TELL |
|-----|------|
| He **said** that... | He **told me** that... |
| No persona después | Siempre + persona |

### Questions
| Tipo | Estructura |
|------|-----------|
| Yes/No | asked **if** + S + V |
| WH- | asked **what/where** + S + V |

⚠️ **Sin inversión**: He asked where I lived (NO "where did I live")

### Órdenes
| Directo | Reportado |
|---------|-----------|
| "Close it." | told me **to close** it |
| "Don't touch." | told me **not to** touch |
'''
    },
    
    'gerunds-infinitives': {
        'title': 'Gerunds vs Infinitives',
        'icon': '⚔️',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Cuándo usar -ING y cuándo usar TO + verbo.',
        
        'theory': {
            'introduction': '''
Algunos verbos van seguidos de **GERUND** (verb + -ING): enjoy swimming
Otros van seguidos de **INFINITIVE** (to + verb): want to swim
Algunos cambian de significado según cuál uses.

¡No hay una regla mágica! Hay que memorizar los más comunes.
''',
            'rules': [
                {
                    'title': '🔵 Verbos + GERUND (-ING)',
                    'rule': 'Estos verbos siempre van seguidos de -ING',
                    'formula': 'verb + verb-ING',
                    'examples': [
                        {'verb': 'enjoy', 'example': 'I **enjoy swimming**.', 'translation': 'Disfruto nadar'},
                        {'verb': 'finish', 'example': 'She **finished eating**.', 'translation': 'Terminó de comer'},
                        {'verb': 'avoid', 'example': 'He **avoids working** late.', 'translation': 'Evita trabajar tarde'},
                        {'verb': 'mind', 'example': 'Do you **mind waiting**?', 'translation': '¿Te importa esperar?'},
                        {'verb': 'suggest', 'example': 'I **suggest going** home.', 'translation': 'Sugiero ir a casa'},
                        {'verb': 'consider', 'example': 'She **considered moving**.', 'translation': 'Consideró mudarse'},
                        {'verb': 'practice', 'example': 'I **practice speaking** English.', 'translation': 'Practico hablar inglés'},
                        {'verb': 'keep', 'example': '**Keep studying**!', 'translation': '¡Sigue estudiando!'},
                        {'verb': 'give up', 'example': 'He **gave up smoking**.', 'translation': 'Dejó de fumar'},
                    ],
                    'note': '📝 Memoriza: enjoy, finish, avoid, mind, suggest, consider, practice, keep, give up'
                },
                {
                    'title': '🟢 Verbos + INFINITIVE (TO + verb)',
                    'rule': 'Estos verbos siempre van seguidos de TO + infinitivo',
                    'formula': 'verb + to + verb',
                    'examples': [
                        {'verb': 'want', 'example': 'I **want to go**.', 'translation': 'Quiero ir'},
                        {'verb': 'need', 'example': 'She **needs to study**.', 'translation': 'Necesita estudiar'},
                        {'verb': 'decide', 'example': 'He **decided to leave**.', 'translation': 'Decidió irse'},
                        {'verb': 'hope', 'example': 'I **hope to see** you.', 'translation': 'Espero verte'},
                        {'verb': 'plan', 'example': 'We **plan to travel**.', 'translation': 'Planeamos viajar'},
                        {'verb': 'promise', 'example': 'She **promised to help**.', 'translation': 'Prometió ayudar'},
                        {'verb': 'refuse', 'example': 'He **refused to pay**.', 'translation': 'Se negó a pagar'},
                        {'verb': 'learn', 'example': 'I\'m **learning to drive**.', 'translation': 'Estoy aprendiendo a manejar'},
                        {'verb': 'afford', 'example': 'I can\'t **afford to buy** it.', 'translation': 'No puedo permitirme comprarlo'},
                    ],
                    'note': '📝 Memoriza: want, need, decide, hope, plan, promise, refuse, learn, afford, agree, offer'
                },
                {
                    'title': '🟡 Verbos que aceptan AMBOS (mismo significado)',
                    'rule': 'Algunos verbos pueden usar gerund o infinitive sin cambiar el significado',
                    'formula': 'verb + -ING = verb + to + verb',
                    'examples': [
                        {'verb': 'start', 'gerund': 'It started **raining**.', 'infinitive': 'It started **to rain**.', 'meaning': 'Mismo significado'},
                        {'verb': 'begin', 'gerund': 'She began **crying**.', 'infinitive': 'She began **to cry**.', 'meaning': 'Mismo significado'},
                        {'verb': 'continue', 'gerund': 'He continued **working**.', 'infinitive': 'He continued **to work**.', 'meaning': 'Mismo significado'},
                        {'verb': 'like/love/hate', 'gerund': 'I like **swimming**.', 'infinitive': 'I like **to swim**.', 'meaning': 'Similar'},
                    ]
                },
                {
                    'title': '🔴 Verbos que CAMBIAN de significado',
                    'rule': '¡CUIDADO! Estos verbos significan algo diferente con -ING o TO',
                    'formula': 'Significado diferente según la forma',
                    'examples': [
                        {
                            'verb': 'STOP',
                            'gerund': 'I stopped **smoking**.',
                            'gerund_meaning': 'Dejé de fumar (ya no fumo)',
                            'infinitive': 'I stopped **to smoke**.',
                            'infinitive_meaning': 'Paré para fumar (tomé un descanso para fumar)'
                        },
                        {
                            'verb': 'REMEMBER',
                            'gerund': 'I remember **locking** the door.',
                            'gerund_meaning': 'Recuerdo que cerré (pasado)',
                            'infinitive': 'Remember **to lock** the door.',
                            'infinitive_meaning': 'Recuerda cerrar (futuro)'
                        },
                        {
                            'verb': 'FORGET',
                            'gerund': 'I\'ll never forget **meeting** her.',
                            'gerund_meaning': 'Nunca olvidaré cuando la conocí (pasado)',
                            'infinitive': 'Don\'t forget **to call** me.',
                            'infinitive_meaning': 'No olvides llamarme (futuro)'
                        },
                        {
                            'verb': 'TRY',
                            'gerund': 'Try **eating** less sugar.',
                            'gerund_meaning': 'Intenta comer menos (experimento)',
                            'infinitive': 'I tried **to open** the door.',
                            'infinitive_meaning': 'Intenté abrir (esfuerzo)'
                        },
                    ]
                },
                {
                    'title': '📍 Después de Preposiciones = GERUND',
                    'rule': 'Después de cualquier preposición, usa siempre GERUND',
                    'formula': 'preposition + verb-ING',
                    'examples': [
                        {'sentence': 'I\'m interested **in learning** English.', 'prep': 'in'},
                        {'sentence': 'She\'s good **at cooking**.', 'prep': 'at'},
                        {'sentence': 'I\'m tired **of waiting**.', 'prep': 'of'},
                        {'sentence': 'Thanks **for helping** me.', 'prep': 'for'},
                        {'sentence': 'He left **without saying** goodbye.', 'prep': 'without'},
                        {'sentence': '**Before leaving**, close the door.', 'prep': 'before'},
                        {'sentence': '**After finishing**, call me.', 'prep': 'after'},
                    ],
                    'note': '⚠️ SIEMPRE gerund después de preposición (in, at, of, for, without, before, after...)'
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I enjoy to swim.',
                'correct': 'I enjoy swimming.',
                'explanation': '❌ ENJOY siempre va con -ING'
            },
            {
                'wrong': 'I want going home.',
                'correct': 'I want to go home.',
                'explanation': '❌ WANT siempre va con TO + infinitive'
            },
            {
                'wrong': 'I\'m interested in to learn English.',
                'correct': 'I\'m interested in learning English.',
                'explanation': '❌ Después de preposición (in) siempre -ING'
            },
            {
                'wrong': 'I stopped to smoke. (queriendo decir "dejé de fumar")',
                'correct': 'I stopped smoking.',
                'explanation': '❌ Stop + -ING = dejar de hacer. Stop + to = parar para hacer'
            },
            {
                'wrong': 'I suggest to go home.',
                'correct': 'I suggest going home.',
                'explanation': '❌ SUGGEST siempre va con -ING'
            }
        ],
        
        'tips': [
            {
                'icon': '🔵',
                'title': 'Grupo -ING',
                'content': 'Enjoy, finish, avoid, mind, suggest, consider, practice, keep, give up'
            },
            {
                'icon': '🟢',
                'title': 'Grupo TO',
                'content': 'Want, need, decide, hope, plan, promise, refuse, learn, afford, agree'
            },
            {
                'icon': '📍',
                'title': 'Preposición = -ING',
                'content': 'Siempre -ING después de: in, at, of, for, about, without, before, after...'
            },
            {
                'icon': '⚠️',
                'title': 'Stop/Remember/Forget',
                'content': 'Cambian significado! Stop -ING = dejar de. Stop TO = parar para.'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con gerund (-ING) o infinitive (to + verb).',
                'questions': [
                    {'prompt': 'I enjoy ___ (swim).', 'answer': 'swimming', 'hint': 'Enjoy + -ING'},
                    {'prompt': 'She wants ___ (go) home.', 'answer': 'to go', 'hint': 'Want + to'},
                    {'prompt': 'He finished ___ (eat).', 'answer': 'eating', 'hint': 'Finish + -ING'},
                    {'prompt': 'They decided ___ (leave).', 'answer': 'to leave', 'hint': 'Decide + to'},
                    {'prompt': 'I\'m interested in ___ (learn) Spanish.', 'answer': 'learning', 'hint': 'Preposición (in) + -ING'},
                    {'prompt': 'She stopped ___ (smoke). She doesn\'t smoke now.', 'answer': 'smoking', 'hint': 'Dejó de = stop + -ING'},
                    {'prompt': 'Remember ___ (call) me tomorrow.', 'answer': 'to call', 'hint': 'Futuro = remember + to'},
                    {'prompt': 'I can\'t afford ___ (buy) a new car.', 'answer': 'to buy', 'hint': 'Afford + to'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I avoid ___ junk food.',
                        'options': ['to eat', 'eating', 'eat', 'ate'],
                        'answer': 'eating',
                        'explanation': 'AVOID + -ING'
                    },
                    {
                        'prompt': 'She promised ___ me.',
                        'options': ['helping', 'help', 'to help', 'helped'],
                        'answer': 'to help',
                        'explanation': 'PROMISE + TO + infinitive'
                    },
                    {
                        'prompt': 'I\'m tired of ___ for the bus.',
                        'options': ['wait', 'to wait', 'waiting', 'waited'],
                        'answer': 'waiting',
                        'explanation': 'Preposición (of) + -ING'
                    },
                    {
                        'prompt': 'He stopped ___ a cigarette. (paró para fumar)',
                        'options': ['smoking', 'to smoke', 'smoke', 'smoked'],
                        'answer': 'to smoke',
                        'explanation': 'Stop TO = parar para hacer algo'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### 🔵 Verbos + GERUND (-ING)
| Verbo | Ejemplo |
|-------|---------|
| enjoy | I enjoy **swimming** |
| finish | She finished **eating** |
| avoid | He avoids **working** late |
| mind | Do you mind **waiting**? |
| suggest | I suggest **going** home |
| consider | She considered **moving** |
| practice | Practice **speaking** |
| keep | Keep **studying**! |
| give up | He gave up **smoking** |

### 🟢 Verbos + INFINITIVE (TO)
| Verbo | Ejemplo |
|-------|---------|
| want | I want **to go** |
| need | She needs **to study** |
| decide | He decided **to leave** |
| hope | I hope **to see** you |
| plan | We plan **to travel** |
| promise | She promised **to help** |
| refuse | He refused **to pay** |
| learn | I'm learning **to drive** |
| afford | I can't afford **to buy** |

### 🔴 Cambio de Significado
| Verbo | -ING | TO |
|-------|------|-----|
| stop | Dejé de fumar | Paré para fumar |
| remember | Recuerdo que hice | Recuerda hacer |
| forget | Olvidé que hice | Olvidé hacer |
| try | Experimenta | Esfuérzate |

### 📍 Preposición + GERUND
Siempre -ING después de: in, at, of, for, without, before, after

*interested **in learning*** | *good **at cooking*** | *tired **of waiting***
'''
    },
    
    'future-forms': {
        'title': 'Future Forms',
        'icon': '🚀',
        'difficulty': 'intermediate',
        'estimated_time': '25 min',
        'description': 'Will, Going to, Present Continuous y Present Simple para el futuro.',
        
        'theory': {
            'introduction': '''
En inglés hay varias formas de hablar del futuro. Cada una tiene un uso específico:

1. **WILL** - Decisiones espontáneas, predicciones, promesas
2. **GOING TO** - Planes/intenciones, predicciones con evidencia
3. **Present Continuous** - Citas, arreglos fijos
4. **Present Simple** - Horarios, itinerarios fijos
''',
            'rules': [
                {
                    'title': '⚡ WILL',
                    'rule': 'Para decisiones espontáneas, promesas y predicciones sin evidencia',
                    'formula': 'S + will + verb (base)',
                    'examples': [
                        {
                            'sentence': 'I\'ll help you with that.',
                            'use': 'Decisión espontánea (ahora mismo)',
                            'context': 'Alguien te pide ayuda y decides ayudar en ese momento'
                        },
                        {
                            'sentence': 'I promise I **will call** you.',
                            'use': 'Promesa',
                            'context': 'Prometiendo algo'
                        },
                        {
                            'sentence': 'I think it **will rain** tomorrow.',
                            'use': 'Predicción (opinión)',
                            'context': 'Creo que... (sin evidencia directa)'
                        },
                        {
                            'sentence': 'She **will be** 30 next year.',
                            'use': 'Hecho futuro',
                            'context': 'Algo que sabemos que pasará'
                        },
                    ],
                    'keywords': 'I think, probably, maybe, I promise, I\'ll'
                },
                {
                    'title': '🎯 GOING TO',
                    'rule': 'Para planes/intenciones y predicciones con evidencia',
                    'formula': 'S + am/is/are + going to + verb',
                    'examples': [
                        {
                            'sentence': 'I\'m **going to study** medicine.',
                            'use': 'Plan/intención',
                            'context': 'Ya lo decidí antes'
                        },
                        {
                            'sentence': 'Look at those clouds! It\'s **going to rain**.',
                            'use': 'Predicción con evidencia',
                            'context': 'Veo las nubes = evidencia'
                        },
                        {
                            'sentence': 'She\'s **going to have** a baby.',
                            'use': 'Algo evidente',
                            'context': 'Está embarazada = evidencia visible'
                        },
                        {
                            'sentence': 'We\'re **going to move** next month.',
                            'use': 'Plan decidido',
                            'context': 'Ya decidimos mudarnos'
                        },
                    ],
                    'keywords': 'I\'ve decided, I\'m planning, Look! (evidencia)'
                },
                {
                    'title': '📅 Present Continuous (para futuro)',
                    'rule': 'Para citas y arreglos fijos/confirmados',
                    'formula': 'S + am/is/are + verb-ING',
                    'examples': [
                        {
                            'sentence': 'I\'m **meeting** John at 6 PM.',
                            'use': 'Cita confirmada',
                            'context': 'Ya coordiné con John'
                        },
                        {
                            'sentence': 'We\'re **flying** to Paris next week.',
                            'use': 'Viaje reservado',
                            'context': 'Ya tenemos los boletos'
                        },
                        {
                            'sentence': 'She\'s **having** dinner with her boss tonight.',
                            'use': 'Arreglo fijo',
                            'context': 'Ya está confirmado'
                        },
                    ],
                    'note': '⚠️ Requiere evidencia de que es algo FIJO (cita, reservación, acuerdo)'
                },
                {
                    'title': '🕐 Present Simple (para futuro)',
                    'rule': 'Para horarios y eventos programados oficialmente',
                    'formula': 'S + verb (s/es)',
                    'examples': [
                        {
                            'sentence': 'The train **leaves** at 8 AM.',
                            'use': 'Horario oficial',
                            'context': 'Horario del tren'
                        },
                        {
                            'sentence': 'The movie **starts** at 9 PM.',
                            'use': 'Programa fijo',
                            'context': 'Horario del cine'
                        },
                        {
                            'sentence': 'School **begins** on September 1st.',
                            'use': 'Fecha oficial',
                            'context': 'Calendario escolar'
                        },
                    ],
                    'note': '⚠️ Solo para horarios/itinerarios OFICIALES (transporte, cine, eventos)'
                },
                {
                    'title': '⚖️ Comparación',
                    'rule': 'Cuándo usar cada forma',
                    'formula': 'Depende del contexto',
                    'examples': [
                        {
                            'situation': 'A: I\'m cold. B: I\'ll close the window.',
                            'form': 'WILL',
                            'reason': 'Decisión espontánea (ahora)'
                        },
                        {
                            'situation': 'I\'m going to learn French this year.',
                            'form': 'GOING TO',
                            'reason': 'Plan/intención (ya decidido)'
                        },
                        {
                            'situation': 'I\'m having lunch with Sarah tomorrow.',
                            'form': 'PRESENT CONTINUOUS',
                            'reason': 'Cita confirmada'
                        },
                        {
                            'situation': 'The plane lands at 3 PM.',
                            'form': 'PRESENT SIMPLE',
                            'reason': 'Horario oficial'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I will meet John at 6. (si es una cita)',
                'correct': 'I\'m meeting John at 6.',
                'explanation': '❌ Para citas confirmadas, usa Present Continuous'
            },
            {
                'wrong': 'Look! It will rain!',
                'correct': "Look! It's going to rain!",
                'explanation': '❌ Con evidencia presente, usa GOING TO'
            },
            {
                'wrong': 'The train will leave at 8 AM. (horario)',
                'correct': 'The train leaves at 8 AM.',
                'explanation': '❌ Para horarios oficiales, usa Present Simple'
            },
            {
                'wrong': 'I\'m going to help you. (decisión espontánea)',
                'correct': "I'll help you.",
                'explanation': '❌ Para decisiones del momento, usa WILL'
            }
        ],
        
        'tips': [
            {
                'icon': '⚡',
                'title': 'WILL = espontáneo',
                'content': 'Decisión en el momento: "I\'ll answer the phone." "I\'ll help you."'
            },
            {
                'icon': '🎯',
                'title': 'GOING TO = planeado',
                'content': 'Ya lo decidiste antes: "I\'m going to study abroad next year."'
            },
            {
                'icon': '📅',
                'title': 'Present Continuous = arreglo',
                'content': 'Cita confirmada con alguien: "I\'m meeting the doctor at 4."'
            },
            {
                'icon': '🕐',
                'title': 'Present Simple = horario',
                'content': 'Solo para horarios oficiales: "The bus leaves at 7."'
            },
            {
                'icon': '👁️',
                'title': 'Con evidencia = GOING TO',
                'content': '"Look at those clouds! It\'s going to rain." (veo la evidencia)'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con will, going to, present continuous o present simple.',
                'questions': [
                    {'prompt': 'A: It\'s cold. B: I ___ (close) the window.', 'answer': "'ll close", 'hint': 'Decisión espontánea = will'},
                    {'prompt': 'Look at those clouds! It ___ (rain).', 'answer': 'is going to rain', 'hint': 'Evidencia = going to'},
                    {'prompt': 'I ___ (meet) Sarah at 6. We made plans.', 'answer': 'am meeting', 'hint': 'Cita confirmada = Present Continuous'},
                    {'prompt': 'The movie ___ (start) at 8 PM.', 'answer': 'starts', 'hint': 'Horario = Present Simple'},
                    {'prompt': 'I\'ve decided. I ___ (learn) to play guitar.', 'answer': 'am going to learn', 'hint': 'Plan decidido = going to'},
                    {'prompt': 'I promise I ___ (call) you tomorrow.', 'answer': 'will call', 'hint': 'Promesa = will'},
                    {'prompt': 'We ___ (fly) to London next Monday. I have the tickets.', 'answer': 'are flying', 'hint': 'Boletos = arreglo confirmado = Present Continuous'},
                    {'prompt': 'I think she ___ (be) late.', 'answer': 'will be', 'hint': 'I think (opinión) = will'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la mejor opción.',
                'questions': [
                    {
                        'prompt': 'The phone is ringing! I ___ answer it.',
                        'options': ['am going to', "'ll", 'am', 'going to'],
                        'answer': "'ll",
                        'explanation': 'Decisión espontánea = will (\'ll)'
                    },
                    {
                        'prompt': 'She ___ a baby. Look, she\'s pregnant!',
                        'options': ['will have', 'is going to have', 'has', 'is having'],
                        'answer': 'is going to have',
                        'explanation': 'Evidencia visible = going to'
                    },
                    {
                        'prompt': 'My flight ___ at 6 AM tomorrow.',
                        'options': ['leaves', 'is leaving', 'will leave', 'is going to leave'],
                        'answer': 'leaves',
                        'explanation': 'Horario de vuelo = Present Simple'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Las 4 Formas de Futuro

| Forma | Uso | Ejemplo |
|-------|-----|---------|
| **WILL** | Espontáneo, promesas | I'll help you |
| **GOING TO** | Planes, evidencia | I'm going to study |
| **Present Cont.** | Citas confirmadas | I'm meeting John |
| **Present Simple** | Horarios oficiales | The train leaves at 8 |

### ⚡ WILL
- Decisión del momento: "I'll open the door"
- Promesas: "I will call you"
- Predicciones (opinión): "I think it will rain"

### 🎯 GOING TO
- Planes decididos: "I'm going to travel"
- Evidencia: "Look! It's going to rain"

### 📅 Present Continuous
- Citas/arreglos fijos: "I'm having dinner with Tom"
- Viajes reservados: "We're flying to Paris"

### 🕐 Present Simple
- Horarios: "The bus leaves at 7"
- Programas: "The movie starts at 9"

### Pregunta Clave
| ¿Qué tipo de futuro? | Forma |
|----------------------|-------|
| Decisión ahora mismo | WILL |
| Plan ya decidido | GOING TO |
| Cita confirmada | Present Continuous |
| Horario oficial | Present Simple |
'''
    },
    
    'wish-if-only': {
        'title': 'Wish / If Only',
        'icon': '🌟',
        'difficulty': 'advanced',
        'estimated_time': '20 min',
        'description': 'Expresa deseos sobre el presente, pasado y situaciones irreales.',
        
        'theory': {
            'introduction': '''
**WISH** e **IF ONLY** expresan deseos sobre situaciones que NO son reales.
Son "lamentos" o deseos de que algo fuera diferente.

- **Presente irreal**: Wish + Past Simple
- **Pasado irreal**: Wish + Past Perfect
- **Situaciones molestas**: Wish + would
''',
            'rules': [
                {
                    'title': '😔 Deseos sobre el PRESENTE',
                    'rule': 'Para desear que algo fuera diferente AHORA',
                    'formula': 'I wish / If only + Past Simple',
                    'examples': [
                        {
                            'wish': 'I **wish I had** more money.',
                            'reality': 'No tengo suficiente dinero.',
                            'translation': 'Ojalá tuviera más dinero.'
                        },
                        {
                            'wish': 'If only I **were** taller.',
                            'reality': 'No soy alto.',
                            'translation': 'Si tan solo fuera más alto.'
                        },
                        {
                            'wish': 'She **wishes** she **spoke** French.',
                            'reality': 'No habla francés.',
                            'translation': 'Ella desearía hablar francés.'
                        },
                        {
                            'wish': 'I wish I **didn\'t have** to work tomorrow.',
                            'reality': 'Tengo que trabajar.',
                            'translation': 'Ojalá no tuviera que trabajar.'
                        },
                    ],
                    'note': '⚠️ Usa WERE para todas las personas (I were, he were) - más formal'
                },
                {
                    'title': '😢 Deseos sobre el PASADO',
                    'rule': 'Para lamentar algo que ya pasó y no puedes cambiar',
                    'formula': 'I wish / If only + Past Perfect (had + PP)',
                    'examples': [
                        {
                            'wish': 'I wish I **had studied** harder.',
                            'reality': 'No estudié lo suficiente.',
                            'translation': 'Ojalá hubiera estudiado más.'
                        },
                        {
                            'wish': 'If only we **hadn\'t missed** the train.',
                            'reality': 'Perdimos el tren.',
                            'translation': 'Si tan solo no hubiéramos perdido el tren.'
                        },
                        {
                            'wish': 'She wishes she **had accepted** the job.',
                            'reality': 'No aceptó el trabajo.',
                            'translation': 'Ella desearía haber aceptado el trabajo.'
                        },
                    ],
                    'note': 'Expresa ARREPENTIMIENTO - cosas que no podemos cambiar'
                },
                {
                    'title': '😤 Quejas / Situaciones molestas',
                    'rule': 'Para quejarte de hábitos o situaciones que te molestan',
                    'formula': 'I wish + subject + WOULD + verb',
                    'examples': [
                        {
                            'wish': 'I wish you **would stop** making noise.',
                            'meaning': 'Me molesta que hagas ruido.',
                            'translation': 'Ojalá dejaras de hacer ruido.'
                        },
                        {
                            'wish': 'I wish it **would stop** raining.',
                            'meaning': 'Me molesta que siga lloviendo.',
                            'translation': 'Ojalá dejara de llover.'
                        },
                        {
                            'wish': 'If only he **would listen** to me.',
                            'meaning': 'Me frustra que no me escuche.',
                            'translation': 'Si tan solo me escuchara.'
                        },
                    ],
                    'note': '⚠️ No uses "I wish I would" - es incorrecto'
                },
                {
                    'title': '📊 Resumen de estructuras',
                    'rule': 'Las tres formas de WISH',
                    'formula': 'Depende del tiempo',
                    'examples': [
                        {
                            'type': 'PRESENTE',
                            'structure': 'wish + Past Simple',
                            'example': 'I wish I **knew** the answer.'
                        },
                        {
                            'type': 'PASADO',
                            'structure': 'wish + Past Perfect',
                            'example': 'I wish I **had known** the answer.'
                        },
                        {
                            'type': 'QUEJA',
                            'structure': 'wish + would',
                            'example': 'I wish you **would help** me.'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I wish I am rich.',
                'correct': 'I wish I were/was rich.',
                'explanation': '❌ Wish + PAST Simple (were/was), no present'
            },
            {
                'wrong': 'I wish I would have more time.',
                'correct': 'I wish I had more time.',
                'explanation': '❌ "I wish I would" es incorrecto. Usa past simple'
            },
            {
                'wrong': 'I wish I studied harder yesterday.',
                'correct': 'I wish I had studied harder yesterday.',
                'explanation': '❌ Para el pasado, usa Past Perfect (had studied)'
            },
            {
                'wrong': 'If only I can fly.',
                'correct': 'If only I could fly.',
                'explanation': '❌ Usa COULD (pasado), no CAN'
            }
        ],
        
        'tips': [
            {
                'icon': '⏰',
                'title': 'Presente → Past Simple',
                'content': 'Para deseos sobre AHORA: I wish I HAD... I wish I KNEW...'
            },
            {
                'icon': '⏮️',
                'title': 'Pasado → Past Perfect',
                'content': 'Para lamentos sobre el PASADO: I wish I HAD STUDIED...'
            },
            {
                'icon': '😤',
                'title': 'Quejas → Would',
                'content': 'Para situaciones molestas: I wish you WOULD stop...'
            },
            {
                'icon': '✨',
                'title': 'WERE formal',
                'content': '"I wish I WERE" es más formal que "I wish I was".'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la forma correcta de WISH.',
                'questions': [
                    {'prompt': 'I wish I ___ (have) more free time. (presente)', 'answer': 'had', 'hint': 'Presente irreal = Past Simple'},
                    {'prompt': 'If only I ___ (study) harder for the exam. (pasado)', 'answer': 'had studied', 'hint': 'Pasado irreal = Past Perfect'},
                    {'prompt': 'I wish you ___ (stop) talking! (queja)', 'answer': 'would stop', 'hint': 'Queja = would'},
                    {'prompt': 'She wishes she ___ (can) speak Japanese.', 'answer': 'could', 'hint': 'Can → could'},
                    {'prompt': 'I wish I ___ (be) taller.', 'answer': 'were', 'hint': 'Be → were (formal)'},
                    {'prompt': 'If only we ___ (not/miss) the bus yesterday.', 'answer': "hadn't missed", 'hint': 'Pasado = Past Perfect'},
                    {'prompt': 'I wish it ___ (not/rain) so much.', 'answer': "didn't rain", 'hint': 'Presente irreal = Past Simple'},
                    {'prompt': 'She wishes she ___ (accept) that job offer. (pasado)', 'answer': 'had accepted', 'hint': 'Lamento = Past Perfect'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I wish I ___ rich.',
                        'options': ['am', 'was/were', 'will be', 'would be'],
                        'answer': 'was/were',
                        'explanation': 'Presente irreal = Past Simple (was/were)'
                    },
                    {
                        'prompt': 'If only I ___ harder for the exam. I failed.',
                        'options': ['study', 'studied', 'had studied', 'would study'],
                        'answer': 'had studied',
                        'explanation': 'Lamento pasado = Past Perfect'
                    },
                    {
                        'prompt': 'I wish you ___ making so much noise!',
                        'options': ['stop', 'stopped', 'would stop', 'had stopped'],
                        'answer': 'would stop',
                        'explanation': 'Queja sobre situación molesta = would'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Estructura de WISH / IF ONLY

| Tipo | Estructura | Ejemplo |
|------|------------|---------|
| **Presente** | wish + Past Simple | I wish I **had** money |
| **Pasado** | wish + Past Perfect | I wish I **had studied** |
| **Queja** | wish + would | I wish you **would stop** |

### Ejemplos Completos
| Deseo | Realidad |
|-------|----------|
| I wish I **were** rich | No soy rico |
| I wish I **had gone** | No fui |
| I wish he **would call** | No me llama |

### ⚠️ Errores Comunes
| ❌ Incorrecto | ✅ Correcto |
|---------------|-------------|
| I wish I am... | I wish I **were/was**... |
| I wish I would... | I wish I **had**... |
| I wish I studied (pasado) | I wish I **had studied** |

### Traducción
| Inglés | Español |
|--------|---------|
| I wish I had... | Ojalá tuviera... |
| I wish I had done... | Ojalá hubiera hecho... |
| If only... | Si tan solo... |
'''
    },
    
    'quantifiers': {
        'title': 'Quantifiers',
        'icon': '📊',
        'difficulty': 'intermediate',
        'estimated_time': '20 min',
        'description': 'Domina some, any, much, many, few, little, a lot of.',
        
        'theory': {
            'introduction': '''
Los **quantifiers** (cuantificadores) expresan CANTIDAD.
La elección depende de:
1. **Contable** (se puede contar: books, apples) vs **Incontable** (no se cuenta: water, money)
2. **Afirmativo**, **negativo** o **pregunta**
''',
            'rules': [
                {
                    'title': '✅ SOME / ANY',
                    'rule': 'Para cantidades indefinidas',
                    'formula': 'SOME (afirmativo) / ANY (negativo, pregunta)',
                    'examples': [
                        {
                            'sentence': 'I have **some** friends.',
                            'type': 'Afirmativo',
                            'note': 'Tengo algunos amigos'
                        },
                        {
                            'sentence': 'There is **some** water.',
                            'type': 'Afirmativo + incontable',
                            'note': 'Hay algo de agua'
                        },
                        {
                            'sentence': 'I don\'t have **any** money.',
                            'type': 'Negativo',
                            'note': 'No tengo nada de dinero'
                        },
                        {
                            'sentence': 'Do you have **any** questions?',
                            'type': 'Pregunta',
                            'note': '¿Tienes alguna pregunta?'
                        },
                        {
                            'sentence': 'Would you like **some** coffee?',
                            'type': 'Oferta (some en pregunta)',
                            'note': '¿Quieres café? (espero que sí)'
                        },
                    ],
                    'note': '⚠️ SOME en preguntas cuando ofreces algo o esperas "sí"'
                },
                {
                    'title': '📈 MUCH / MANY',
                    'rule': 'Para gran cantidad (negativo/pregunta)',
                    'formula': 'MANY (contable) / MUCH (incontable)',
                    'examples': [
                        {
                            'sentence': 'There aren\'t **many** people here.',
                            'type': 'MANY + contable plural',
                            'note': 'No hay muchas personas'
                        },
                        {
                            'sentence': 'I don\'t have **much** time.',
                            'type': 'MUCH + incontable',
                            'note': 'No tengo mucho tiempo'
                        },
                        {
                            'sentence': 'Do you have **many** books?',
                            'type': 'Pregunta + contable',
                            'note': '¿Tienes muchos libros?'
                        },
                        {
                            'sentence': 'How **much** money do you need?',
                            'type': 'Pregunta + incontable',
                            'note': '¿Cuánto dinero necesitas?'
                        },
                    ],
                    'note': '⚠️ Much/Many en afirmativo suena formal. Mejor usar "a lot of"'
                },
                {
                    'title': '📦 A LOT OF / LOTS OF',
                    'rule': 'Para gran cantidad (afirmativo, todo tipo)',
                    'formula': 'A LOT OF + contable o incontable',
                    'examples': [
                        {
                            'sentence': 'I have **a lot of** friends.',
                            'type': 'Contable',
                            'note': 'Tengo muchos amigos'
                        },
                        {
                            'sentence': 'She has **a lot of** money.',
                            'type': 'Incontable',
                            'note': 'Tiene mucho dinero'
                        },
                        {
                            'sentence': 'There are **lots of** things to do.',
                            'type': 'Informal',
                            'note': 'Hay muchas cosas que hacer'
                        },
                    ],
                    'note': '✓ A LOT OF funciona con TODO y es más natural que much/many en afirmativo'
                },
                {
                    'title': '📉 FEW / LITTLE',
                    'rule': 'Para poca cantidad',
                    'formula': 'FEW (contable) / LITTLE (incontable)',
                    'examples': [
                        {
                            'sentence': 'I have **few** friends.',
                            'meaning': 'Pocos amigos (negativo, casi nada)',
                            'type': 'Contable'
                        },
                        {
                            'sentence': 'I have **a few** friends.',
                            'meaning': 'Algunos amigos (positivo, suficiente)',
                            'type': 'Contable'
                        },
                        {
                            'sentence': 'There is **little** hope.',
                            'meaning': 'Poca esperanza (negativo)',
                            'type': 'Incontable'
                        },
                        {
                            'sentence': 'There is **a little** hope.',
                            'meaning': 'Algo de esperanza (positivo)',
                            'type': 'Incontable'
                        },
                    ],
                    'note': '⚠️ FEW/LITTLE = casi nada (negativo). A FEW/A LITTLE = algo (positivo)'
                },
                {
                    'title': '📋 Contable vs Incontable',
                    'rule': 'Memoriza cuáles son incontables',
                    'formula': 'Incontable = no plural, no "a/an"',
                    'examples': [
                        {
                            'category': 'INCONTABLES comunes:',
                            'items': 'money, water, milk, coffee, tea, bread, rice, information, advice, news, homework, work, music, furniture, luggage, weather, time'
                        },
                        {
                            'category': 'CONTABLES:',
                            'items': 'book/books, apple/apples, friend/friends, idea/ideas, question/questions'
                        },
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {
                'wrong': 'I have much money.',
                'correct': 'I have a lot of money.',
                'explanation': '❌ MUCH en afirmativo suena raro. Usa A LOT OF'
            },
            {
                'wrong': 'Do you have some questions?',
                'correct': 'Do you have any questions?',
                'explanation': '❌ En preguntas normales usa ANY (SOME solo en ofertas)'
            },
            {
                'wrong': 'I don\'t have many money.',
                'correct': "I don't have much money.",
                'explanation': '❌ MONEY es incontable, usa MUCH, no MANY'
            },
            {
                'wrong': 'I have a few money.',
                'correct': 'I have a little money.',
                'explanation': '❌ MONEY es incontable, usa LITTLE, no FEW'
            },
            {
                'wrong': 'There aren\'t a lot of people.',
                'correct': "There aren't many people.",
                'explanation': '❌ En negativo es más natural usar MANY'
            }
        ],
        
        'tips': [
            {
                'icon': '✅',
                'title': 'SOME vs ANY',
                'content': 'SOME = afirmativo u ofertas. ANY = negativo y preguntas.'
            },
            {
                'icon': '📦',
                'title': 'A LOT OF = comodín',
                'content': 'A LOT OF funciona con contables e incontables, afirmativo.'
            },
            {
                'icon': '📉',
                'title': 'A cambia el significado',
                'content': 'FEW = casi nada 😔. A FEW = algunos 😊. (Little/A little igual)'
            },
            {
                'icon': '❓',
                'title': '¿Contable o incontable?',
                'content': '¿Tiene plural? → Contable. ¿No? → Incontable (water, money, advice)'
            }
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con some, any, much, many, a lot of, few, little.',
                'questions': [
                    {'prompt': 'I don\'t have ___ money.', 'answer': 'much', 'hint': 'Money = incontable, negativo'},
                    {'prompt': 'There are ___ books on the table.', 'answer': 'some', 'hint': 'Afirmativo = some'},
                    {'prompt': 'Do you have ___ questions?', 'answer': 'any', 'hint': 'Pregunta = any'},
                    {'prompt': 'She has ___ friends. She\'s very popular.', 'answer': 'a lot of', 'hint': 'Muchos (afirmativo) = a lot of'},
                    {'prompt': 'There is very ___ time left. Hurry!', 'answer': 'little', 'hint': 'Poco tiempo (negativo) = little'},
                    {'prompt': 'I have ___ friends in this city. I feel lonely.', 'answer': 'few', 'hint': 'Pocos (negativo) = few'},
                    {'prompt': 'Would you like ___ coffee?', 'answer': 'some', 'hint': 'Oferta = some'},
                    {'prompt': 'How ___ students are in your class?', 'answer': 'many', 'hint': 'Students = contable = many'}
                ]
            },
            {
                'type': 'multiple_choice',
                'instruction': 'Elige la opción correcta.',
                'questions': [
                    {
                        'prompt': 'I don\'t have ___ time today.',
                        'options': ['many', 'much', 'a lot of', 'few'],
                        'answer': 'much',
                        'explanation': 'TIME = incontable, negativo = MUCH'
                    },
                    {
                        'prompt': 'There are ___ people at the party.',
                        'options': ['much', 'a lot of', 'little', 'any'],
                        'answer': 'a lot of',
                        'explanation': 'Afirmativo + cantidad grande = A LOT OF'
                    },
                    {
                        'prompt': 'She has ___ experience. She just graduated.',
                        'options': ['few', 'little', 'many', 'a lot of'],
                        'answer': 'little',
                        'explanation': 'EXPERIENCE = incontable, poca cantidad negativa = LITTLE'
                    }
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Referencia Rápida

### Tabla General
| Quantifier | Contable | Incontable | Uso |
|------------|----------|------------|-----|
| some | ✓ | ✓ | Afirmativo |
| any | ✓ | ✓ | Negativo/Pregunta |
| many | ✓ | ❌ | Neg/Pregunta |
| much | ❌ | ✓ | Neg/Pregunta |
| a lot of | ✓ | ✓ | Afirmativo |
| few | ✓ | ❌ | Poco (−) |
| a few | ✓ | ❌ | Algunos (+) |
| little | ❌ | ✓ | Poco (−) |
| a little | ❌ | ✓ | Algo (+) |

### SOME vs ANY
| SOME | ANY |
|------|-----|
| Afirmativo | Negativo/Pregunta |
| Ofertas | Normal |
| I have **some** | I don't have **any** |

### FEW/LITTLE vs A FEW/A LITTLE
| Sin "a" | Con "a" |
|---------|---------|
| Casi nada 😔 | Algo 😊 |
| **Few** friends (pocos) | **A few** friends (algunos) |
| **Little** hope (poca) | **A little** hope (algo de) |

### Incontables Comunes
money, water, milk, coffee, bread, rice, information, advice, news, homework, work, music, furniture, luggage, weather, time
'''
    },
    
    # ==================== NUEVOS TEMAS ====================
    'phrasal-verbs': {
        'title': 'Phrasal Verbs',
        'icon': '🔀',
        'difficulty': 'intermediate',
        'estimated_time': '30 min',
        'description': 'Domina los verbos compuestos más comunes del inglés.',
        
        'theory': {
            'introduction': '''
Los **Phrasal Verbs** son verbos compuestos formados por un verbo + partícula (preposición o adverbio).
El significado generalmente es **diferente** del verbo original.

**Ejemplo:** **look** = mirar, pero **look after** = cuidar
''',
            'rules': [
                {
                    'title': '📌 Tipos de Phrasal Verbs',
                    'rule': 'Pueden ser separables o inseparables',
                    'formula': 'Verb + Particle (+ Object)',
                    'examples': [
                        {'type': 'Separable', 'example': 'Turn **off** the TV / Turn the TV **off** / Turn **it** off',
                         'note': 'Con pronombres, SIEMPRE van separados'},
                        {'type': 'Inseparable', 'example': 'Look **after** the baby / Look **after** it (NO: Look it after)',
                         'note': 'Nunca se separan'},
                        {'type': 'Intransitivo', 'example': 'The plane **took off** at 8am.',
                         'note': 'No llevan objeto'}
                    ]
                },
                {
                    'title': '🔄 Phrasal Verbs con GET',
                    'rule': 'GET es uno de los más versátiles',
                    'formula': 'GET + partícula',
                    'examples': [
                        {'verb': 'get up', 'meaning': 'levantarse', 'sentence': 'I **get up** at 7am every day.'},
                        {'verb': 'get on', 'meaning': 'subir (transporte)', 'sentence': 'We **get on** the bus here.'},
                        {'verb': 'get off', 'meaning': 'bajar (transporte)', 'sentence': '**Get off** at the next stop.'},
                        {'verb': 'get along', 'meaning': 'llevarse bien', 'sentence': 'Do you **get along** with your boss?'},
                        {'verb': 'get over', 'meaning': 'superar/recuperarse', 'sentence': 'She finally **got over** the breakup.'},
                        {'verb': 'get away', 'meaning': 'escapar', 'sentence': 'The thief **got away**.'}
                    ]
                },
                {
                    'title': '🔄 Phrasal Verbs con LOOK',
                    'rule': 'Muy comunes en conversación',
                    'formula': 'LOOK + partícula',
                    'examples': [
                        {'verb': 'look for', 'meaning': 'buscar', 'sentence': "I'm **looking for** my keys."},
                        {'verb': 'look after', 'meaning': 'cuidar', 'sentence': 'Can you **look after** my cat?'},
                        {'verb': 'look up', 'meaning': 'buscar (información)', 'sentence': '**Look up** the word in the dictionary.'},
                        {'verb': 'look forward to', 'meaning': 'esperar con ilusión', 'sentence': "I'm **looking forward to** the party."},
                        {'verb': 'look out', 'meaning': 'tener cuidado', 'sentence': "**Look out!** There's a car coming."}
                    ]
                },
                {
                    'title': '🔄 Phrasal Verbs con TAKE',
                    'rule': 'Acciones y cambios',
                    'formula': 'TAKE + partícula',
                    'examples': [
                        {'verb': 'take off', 'meaning': 'despegar/quitarse', 'sentence': '**Take off** your shoes, please.'},
                        {'verb': 'take up', 'meaning': 'empezar (hobby)', 'sentence': "I've **taken up** yoga recently."},
                        {'verb': 'take after', 'meaning': 'parecerse a', 'sentence': 'She **takes after** her mother.'},
                        {'verb': 'take care of', 'meaning': 'encargarse de', 'sentence': "I'll **take care of** the problem."},
                        {'verb': 'take back', 'meaning': 'devolver', 'sentence': 'Can I **take back** this shirt?'}
                    ]
                },
                {
                    'title': '🔄 Phrasal Verbs con TURN',
                    'rule': 'Cambios de estado y dirección',
                    'formula': 'TURN + partícula',
                    'examples': [
                        {'verb': 'turn on', 'meaning': 'encender', 'sentence': '**Turn on** the lights.'},
                        {'verb': 'turn off', 'meaning': 'apagar', 'sentence': 'Please **turn off** your phone.'},
                        {'verb': 'turn up', 'meaning': 'subir (volumen)/aparecer', 'sentence': 'He **turned up** late to the meeting.'},
                        {'verb': 'turn down', 'meaning': 'bajar/rechazar', 'sentence': 'She **turned down** the job offer.'},
                        {'verb': 'turn into', 'meaning': 'convertirse en', 'sentence': 'The caterpillar **turned into** a butterfly.'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': "I'm looking forward to see you.", 'correct': "I'm looking forward **to seeing** you.",
             'explanation': 'Después de "to" en phrasal verbs, usa GERUNDIO'},
            {'wrong': 'Turn off it.', 'correct': 'Turn **it** off.',
             'explanation': 'Con pronombres, los phrasal separables DEBEN separarse'},
            {'wrong': 'I must look after him him.', 'correct': 'I must look **after** him.',
             'explanation': 'Look after es inseparable'}
        ],
        
        'tips': [
            {'icon': '📚', 'title': 'Aprende en contexto', 'content': 'No memorices listas, aprende phrasal verbs en oraciones.'},
            {'icon': '🎯', 'title': 'Enfócate en los más comunes', 'content': 'GET, TAKE, LOOK, PUT, TURN, GIVE, COME, GO cubren el 80%.'},
            {'icon': '📝', 'title': 'Pronombres = separar', 'content': 'Si es separable y usas pronombre: SIEMPRE separar.'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con la partícula correcta.',
                'questions': [
                    {'prompt': "I'm looking ___ my glasses. Have you seen them?", 'answer': 'for', 'hint': 'look for = buscar'},
                    {'prompt': "Please turn ___ the music. It's too loud.", 'answer': 'down', 'hint': 'turn down = bajar'},
                    {'prompt': 'She takes ___ her grandmother.', 'answer': 'after', 'hint': 'take after = parecerse a'},
                    {'prompt': 'What time do you usually get ___?', 'answer': 'up', 'hint': 'get up = levantarse'},
                    {'prompt': "I'm looking forward ___ meeting you.", 'answer': 'to', 'hint': 'look forward to = esperar con ilusión'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📋 Phrasal Verbs Esenciales

| Phrasal Verb | Significado | Ejemplo |
|--------------|-------------|---------|
| get up | levantarse | I get up at 7. |
| look for | buscar | I'm looking for my keys. |
| look after | cuidar | Look after your sister. |
| turn on/off | encender/apagar | Turn off the TV. |
| take off | despegar/quitarse | Take off your coat. |
| give up | rendirse/dejar | Don't give up! |
| put on | ponerse | Put on your jacket. |
| find out | descubrir | I found out the truth. |
| run out of | quedarse sin | We ran out of milk. |
| come back | regresar | Come back soon! |
'''
    },
    
    'prepositions-time': {
        'title': 'Prepositions of Time',
        'icon': '⏰',
        'difficulty': 'beginner',
        'estimated_time': '20 min',
        'description': 'Domina IN, ON, AT para expresar tiempo correctamente.',
        
        'theory': {
            'introduction': '''
Las preposiciones de tiempo **IN, ON, AT** tienen reglas específicas:
- **AT** - horas, momentos precisos
- **ON** - días, fechas
- **IN** - períodos largos (meses, años, estaciones)
''',
            'rules': [
                {
                    'title': '⏰ AT - Momentos Precisos',
                    'rule': 'Usa AT para horas y momentos específicos',
                    'formula': 'AT + hora/momento',
                    'examples': [
                        {'prep': 'at', 'example': "I wake up **at 7 o'clock**.", 'use': 'Horas'},
                        {'prep': 'at', 'example': "Let's meet **at noon**.", 'use': 'Mediodía/Medianoche'},
                        {'prep': 'at', 'example': 'We eat turkey **at Christmas**.', 'use': 'Festividades'},
                        {'prep': 'at', 'example': "I'll call you **at the weekend**.", 'use': 'Fin de semana (UK)'},
                        {'prep': 'at', 'example': '**At that moment**, I realized the truth.', 'use': 'Momentos'}
                    ]
                },
                {
                    'title': '📅 ON - Días y Fechas',
                    'rule': 'Usa ON para días específicos',
                    'formula': 'ON + día/fecha',
                    'examples': [
                        {'prep': 'on', 'example': 'I go to gym **on Mondays**.', 'use': 'Días de la semana'},
                        {'prep': 'on', 'example': 'My birthday is **on March 15th**.', 'use': 'Fechas'},
                        {'prep': 'on', 'example': 'We got married **on a sunny day**.', 'use': 'Día + descripción'},
                        {'prep': 'on', 'example': '**On the weekend**, I relax.', 'use': 'Fin de semana (US)'},
                        {'prep': 'on', 'example': 'See you **on Christmas Day**.', 'use': 'Día festivo específico'}
                    ]
                },
                {
                    'title': '📆 IN - Períodos Largos',
                    'rule': 'Usa IN para meses, años, estaciones, décadas, siglos',
                    'formula': 'IN + período',
                    'examples': [
                        {'prep': 'in', 'example': 'I was born **in 1995**.', 'use': 'Años'},
                        {'prep': 'in', 'example': "It's hot **in summer**.", 'use': 'Estaciones'},
                        {'prep': 'in', 'example': "We'll travel **in December**.", 'use': 'Meses'},
                        {'prep': 'in', 'example': 'Disco was popular **in the 70s**.', 'use': 'Décadas'},
                        {'prep': 'in', 'example': "I'll be ready **in 5 minutes**.", 'use': 'Dentro de (futuro)'},
                        {'prep': 'in', 'example': 'I work best **in the morning**.', 'use': 'Partes del día'}
                    ]
                },
                {
                    'title': '⚠️ Sin Preposición',
                    'rule': 'NO uses preposición con: this, last, next, every, yesterday, tomorrow, today',
                    'formula': 'CERO preposición',
                    'examples': [
                        {'wrong': 'on this Monday', 'correct': '**this** Monday', 'note': 'This = sin preposición'},
                        {'wrong': 'in last year', 'correct': '**last** year', 'note': 'Last = sin preposición'},
                        {'wrong': 'on next Friday', 'correct': '**next** Friday', 'note': 'Next = sin preposición'},
                        {'wrong': 'on every day', 'correct': '**every** day', 'note': 'Every = sin preposición'},
                        {'wrong': 'in yesterday', 'correct': '**yesterday**', 'note': 'Yesterday = sin preposición'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'I was born in March 15th.', 'correct': 'I was born **on** March 15th.',
             'explanation': 'Fechas específicas usan ON'},
            {'wrong': 'See you in Monday.', 'correct': 'See you **on** Monday.',
             'explanation': 'Días de la semana usan ON'},
            {'wrong': 'I wake up in 6am.', 'correct': 'I wake up **at** 6am.',
             'explanation': 'Horas usan AT'}
        ],
        
        'tips': [
            {'icon': '🎯', 'title': 'Regla de precisión', 'content': 'Más preciso = AT. Menos preciso = IN. Días = ON.'},
            {'icon': '📝', 'title': 'Truco "IN the"', 'content': 'morning, afternoon, evening usan IN. Pero AT night.'},
            {'icon': '⚡', 'title': 'Memoria: A-O-I', 'content': 'AT=momento, ON=día, IN=período. Orden de precisión.'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con AT, ON o IN.',
                'questions': [
                    {'prompt': "I'll see you ___ 3 o'clock.", 'answer': 'at', 'hint': 'Hora = at'},
                    {'prompt': 'We go to church ___ Sundays.', 'answer': 'on', 'hint': 'Día = on'},
                    {'prompt': 'She was born ___ 1998.', 'answer': 'in', 'hint': 'Año = in'},
                    {'prompt': 'The meeting is ___ Monday morning.', 'answer': 'on', 'hint': 'Día específico = on'},
                    {'prompt': "I'll call you back ___ 5 minutes.", 'answer': 'in', 'hint': 'Dentro de = in'},
                    {'prompt': 'We met ___ Christmas.', 'answer': 'at', 'hint': 'Festividad = at'}
                ]
            }
        ],
        
        'quick_reference': '''
## ⏰ AT, ON, IN para Tiempo

| Preposición | Uso | Ejemplos |
|-------------|-----|----------|
| **AT** | Horas, momentos | at 5pm, at noon, at midnight |
| **AT** | Festividades | at Christmas, at Easter |
| **ON** | Días | on Monday, on weekends |
| **ON** | Fechas | on July 4th, on my birthday |
| **IN** | Meses | in January, in December |
| **IN** | Años/Décadas | in 2020, in the 90s |
| **IN** | Estaciones | in summer, in winter |
| **IN** | Partes del día | in the morning (pero AT night) |

### ⚠️ Sin Preposición
this, last, next, every, yesterday, tomorrow, today
'''
    },
    
    'prepositions-place': {
        'title': 'Prepositions of Place',
        'icon': '📍',
        'difficulty': 'beginner',
        'estimated_time': '20 min',
        'description': 'Aprende a usar IN, ON, AT para lugares correctamente.',
        
        'theory': {
            'introduction': '''
Las preposiciones de lugar **IN, ON, AT** siguen estas reglas:
- **IN** - dentro de espacios cerrados/áreas
- **ON** - sobre superficies
- **AT** - puntos específicos/direcciones
''',
            'rules': [
                {
                    'title': '📦 IN - Dentro de',
                    'rule': 'Usa IN para espacios cerrados o áreas',
                    'formula': 'IN + espacio/área',
                    'examples': [
                        {'prep': 'in', 'example': 'The keys are **in** the drawer.', 'use': 'Dentro de contenedor'},
                        {'prep': 'in', 'example': 'I live **in** Mexico City.', 'use': 'Ciudades'},
                        {'prep': 'in', 'example': 'She works **in** an office.', 'use': 'Edificios (interior)'},
                        {'prep': 'in', 'example': "He's **in** the kitchen.", 'use': 'Habitaciones'},
                        {'prep': 'in', 'example': 'I read it **in** the newspaper.', 'use': 'Medios impresos'}
                    ]
                },
                {
                    'title': '📄 ON - Sobre',
                    'rule': 'Usa ON para superficies y medios de transporte',
                    'formula': 'ON + superficie',
                    'examples': [
                        {'prep': 'on', 'example': 'The book is **on** the table.', 'use': 'Superficies'},
                        {'prep': 'on', 'example': "There's a picture **on** the wall.", 'use': 'Paredes'},
                        {'prep': 'on', 'example': 'I saw it **on** TV.', 'use': 'Pantallas'},
                        {'prep': 'on', 'example': "She's **on** the bus.", 'use': 'Transporte público'},
                        {'prep': 'on', 'example': 'I live **on** Main Street.', 'use': 'Calles (sin número)'}
                    ]
                },
                {
                    'title': '📌 AT - Punto Específico',
                    'rule': 'Usa AT para lugares específicos y direcciones',
                    'formula': 'AT + punto/dirección',
                    'examples': [
                        {'prep': 'at', 'example': "I'm **at** the bus stop.", 'use': 'Puntos específicos'},
                        {'prep': 'at', 'example': "She's **at** work.", 'use': 'Actividades/Lugares comunes'},
                        {'prep': 'at', 'example': 'Meet me **at** the entrance.', 'use': 'Puntos de encuentro'},
                        {'prep': 'at', 'example': 'I live **at** 25 Oak Street.', 'use': 'Direcciones con número'},
                        {'prep': 'at', 'example': "He's **at** the doctor's.", 'use': 'Negocios/Servicios'}
                    ]
                },
                {
                    'title': '🚗 Transporte',
                    'rule': 'IN para carros/taxis, ON para transporte público',
                    'formula': 'IN car/taxi, ON bus/train/plane',
                    'examples': [
                        {'prep': 'in', 'example': "He's **in** the car.", 'use': 'Carros, taxis'},
                        {'prep': 'on', 'example': "She's **on** the train.", 'use': 'Trenes'},
                        {'prep': 'on', 'example': "We're **on** the plane.", 'use': 'Aviones'},
                        {'prep': 'on', 'example': "I'm **on** my bike.", 'use': 'Bicicletas, motos'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': "I'm in the bus stop.", 'correct': "I'm **at** the bus stop.",
             'explanation': 'Puntos específicos usan AT'},
            {'wrong': 'She lives on Paris.', 'correct': 'She lives **in** Paris.',
             'explanation': 'Ciudades usan IN'},
            {'wrong': 'The picture is in the wall.', 'correct': 'The picture is **on** the wall.',
             'explanation': 'Superficies verticales usan ON'}
        ],
        
        'tips': [
            {'icon': '🎯', 'title': 'IN = dentro', 'content': 'Si puedes entrar, probablemente es IN.'},
            {'icon': '📝', 'title': 'ON = superficie', 'content': 'Si algo toca una superficie, es ON.'},
            {'icon': '📍', 'title': 'AT = punto', 'content': 'Si es un punto en el mapa o dirección, es AT.'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con IN, ON o AT.',
                'questions': [
                    {'prompt': 'I live ___ Mexico.', 'answer': 'in', 'hint': 'País = in'},
                    {'prompt': 'The cat is ___ the roof.', 'answer': 'on', 'hint': 'Superficie = on'},
                    {'prompt': 'Meet me ___ the airport.', 'answer': 'at', 'hint': 'Punto de encuentro = at'},
                    {'prompt': "She's ___ her car.", 'answer': 'in', 'hint': 'Carros = in'},
                    {'prompt': 'I saw it ___ the news.', 'answer': 'on', 'hint': 'TV/medios = on'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📍 IN, ON, AT para Lugar

| Preposición | Uso | Ejemplos |
|-------------|-----|----------|
| **IN** | Países, ciudades | in Mexico, in Paris |
| **IN** | Habitaciones, edificios | in the kitchen, in a hotel |
| **IN** | Carros, taxis | in the car, in a taxi |
| **ON** | Superficies | on the table, on the floor |
| **ON** | Calles (sin número) | on Main Street |
| **ON** | Transporte público | on the bus, on the train |
| **AT** | Direcciones | at 123 Main St. |
| **AT** | Lugares específicos | at the station, at work |
'''
    },
    
    'have-has-got': {
        'title': 'Have / Has Got',
        'icon': '🎁',
        'difficulty': 'beginner',
        'estimated_time': '15 min',
        'description': 'Aprende a expresar posesión y características con have got.',
        
        'theory': {
            'introduction': '''
**Have got** se usa para expresar **posesión** y **características**.
Es más común en inglés británico. En inglés americano se prefiere **have**.

**I have got** = **I've got** = Tengo
''',
            'rules': [
                {
                    'title': '✅ Afirmativo',
                    'rule': 'Subject + have/has got + complement',
                    'formula': 'I/You/We/They + HAVE GOT | He/She/It + HAS GOT',
                    'examples': [
                        {'sentence': "I **have got** a new car. / I'**ve got** a new car."},
                        {'sentence': "She **has got** blue eyes. / She'**s got** blue eyes."},
                        {'sentence': "They **have got** two children. / They'**ve got** two children."},
                        {'sentence': "He **has got** a headache. / He'**s got** a headache."}
                    ]
                },
                {
                    'title': '❌ Negativo',
                    'rule': "Subject + haven't/hasn't got + complement",
                    'formula': "have not got = haven't got | has not got = hasn't got",
                    'examples': [
                        {'sentence': "I **haven't got** any money."},
                        {'sentence': "She **hasn't got** a boyfriend."},
                        {'sentence': "We **haven't got** time."},
                        {'sentence': "It **hasn't got** a battery."}
                    ]
                },
                {
                    'title': '❓ Preguntas',
                    'rule': 'Have/Has + subject + got + complement?',
                    'formula': 'HAVE/HAS + sujeto + GOT?',
                    'examples': [
                        {'sentence': '**Have** you **got** a pen?', 'translation': '¿Tienes un bolígrafo?'},
                        {'sentence': '**Has** she **got** a car?', 'translation': '¿Tiene ella un carro?'},
                        {'sentence': '**Have** they **got** any news?', 'translation': '¿Tienen noticias?'},
                        {'sentence': 'What **have** you **got** in your bag?', 'translation': '¿Qué tienes en tu bolsa?'}
                    ]
                },
                {
                    'title': '🔄 Have Got vs Have',
                    'rule': 'Mismo significado, diferente estructura',
                    'formula': 'HAVE GOT (UK) = HAVE (US)',
                    'examples': [
                        {'sentence': "I've got a dog. = I have a dog.", 'note': 'Ambos correctos'},
                        {'sentence': 'Have you got time? = Do you have time?', 'note': 'Pregunta'},
                        {'sentence': "She hasn't got money. = She doesn't have money.", 'note': 'Negativo'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'I have got go to work.', 'correct': 'I **have to** go to work.',
             'explanation': 'Para obligación, usa HAVE TO, no HAVE GOT'},
            {'wrong': 'Do you have got a car?', 'correct': '**Have** you **got** a car? / Do you have a car?',
             'explanation': 'No mezcles DO con HAVE GOT'},
            {'wrong': 'She has got breakfast.', 'correct': 'She **has** breakfast.',
             'explanation': 'Para acciones (eat breakfast), usa HAVE sin GOT'}
        ],
        
        'tips': [
            {'icon': '🇬🇧', 'title': 'UK vs US', 'content': 'HAVE GOT es más británico. HAVE es más americano.'},
            {'icon': '⚡', 'title': 'Contracciones', 'content': "En habla informal: I've got, She's got, We've got."},
            {'icon': '🎯', 'title': 'Solo posesión', 'content': 'HAVE GOT solo para posesión, no para acciones.'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con have got o has got.',
                'questions': [
                    {'prompt': 'I ___ a new phone.', 'answer': 'have got', 'hint': 'I = have got'},
                    {'prompt': 'She ___ beautiful eyes.', 'answer': 'has got', 'hint': 'She = has got'},
                    {'prompt': '___ you ___ any brothers?', 'answer': 'Have...got', 'hint': 'Pregunta: Have + sujeto + got'},
                    {'prompt': 'We ___ a big house.', 'answer': "haven't got", 'hint': "Negativo: haven't got"},
                    {'prompt': 'He ___ a lot of friends.', 'answer': 'has got', 'hint': 'He = has got'}
                ]
            }
        ],
        
        'quick_reference': '''
## 🎁 Have Got - Resumen

| Forma | I/You/We/They | He/She/It |
|-------|---------------|-----------|
| ✅ Afirmativo | have got ('ve got) | has got ('s got) |
| ❌ Negativo | haven't got | hasn't got |
| ❓ Pregunta | Have...got? | Has...got? |

### Ejemplos
- ✅ I've got a car. (Tengo un carro)
- ❌ She hasn't got time. (No tiene tiempo)
- ❓ Have you got a pen? (¿Tienes un bolígrafo?)
'''
    },
    
    'there-is-are': {
        'title': 'There is / There are',
        'icon': '📍',
        'difficulty': 'beginner',
        'estimated_time': '15 min',
        'description': 'Expresa existencia y ubicación con there is/are.',
        
        'theory': {
            'introduction': '''
**There is** y **There are** se usan para decir que algo **existe** o **está en un lugar**.
- **There is** - Singular / Incontable
- **There are** - Plural
''',
            'rules': [
                {
                    'title': '✅ Afirmativo',
                    'rule': 'There is/are + sustantivo + lugar',
                    'formula': 'There is (singular) / There are (plural)',
                    'examples': [
                        {'sentence': '**There is** a book on the table.', 'translation': 'Hay un libro en la mesa.'},
                        {'sentence': '**There are** three cats in the garden.', 'translation': 'Hay tres gatos en el jardín.'},
                        {'sentence': "**There's** some milk in the fridge.", 'translation': 'Hay leche en el refrigerador.'},
                        {'sentence': '**There are** many people here.', 'translation': 'Hay muchas personas aquí.'}
                    ]
                },
                {
                    'title': '❌ Negativo',
                    'rule': "There isn't/aren't + sustantivo",
                    'formula': "There is not = There isn't | There are not = There aren't",
                    'examples': [
                        {'sentence': "**There isn't** any water.", 'translation': 'No hay agua.'},
                        {'sentence': "**There aren't** any chairs.", 'translation': 'No hay sillas.'},
                        {'sentence': "**There's no** time.", 'translation': 'No hay tiempo.'},
                        {'sentence': '**There are no** problems.', 'translation': 'No hay problemas.'}
                    ]
                },
                {
                    'title': '❓ Preguntas',
                    'rule': 'Is/Are there + sustantivo?',
                    'formula': 'Is there...? / Are there...?',
                    'examples': [
                        {'sentence': '**Is there** a bank near here?', 'translation': '¿Hay un banco cerca de aquí?'},
                        {'sentence': '**Are there** any questions?', 'translation': '¿Hay alguna pregunta?'},
                        {'sentence': 'How many students **are there**?', 'translation': '¿Cuántos estudiantes hay?'},
                        {'sentence': '**Is there** any coffee left?', 'translation': '¿Queda café?'}
                    ]
                },
                {
                    'title': '🔢 Some/Any con There is/are',
                    'rule': 'SOME en afirmativo, ANY en negativo/pregunta',
                    'formula': 'There is/are + some (✅) / any (❓❌)',
                    'examples': [
                        {'sentence': 'There are **some** apples. ✅'},
                        {'sentence': "There aren't **any** apples. ❌"},
                        {'sentence': 'Are there **any** apples? ❓'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'There is many people.', 'correct': 'There **are** many people.',
             'explanation': 'PEOPLE es plural, usa ARE'},
            {'wrong': 'Have a book on the table.', 'correct': '**There is** a book on the table.',
             'explanation': 'Para existencia, usa THERE IS/ARE, no HAVE'},
            {'wrong': 'There are some water.', 'correct': 'There **is** some water.',
             'explanation': 'WATER es incontable, usa IS'}
        ],
        
        'tips': [
            {'icon': '🔢', 'title': 'Cuenta el sustantivo', 'content': '1 cosa = is. 2+ cosas = are.'},
            {'icon': '💧', 'title': 'Incontables = is', 'content': 'Water, money, time siempre con IS.'},
            {'icon': '📝', 'title': "There's", 'content': "En habla informal: There's = There is."}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con there is o there are.',
                'questions': [
                    {'prompt': '___ a dog in the park.', 'answer': 'There is', 'hint': 'A dog = singular'},
                    {'prompt': '___ many cars on the street.', 'answer': 'There are', 'hint': 'Many cars = plural'},
                    {'prompt': '___ any milk?', 'answer': 'Is there', 'hint': 'Pregunta + singular'},
                    {'prompt': '___ no chairs in the room.', 'answer': 'There are', 'hint': 'Chairs = plural'},
                    {'prompt': '___ some coffee in the cup.', 'answer': 'There is', 'hint': 'Coffee = incontable'}
                ]
            }
        ],
        
        'quick_reference': '''
## 📍 There is / There are

| | Singular/Incontable | Plural |
|--|---------------------|--------|
| ✅ | There is / There's | There are |
| ❌ | There isn't / There's no | There aren't / There are no |
| ❓ | Is there...? | Are there...? |

### Ejemplos
- There **is** a cat. (singular)
- There **is** some water. (incontable)
- There **are** five books. (plural)
'''
    },
    
    'possessives': {
        'title': 'Possessives',
        'icon': '👤',
        'difficulty': 'beginner',
        'estimated_time': '20 min',
        'description': 'Domina los adjetivos y pronombres posesivos en inglés.',
        
        'theory': {
            'introduction': '''
Los posesivos indican **pertenencia**. Hay dos tipos:
- **Adjetivos posesivos**: van ANTES del sustantivo (my book)
- **Pronombres posesivos**: REEMPLAZAN al sustantivo (It's mine)
''',
            'rules': [
                {
                    'title': '📝 Adjetivos Posesivos',
                    'rule': 'Van ANTES del sustantivo, nunca solos',
                    'formula': 'Possessive Adjective + Noun',
                    'examples': [
                        {'sentence': '**My** name is John.', 'translation': 'Mi nombre es John.'},
                        {'sentence': 'Is this **your** bag?', 'translation': '¿Esta es tu bolsa?'},
                        {'sentence': '**His** car is red.', 'translation': 'Su carro (de él) es rojo.'},
                        {'sentence': '**Her** eyes are blue.', 'translation': 'Sus ojos (de ella) son azules.'},
                        {'sentence': 'The cat loves **its** toy.', 'translation': 'El gato ama su juguete.'},
                        {'sentence': '**Our** house is big.', 'translation': 'Nuestra casa es grande.'},
                        {'sentence': '**Their** children are smart.', 'translation': 'Sus hijos (de ellos) son inteligentes.'}
                    ]
                },
                {
                    'title': '📌 Pronombres Posesivos',
                    'rule': 'Van SOLOS, reemplazan sustantivo',
                    'formula': 'Pronombre Posesivo (sin sustantivo)',
                    'examples': [
                        {'sentence': 'This book is **mine**.', 'translation': 'Este libro es mío.'},
                        {'sentence': 'Is this **yours**?', 'translation': '¿Esto es tuyo?'},
                        {'sentence': 'The red car is **his**.', 'translation': 'El carro rojo es de él.'},
                        {'sentence': 'This seat is **hers**.', 'translation': 'Este asiento es de ella.'},
                        {'sentence': 'That house is **ours**.', 'translation': 'Esa casa es nuestra.'},
                        {'sentence': 'The kids are **theirs**.', 'translation': 'Los niños son de ellos.'}
                    ]
                },
                {
                    'title': '📊 Tabla Comparativa',
                    'rule': 'Memoriza ambas formas',
                    'formula': 'Sujeto - Adjetivo - Pronombre',
                    'examples': [
                        {'sentence': 'I - **my** - **mine**'},
                        {'sentence': 'you - **your** - **yours**'},
                        {'sentence': 'he - **his** - **his**'},
                        {'sentence': 'she - **her** - **hers**'},
                        {'sentence': 'it - **its** - (no tiene)'},
                        {'sentence': 'we - **our** - **ours**'},
                        {'sentence': 'they - **their** - **theirs**'}
                    ]
                },
                {
                    'title': "'S Posesivo",
                    'rule': "Para nombres y sustantivos, agrega 'S",
                    'formula': "Noun + 's + Noun",
                    'examples': [
                        {'sentence': "**John's** car is blue.", 'translation': 'El carro de John es azul.'},
                        {'sentence': "This is **my mother's** house.", 'translation': 'Esta es la casa de mi madre.'},
                        {'sentence': "**The dog's** name is Max.", 'translation': 'El nombre del perro es Max.'},
                        {'sentence': "**Children's** toys are colorful.", 'translation': 'Los juguetes de los niños son coloridos.'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'This is mine book.', 'correct': 'This is **my** book.',
             'explanation': 'Con sustantivo = adjetivo (my), sin sustantivo = pronombre (mine)'},
            {'wrong': "The dog lost it's toy.", 'correct': 'The dog lost **its** toy.',
             'explanation': "ITS (posesivo) no lleva apóstrofo. IT'S = it is"},
            {'wrong': 'Is this book your?', 'correct': 'Is this book **yours**?',
             'explanation': 'Sin sustantivo después = pronombre posesivo (yours)'}
        ],
        
        'tips': [
            {'icon': '📝', 'title': 'Adjetivo + Sustantivo', 'content': 'My, your, his, her, its, our, their + NOUN'},
            {'icon': '🎯', 'title': 'Pronombre solo', 'content': 'Mine, yours, his, hers, ours, theirs = SIN sustantivo'},
            {'icon': '⚠️', 'title': "Its vs It's", 'content': "ITS = de ello (posesivo). IT'S = it is (contracción)"}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con el posesivo correcto.',
                'questions': [
                    {'prompt': 'This is ___ (I) book.', 'answer': 'my', 'hint': 'Adjetivo + sustantivo = my'},
                    {'prompt': 'Is this pen ___ (you)?', 'answer': 'yours', 'hint': 'Sin sustantivo = pronombre'},
                    {'prompt': 'The cat is playing with ___ (it) toy.', 'answer': 'its', 'hint': 'Adjetivo posesivo de it'},
                    {'prompt': 'This house is ___ (they).', 'answer': 'theirs', 'hint': 'Sin sustantivo = pronombre'},
                    {'prompt': '___ (she) name is Maria.', 'answer': 'Her', 'hint': 'Adjetivo + sustantivo'}
                ]
            }
        ],
        
        'quick_reference': '''
## 👤 Posesivos

| Sujeto | Adjetivo | Pronombre |
|--------|----------|-----------|
| I | my | mine |
| you | your | yours |
| he | his | his |
| she | her | hers |
| it | its | - |
| we | our | ours |
| they | their | theirs |

### Regla
- **Adjetivo** + sustantivo: This is **my** car.
- **Pronombre** solo: This car is **mine**.
- ITS (posesivo) ≠ IT'S (it is)
'''
    },
    
    'can-could-be-able': {
        'title': 'Can, Could & Be Able To',
        'icon': '💪',
        'difficulty': 'beginner',
        'estimated_time': '20 min',
        'description': 'Expresa habilidad, posibilidad y permisos correctamente.',
        
        'theory': {
            'introduction': '''
**CAN** expresa habilidad y posibilidad en presente.
**COULD** es el pasado de CAN o expresa posibilidad/cortesía.
**BE ABLE TO** se usa para otros tiempos verbales.
''',
            'rules': [
                {
                    'title': '✅ CAN - Habilidad/Posibilidad (Presente)',
                    'rule': 'Sujeto + CAN + verbo base',
                    'formula': 'Subject + CAN + verb (infinitivo sin TO)',
                    'examples': [
                        {'sentence': 'I **can** swim.', 'translation': 'Puedo/Sé nadar.', 'use': 'Habilidad'},
                        {'sentence': 'She **can** speak French.', 'translation': 'Ella sabe hablar francés.', 'use': 'Habilidad'},
                        {'sentence': '**Can** I go now?', 'translation': '¿Puedo irme ahora?', 'use': 'Permiso'},
                        {'sentence': 'It **can** be dangerous.', 'translation': 'Puede ser peligroso.', 'use': 'Posibilidad'},
                        {'sentence': '**Can** you help me?', 'translation': '¿Puedes ayudarme?', 'use': 'Petición'}
                    ]
                },
                {
                    'title': '🕰️ COULD - Pasado/Cortesía',
                    'rule': 'Pasado de CAN o petición cortés',
                    'formula': 'Subject + COULD + verb',
                    'examples': [
                        {'sentence': 'I **could** swim when I was 5.', 'translation': 'Sabía nadar cuando tenía 5 años.', 'use': 'Habilidad pasada'},
                        {'sentence': "She **couldn't** come yesterday.", 'translation': 'Ella no pudo venir ayer.', 'use': 'Incapacidad pasada'},
                        {'sentence': '**Could** you help me, please?', 'translation': '¿Podría ayudarme, por favor?', 'use': 'Petición cortés'},
                        {'sentence': 'It **could** rain later.', 'translation': 'Podría llover más tarde.', 'use': 'Posibilidad'}
                    ]
                },
                {
                    'title': '🔄 BE ABLE TO - Otros Tiempos',
                    'rule': 'Para futuro, presente perfecto, etc.',
                    'formula': 'BE + ABLE TO + verb',
                    'examples': [
                        {'sentence': 'I **will be able to** come tomorrow.', 'translation': 'Podré venir mañana.', 'use': 'Futuro'},
                        {'sentence': 'She **has been able to** finish.', 'translation': 'Ha podido terminar.', 'use': 'Presente Perfecto'},
                        {'sentence': 'I **was able to** escape.', 'translation': 'Pude escapar.', 'use': 'Logro específico'},
                        {'sentence': "He **won't be able to** help.", 'translation': 'No podrá ayudar.', 'use': 'Futuro negativo'}
                    ]
                },
                {
                    'title': '⚠️ COULD vs WAS ABLE TO',
                    'rule': 'COULD = habilidad general, WAS ABLE TO = logro específico',
                    'formula': 'COULD (general) vs WAS ABLE TO (específico)',
                    'examples': [
                        {'sentence': 'I **could** play piano as a child.', 'note': 'Habilidad general'},
                        {'sentence': 'After trying hard, I **was able to** pass.', 'note': 'Logro específico'},
                        {'sentence': 'The door was locked, but I **was able to** open it.', 'note': 'Logro específico'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'I can to swim.', 'correct': 'I **can swim**.',
             'explanation': 'CAN + verbo sin TO'},
            {'wrong': 'She cans play guitar.', 'correct': 'She **can** play guitar.',
             'explanation': 'CAN nunca cambia (no cans, no canned para modal)'},
            {'wrong': 'I will can come tomorrow.', 'correct': 'I **will be able to** come tomorrow.',
             'explanation': 'Usa BE ABLE TO para futuro'}
        ],
        
        'tips': [
            {'icon': '🎯', 'title': 'CAN = simple', 'content': 'Presente y habilidad general = CAN'},
            {'icon': '🕰️', 'title': 'COULD = pasado/cortés', 'content': 'Habilidad pasada o petición educada = COULD'},
            {'icon': '📅', 'title': 'BE ABLE TO = flexibilidad', 'content': 'Para futuro, perfecto, y otros tiempos = BE ABLE TO'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con can, could o be able to.',
                'questions': [
                    {'prompt': 'I ___ speak three languages.', 'answer': 'can', 'hint': 'Habilidad presente = can'},
                    {'prompt': 'She ___ swim when she was 3.', 'answer': 'could', 'hint': 'Habilidad pasada = could'},
                    {'prompt': '___ you help me, please?', 'answer': 'Could', 'hint': 'Petición cortés = could'},
                    {'prompt': 'I will ___ finish tomorrow.', 'answer': 'be able to', 'hint': 'Futuro = will be able to'},
                    {'prompt': 'He ___ come to the party last night.', 'answer': "couldn't", 'hint': "Pasado negativo = couldn't"}
                ]
            }
        ],
        
        'quick_reference': '''
## 💪 CAN, COULD, BE ABLE TO

| Modal | Uso | Ejemplo |
|-------|-----|---------|
| CAN | Presente, habilidad | I can swim. |
| CAN | Permiso informal | Can I go? |
| COULD | Pasado de can | I could swim as a child. |
| COULD | Petición cortés | Could you help? |
| BE ABLE TO | Futuro | I will be able to come. |
| BE ABLE TO | Perfecto | I have been able to finish. |

### Recuerda
- CAN + verbo (sin TO)
- CAN no cambia (no cans, no canning)
- Futuro = will be able to (no will can)
'''
    },
    
    'subject-object-pronouns': {
        'title': 'Subject & Object Pronouns',
        'icon': '👥',
        'difficulty': 'beginner',
        'estimated_time': '15 min',
        'description': 'Diferencia entre pronombres sujeto y objeto.',
        
        'theory': {
            'introduction': '''
Los **pronombres sujeto** realizan la acción (yo, tú, él...).
Los **pronombres objeto** reciben la acción (me, te, lo...).

**I** love **her**. = **Yo** la amo.
''',
            'rules': [
                {
                    'title': '👤 Pronombres Sujeto',
                    'rule': 'Van ANTES del verbo, realizan la acción',
                    'formula': 'Subject Pronoun + Verb',
                    'examples': [
                        {'sentence': '**I** am a student.', 'translation': 'Yo soy estudiante.'},
                        {'sentence': '**You** are my friend.', 'translation': 'Tú eres mi amigo.'},
                        {'sentence': '**He** works here.', 'translation': 'Él trabaja aquí.'},
                        {'sentence': '**She** is beautiful.', 'translation': 'Ella es hermosa.'},
                        {'sentence': '**It** is cold.', 'translation': 'Hace frío. (Está frío)'},
                        {'sentence': '**We** are happy.', 'translation': 'Nosotros estamos felices.'},
                        {'sentence': '**They** live in Paris.', 'translation': 'Ellos viven en París.'}
                    ]
                },
                {
                    'title': '🎯 Pronombres Objeto',
                    'rule': 'Van DESPUÉS del verbo, reciben la acción',
                    'formula': 'Verb + Object Pronoun',
                    'examples': [
                        {'sentence': 'Call **me** later.', 'translation': 'Llámame después.'},
                        {'sentence': 'I love **you**.', 'translation': 'Te amo.'},
                        {'sentence': 'She knows **him**.', 'translation': 'Ella lo conoce.'},
                        {'sentence': 'We saw **her** yesterday.', 'translation': 'La vimos ayer.'},
                        {'sentence': 'I broke **it**.', 'translation': 'Lo rompí.'},
                        {'sentence': 'They visited **us**.', 'translation': 'Ellos nos visitaron.'},
                        {'sentence': 'I helped **them**.', 'translation': 'Los ayudé.'}
                    ]
                },
                {
                    'title': '📊 Tabla Comparativa',
                    'rule': 'Memoriza ambas formas',
                    'formula': 'Sujeto - Objeto',
                    'examples': [
                        {'sentence': 'I - **me**'},
                        {'sentence': 'you - **you**'},
                        {'sentence': 'he - **him**'},
                        {'sentence': 'she - **her**'},
                        {'sentence': 'it - **it**'},
                        {'sentence': 'we - **us**'},
                        {'sentence': 'they - **them**'}
                    ]
                },
                {
                    'title': '🔄 Después de Preposiciones',
                    'rule': 'Siempre usa pronombre OBJETO después de preposiciones',
                    'formula': 'Preposition + Object Pronoun',
                    'examples': [
                        {'sentence': 'This gift is for **you**.', 'translation': 'Este regalo es para ti.'},
                        {'sentence': "I'm thinking about **her**.", 'translation': 'Estoy pensando en ella.'},
                        {'sentence': 'Come with **me**.', 'translation': 'Ven conmigo.'},
                        {'sentence': "There's a message for **him**.", 'translation': 'Hay un mensaje para él.'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'Me am happy.', 'correct': '**I** am happy.',
             'explanation': 'Antes del verbo = pronombre SUJETO'},
            {'wrong': 'I love she.', 'correct': 'I love **her**.',
             'explanation': 'Después del verbo = pronombre OBJETO'},
            {'wrong': 'Between you and I.', 'correct': 'Between you and **me**.',
             'explanation': 'Después de preposición = pronombre OBJETO'}
        ],
        
        'tips': [
            {'icon': '👤', 'title': 'Antes del verbo', 'content': 'Pronombre sujeto: I, you, he, she, it, we, they'},
            {'icon': '🎯', 'title': 'Después del verbo', 'content': 'Pronombre objeto: me, you, him, her, it, us, them'},
            {'icon': '📍', 'title': 'Después de preposición', 'content': 'Siempre objeto: for me, with her, to them'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Elige el pronombre correcto.',
                'questions': [
                    {'prompt': '___ am a teacher. (I/Me)', 'answer': 'I', 'hint': 'Antes del verbo = sujeto'},
                    {'prompt': 'Call ___ tomorrow. (I/me)', 'answer': 'me', 'hint': 'Después del verbo = objeto'},
                    {'prompt': '___ is my sister. (She/Her)', 'answer': 'She', 'hint': 'Antes del verbo = sujeto'},
                    {'prompt': 'I saw ___ at the party. (they/them)', 'answer': 'them', 'hint': 'Después del verbo = objeto'},
                    {'prompt': 'This is for ___. (he/him)', 'answer': 'him', 'hint': 'Después de preposición = objeto'}
                ]
            }
        ],
        
        'quick_reference': '''
## 👥 Pronombres Sujeto y Objeto

| Sujeto | Objeto |
|--------|--------|
| I | me |
| you | you |
| he | him |
| she | her |
| it | it |
| we | us |
| they | them |

### Regla
- **Antes** del verbo = SUJETO: **I** love you.
- **Después** del verbo = OBJETO: I love **you**.
- **Después** de preposición = OBJETO: for **me**, with **her**
'''
    },
    
    'countable-uncountable': {
        'title': 'Countable & Uncountable Nouns',
        'icon': '🔢',
        'difficulty': 'beginner',
        'estimated_time': '20 min',
        'description': 'Distingue entre sustantivos contables e incontables.',
        
        'theory': {
            'introduction': '''
En inglés, los sustantivos se dividen en:
- **Contables**: Se pueden contar (one apple, two apples)
- **Incontables**: NO se pueden contar (water, information)

Esto afecta qué palabras usar: a/an, some, any, much, many, etc.
''',
            'rules': [
                {
                    'title': '🔢 Sustantivos Contables',
                    'rule': 'Tienen singular y plural, usan a/an, many, few',
                    'formula': 'a/an + singular | many/few + plural',
                    'examples': [
                        {'sentence': 'I have **a** book.', 'note': 'Singular + a/an'},
                        {'sentence': 'There are **many** books.', 'note': 'Plural + many'},
                        {'sentence': 'I have **a few** friends.', 'note': 'Plural + a few'},
                        {'sentence': 'How **many** apples do you want?', 'note': 'Pregunta + many'}
                    ]
                },
                {
                    'title': '💧 Sustantivos Incontables',
                    'rule': 'No tienen plural, usan much, little, some',
                    'formula': 'much/little + incontable (NUNCA a/an)',
                    'examples': [
                        {'sentence': 'I need **some** water.', 'note': 'Nunca: a water'},
                        {'sentence': "There isn't **much** money.", 'note': 'Negativo + much'},
                        {'sentence': 'I have **a little** time.', 'note': 'A little = algo de'},
                        {'sentence': 'How **much** sugar do you need?', 'note': 'Pregunta + much'}
                    ]
                },
                {
                    'title': '📋 Incontables Comunes',
                    'rule': 'Memoriza los más usados',
                    'formula': 'Categorías de incontables',
                    'examples': [
                        {'category': 'Líquidos', 'items': ['water', 'milk', 'coffee', 'tea', 'juice', 'oil']},
                        {'category': 'Comida', 'items': ['bread', 'rice', 'pasta', 'meat', 'cheese', 'butter']},
                        {'category': 'Materiales', 'items': ['wood', 'glass', 'paper', 'gold', 'plastic']},
                        {'category': 'Abstractos', 'items': ['information', 'advice', 'news', 'homework', 'work']},
                        {'category': 'Otros', 'items': ['money', 'furniture', 'luggage', 'weather', 'traffic']}
                    ]
                },
                {
                    'title': '📦 Cómo Contar Incontables',
                    'rule': 'Usa contenedores o medidas',
                    'formula': 'a/an + contenedor + of + incontable',
                    'examples': [
                        {'sentence': '**a glass of** water', 'translation': 'un vaso de agua'},
                        {'sentence': '**a piece of** advice', 'translation': 'un consejo'},
                        {'sentence': '**a slice of** bread', 'translation': 'una rebanada de pan'},
                        {'sentence': '**a cup of** coffee', 'translation': 'una taza de café'},
                        {'sentence': '**a bottle of** milk', 'translation': 'una botella de leche'}
                    ]
                }
            ]
        },
        
        'common_mistakes': [
            {'wrong': 'I need an information.', 'correct': 'I need **(some) information** / **a piece of information**.',
             'explanation': 'INFORMATION es incontable, no usa a/an'},
            {'wrong': 'There are many furnitures.', 'correct': 'There is **much/a lot of furniture**.',
             'explanation': 'FURNITURE es incontable, no tiene plural'},
            {'wrong': 'I have few money.', 'correct': 'I have **little** money.',
             'explanation': 'MONEY es incontable: little (no few)'}
        ],
        
        'tips': [
            {'icon': '🔢', 'title': '¿Se puede contar?', 'content': 'Si puedes decir "one, two, three...", es contable.'},
            {'icon': '📦', 'title': 'Contenedores', 'content': 'Para contar incontables: a glass of, a piece of...'},
            {'icon': '⚠️', 'title': 'NEWS es singular', 'content': 'The news IS good (no ARE). Es incontable.'}
        ],
        
        'exercises': [
            {
                'type': 'fill_blank',
                'instruction': 'Completa con much o many.',
                'questions': [
                    {'prompt': 'How ___ water do you need?', 'answer': 'much', 'hint': 'Water = incontable'},
                    {'prompt': "There aren't ___ students today.", 'answer': 'many', 'hint': 'Students = contable'},
                    {'prompt': "I don't have ___ time.", 'answer': 'much', 'hint': 'Time = incontable'},
                    {'prompt': 'How ___ books did you read?', 'answer': 'many', 'hint': 'Books = contable'},
                    {'prompt': "There isn't ___ traffic today.", 'answer': 'much', 'hint': 'Traffic = incontable'}
                ]
            }
        ],
        
        'quick_reference': '''
## 🔢 Contables vs Incontables

| | Contables | Incontables |
|--|-----------|-------------|
| Singular | a/an | No |
| Plural | -s/-es | No (no plural) |
| Cantidad + | many, a few | much, a little |
| Cantidad - | few | little |
| Pregunta | How many? | How much? |

### Incontables Comunes
water, milk, money, information, advice, news, bread, rice, furniture, luggage, traffic, weather

### Contar Incontables
a glass of water, a piece of information, a slice of bread
'''
    }
}


def get_all_topics():
    """Retorna lista de todos los temas con información básica."""
    return [
        {
            'id': key,
            'title': data['title'],
            'icon': data['icon'],
            'difficulty': data['difficulty'],
            'estimated_time': data['estimated_time'],
            'description': data['description']
        }
        for key, data in STUDY_TOPICS.items()
    ]


def get_topic(topic_id):
    """Retorna el contenido completo de un tema."""
    return STUDY_TOPICS.get(topic_id)


def get_topic_exercises(topic_id):
    """Retorna solo los ejercicios de un tema."""
    topic = STUDY_TOPICS.get(topic_id)
    if topic:
        return topic.get('exercises', [])
    return []


def check_exercise_answer(topic_id, exercise_index, question_index, user_answer):
    """Verifica una respuesta de ejercicio."""
    topic = STUDY_TOPICS.get(topic_id)
    if not topic:
        return {'correct': False, 'message': 'Tema no encontrado'}
    
    exercises = topic.get('exercises', [])
    if exercise_index >= len(exercises):
        return {'correct': False, 'message': 'Ejercicio no encontrado'}
    
    exercise = exercises[exercise_index]
    questions = exercise.get('questions', [])
    if question_index >= len(questions):
        return {'correct': False, 'message': 'Pregunta no encontrada'}
    
    question = questions[question_index]
    correct_answer = question.get('answer', '').lower().strip()
    user_answer = user_answer.lower().strip()
    
    # Manejar respuestas con múltiples partes (ej: "Do...need to")
    correct_parts = correct_answer.replace('...', ' ').replace('  ', ' ').split()
    user_parts = user_answer.replace('...', ' ').replace('  ', ' ').split()
    
    is_correct = correct_answer == user_answer or correct_parts == user_parts
    
    return {
        'correct': is_correct,
        'correct_answer': question.get('answer'),
        'explanation': question.get('explanation', question.get('hint', ''))
    }
