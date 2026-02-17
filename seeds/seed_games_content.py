#!/usr/bin/env python3
"""
Seed para poblar contenido de minijuegos
"""
from app import create_app, db
from app.models import MiniGameContent, QuickQuiz, ReadingComprehension, SpeedTyping, ReadingQuestion
from datetime import datetime

app = create_app()

# ==========================================
# WORD SCRAMBLE - Palabras para desordenar
# ==========================================
word_scramble_data = {
    'A1': [
        {'word': 'apple', 'hint': 'A red or green fruit'},
        {'word': 'house', 'hint': 'Where you live'},
        {'word': 'water', 'hint': 'You drink this'},
        {'word': 'happy', 'hint': 'Feeling good'},
        {'word': 'green', 'hint': 'Color of grass'},
        {'word': 'bread', 'hint': 'Made from flour'},
        {'word': 'chair', 'hint': 'You sit on this'},
        {'word': 'table', 'hint': 'Where you eat'},
        {'word': 'phone', 'hint': 'You call with this'},
        {'word': 'money', 'hint': 'You buy things with this'},
    ],
    'A2': [
        {'word': 'beautiful', 'hint': 'Very pretty'},
        {'word': 'different', 'hint': 'Not the same'},
        {'word': 'important', 'hint': 'Very necessary'},
        {'word': 'sometimes', 'hint': 'Not always'},
        {'word': 'yesterday', 'hint': 'The day before today'},
        {'word': 'breakfast', 'hint': 'Morning meal'},
        {'word': 'afternoon', 'hint': 'After 12pm'},
        {'word': 'together', 'hint': 'With other people'},
        {'word': 'remember', 'hint': 'Not forget'},
        {'word': 'birthday', 'hint': 'Day you were born'},
    ],
    'B1': [
        {'word': 'comfortable', 'hint': 'Feeling relaxed'},
        {'word': 'environment', 'hint': 'Nature around us'},
        {'word': 'opportunity', 'hint': 'A chance to do something'},
        {'word': 'experience', 'hint': 'What you learn by doing'},
        {'word': 'information', 'hint': 'Facts and data'},
        {'word': 'immediately', 'hint': 'Right now'},
        {'word': 'responsibility', 'hint': 'Duty to do something'},
        {'word': 'unfortunately', 'hint': 'Sadly'},
        {'word': 'temperature', 'hint': 'How hot or cold'},
        {'word': 'relationship', 'hint': 'Connection between people'},
    ],
    'B2': [
        {'word': 'approximately', 'hint': 'About, more or less'},
        {'word': 'controversial', 'hint': 'Causing disagreement'},
        {'word': 'sophisticated', 'hint': 'Complex and refined'},
        {'word': 'infrastructure', 'hint': 'Basic systems of a country'},
        {'word': 'simultaneously', 'hint': 'At the same time'},
        {'word': 'phenomenon', 'hint': 'An observable event'},
        {'word': 'consciousness', 'hint': 'State of being aware'},
        {'word': 'entrepreneur', 'hint': 'Business starter'},
        {'word': 'administration', 'hint': 'Management of organization'},
        {'word': 'acknowledgement', 'hint': 'Recognition of something'},
    ],
    'C1': [
        {'word': 'unprecedented', 'hint': 'Never happened before'},
        {'word': 'comprehensive', 'hint': 'Including everything'},
        {'word': 'indispensable', 'hint': 'Absolutely necessary'},
        {'word': 'miscellaneous', 'hint': 'Various, mixed'},
        {'word': 'quintessential', 'hint': 'Perfect example'},
        {'word': 'procrastination', 'hint': 'Delaying things'},
        {'word': 'counterintuitive', 'hint': 'Against common sense'},
        {'word': 'rehabilitation', 'hint': 'Restoring to normal'},
        {'word': 'overwhelmingly', 'hint': 'To a very great degree'},
        {'word': 'notwithstanding', 'hint': 'In spite of'},
    ],
    'C2': [
        {'word': 'idiosyncratic', 'hint': 'Peculiar to individual'},
        {'word': 'serendipitous', 'hint': 'Happy accident'},
        {'word': 'anthropomorphic', 'hint': 'Human-like qualities'},
        {'word': 'disproportionate', 'hint': 'Out of proportion'},
        {'word': 'uncharacteristically', 'hint': 'Not typical behavior'},
        {'word': 'incomprehensible', 'hint': 'Cannot be understood'},
        {'word': 'inconsequential', 'hint': 'Not important'},
        {'word': 'presumptuousness', 'hint': 'Too confident'},
        {'word': 'unprecedentedly', 'hint': 'In a never-seen way'},
        {'word': 'disenfranchisement', 'hint': 'Depriving of rights'},
    ],
}

