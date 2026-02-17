#!/usr/bin/env python3
"""
Seed de Reading Comprehension - Textos para comprensión lectora
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import ReadingComprehension, ReadingQuestion

app = create_app()

READING_PASSAGES = [
    # A1 Level
    {
        'title': 'My Family',
        'passage': '''My name is John. I am 25 years old. I have a family. My mother is Sarah. She is a teacher. My father is Mike. He is an engineer. I have a sister named Emma. She is 20 years old. Emma is a student. 

We live in London. Our house is big and comfortable. We have a garden. I like to play football in the garden. My mother likes to read books. My father likes to watch films. Emma likes to listen to music.

Every Sunday, we have lunch together. We eat pizza or chicken. My mother cooks very well. We talk about our week. We are a happy family.''',
        'cefr_level': 'A1',
        'category': 'Family',
        'word_count': 150,
        'reading_time_minutes': 3,
        'questions': [
            {
                'question': 'What is John\'s mother\'s name?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Sarah',
                'wrong_answers': ['Emma', 'Mike', 'Lucy']
            },
            {
                'question': 'Where does John\'s family live?',
                'question_type': 'multiple_choice',
                'correct_answer': 'London',
                'wrong_answers': ['Paris', 'Berlin', 'Madrid']
            },
            {
                'question': 'What sport does John like?',
                'question_type': 'multiple_choice',
                'correct_answer': 'football',
                'wrong_answers': ['tennis', 'basketball', 'swimming']
            },
            {
                'question': 'What does John\'s family do every Sunday?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Have lunch together',
                'wrong_answers': ['Go to the cinema', 'Play games', 'Watch TV']
            }
        ]
    },
    
    # A2 Level
    {
        'title': 'A Day at School',
        'passage': '''Lisa is 16 years old. She goes to a secondary school in Manchester. She gets up at 7 o'clock every morning. She has breakfast and then goes to school by bus. It takes 20 minutes.

School starts at 8:30 in the morning. Lisa has 5 lessons every day. Her favorite subjects are English and Science. She likes her English teacher because he is funny and interesting. During lunch, Lisa sits with her friends. They talk and laugh together. They usually eat in the cafeteria.

After school, Lisa has sports. She plays tennis twice a week. She is a good player. After sports, she goes home and does her homework. She usually finishes at 6 o'clock. Then she has dinner with her family. In the evening, she sometimes does more studying or watches TV.

Lisa likes school because she has many good friends and interesting lessons.''',
        'cefr_level': 'A2',
        'category': 'Education',
        'word_count': 190,
        'reading_time_minutes': 4,
        'questions': [
            {
                'question': 'What time does Lisa get up?',
                'question_type': 'multiple_choice',
                'correct_answer': '7 o\'clock',
                'wrong_answers': ['6 o\'clock', '8 o\'clock', '9 o\'clock']
            },
            {
                'question': 'How long does the bus ride to school take?',
                'question_type': 'multiple_choice',
                'correct_answer': '20 minutes',
                'wrong_answers': ['10 minutes', '30 minutes', '40 minutes']
            },
            {
                'question': 'Which is NOT mentioned as something Lisa does?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Go swimming',
                'wrong_answers': ['Play tennis', 'Watch TV', 'Do homework']
            },
            {
                'question': 'Why does Lisa like her English teacher?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Because he is funny and interesting',
                'wrong_answers': ['Because he is strict', 'Because he gives no homework', 'Because he is young']
            }
        ]
    },
    
    # B1 Level
    {
        'title': 'The History of Coffee',
        'passage': '''Coffee is one of the most popular beverages in the world. It is consumed by millions of people every day. But where does coffee come from, and how did it become so popular?

The story of coffee began in Ethiopia, where coffee plants grow wild. According to legend, a goat herder discovered the energizing effect of coffee beans after noticing that his goats became very active after eating the berries of the coffee plant. This discovery eventually led to the development of coffee as a beverage.

Coffee cultivation spread from Ethiopia to the Arab world in the 15th century. By the 16th century, coffee was becoming popular in the Ottoman Empire. Coffee houses began to open in cities like Cairo, Mecca, and Istanbul. These coffee houses became important social centers where people gathered to drink coffee, discuss ideas, and share knowledge.

From the Arab world, coffee spread to Europe through merchants and traders. In the 17th century, coffee arrived in Venice, which was a major trading center. Gradually, coffee became popular throughout Europe. By the 18th century, coffee houses had become important gathering places in European cities, similar to their role in the Arab world.

Today, coffee is the second most traded commodity in the world, after oil. It is produced in many countries around the equator, including Brazil, Colombia, and Vietnam. The global coffee industry employs millions of people and affects the economies of many developing nations.''',
        'cefr_level': 'B1',
        'category': 'History',
        'word_count': 280,
        'reading_time_minutes': 5,
        'questions': [
            {
                'question': 'According to the passage, where did coffee originate?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Ethiopia',
                'wrong_answers': ['Brazil', 'Arab world', 'Europe']
            },
            {
                'question': 'How was coffee discovered according to the legend?',
                'question_type': 'multiple_choice',
                'correct_answer': 'A goat herder noticed his goats became active after eating coffee berries',
                'wrong_answers': ['A farmer planted coffee seeds', 'A merchant brought it from Asia', 'A scientist invented it']
            },
            {
                'question': 'What was the main purpose of coffee houses in the Arab world?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Social centers where people gathered and shared ideas',
                'wrong_answers': ['To sell expensive spices', 'To train soldiers', 'To worship']
            },
            {
                'question': 'When did coffee arrive in Europe?',
                'question_type': 'multiple_choice',
                'correct_answer': 'In the 17th century',
                'wrong_answers': ['In the 15th century', 'In the 18th century', 'In the 16th century']
            }
        ]
    },
    
    # B2 Level
    {
        'title': 'Climate Change and Global Warming',
        'passage': '''Climate change represents one of the most pressing challenges facing humanity in the 21st century. While the term "global warming" is often used interchangeably with "climate change," they are distinct phenomena. Global warming refers specifically to the increase in average global temperatures, whereas climate change encompasses broader alterations to Earth\'s climate patterns.

The primary driver of contemporary global warming is the accumulation of greenhouse gases in the atmosphere, particularly carbon dioxide (CO2). Since the Industrial Revolution, human activities such as burning fossil fuels and deforestation have significantly increased atmospheric CO2 concentrations. This greenhouse effect traps solar radiation, preventing heat from escaping to space and thereby raising global temperatures.

The consequences of climate change are multifaceted and increasingly evident. Rising sea levels threaten coastal communities, while altered precipitation patterns jeopardize agricultural productivity. Extreme weather events, including hurricanes and droughts, are becoming more frequent and severe. Biodiversity is declining as ecosystems struggle to adapt to rapidly changing conditions.

International efforts to mitigate climate change have gained momentum. The Paris Agreement of 2015 represents a watershed moment, with nearly all nations committing to limit global warming to well below 2°C above pre-industrial levels. However, implementing these commitments requires substantial transformations in energy systems, transportation, and industrial processes.

Individual actions, while important, must be complemented by systemic changes at governmental and corporate levels. Transitioning to renewable energy sources, promoting sustainable agriculture, and developing carbon capture technologies are essential strategies for addressing this existential threat.''',
        'cefr_level': 'B2',
        'category': 'Science',
        'word_count': 280,
        'reading_time_minutes': 6,
        'questions': [
            {
                'question': 'What is the primary difference between global warming and climate change?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Global warming refers to temperature increase while climate change encompasses broader alterations',
                'wrong_answers': ['Global warming is more serious', 'They are exactly the same', 'Global warming affects only cities']
            },
            {
                'question': 'What is the main cause of contemporary global warming?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Accumulation of greenhouse gases from human activities',
                'wrong_answers': ['Natural solar radiation changes', 'Volcanic eruptions', 'Ocean currents']
            },
            {
                'question': 'According to the passage, what is the Paris Agreement\'s goal?',
                'question_type': 'multiple_choice',
                'correct_answer': 'Limit global warming to below 2°C above pre-industrial levels',
                'wrong_answers': ['Stop all greenhouse gas emissions', 'Eliminate fossil fuels by 2050', 'Fund renewable energy only']
            }
        ]
    },
]


def seed_reading_comprehension():
    """Seed del contenido de Reading Comprehension"""
    with app.app_context():
        try:
            print("📖 CREANDO READING COMPREHENSION")
            
            for passage_data in READING_PASSAGES:
                # Verificar si ya existe
                existing = ReadingComprehension.query.filter_by(
                    title=passage_data['title']
                ).first()
                
                if not existing:
                    reading = ReadingComprehension(
                        title=passage_data['title'],
                        passage=passage_data['passage'],
                        cefr_level=passage_data['cefr_level'],
                        category=passage_data.get('category'),
                        word_count=passage_data.get('word_count'),
                        reading_time_minutes=passage_data.get('reading_time_minutes'),
                        is_active=True
                    )
                    db.session.add(reading)
                    db.session.flush()  # Para obtener el ID
                    
                    # Agregar preguntas
                    for idx, question_data in enumerate(passage_data['questions'], 1):
                        question = ReadingQuestion(
                            reading_id=reading.id,
                            question=question_data['question'],
                            question_type=question_data.get('question_type', 'multiple_choice'),
                            correct_answer=question_data['correct_answer'],
                            wrong_answers=question_data.get('wrong_answers'),
                            question_order=idx
                        )
                        db.session.add(question)
            
            db.session.commit()
            
            # Estadísticas
            total = ReadingComprehension.query.count()
            print(f"✅ Lecturas creadas: {total}")
            
            # Contar por nivel
            for level in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
                count = ReadingComprehension.query.filter_by(cefr_level=level).count()
                if count > 0:
                    print(f"   - {level}: {count} lecturas")
            
            total_questions = ReadingQuestion.query.count()
            print(f"✅ Preguntas creadas: {total_questions}")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()


if __name__ == '__main__':
    seed_reading_comprehension()
