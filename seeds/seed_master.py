"""
Script maestro para completar todo el contenido faltante
=========================================================
- Quizzes con preguntas por unidad
- Mensajes motivacionales
- Más explicaciones de unidad
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Unit, Quiz, QuizQuestion, QuizOption, MotivationalMessage, UnitExplanation
import random

app = create_app()

# ============================================================================
# QUIZZES POR NIVEL
# ============================================================================

def get_level(unit_num):
    if unit_num <= 12: return 'A1'
    elif unit_num <= 24: return 'A2'
    elif unit_num <= 36: return 'B1'
    elif unit_num <= 48: return 'B2'
    elif unit_num <= 60: return 'C1'
    else: return 'C2'

QUIZ_QUESTIONS_BY_LEVEL = {
    'A1': [
        # Verb TO BE
        {'question': 'She ___ a teacher.', 'correct': 'is', 'options': ['am', 'is', 'are', 'be']},
        {'question': 'They ___ from Spain.', 'correct': 'are', 'options': ['is', 'am', 'are', 'be']},
        {'question': 'I ___ 25 years old.', 'correct': 'am', 'options': ['am', 'is', 'are', 'be']},
        {'question': 'The book ___ on the table.', 'correct': 'is', 'options': ['am', 'is', 'are', 'be']},
        {'question': 'We ___ happy today.', 'correct': 'are', 'options': ['am', 'is', 'are', 'be']},
        # Present Simple
        {'question': 'He ___ to work every day.', 'correct': 'goes', 'options': ['go', 'goes', 'going', 'gone']},
        {'question': 'She ___ breakfast at 7 AM.', 'correct': 'has', 'options': ['have', 'has', 'having', 'had']},
        {'question': 'They ___ English very well.', 'correct': 'speak', 'options': ['speaks', 'speak', 'speaking', 'spoke']},
        {'question': 'My father ___ a car.', 'correct': 'drives', 'options': ['drive', 'drives', 'driving', 'drove']},
        {'question': 'The sun ___ in the east.', 'correct': 'rises', 'options': ['rise', 'rises', 'rising', 'rose']},
        # Articles
        {'question': 'I have ___ apple.', 'correct': 'an', 'options': ['a', 'an', 'the', '-']},
        {'question': '___ Eiffel Tower is in Paris.', 'correct': 'The', 'options': ['A', 'An', 'The', '-']},
        {'question': 'She is ___ doctor.', 'correct': 'a', 'options': ['a', 'an', 'the', '-']},
        {'question': 'I love ___ music.', 'correct': '-', 'options': ['a', 'an', 'the', '-']},
        {'question': 'Can you pass me ___ salt?', 'correct': 'the', 'options': ['a', 'an', 'the', '-']},
        # Possessives
        {'question': 'This is ___ book. (I)', 'correct': 'my', 'options': ['my', 'mine', 'me', 'I']},
        {'question': 'Is this pen ___? (you)', 'correct': 'yours', 'options': ['your', 'yours', 'you', "you're"]},
        {'question': 'The dog wagged ___ tail.', 'correct': 'its', 'options': ['it', 'its', "it's", 'his']},
        # Prepositions
        {'question': 'The meeting is ___ Monday.', 'correct': 'on', 'options': ['in', 'on', 'at', 'by']},
        {'question': 'I wake up ___ 7 o\'clock.', 'correct': 'at', 'options': ['in', 'on', 'at', 'by']},
        {'question': 'My birthday is ___ July.', 'correct': 'in', 'options': ['in', 'on', 'at', 'by']},
        {'question': 'The cat is ___ the table.', 'correct': 'under', 'options': ['in', 'on', 'at', 'under']},
        {'question': 'She lives ___ London.', 'correct': 'in', 'options': ['in', 'on', 'at', 'by']},
        # Questions
        {'question': '___ is your name?', 'correct': 'What', 'options': ['What', 'Where', 'When', 'Who']},
        {'question': '___ do you live?', 'correct': 'Where', 'options': ['What', 'Where', 'When', 'Who']},
        {'question': '___ old are you?', 'correct': 'How', 'options': ['What', 'How', 'When', 'Who']},
        {'question': '___ is your birthday?', 'correct': 'When', 'options': ['What', 'Where', 'When', 'Who']},
        {'question': '___ is that man?', 'correct': 'Who', 'options': ['What', 'Where', 'When', 'Who']},
        # Can
        {'question': 'She ___ swim very well.', 'correct': 'can', 'options': ['can', 'cans', 'could', 'is can']},
        {'question': 'I ___ speak three languages.', 'correct': 'can', 'options': ['can', 'am can', 'could', 'do can']},
    ],
    'A2': [
        # Past Simple
        {'question': 'I ___ to Paris last year.', 'correct': 'went', 'options': ['go', 'goes', 'went', 'gone']},
        {'question': 'She ___ a delicious cake yesterday.', 'correct': 'made', 'options': ['make', 'makes', 'made', 'making']},
        {'question': 'They ___ the movie last night.', 'correct': 'watched', 'options': ['watch', 'watches', 'watched', 'watching']},
        {'question': 'He ___ his homework an hour ago.', 'correct': 'finished', 'options': ['finish', 'finishes', 'finished', 'finishing']},
        {'question': 'We ___ a great time at the party.', 'correct': 'had', 'options': ['have', 'has', 'had', 'having']},
        # Past Continuous
        {'question': 'I ___ when you called.', 'correct': 'was sleeping', 'options': ['slept', 'was sleeping', 'am sleeping', 'sleep']},
        {'question': 'They ___ football at 5 PM yesterday.', 'correct': 'were playing', 'options': ['played', 'play', 'were playing', 'are playing']},
        {'question': 'She ___ dinner when the doorbell rang.', 'correct': 'was cooking', 'options': ['cooked', 'cooks', 'was cooking', 'is cooking']},
        # Comparatives
        {'question': 'This book is ___ than that one.', 'correct': 'more interesting', 'options': ['interesting', 'more interesting', 'most interesting', 'interestinger']},
        {'question': 'He is ___ than his brother.', 'correct': 'taller', 'options': ['tall', 'taller', 'tallest', 'more tall']},
        {'question': 'This exercise is ___ than the last one.', 'correct': 'easier', 'options': ['easy', 'easier', 'easiest', 'more easy']},
        {'question': 'Gold is ___ than silver.', 'correct': 'more expensive', 'options': ['expensive', 'more expensive', 'most expensive', 'expensiver']},
        # Superlatives
        {'question': 'She is the ___ student in the class.', 'correct': 'smartest', 'options': ['smart', 'smarter', 'smartest', 'most smart']},
        {'question': 'This is the ___ movie I have ever seen.', 'correct': 'best', 'options': ['good', 'better', 'best', 'most good']},
        {'question': 'Mount Everest is the ___ mountain.', 'correct': 'highest', 'options': ['high', 'higher', 'highest', 'most high']},
        # Future
        {'question': 'I ___ help you tomorrow.', 'correct': 'will', 'options': ['will', 'going', 'am', 'do']},
        {'question': 'She ___ going to study medicine.', 'correct': 'is', 'options': ['will', 'is', 'are', 'going']},
        {'question': 'They ___ arrive at 8 PM.', 'correct': 'will', 'options': ['will', 'are', 'going', 'is']},
        # Modal Verbs
        {'question': 'You ___ smoke here. It\'s prohibited.', 'correct': "mustn't", 'options': ['must', "mustn't", 'should', "shouldn't"]},
        {'question': 'You ___ see a doctor. You look sick.', 'correct': 'should', 'options': ['must', "mustn't", 'should', "shouldn't"]},
        {'question': '___ I use your phone?', 'correct': 'May', 'options': ['May', 'Must', 'Will', 'Should']},
        # Some/Any
        {'question': 'Is there ___ milk in the fridge?', 'correct': 'any', 'options': ['some', 'any', 'no', 'a']},
        {'question': 'I have ___ friends in New York.', 'correct': 'some', 'options': ['some', 'any', 'no', 'a']},
        {'question': 'There isn\'t ___ sugar left.', 'correct': 'any', 'options': ['some', 'any', 'no', 'a']},
        # Too/Enough
        {'question': 'This coffee is ___ hot to drink.', 'correct': 'too', 'options': ['too', 'enough', 'very', 'so']},
        {'question': 'He is old ___ to drive.', 'correct': 'enough', 'options': ['too', 'enough', 'very', 'so']},
        {'question': 'The box is ___ heavy for me.', 'correct': 'too', 'options': ['too', 'enough', 'very', 'such']},
    ],
    'B1': [
        # Present Perfect
        {'question': 'I ___ never been to Japan.', 'correct': 'have', 'options': ['have', 'has', 'had', 'am']},
        {'question': 'She ___ already finished her homework.', 'correct': 'has', 'options': ['have', 'has', 'had', 'is']},
        {'question': 'They ___ lived here for 10 years.', 'correct': 'have', 'options': ['have', 'has', 'had', 'are']},
        {'question': 'I ___ just eaten lunch.', 'correct': 'have', 'options': ['have', 'has', 'had', 'am']},
        {'question': 'He ___ been working here since 2010.', 'correct': 'has', 'options': ['have', 'has', 'had', 'is']},
        # Present Perfect Continuous
        {'question': 'I ___ been waiting for an hour.', 'correct': 'have', 'options': ['have', 'has', 'had', 'am']},
        {'question': 'She ___ been studying all day.', 'correct': 'has', 'options': ['have', 'has', 'had', 'is']},
        {'question': 'They ___ been living here since May.', 'correct': 'have', 'options': ['have', 'has', 'had', 'are']},
        # First Conditional
        {'question': 'If it ___, I will stay home.', 'correct': 'rains', 'options': ['rains', 'will rain', 'rained', 'rain']},
        {'question': 'If you study hard, you ___ pass.', 'correct': 'will', 'options': ['will', 'would', 'can', 'should']},
        {'question': 'I ___ call you if I need help.', 'correct': 'will', 'options': ['will', 'would', 'am', 'do']},
        # Second Conditional
        {'question': 'If I ___ rich, I would travel the world.', 'correct': 'were', 'options': ['am', 'was', 'were', 'be']},
        {'question': 'If she studied more, she ___ get better grades.', 'correct': 'would', 'options': ['will', 'would', 'can', 'should']},
        {'question': 'I would help you if I ___ more time.', 'correct': 'had', 'options': ['have', 'has', 'had', 'having']},
        # Relative Clauses
        {'question': 'The woman ___ lives next door is a doctor.', 'correct': 'who', 'options': ['who', 'which', 'whose', 'whom']},
        {'question': 'The book ___ I bought is interesting.', 'correct': 'which/that', 'options': ['who', 'which/that', 'whose', 'whom']},
        {'question': 'The man ___ car was stolen called the police.', 'correct': 'whose', 'options': ['who', 'which', 'whose', 'whom']},
        # Passive Voice
        {'question': 'The letter ___ written by my brother.', 'correct': 'was', 'options': ['is', 'was', 'were', 'be']},
        {'question': 'English ___ spoken in many countries.', 'correct': 'is', 'options': ['is', 'was', 'were', 'be']},
        {'question': 'The windows ___ cleaned every week.', 'correct': 'are', 'options': ['is', 'are', 'was', 'be']},
        # Reported Speech
        {'question': 'She said she ___ tired.', 'correct': 'was', 'options': ['is', 'was', 'will be', 'be']},
        {'question': 'He told me he ___ come.', 'correct': 'would', 'options': ['will', 'would', 'can', 'should']},
        {'question': 'They said they ___ seen the movie.', 'correct': 'had', 'options': ['have', 'has', 'had', 'having']},
        # Used to
        {'question': 'I ___ to play football when I was young.', 'correct': 'used', 'options': ['use', 'used', 'using', 'uses']},
        {'question': 'She didn\'t ___ to like vegetables.', 'correct': 'use', 'options': ['use', 'used', 'using', 'uses']},
        {'question': 'We ___ to live in a small town.', 'correct': 'used', 'options': ['use', 'used', 'using', 'uses']},
        # Gerunds and Infinitives
        {'question': 'I enjoy ___ books.', 'correct': 'reading', 'options': ['read', 'reading', 'to read', 'reads']},
        {'question': 'She wants ___ a doctor.', 'correct': 'to be', 'options': ['be', 'being', 'to be', 'been']},
        {'question': 'He stopped ___ when he was 30.', 'correct': 'smoking', 'options': ['smoke', 'smoking', 'to smoke', 'smokes']},
    ],
    'B2': [
        # Third Conditional
        {'question': 'If I had known, I ___ have told you.', 'correct': 'would', 'options': ['will', 'would', 'could', 'should']},
        {'question': 'If she ___ studied, she would have passed.', 'correct': 'had', 'options': ['has', 'have', 'had', 'having']},
        {'question': 'He wouldn\'t have been late if he ___ earlier.', 'correct': 'had left', 'options': ['left', 'leaves', 'had left', 'has left']},
        # Mixed Conditionals
        {'question': 'If I ___ you, I would have accepted.', 'correct': 'were', 'options': ['am', 'was', 'were', 'be']},
        {'question': 'If he had studied medicine, he ___ a doctor now.', 'correct': 'would be', 'options': ['is', 'was', 'would be', 'will be']},
        # Future Perfect
        {'question': 'By next year, I ___ finished my degree.', 'correct': 'will have', 'options': ['will', 'will have', 'would', 'have']},
        {'question': 'She ___ have completed the project by Friday.', 'correct': 'will', 'options': ['will', 'would', 'has', 'had']},
        # Future Continuous
        {'question': 'This time tomorrow, I ___ be flying to Paris.', 'correct': 'will', 'options': ['will', 'would', 'am', 'should']},
        {'question': 'They ___ be waiting for you at the airport.', 'correct': 'will', 'options': ['will', 'would', 'are', 'should']},
        # Wish
        {'question': 'I wish I ___ more money.', 'correct': 'had', 'options': ['have', 'has', 'had', 'having']},
        {'question': 'I wish I ___ spoken to her.', 'correct': 'had', 'options': ['have', 'has', 'had', 'would']},
        {'question': 'She wishes she ___ taller.', 'correct': 'were', 'options': ['is', 'was', 'were', 'be']},
        # Inversion
        {'question': 'Not only ___ she smart, but also hardworking.', 'correct': 'is', 'options': ['is', 'was', 'does', 'did']},
        {'question': 'Never ___ I seen such a beautiful sunset.', 'correct': 'have', 'options': ['have', 'has', 'had', 'do']},
        {'question': 'Rarely ___ he go to parties.', 'correct': 'does', 'options': ['do', 'does', 'did', 'is']},
        # Causative
        {'question': 'I need to ___ my car repaired.', 'correct': 'get/have', 'options': ['do', 'make', 'get/have', 'let']},
        {'question': 'She ___ her hair cut yesterday.', 'correct': 'had', 'options': ['did', 'made', 'had', 'got']},
        {'question': 'We ___ the house painted last month.', 'correct': 'had', 'options': ['did', 'made', 'had', 'got']},
        # Narrative Tenses
        {'question': 'I ___ sleeping when the phone rang.', 'correct': 'was', 'options': ['am', 'was', 'were', 'had been']},
        {'question': 'She realized she ___ forgotten her keys.', 'correct': 'had', 'options': ['has', 'have', 'had', 'was']},
        # Advanced Passive
        {'question': 'The project is said ___ very expensive.', 'correct': 'to be', 'options': ['be', 'being', 'to be', 'been']},
        {'question': 'He is believed ___ left the country.', 'correct': 'to have', 'options': ['to', 'have', 'to have', 'having']},
        # Modal Perfect
        {'question': 'You ___ have told me earlier!', 'correct': 'should', 'options': ['must', 'should', 'would', 'can']},
        {'question': 'She ___ have missed the train.', 'correct': 'might', 'options': ['might', 'must', 'should', 'would']},
        {'question': 'He ___ have been at the party. I saw him.', 'correct': 'must', 'options': ['might', 'must', 'should', 'would']},
    ],
    'C1': [
        # Advanced Conditionals
        {'question': 'Were it not ___ your help, I would have failed.', 'correct': 'for', 'options': ['to', 'for', 'by', 'with']},
        {'question': 'Had I known, I ___ never have agreed.', 'correct': 'would', 'options': ['will', 'would', 'could', 'should']},
        {'question': '___ he to arrive, please let me know.', 'correct': 'Were', 'options': ['If', 'Were', 'Should', 'Had']},
        # Subjunctive
        {'question': 'It is essential that he ___ on time.', 'correct': 'be', 'options': ['is', 'be', 'was', 'were']},
        {'question': 'I suggest that she ___ a doctor.', 'correct': 'see', 'options': ['sees', 'see', 'saw', 'seen']},
        {'question': 'It is vital that everyone ___ aware.', 'correct': 'be', 'options': ['is', 'be', 'are', 'being']},
        # Participle Clauses
        {'question': '___ the news, she started crying.', 'correct': 'Having heard', 'options': ['Hear', 'Heard', 'Having heard', 'Hearing']},
        {'question': '___ carefully, the instructions are clear.', 'correct': 'Read', 'options': ['Reading', 'Read', 'Having read', 'To read']},
        {'question': '___ a millionaire, he lives simply.', 'correct': 'Despite being', 'options': ['Despite', 'Although', 'Despite being', 'Being']},
        # Cleft Sentences
        {'question': 'It ___ John who broke the window.', 'correct': 'was', 'options': ['is', 'was', 'were', 'being']},
        {'question': 'What I need ___ a vacation.', 'correct': 'is', 'options': ['is', 'are', 'was', 'were']},
        {'question': 'It is the quality that ___.', 'correct': 'matters', 'options': ['matter', 'matters', 'mattering', 'mattered']},
        # Advanced Modals
        {'question': 'He ___ to have left already.', 'correct': 'seems', 'options': ['seem', 'seems', 'seemed', 'seeming']},
        {'question': 'She ___ be at least 40.', 'correct': 'must', 'options': ['must', 'can', 'should', 'would']},
        {'question': 'This ___ not be right.', 'correct': 'cannot', 'options': ["can't", 'cannot', "mustn't", "shouldn't"]},
        # Discourse Markers
        {'question': '___ that, we should consider other factors.', 'correct': 'Having said', 'options': ['Say', 'Said', 'Having said', 'Saying']},
        {'question': 'The results were, ___, inconclusive.', 'correct': 'nevertheless', 'options': ['however', 'nevertheless', 'therefore', 'moreover']},
        # Emphasis
        {'question': 'Little ___ he know what awaited him.', 'correct': 'did', 'options': ['do', 'did', 'does', 'was']},
        {'question': 'Only then ___ I understand.', 'correct': 'did', 'options': ['do', 'did', 'does', 'had']},
        {'question': 'So important ___ this that we must act now.', 'correct': 'is', 'options': ['is', 'was', 'were', 'be']},
    ],
    'C2': [
        # Advanced Inversion
        {'question': 'At no time ___ I suggest such a thing.', 'correct': 'did', 'options': ['do', 'did', 'have', 'had']},
        {'question': 'Under no circumstances ___ you to leave.', 'correct': 'are', 'options': ['are', 'were', 'do', 'should']},
        {'question': 'Not until later ___ I realize my mistake.', 'correct': 'did', 'options': ['do', 'did', 'have', 'had']},
        # Subtle Modality
        {'question': 'He ___ well be the right candidate.', 'correct': 'might', 'options': ['can', 'might', 'must', 'should']},
        {'question': 'You ___ as well go home.', 'correct': 'might', 'options': ['can', 'might', 'must', 'should']},
        {'question': 'She ___ sooner die than betray her friends.', 'correct': 'would', 'options': ['will', 'would', 'should', 'could']},
        # Complex Passives
        {'question': 'The matter is being ___ into.', 'correct': 'looked', 'options': ['look', 'looked', 'looking', 'looks']},
        {'question': 'The house appears to have been ___ into.', 'correct': 'broken', 'options': ['break', 'broke', 'broken', 'breaking']},
        # Ellipsis
        {'question': "I haven't finished, but I should ___.", 'correct': 'have', 'options': ['do', 'be', 'have', 'done']},
        {'question': "She won't help and I don't expect ___ to.", 'correct': 'her', 'options': ['she', 'her', 'it', 'so']},
        # Substitution
        {'question': 'I wanted to buy a car and I did ___', 'correct': 'so', 'options': ['it', 'that', 'so', 'too']},
        {'question': 'She asked me to wait and I did ___', 'correct': 'so', 'options': ['it', 'that', 'so', 'one']},
        # Concessive Clauses
        {'question': '___ as it may, we must proceed.', 'correct': 'Be', 'options': ['Be', 'Being', 'Been', 'Is']},
        {'question': 'Try ___ he might, he couldn\'t succeed.', 'correct': 'as', 'options': ['as', 'that', 'which', 'what']},
        # Hedging
        {'question': 'It would ___ that he has resigned.', 'correct': 'appear', 'options': ['seem', 'appear', 'look', 'sound']},
        {'question': 'The evidence ___ suggest otherwise.', 'correct': 'would', 'options': ['will', 'would', 'should', 'could']},
        # Register Shifts
        {'question': 'The aforementioned ___ shall be null and void.', 'correct': 'agreement', 'options': ['deal', 'agreement', 'contract', 'promise']},
        {'question': 'Hitherto, no one ___ succeeded.', 'correct': 'has', 'options': ['have', 'has', 'had', 'having']},
    ]
}


def seed_quizzes():
    """Crear quizzes con preguntas para cada unidad"""
    print("\n📝 Creando Quizzes...")
    
    units = Unit.query.order_by(Unit.unit_number).all()
    quizzes_created = 0
    questions_created = 0
    
    for unit in units:
        level = get_level(unit.unit_number)
        
        # Verificar si ya existe un quiz para esta unidad
        existing_quiz = Quiz.query.filter_by(unit_id=unit.id).first()
        if existing_quiz:
            continue
        
        # Crear el quiz
        quiz = Quiz(
            unit_id=unit.id,
            title=f"Quiz - {unit.title}",
            description=f"Test your knowledge of {unit.title.split(':')[-1].strip()}"
        )
        db.session.add(quiz)
        db.session.flush()
        quizzes_created += 1
        
        # Obtener preguntas del nivel
        level_questions = QUIZ_QUESTIONS_BY_LEVEL.get(level, QUIZ_QUESTIONS_BY_LEVEL['A1'])
        
        # Seleccionar 10 preguntas aleatorias
        selected_questions = random.sample(level_questions, min(10, len(level_questions)))
        
        for i, q_data in enumerate(selected_questions):
            question = QuizQuestion(
                quiz_id=quiz.id,
                prompt=q_data['question'],
                order=i + 1
            )
            db.session.add(question)
            db.session.flush()
            
            # Agregar opciones para la pregunta
            for j, option_text in enumerate(q_data['options']):
                is_correct = (option_text == q_data['correct'])
                option = QuizOption(
                    question_id=question.id,
                    text=option_text,
                    is_correct=is_correct,
                    order=j + 1
                )
                db.session.add(option)
            
            questions_created += 1
    
    db.session.commit()
    print(f"   ✅ {quizzes_created} quizzes creados")
    print(f"   ✅ {questions_created} preguntas creadas")
    return quizzes_created, questions_created


# ============================================================================
# MENSAJES MOTIVACIONALES
# ============================================================================

MOTIVATIONAL_MESSAGES = [
    # Mindset
    {'title': 'Growth Mindset', 'content': 'Every mistake is a learning opportunity. The more you practice, the better you become!', 'icon': '🌱'},
    {'title': 'Persistence', 'content': 'Success is not final, failure is not fatal: it is the courage to continue that counts.', 'icon': '💪'},
    {'title': 'Progress', 'content': 'You don\'t have to be perfect, you just have to be better than yesterday.', 'icon': '📈'},
    {'title': 'Consistency', 'content': 'Small daily improvements lead to stunning results. Keep going!', 'icon': '⭐'},
    {'title': 'Belief', 'content': 'Believe you can and you\'re halfway there.', 'icon': '✨'},
    
    # Learning specific
    {'title': 'Language Learning', 'content': 'Every word you learn is a bridge to new connections and opportunities.', 'icon': '🌍'},
    {'title': 'Practice', 'content': 'The more you use English, the more natural it becomes. Don\'t be afraid to make mistakes!', 'icon': '🎯'},
    {'title': 'Vocabulary', 'content': 'Learning 5 new words every day means 1,825 new words in a year!', 'icon': '📚'},
    {'title': 'Speaking', 'content': 'Your accent is a sign that you\'re brave enough to learn another language.', 'icon': '🗣️'},
    {'title': 'Listening', 'content': 'Watch movies, listen to podcasts - immersion is the fastest way to learn!', 'icon': '🎧'},
    
    # Encouragement
    {'title': 'You\'ve Got This!', 'content': 'Remember: native speakers were once beginners too!', 'icon': '👊'},
    {'title': 'Keep Going', 'content': 'Fluency is not a destination, it\'s a journey. Enjoy the ride!', 'icon': '🚀'},
    {'title': 'Celebrate', 'content': 'Look how far you\'ve come! Every lesson completed is a victory.', 'icon': '🎉'},
    {'title': 'Patience', 'content': 'Language learning is a marathon, not a sprint. Take your time and enjoy!', 'icon': '🏃'},
    {'title': 'Effort', 'content': 'The effort you put in today builds the skills you\'ll use tomorrow.', 'icon': '💎'},
    
    # Tips
    {'title': 'Study Tip', 'content': 'Studying for 20 minutes every day is better than 2 hours once a week.', 'icon': '💡'},
    {'title': 'Memory Tip', 'content': 'Teach what you learn to someone else - it\'s the best way to remember!', 'icon': '🧠'},
    {'title': 'Fun Tip', 'content': 'Change your phone language to English for constant practice!', 'icon': '📱'},
    {'title': 'Reading Tip', 'content': 'Reading English books, even children\'s books, builds vocabulary naturally.', 'icon': '📖'},
    {'title': 'Music Tip', 'content': 'Listen to English songs and look up the lyrics. It\'s fun and educational!', 'icon': '🎵'},
    
    # Streak motivation
    {'title': 'Streak Power', 'content': 'Keep your streak alive! Consistency builds habits, and habits build fluency.', 'icon': '🔥'},
    {'title': 'Daily Goal', 'content': 'Just 10 minutes of practice today keeps your skills sharp!', 'icon': '⏰'},
    {'title': 'Commitment', 'content': 'You\'re here, you\'re learning, you\'re growing. That\'s what matters!', 'icon': '🌟'},
]


def seed_motivational_messages():
    """Crear mensajes motivacionales"""
    print("\n💬 Creando mensajes motivacionales...")
    
    # Verificar si la tabla existe
    try:
        existing = MotivationalMessage.query.count()
        if existing >= len(MOTIVATIONAL_MESSAGES):
            print(f"   ⚠️ Ya existen {existing} mensajes")
            return 0
    except Exception as e:
        print(f"   ❌ Tabla no existe o error: {e}")
        return 0
    
    created = 0
    for i, msg in enumerate(MOTIVATIONAL_MESSAGES):
        if not MotivationalMessage.query.filter_by(title=msg['title']).first():
            message = MotivationalMessage(
                title=msg['title'],
                content=msg['content'],
                icon=msg['icon'],
                order=i + 1,
                is_active=True
            )
            db.session.add(message)
            created += 1
    
    db.session.commit()
    print(f"   ✅ {created} mensajes creados")
    return created


# ============================================================================
# EXPLICACIONES DE UNIDAD ADICIONALES
# ============================================================================

UNIT_EXPLANATIONS = {
    'A1': [
        {
            'title': 'Welcome to A1!',
            'content': '''Welcome to your English learning journey! At the A1 level, you're taking your first steps.

**What you'll learn:**
- Basic greetings and introductions
- Numbers, colors, and everyday vocabulary  
- Simple present tense
- How to talk about yourself and your family

**Tips for success:**
- Practice every day, even if just for 10 minutes
- Don't be afraid to make mistakes - they help you learn!
- Listen to simple English songs and videos
- Label objects in your home with their English names'''
        }
    ],
    'A2': [
        {
            'title': 'Moving to A2!',
            'content': '''Congratulations on reaching A2! You can now handle basic conversations.

**What you'll learn:**
- Past tense - talking about what happened
- Future plans and intentions
- Comparisons and descriptions
- More complex questions and answers

**Tips for this level:**
- Start reading simple graded readers
- Watch English shows with subtitles
- Keep a vocabulary journal
- Practice speaking with a partner or tutor'''
        }
    ],
    'B1': [
        {
            'title': 'Welcome to Intermediate!',
            'content': '''You've reached B1 - the intermediate level! You can now communicate in most everyday situations.

**What you'll learn:**
- Present perfect and its uses
- Conditional sentences
- Passive voice
- Relative clauses

**Tips for this level:**
- Read news articles and blog posts in English
- Listen to podcasts on topics you enjoy
- Start writing in English regularly
- Have conversations about abstract topics'''
        }
    ],
    'B2': [
        {
            'title': 'Upper Intermediate Achievement!',
            'content': '''Welcome to B2! You're becoming an independent user of English.

**What you'll learn:**
- Complex conditionals
- Advanced passive structures
- Formal and informal register
- Nuanced expression of opinions

**Tips for this level:**
- Read authentic materials (news, novels, articles)
- Watch movies without subtitles
- Engage in debates and discussions
- Write essays and formal letters'''
        }
    ],
    'C1': [
        {
            'title': 'Advanced Level!',
            'content': '''You've reached C1 - Advanced level! You can express yourself fluently and spontaneously.

**What you'll learn:**
- Subtle distinctions in meaning
- Idiomatic and colloquial expressions
- Academic and professional language
- Complex grammatical structures

**Tips for this level:**
- Read literature and academic texts
- Participate in professional discussions
- Write reports and analytical essays
- Focus on precision and nuance'''
        }
    ],
    'C2': [
        {
            'title': 'Mastery Level!',
            'content': '''Welcome to C2 - Near-native proficiency! You can understand virtually everything.

**What you'll learn:**
- Subtle stylistic differences
- Rare grammatical structures
- Cultural and literary references
- Native-like precision

**Tips for this level:**
- Read classic literature and poetry
- Analyze rhetorical techniques
- Practice simultaneous interpreting
- Focus on perfect accuracy and style'''
        }
    ]
}


def seed_unit_explanations():
    """Crear explicaciones de unidad para todos los niveles"""
    print("\n📘 Creando explicaciones de unidad...")
    
    units = Unit.query.order_by(Unit.unit_number).all()
    created = 0
    
    for unit in units:
        level = get_level(unit.unit_number)
        
        # Verificar si ya existe
        existing = UnitExplanation.query.filter_by(unit_id=unit.id).count()
        if existing >= 2:
            continue
        
        explanations = UNIT_EXPLANATIONS.get(level, UNIT_EXPLANATIONS['A1'])
        
        for exp in explanations:
            if not UnitExplanation.query.filter_by(unit_id=unit.id, section_title=exp['title']).first():
                explanation = UnitExplanation(
                    unit_id=unit.id,
                    section_title=exp['title'],
                    content=exp['content'],
                    order=existing + 1
                )
                db.session.add(explanation)
                created += 1
    
    db.session.commit()
    print(f"   ✅ {created} explicaciones creadas")
    return created


# ============================================================================
# MAIN
# ============================================================================

def main():
    with app.app_context():
        print("=" * 80)
        print("🚀 SCRIPT MAESTRO DE SEED - COMPLETANDO TODO EL SISTEMA")
        print("=" * 80)
        
        # 1. Quizzes
        q, qp = seed_quizzes()
        
        # 2. Mensajes motivacionales
        m = seed_motivational_messages()
        
        # 3. Explicaciones de unidad
        e = seed_unit_explanations()
        
        print("\n" + "=" * 80)
        print("✅ RESUMEN")
        print("=" * 80)
        print(f"📝 Quizzes: {q}")
        print(f"❓ Preguntas quiz: {qp}")
        print(f"💬 Mensajes motivacionales: {m}")
        print(f"📘 Explicaciones de unidad: {e}")
        
        # Verificación final
        print("\n" + "=" * 80)
        print("📊 ESTADO FINAL DEL SISTEMA")
        print("=" * 80)
        
        from app.models import (Reading, GrammarRule, VocabularyItem, 
                               Flashcard, SentenceExercise, WritingPractice,
                               Badge, UnitChallenge, ChallengeQuestion)
        
        stats = [
            ('Unidades', Unit.query.count()),
            ('Lecturas', Reading.query.count()),
            ('Reglas Gramática', GrammarRule.query.count()),
            ('Vocabulario', VocabularyItem.query.count()),
            ('Flashcards', Flashcard.query.count()),
            ('Ejercicios', SentenceExercise.query.count()),
            ('Quizzes', Quiz.query.count()),
            ('Preguntas Quiz', QuizQuestion.query.count()),
            ('Prácticas Escritura', WritingPractice.query.count()),
            ('Badges', Badge.query.count()),
            ('Explicaciones', UnitExplanation.query.count()),
            ('Challenges', UnitChallenge.query.count()),
            ('Preguntas Challenge', ChallengeQuestion.query.count()),
        ]
        
        for name, count in stats:
            status = '✅' if count > 0 else '⚠️'
            print(f'{status} {name}: {count}')


if __name__ == '__main__':
    main()