# ==========================================
# HANGMAN - Palabras para adivinar
# ==========================================
hangman_data = {
    'A1': [
        {'word': 'cat', 'hint': 'A small pet that meows'},
        {'word': 'dog', 'hint': 'A pet that barks'},
        {'word': 'sun', 'hint': 'It shines in the sky'},
        {'word': 'book', 'hint': 'You read this'},
        {'word': 'tree', 'hint': 'It has leaves'},
        {'word': 'fish', 'hint': 'Lives in water'},
        {'word': 'bird', 'hint': 'It can fly'},
        {'word': 'milk', 'hint': 'White drink from cows'},
        {'word': 'ball', 'hint': 'Round toy'},
        {'word': 'door', 'hint': 'You open to enter'},
    ],
    'A2': [
        {'word': 'garden', 'hint': 'Where flowers grow'},
        {'word': 'market', 'hint': 'Where you buy food'},
        {'word': 'doctor', 'hint': 'Helps sick people'},
        {'word': 'camera', 'hint': 'Takes photos'},
        {'word': 'bridge', 'hint': 'Crosses over water'},
        {'word': 'letter', 'hint': 'Written message'},
        {'word': 'ticket', 'hint': 'Needed for train'},
        {'word': 'corner', 'hint': 'Where streets meet'},
        {'word': 'window', 'hint': 'Made of glass'},
        {'word': 'secret', 'hint': 'Not told to others'},
    ],
    'B1': [
        {'word': 'adventure', 'hint': 'Exciting experience'},
        {'word': 'chocolate', 'hint': 'Sweet brown candy'},
        {'word': 'dangerous', 'hint': 'Not safe'},
        {'word': 'celebrate', 'hint': 'Party for occasion'},
        {'word': 'knowledge', 'hint': 'What you learn'},
        {'word': 'expensive', 'hint': 'Costs a lot'},
        {'word': 'fantastic', 'hint': 'Really great'},
        {'word': 'difficult', 'hint': 'Not easy'},
        {'word': 'apartment', 'hint': 'Place to live in building'},
        {'word': 'delicious', 'hint': 'Tastes very good'},
    ],
    'B2': [
        {'word': 'achievement', 'hint': 'Something accomplished'},
        {'word': 'breakthrough', 'hint': 'Important discovery'},
        {'word': 'consequence', 'hint': 'Result of action'},
        {'word': 'distinguish', 'hint': 'Tell apart'},
        {'word': 'enthusiasm', 'hint': 'Strong excitement'},
        {'word': 'fundamental', 'hint': 'Basic and important'},
        {'word': 'hypothesis', 'hint': 'Scientific guess'},
        {'word': 'influential', 'hint': 'Having great effect'},
        {'word': 'magnificent', 'hint': 'Extremely beautiful'},
        {'word': 'perspective', 'hint': 'Point of view'},
    ],
    'C1': [
        {'word': 'accountability', 'hint': 'Being responsible'},
        {'word': 'biodegradable', 'hint': 'Breaks down naturally'},
        {'word': 'collaboration', 'hint': 'Working together'},
        {'word': 'determination', 'hint': 'Strong willpower'},
        {'word': 'entrepreneurship', 'hint': 'Starting businesses'},
        {'word': 'fascination', 'hint': 'Strong interest'},
        {'word': 'globalization', 'hint': 'World becoming connected'},
        {'word': 'humanitarian', 'hint': 'Helping people'},
        {'word': 'implementation', 'hint': 'Putting into action'},
        {'word': 'justification', 'hint': 'Good reason'},
    ],
    'C2': [
        {'word': 'acknowledgement', 'hint': 'Recognition'},
        {'word': 'bureaucratization', 'hint': 'Making more official'},
        {'word': 'counterproductive', 'hint': 'Having opposite effect'},
        {'word': 'disillusionment', 'hint': 'Lost hopes'},
        {'word': 'entrepreneurialism', 'hint': 'Business mindset'},
        {'word': 'fundamentalism', 'hint': 'Strict beliefs'},
        {'word': 'incomprehensibility', 'hint': 'Being impossible to understand'},
        {'word': 'internationalization', 'hint': 'Making worldwide'},
        {'word': 'multidimensional', 'hint': 'Having many aspects'},
        {'word': 'oversimplification', 'hint': 'Making too simple'},
    ],
}

