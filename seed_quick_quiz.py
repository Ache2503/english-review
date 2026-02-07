#!/usr/bin/env python3
"""
Seed de Quick Quiz - Preguntas rápidas para practicar
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import QuickQuiz

app = create_app()

QUIZ_QUESTIONS = [
    # A1 Level - Vocabulary
    {
        'question': 'What is the opposite of "hot"?',
        'correct_answer': 'cold',
        'wrong_answers': ['warm', 'cool', 'chilly'],
        'explanation': '"Cold" is the direct opposite of "hot".',
        'category': 'vocabulary',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    {
        'question': 'Which is a color?',
        'correct_answer': 'blue',
        'wrong_answers': ['table', 'happy', 'run'],
        'explanation': '"Blue" is a color. The others are not colors.',
        'category': 'vocabulary',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    {
        'question': 'How many days are there in a week?',
        'correct_answer': 'seven',
        'wrong_answers': ['five', 'ten', 'six'],
        'explanation': 'There are 7 days in a week: Monday to Sunday.',
        'category': 'vocabulary',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    {
        'question': 'What do you use to eat soup?',
        'correct_answer': 'spoon',
        'wrong_answers': ['fork', 'knife', 'plate'],
        'explanation': 'You use a spoon to eat soup.',
        'category': 'vocabulary',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    {
        'question': 'Which animal says "meow"?',
        'correct_answer': 'cat',
        'wrong_answers': ['dog', 'bird', 'cow'],
        'explanation': 'A cat says "meow".',
        'category': 'vocabulary',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    
    # A1 Level - Grammar
    {
        'question': 'Complete: "I ___ from Spain."',
        'correct_answer': 'am',
        'wrong_answers': ['is', 'are', 'be'],
        'explanation': 'With "I", we use "am" (present tense of "to be").',
        'category': 'grammar',
        'cefr_level': 'A1',
        'difficulty': 'easy'
    },
    {
        'question': 'Which is the plural of "child"?',
        'correct_answer': 'children',
        'wrong_answers': ['childs', 'childes', 'childer'],
        'explanation': '"Children" is the irregular plural of "child".',
        'category': 'grammar',
        'cefr_level': 'A1',
        'difficulty': 'medium'
    },
    {
        'question': 'Select the correct sentence:',
        'correct_answer': 'She goes to school every day',
        'wrong_answers': ['She go to school every day', 'She goes to school every days', 'She going to school every day'],
        'explanation': 'With third person singular (she), we add "s" to the verb: goes.',
        'category': 'grammar',
        'cefr_level': 'A1',
        'difficulty': 'medium'
    },
    {
        'question': 'Complete: "This is ___ book."',
        'correct_answer': 'my',
        'wrong_answers': ['me', 'mine', 'I'],
        'explanation': '"My" is a possessive adjective. "Mine" is a possessive pronoun.',
        'category': 'grammar',
        'cefr_level': 'A1',
        'difficulty': 'medium'
    },
    
    # A2 Level - Vocabulary
    {
        'question': 'What does "grateful" mean?',
        'correct_answer': 'thankful',
        'wrong_answers': ['angry', 'sad', 'confused'],
        'explanation': '"Grateful" means feeling or showing thanks.',
        'category': 'vocabulary',
        'cefr_level': 'A2',
        'difficulty': 'medium'
    },
    {
        'question': 'Which word means "to make something"?',
        'correct_answer': 'create',
        'wrong_answers': ['destroy', 'find', 'hide'],
        'explanation': '"Create" means to make something new or original.',
        'category': 'vocabulary',
        'cefr_level': 'A2',
        'difficulty': 'medium'
    },
    {
        'question': 'What is a "recipe"?',
        'correct_answer': 'instructions for cooking',
        'wrong_answers': ['a type of food', 'a kitchen tool', 'a restaurant'],
        'explanation': 'A recipe is a set of instructions for preparing food.',
        'category': 'vocabulary',
        'cefr_level': 'A2',
        'difficulty': 'medium'
    },
    {
        'question': 'Which is a synonym for "happy"?',
        'correct_answer': 'cheerful',
        'wrong_answers': ['sad', 'angry', 'lonely'],
        'explanation': '"Cheerful" is a synonym for happy, meaning feeling joy.',
        'category': 'vocabulary',
        'cefr_level': 'A2',
        'difficulty': 'medium'
    },
    
    # A2 Level - Grammar
    {
        'question': 'Complete: "If I had money, I ___ a car."',
        'correct_answer': 'would buy',
        'wrong_answers': ['buy', 'would have bought', 'buying'],
        'explanation': 'This is a second conditional (if + past, would + infinitive).',
        'category': 'grammar',
        'cefr_level': 'A2',
        'difficulty': 'medium'
    },
    {
        'question': 'Which is correct?',
        'correct_answer': 'I have been studying for 2 hours',
        'wrong_answers': ['I am studying for 2 hours', 'I study for 2 hours', 'I have studied for 2 hours'],
        'explanation': 'Present perfect continuous shows an action that started in the past and continues to now.',
        'category': 'grammar',
        'cefr_level': 'A2',
        'difficulty': 'hard'
    },
    {
        'question': 'Complete: "She would have gone if she ___ time."',
        'correct_answer': 'had had',
        'wrong_answers': ['had', 'would have', 'has'],
        'explanation': 'Third conditional: if + past perfect, would have + past participle.',
        'category': 'grammar',
        'cefr_level': 'A2',
        'difficulty': 'hard'
    },
    
    # B1 Level - Vocabulary
    {
        'question': 'What does "ambition" mean?',
        'correct_answer': 'a strong desire to succeed',
        'wrong_answers': ['fear', 'laziness', 'confusion'],
        'explanation': 'Ambition is a strong desire to be successful.',
        'category': 'vocabulary',
        'cefr_level': 'B1',
        'difficulty': 'medium'
    },
    {
        'question': 'Which word means "to reduce"?',
        'correct_answer': 'diminish',
        'wrong_answers': ['increase', 'expand', 'enhance'],
        'explanation': '"Diminish" means to make or become smaller or less.',
        'category': 'vocabulary',
        'cefr_level': 'B1',
        'difficulty': 'hard'
    },
    {
        'question': 'What does "sustainable" mean?',
        'correct_answer': 'able to be maintained long-term',
        'wrong_answers': ['temporary', 'broken', 'weak'],
        'explanation': '"Sustainable" means able to be maintained or continue indefinitely.',
        'category': 'vocabulary',
        'cefr_level': 'B1',
        'difficulty': 'hard'
    },
    
    # B1 Level - Grammar
    {
        'question': 'Complete: "He got the job despite ___ no experience."',
        'correct_answer': 'having',
        'wrong_answers': ['have', 'has', 'had'],
        'explanation': 'After "despite", we use a gerund (verb + -ing).',
        'category': 'grammar',
        'cefr_level': 'B1',
        'difficulty': 'hard'
    },
    {
        'question': 'Which is correct?',
        'correct_answer': 'By the time you arrive, I will have finished',
        'wrong_answers': ['By the time you arrive, I finish', 'By the time you arrive, I have finished', 'By the time you arrive, I will finish'],
        'explanation': 'Future perfect shows an action that will be complete before a future time.',
        'category': 'grammar',
        'cefr_level': 'B1',
        'difficulty': 'hard'
    },
    
    # B2 Level - Vocabulary
    {
        'question': 'What does "meticulous" mean?',
        'correct_answer': 'very careful and precise',
        'wrong_answers': ['careless', 'lazy', 'fast'],
        'explanation': '"Meticulous" means showing great attention to detail; very careful and precise.',
        'category': 'vocabulary',
        'cefr_level': 'B2',
        'difficulty': 'hard'
    },
    {
        'question': 'Complete the phrase: "A ___ of justice"',
        'correct_answer': 'miscarriage',
        'wrong_answers': ['accident', 'failure', 'error'],
        'explanation': '"A miscarriage of justice" is a legal phrase meaning an unjust verdict or result.',
        'category': 'vocabulary',
        'cefr_level': 'B2',
        'difficulty': 'hard'
    },
]


def seed_quick_quiz():
    """Seed del contenido de Quick Quiz"""
    with app.app_context():
        try:
            print("🎯 CREANDO QUICK QUIZ")
            
            for question_data in QUIZ_QUESTIONS:
                # Verificar si ya existe
                existing = QuickQuiz.query.filter_by(
                    question=question_data['question']
                ).first()
                
                if not existing:
                    quiz = QuickQuiz(
                        question=question_data['question'],
                        correct_answer=question_data['correct_answer'],
                        wrong_answers=question_data['wrong_answers'],
                        explanation=question_data.get('explanation'),
                        category=question_data.get('category'),
                        cefr_level=question_data.get('cefr_level'),
                        difficulty=question_data.get('difficulty'),
                        is_active=True
                    )
                    db.session.add(quiz)
            
            db.session.commit()
            
            # Estadísticas
            total = QuickQuiz.query.count()
            print(f"✅ Quiz creados: {total} preguntas")
            
            # Contar por nivel
            for level in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
                count = QuickQuiz.query.filter_by(cefr_level=level).count()
                if count > 0:
                    print(f"   - {level}: {count} preguntas")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()


if __name__ == '__main__':
    seed_quick_quiz()