# ==========================================
# MEMORY MATCH - Pares de palabras
# ==========================================
memory_data = {
    'A1': [
        {'pairs': [
            {'english': 'Hello', 'spanish': 'Hola'},
            {'english': 'Goodbye', 'spanish': 'Adiós'},
            {'english': 'Please', 'spanish': 'Por favor'},
            {'english': 'Thank you', 'spanish': 'Gracias'},
            {'english': 'Yes', 'spanish': 'Sí'},
            {'english': 'No', 'spanish': 'No'},
        ]},
        {'pairs': [
            {'english': 'Water', 'spanish': 'Agua'},
            {'english': 'Food', 'spanish': 'Comida'},
            {'english': 'House', 'spanish': 'Casa'},
            {'english': 'Car', 'spanish': 'Carro'},
            {'english': 'Book', 'spanish': 'Libro'},
            {'english': 'Pen', 'spanish': 'Pluma'},
        ]},
        {'pairs': [
            {'english': 'Red', 'spanish': 'Rojo'},
            {'english': 'Blue', 'spanish': 'Azul'},
            {'english': 'Green', 'spanish': 'Verde'},
            {'english': 'Yellow', 'spanish': 'Amarillo'},
            {'english': 'White', 'spanish': 'Blanco'},
            {'english': 'Black', 'spanish': 'Negro'},
        ]},
    ],
    'A2': [
        {'pairs': [
            {'english': 'Beautiful', 'spanish': 'Hermoso'},
            {'english': 'Difficult', 'spanish': 'Difícil'},
            {'english': 'Important', 'spanish': 'Importante'},
            {'english': 'Different', 'spanish': 'Diferente'},
            {'english': 'Interesting', 'spanish': 'Interesante'},
            {'english': 'Necessary', 'spanish': 'Necesario'},
        ]},
        {'pairs': [
            {'english': 'Kitchen', 'spanish': 'Cocina'},
            {'english': 'Bedroom', 'spanish': 'Dormitorio'},
            {'english': 'Bathroom', 'spanish': 'Baño'},
            {'english': 'Garden', 'spanish': 'Jardín'},
            {'english': 'Office', 'spanish': 'Oficina'},
            {'english': 'School', 'spanish': 'Escuela'},
        ]},
        {'pairs': [
            {'english': 'Yesterday', 'spanish': 'Ayer'},
            {'english': 'Tomorrow', 'spanish': 'Mañana'},
            {'english': 'Always', 'spanish': 'Siempre'},
            {'english': 'Never', 'spanish': 'Nunca'},
            {'english': 'Sometimes', 'spanish': 'A veces'},
            {'english': 'Often', 'spanish': 'A menudo'},
        ]},
    ],
    'B1': [
        {'pairs': [
            {'english': 'Achievement', 'spanish': 'Logro'},
            {'english': 'Opportunity', 'spanish': 'Oportunidad'},
            {'english': 'Experience', 'spanish': 'Experiencia'},
            {'english': 'Knowledge', 'spanish': 'Conocimiento'},
            {'english': 'Relationship', 'spanish': 'Relación'},
            {'english': 'Responsibility', 'spanish': 'Responsabilidad'},
        ]},
        {'pairs': [
            {'english': 'Meanwhile', 'spanish': 'Mientras tanto'},
            {'english': 'However', 'spanish': 'Sin embargo'},
            {'english': 'Therefore', 'spanish': 'Por lo tanto'},
            {'english': 'Although', 'spanish': 'Aunque'},
            {'english': 'Furthermore', 'spanish': 'Además'},
            {'english': 'Nevertheless', 'spanish': 'No obstante'},
        ]},
    ],
    'B2': [
        {'pairs': [
            {'english': 'Breakthrough', 'spanish': 'Avance'},
            {'english': 'Outcome', 'spanish': 'Resultado'},
            {'english': 'Insight', 'spanish': 'Perspicacia'},
            {'english': 'Drawback', 'spanish': 'Inconveniente'},
            {'english': 'Undertaking', 'spanish': 'Empresa'},
            {'english': 'Endeavor', 'spanish': 'Esfuerzo'},
        ]},
        {'pairs': [
            {'english': 'Allegedly', 'spanish': 'Supuestamente'},
            {'english': 'Presumably', 'spanish': 'Presumiblemente'},
            {'english': 'Apparently', 'spanish': 'Aparentemente'},
            {'english': 'Undoubtedly', 'spanish': 'Indudablemente'},
            {'english': 'Inevitably', 'spanish': 'Inevitablemente'},
            {'english': 'Considerably', 'spanish': 'Considerablemente'},
        ]},
    ],
    'C1': [
        {'pairs': [
            {'english': 'Acquiescence', 'spanish': 'Aquiescencia'},
            {'english': 'Benevolence', 'spanish': 'Benevolencia'},
            {'english': 'Complacency', 'spanish': 'Complacencia'},
            {'english': 'Discrepancy', 'spanish': 'Discrepancia'},
            {'english': 'Eloquence', 'spanish': 'Elocuencia'},
            {'english': 'Flamboyance', 'spanish': 'Extravagancia'},
        ]},
    ],
    'C2': [
        {'pairs': [
            {'english': 'Obsequiousness', 'spanish': 'Servilismo'},
            {'english': 'Pusillanimity', 'spanish': 'Pusilanimidad'},
            {'english': 'Quintessence', 'spanish': 'Quintaesencia'},
            {'english': 'Recalcitrance', 'spanish': 'Obstinación'},
            {'english': 'Sycophancy', 'spanish': 'Adulación'},
            {'english': 'Truculence', 'spanish': 'Truculencia'},
        ]},
    ],
}

# ==========================================
# FILL THE GAPS - Oraciones con huecos
# ==========================================
fill_gaps_data = {
    'A1': [
        {
            'sentence': 'I ___ a student.',
            'answer': 'am',
            'options': ['am', 'is', 'are', 'be'],
            'hint': 'Verb to be with I'
        },
        {
            'sentence': 'She ___ to school every day.',
            'answer': 'goes',
            'options': ['go', 'goes', 'going', 'went'],
            'hint': 'Present simple with she'
        },
        {
            'sentence': 'They ___ playing football.',
            'answer': 'are',
            'options': ['is', 'am', 'are', 'be'],
            'hint': 'Present continuous with they'
        },
        {
            'sentence': 'I have ___ apple.',
            'answer': 'an',
            'options': ['a', 'an', 'the', 'some'],
            'hint': 'Article before vowel'
        },
        {
            'sentence': 'The cat is ___ the table.',
            'answer': 'on',
            'options': ['on', 'in', 'at', 'to'],
            'hint': 'Preposition of place'
        },
    ],
    'A2': [
        {
            'sentence': 'I ___ never been to Paris.',
            'answer': 'have',
            'options': ['have', 'has', 'had', 'having'],
            'hint': 'Present perfect with I'
        },
        {
            'sentence': 'She ___ working when I called.',
            'answer': 'was',
            'options': ['is', 'was', 'were', 'been'],
            'hint': 'Past continuous'
        },
        {
            'sentence': 'If it rains, I ___ stay home.',
            'answer': 'will',
            'options': ['will', 'would', 'can', 'should'],
            'hint': 'First conditional'
        },
        {
            'sentence': 'This is the ___ book I have ever read.',
            'answer': 'best',
            'options': ['good', 'better', 'best', 'most good'],
            'hint': 'Superlative form'
        },
        {
            'sentence': 'He asked me ___ I was from.',
            'answer': 'where',
            'options': ['where', 'what', 'which', 'who'],
            'hint': 'Indirect question'
        },
    ],
    'B1': [
        {
            'sentence': 'By next year, I ___ graduated from university.',
            'answer': 'will have',
            'options': ['will have', 'will be', 'have', 'would have'],
            'hint': 'Future perfect'
        },
        {
            'sentence': 'The movie ___ by Steven Spielberg.',
            'answer': 'was directed',
            'options': ['directed', 'was directed', 'is directing', 'has directed'],
            'hint': 'Passive voice'
        },
        {
            'sentence': 'I wish I ___ more time to study.',
            'answer': 'had',
            'options': ['have', 'had', 'would have', 'having'],
            'hint': 'Wish + past simple'
        },
        {
            'sentence': 'She suggested ___ to the cinema.',
            'answer': 'going',
            'options': ['to go', 'going', 'go', 'went'],
            'hint': 'Verb pattern with suggest'
        },
        {
            'sentence': 'The harder you work, ___ you will succeed.',
            'answer': 'the more',
            'options': ['more', 'the more', 'most', 'the most'],
            'hint': 'Comparative structure'
        },
    ],
    'B2': [
        {
            'sentence': 'Had I known earlier, I ___ you.',
            'answer': 'would have told',
            'options': ['told', 'would tell', 'would have told', 'had told'],
            'hint': 'Third conditional inverted'
        },
        {
            'sentence': 'Not until he arrived ___ the meeting start.',
            'answer': 'did',
            'options': ['did', 'was', 'had', 'could'],
            'hint': 'Inversion after negative adverbial'
        },
        {
            'sentence': 'It is essential that he ___ on time.',
            'answer': 'be',
            'options': ['is', 'be', 'was', 'being'],
            'hint': 'Subjunctive mood'
        },
        {
            'sentence': 'The project, ___ was completed last month, won an award.',
            'answer': 'which',
            'options': ['that', 'which', 'what', 'who'],
            'hint': 'Non-defining relative clause'
        },
        {
            'sentence': '___ the weather, we will go hiking.',
            'answer': 'Regardless of',
            'options': ['Despite of', 'Regardless of', 'Although', 'In spite'],
            'hint': 'Concession connector'
        },
    ],
    'C1': [
        {
            'sentence': 'Scarcely ___ the door when the phone rang.',
            'answer': 'had I opened',
            'options': ['I opened', 'had I opened', 'I had opened', 'did I open'],
            'hint': 'Inversion with scarcely'
        },
        {
            'sentence': '___ he to arrive late, we would start without him.',
            'answer': 'Were',
            'options': ['If', 'Were', 'Should', 'Had'],
            'hint': 'Formal conditional inversion'
        },
        {
            'sentence': 'The proposal was rejected, ___ surprised nobody.',
            'answer': 'which',
            'options': ['that', 'which', 'what', 'it'],
            'hint': 'Relative clause referring to whole sentence'
        },
        {
            'sentence': 'Little ___ that the decision would change everything.',
            'answer': 'did she know',
            'options': ['she knew', 'did she know', 'she did know', 'knew she'],
            'hint': 'Inversion with little'
        },
    ],
    'C2': [
        {
            'sentence': 'So profound ___ his knowledge that he was considered an expert.',
            'answer': 'was',
            'options': ['is', 'was', 'were', 'has been'],
            'hint': 'Inversion with so...that'
        },
        {
            'sentence': '___ it not been for your help, I would have failed.',
            'answer': 'Had',
            'options': ['If', 'Had', 'Were', 'Should'],
            'hint': 'Third conditional inversion'
        },
        {
            'sentence': 'Not only ___ the exam, but she also got the highest score.',
            'answer': 'did she pass',
            'options': ['she passed', 'did she pass', 'passed she', 'she did pass'],
            'hint': 'Inversion with not only'
        },
    ],
}

# ==========================================
# QUICK QUIZ - Preguntas rápidas
# ==========================================
quick_quiz_data = [
    # Grammar
    {'question': 'Which is correct?', 'options': ['He don\'t like coffee', 'He doesn\'t like coffee', 'He not like coffee', 'He no like coffee'], 'correct_answer': 'He doesn\'t like coffee', 'explanation': 'Third person singular uses "doesn\'t" in negative sentences.', 'category': 'grammar', 'difficulty': 'A1'},
    {'question': 'Complete: She ___ to the store yesterday.', 'options': ['go', 'goes', 'went', 'going'], 'correct_answer': 'went', 'explanation': '"Went" is the past tense of "go".', 'category': 'grammar', 'difficulty': 'A1'},
    {'question': 'Which sentence is correct?', 'options': ['I am agree', 'I agree', 'I am agreed', 'I agreeing'], 'correct_answer': 'I agree', 'explanation': 'Agree is a stative verb that doesn\'t use "am" before it.', 'category': 'grammar', 'difficulty': 'A2'},
    {'question': 'Choose the correct option: I have been living here ___ 2010.', 'options': ['for', 'since', 'from', 'at'], 'correct_answer': 'since', 'explanation': '"Since" is used with specific points in time.', 'category': 'grammar', 'difficulty': 'A2'},
    {'question': 'If I ___ rich, I would buy a yacht.', 'options': ['am', 'was', 'were', 'be'], 'correct_answer': 'were', 'explanation': 'In second conditional, we use "were" for all subjects.', 'category': 'grammar', 'difficulty': 'B1'},
    {'question': 'The book ___ by millions of people.', 'options': ['has read', 'has been read', 'have been read', 'was reading'], 'correct_answer': 'has been read', 'explanation': 'Present perfect passive for actions completed with relevance to present.', 'category': 'grammar', 'difficulty': 'B1'},
    {'question': 'Had I known, I ___ differently.', 'options': ['would act', 'would have acted', 'acted', 'will act'], 'correct_answer': 'would have acted', 'explanation': 'Third conditional uses "would have + past participle".', 'category': 'grammar', 'difficulty': 'B2'},
    {'question': 'Rarely ___ such a beautiful sunset.', 'options': ['I have seen', 'have I seen', 'I saw', 'did I saw'], 'correct_answer': 'have I seen', 'explanation': 'Negative adverbs at the beginning require inversion.', 'category': 'grammar', 'difficulty': 'B2'},
    {'question': 'It is imperative that he ___ on time.', 'options': ['arrives', 'arrive', 'arrived', 'arriving'], 'correct_answer': 'arrive', 'explanation': 'Subjunctive mood after "it is imperative that".', 'category': 'grammar', 'difficulty': 'C1'},
    {'question': 'So eloquent ___ her speech that everyone was moved.', 'options': ['is', 'was', 'were', 'been'], 'correct_answer': 'was', 'explanation': 'Inversion with "so + adjective + be" for emphasis.', 'category': 'grammar', 'difficulty': 'C1'},
    
    # Vocabulary
    {'question': 'What does "beautiful" mean?', 'options': ['Ugly', 'Very pretty', 'Fast', 'Slow'], 'correct_answer': 'Very pretty', 'explanation': 'Beautiful means having qualities of beauty, very pretty.', 'category': 'vocabulary', 'difficulty': 'A1'},
    {'question': 'The opposite of "hot" is...', 'options': ['Warm', 'Cold', 'Cool', 'Freezing'], 'correct_answer': 'Cold', 'explanation': 'Cold is the direct opposite of hot.', 'category': 'vocabulary', 'difficulty': 'A1'},
    {'question': 'What is a "colleague"?', 'options': ['A friend', 'A family member', 'A person you work with', 'A neighbor'], 'correct_answer': 'A person you work with', 'explanation': 'A colleague is someone who works with you.', 'category': 'vocabulary', 'difficulty': 'A2'},
    {'question': '"To postpone" means to...', 'options': ['Cancel', 'Delay', 'Start', 'Finish'], 'correct_answer': 'Delay', 'explanation': 'Postpone means to delay or put off to a later time.', 'category': 'vocabulary', 'difficulty': 'A2'},
    {'question': 'What does "resilient" mean?', 'options': ['Weak', 'Able to recover quickly', 'Angry', 'Quiet'], 'correct_answer': 'Able to recover quickly', 'explanation': 'Resilient means able to recover from difficulties.', 'category': 'vocabulary', 'difficulty': 'B1'},
    {'question': '"Ubiquitous" means...', 'options': ['Rare', 'Expensive', 'Found everywhere', 'Invisible'], 'correct_answer': 'Found everywhere', 'explanation': 'Ubiquitous means present, appearing, or found everywhere.', 'category': 'vocabulary', 'difficulty': 'B2'},
    {'question': 'What does "ephemeral" mean?', 'options': ['Lasting forever', 'Lasting a short time', 'Very large', 'Very small'], 'correct_answer': 'Lasting a short time', 'explanation': 'Ephemeral means lasting for a very short time.', 'category': 'vocabulary', 'difficulty': 'C1'},
    {'question': '"Sycophant" refers to...', 'options': ['A flatterer', 'A leader', 'A critic', 'A teacher'], 'correct_answer': 'A flatterer', 'explanation': 'A sycophant is a person who praises powerful people to gain advantage.', 'category': 'vocabulary', 'difficulty': 'C2'},
    
    # Phrasal verbs
    {'question': '"Give up" means...', 'options': ['Start', 'Continue', 'Stop trying', 'Begin'], 'correct_answer': 'Stop trying', 'explanation': 'Give up means to stop making an effort, to surrender.', 'category': 'phrasal_verbs', 'difficulty': 'A2'},
    {'question': '"Look after" means...', 'options': ['Search for', 'Take care of', 'Watch', 'Follow'], 'correct_answer': 'Take care of', 'explanation': 'Look after means to take care of someone or something.', 'category': 'phrasal_verbs', 'difficulty': 'A2'},
    {'question': '"Put up with" means...', 'options': ['Tolerate', 'Enjoy', 'Reject', 'Accept happily'], 'correct_answer': 'Tolerate', 'explanation': 'Put up with means to tolerate or endure something unpleasant.', 'category': 'phrasal_verbs', 'difficulty': 'B1'},
    {'question': '"Come across" means...', 'options': ['Cross a street', 'Find by chance', 'Understand', 'Arrive'], 'correct_answer': 'Find by chance', 'explanation': 'Come across means to find or encounter by chance.', 'category': 'phrasal_verbs', 'difficulty': 'B1'},
    {'question': '"Do away with" means...', 'options': ['Keep', 'Abolish', 'Improve', 'Start'], 'correct_answer': 'Abolish', 'explanation': 'Do away with means to abolish or get rid of something.', 'category': 'phrasal_verbs', 'difficulty': 'B2'},
    {'question': '"Play down" means...', 'options': ['Emphasize', 'Minimize importance', 'Enjoy', 'Compete'], 'correct_answer': 'Minimize importance', 'explanation': 'Play down means to make something seem less important.', 'category': 'phrasal_verbs', 'difficulty': 'B2'},
]

# ==========================================
# READING COMPREHENSION
# ==========================================
reading_data = [
    {
        'title': 'My Daily Routine',
        'content': '''Every day I wake up at 7 o'clock. First, I take a shower and get dressed. Then I have breakfast with my family. I usually eat toast and drink orange juice. After breakfast, I go to school by bus. School starts at 8:30 and finishes at 3:00. After school, I do my homework and play with my friends. I have dinner at 7 o'clock and go to bed at 9:30.''',
        'questions': [
            {'question': 'What time does the person wake up?', 'options': ['6 o\'clock', '7 o\'clock', '8 o\'clock', '9 o\'clock'], 'correct': '7 o\'clock'},
            {'question': 'What does the person eat for breakfast?', 'options': ['Cereal', 'Eggs', 'Toast', 'Pancakes'], 'correct': 'Toast'},
            {'question': 'How does the person go to school?', 'options': ['By car', 'By bus', 'On foot', 'By bicycle'], 'correct': 'By bus'},
            {'question': 'What time does school finish?', 'options': ['2:00', '3:00', '4:00', '5:00'], 'correct': '3:00'},
        ],
        'cefr_level': 'A1',
        'category': 'daily_life'
    },
    {
        'title': 'A Trip to the Beach',
        'content': '''Last summer, my family and I went to the beach for a week. We stayed in a small hotel near the sea. Every morning, we had breakfast at the hotel and then walked to the beach. The water was warm and very blue. I learned to swim better and built sandcastles with my sister. In the evenings, we ate at different restaurants and tried local food. It was a wonderful vacation, and I hope we can go again next year.''',
        'questions': [
            {'question': 'How long did they stay at the beach?', 'options': ['A day', 'A weekend', 'A week', 'A month'], 'correct': 'A week'},
            {'question': 'Where did they stay?', 'options': ['In a tent', 'In a hotel', 'With family', 'In an apartment'], 'correct': 'In a hotel'},
            {'question': 'What did the writer learn to do?', 'options': ['Surf', 'Swim better', 'Build boats', 'Cook'], 'correct': 'Swim better'},
            {'question': 'How was the vacation?', 'options': ['Boring', 'Terrible', 'Wonderful', 'Normal'], 'correct': 'Wonderful'},
        ],
        'cefr_level': 'A2',
        'category': 'travel'
    },
    {
        'title': 'The Importance of Exercise',
        'content': '''Regular physical exercise is essential for maintaining good health. Research has shown that people who exercise regularly have lower risks of developing heart disease, diabetes, and obesity. Exercise also has significant mental health benefits, including reducing stress and anxiety, improving mood, and enhancing cognitive function. Experts recommend at least 150 minutes of moderate aerobic activity per week, along with muscle-strengthening activities twice a week. However, any amount of physical activity is better than none, and even short walks can provide health benefits.''',
        'questions': [
            {'question': 'What health problems can regular exercise help prevent?', 'options': ['Only heart disease', 'Heart disease, diabetes, and obesity', 'Only mental problems', 'Only obesity'], 'correct': 'Heart disease, diabetes, and obesity'},
            {'question': 'How much moderate aerobic activity is recommended per week?', 'options': ['100 minutes', '150 minutes', '200 minutes', '250 minutes'], 'correct': '150 minutes'},
            {'question': 'How often should muscle-strengthening activities be done?', 'options': ['Once a week', 'Twice a week', 'Every day', 'Three times a week'], 'correct': 'Twice a week'},
            {'question': 'According to the text, what is true about physical activity?', 'options': ['Only long workouts help', 'Any amount is better than none', 'Walking has no benefits', 'Only gym exercise counts'], 'correct': 'Any amount is better than none'},
        ],
        'cefr_level': 'B1',
        'category': 'health'
    },
    {
        'title': 'The Digital Revolution in Education',
        'content': '''The integration of technology into education has fundamentally transformed how knowledge is acquired and shared. Traditional classroom settings are increasingly being supplemented—or in some cases replaced—by online learning platforms and digital resources. This shift has democratized access to education, enabling students from remote areas to access high-quality learning materials. However, this transformation has not been without challenges. The digital divide remains a significant barrier, as not all students have equal access to technology and reliable internet connections. Furthermore, concerns about screen time, online safety, and the loss of face-to-face interaction continue to spark debate among educators and parents alike.''',
        'questions': [
            {'question': 'What has technology done to education according to the text?', 'options': ['Made it more expensive', 'Fundamentally transformed it', 'Made it less accessible', 'Had no effect'], 'correct': 'Fundamentally transformed it'},
            {'question': 'What does "democratized access" mean in this context?', 'options': ['Made education free', 'Made education more equal and available', 'Created voting systems', 'Reduced quality'], 'correct': 'Made education more equal and available'},
            {'question': 'What is mentioned as a significant barrier?', 'options': ['Teacher training', 'The digital divide', 'Curriculum design', 'Student motivation'], 'correct': 'The digital divide'},
            {'question': 'What concerns are mentioned about digital education?', 'options': ['Only cost', 'Screen time, online safety, and loss of face-to-face interaction', 'Only technical issues', 'Teacher availability'], 'correct': 'Screen time, online safety, and loss of face-to-face interaction'},
        ],
        'cefr_level': 'B2',
        'category': 'education'
    },
    {
        'title': 'The Paradox of Choice',
        'content': '''In contemporary consumer society, individuals are confronted with an unprecedented array of choices in virtually every aspect of their lives. While conventional wisdom suggests that more options lead to greater satisfaction, psychologist Barry Schwartz argues that this abundance of choice can actually be detrimental to our well-being. His research indicates that when faced with too many alternatives, people often experience decision paralysis, heightened anxiety, and diminished satisfaction with their eventual choices. This phenomenon, dubbed "the paradox of choice," challenges the fundamental assumptions of free-market economics and has profound implications for how businesses present their products and how individuals approach decision-making. Schwartz proposes that limiting options and accepting "good enough" rather than seeking the optimal choice may lead to greater happiness.''',
        'questions': [
            {'question': 'What does Barry Schwartz argue about abundance of choice?', 'options': ['It always increases happiness', 'It can be detrimental to well-being', 'It has no effect', 'It only affects businesses'], 'correct': 'It can be detrimental to well-being'},
            {'question': 'What is "decision paralysis"?', 'options': ['Being unable to make decisions due to too many options', 'A physical condition', 'Making decisions too quickly', 'Ignoring all options'], 'correct': 'Being unable to make decisions due to too many options'},
            {'question': 'What does Schwartz suggest as a solution?', 'options': ['Always seek the best option', 'Accept "good enough" choices', 'Avoid all decisions', 'Let others decide'], 'correct': 'Accept "good enough" choices'},
            {'question': 'What assumptions does this paradox challenge?', 'options': ['Educational theories', 'Free-market economics', 'Scientific methods', 'Political systems'], 'correct': 'Free-market economics'},
        ],
        'cefr_level': 'C1',
        'category': 'psychology'
    },
]

# ==========================================
# SPEED TYPING
# ==========================================
speed_typing_data = [
    # Common phrases
    {'phrase': 'How are you today?', 'translation': '¿Cómo estás hoy?', 'category': 'greetings', 'difficulty': 'easy'},
    {'phrase': 'Nice to meet you.', 'translation': 'Encantado de conocerte.', 'category': 'greetings', 'difficulty': 'easy'},
    {'phrase': 'What time is it?', 'translation': '¿Qué hora es?', 'category': 'common_phrases', 'difficulty': 'easy'},
    {'phrase': 'Where is the bathroom?', 'translation': '¿Dónde está el baño?', 'category': 'common_phrases', 'difficulty': 'easy'},
    {'phrase': 'Can you help me, please?', 'translation': '¿Puedes ayudarme, por favor?', 'category': 'common_phrases', 'difficulty': 'easy'},
    {'phrase': 'I would like a coffee.', 'translation': 'Me gustaría un café.', 'category': 'restaurant', 'difficulty': 'easy'},
    {'phrase': 'The weather is beautiful today.', 'translation': 'El clima está hermoso hoy.', 'category': 'common_phrases', 'difficulty': 'medium'},
    {'phrase': 'I have been studying English for two years.', 'translation': 'He estado estudiando inglés por dos años.', 'category': 'education', 'difficulty': 'medium'},
    {'phrase': 'Could you repeat that, please?', 'translation': '¿Podrías repetir eso, por favor?', 'category': 'polite_phrases', 'difficulty': 'medium'},
    {'phrase': 'I am looking forward to meeting you.', 'translation': 'Espero con ansias conocerte.', 'category': 'business', 'difficulty': 'medium'},
    {'phrase': 'It was a pleasure doing business with you.', 'translation': 'Fue un placer hacer negocios contigo.', 'category': 'business', 'difficulty': 'medium'},
    {'phrase': 'The early bird catches the worm.', 'translation': 'Al que madruga, Dios le ayuda.', 'category': 'idioms', 'difficulty': 'medium'},
    {'phrase': 'Actions speak louder than words.', 'translation': 'Las acciones hablan más que las palabras.', 'category': 'idioms', 'difficulty': 'medium'},
    {'phrase': 'You cannot judge a book by its cover.', 'translation': 'No puedes juzgar un libro por su portada.', 'category': 'idioms', 'difficulty': 'hard'},
    {'phrase': 'Nevertheless, the project was completed on time.', 'translation': 'No obstante, el proyecto se completó a tiempo.', 'category': 'discourse_markers', 'difficulty': 'hard'},
    {'phrase': 'Furthermore, the research indicates significant improvements.', 'translation': 'Además, la investigación indica mejoras significativas.', 'category': 'discourse_markers', 'difficulty': 'hard'},
    {'phrase': 'In spite of the challenges, they succeeded.', 'translation': 'A pesar de los desafíos, tuvieron éxito.', 'category': 'discourse_markers', 'difficulty': 'hard'},
    {'phrase': 'The unprecedented situation required innovative solutions.', 'translation': 'La situación sin precedentes requirió soluciones innovadoras.', 'category': 'business', 'difficulty': 'hard'},
    {'phrase': 'Notwithstanding the difficulties, progress was made.', 'translation': 'No obstante las dificultades, se hizo progreso.', 'category': 'formal', 'difficulty': 'hard'},
    {'phrase': 'The committee unanimously approved the proposal.', 'translation': 'El comité aprobó la propuesta por unanimidad.', 'category': 'formal', 'difficulty': 'hard'},
]


def seed_minigame_content():
    """Seed MiniGameContent table"""
    print("\n=== Seeding MiniGameContent ===")
    
    # Word Scramble
    for level, words in word_scramble_data.items():
        existing = MiniGameContent.query.filter_by(game_type='word_scramble', level=level).first()
        if not existing:
            content = MiniGameContent(
                game_type='word_scramble',
                level=level,
                content_data={'words': words},
                is_active=True
            )
            db.session.add(content)
            print(f"  ✓ Word Scramble {level}: {len(words)} words")
    
    # Hangman
    for level, words in hangman_data.items():
        existing = MiniGameContent.query.filter_by(game_type='hangman', level=level).first()
        if not existing:
            content = MiniGameContent(
                game_type='hangman',
                level=level,
                content_data={'words': words},
                is_active=True
            )
            db.session.add(content)
            print(f"  ✓ Hangman {level}: {len(words)} words")
    
    # Memory Match
    for level, games in memory_data.items():
        for i, game in enumerate(games):
            existing = MiniGameContent.query.filter_by(
                game_type='memory', 
                level=level
            ).count()
            if existing < len(games):
                content = MiniGameContent(
                    game_type='memory',
                    level=level,
                    content_data=game,
                    is_active=True
                )
                db.session.add(content)
        print(f"  ✓ Memory {level}: {len(games)} games")
    
    # Fill Gaps
    for level, sentences in fill_gaps_data.items():
        existing = MiniGameContent.query.filter_by(game_type='fill_gaps', level=level).first()
        if not existing:
            content = MiniGameContent(
                game_type='fill_gaps',
                level=level,
                content_data={'sentences': sentences},
                is_active=True
            )
            db.session.add(content)
            print(f"  ✓ Fill Gaps {level}: {len(sentences)} sentences")
    
    db.session.commit()
    print("MiniGameContent seeding complete!")


def seed_quick_quiz():
    """Seed QuickQuiz table"""
    print("\n=== Seeding QuickQuiz ===")
    count = 0
    for quiz_data in quick_quiz_data:
        existing = QuickQuiz.query.filter_by(
            question=quiz_data['question']
        ).first()
        if not existing:
            # Separar respuesta correcta de las incorrectas
            wrong_answers = [opt for opt in quiz_data['options'] if opt != quiz_data['correct_answer']]
            
            quiz = QuickQuiz(
                question=quiz_data['question'],
                correct_answer=quiz_data['correct_answer'],
                wrong_answers=wrong_answers,
                explanation=quiz_data['explanation'],
                category=quiz_data['category'],
                cefr_level=quiz_data['difficulty'],
                is_active=True
            )
            db.session.add(quiz)
            count += 1
    
    db.session.commit()
    print(f"  ✓ Added {count} new questions")


def seed_reading():
    """Seed ReadingComprehension table"""
    print("\n=== Seeding ReadingComprehension ===")
    count = 0
    for reading_item in reading_data:
        existing = ReadingComprehension.query.filter_by(
            title=reading_item['title']
        ).first()
        if not existing:
            # Calcular conteo de palabras
            word_count = len(reading_item['content'].split())
            reading_time = max(1, word_count // 150)  # ~150 palabras por minuto
            
            reading = ReadingComprehension(
                title=reading_item['title'],
                passage=reading_item['content'],
                cefr_level=reading_item['cefr_level'],
                category=reading_item['category'],
                word_count=word_count,
                reading_time_minutes=reading_time,
                is_active=True
            )
            db.session.add(reading)
            db.session.flush()  # Para obtener el ID
            
            # Agregar preguntas
            for i, q in enumerate(reading_item['questions']):
                wrong_answers = [opt for opt in q['options'] if opt != q['correct']]
                question = ReadingQuestion(
                    reading_id=reading.id,
                    question=q['question'],
                    question_type='multiple_choice',
                    correct_answer=q['correct'],
                    wrong_answers=wrong_answers,
                    question_order=i + 1
                )
                db.session.add(question)
            
            count += 1
    
    db.session.commit()
    print(f"  ✓ Added {count} new readings with questions")


def seed_speed_typing():
    """Seed SpeedTyping table"""
    print("\n=== Seeding SpeedTyping ===")
    count = 0
    for typing_item in speed_typing_data:
        existing = SpeedTyping.query.filter_by(
            phrase=typing_item['phrase']
        ).first()
        if not existing:
            typing = SpeedTyping(
                phrase=typing_item['phrase'],
                meaning=typing_item['translation'],
                category=typing_item['category'],
                difficulty=typing_item['difficulty'],
                is_active=True
            )
            db.session.add(typing)
            count += 1
    
    db.session.commit()
    print(f"  ✓ Added {count} new phrases")


def main():
    with app.app_context():
        print("="*50)
        print("SEEDING GAMES CONTENT")
        print("="*50)
        
        seed_minigame_content()
        seed_quick_quiz()
        seed_reading()
        seed_speed_typing()
        
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        print(f"MiniGameContent: {MiniGameContent.query.count()} total")
        print(f"QuickQuiz: {QuickQuiz.query.count()} total")
        print(f"ReadingComprehension: {ReadingComprehension.query.count()} total")
        print(f"SpeedTyping: {SpeedTyping.query.count()} total")
        print("\n✅ Games content seeding complete!")


if __name__ == '__main__':
    main()
