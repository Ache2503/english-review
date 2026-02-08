#!/usr/bin/env python3
"""
Seed para secciones de exámenes (ExamSection)
Secciones completas para TOEFL, IELTS y Cambridge
"""

from app import create_app, db
from app.models import ExamSimulator, ExamSection

EXAM_SECTIONS = {
    "TOEFL Practice Test 1": [
        {
            "section_type": "reading",
            "title": "Reading Comprehension",
            "instructions": "Read the following passages and answer the questions. You have 20 minutes for this section.",
            "time_limit_minutes": 20,
            "points_per_question": 1.0,
            "order": 1,
            "questions": [
                {
                    "passage": "The Amazon rainforest, often referred to as the 'lungs of the Earth,' produces approximately 20% of the world's oxygen. This vast ecosystem spans across nine countries in South America and is home to an estimated 10% of all species on Earth. However, deforestation poses a significant threat to this crucial biome, with an area roughly the size of a football field being cleared every minute.",
                    "question": "According to the passage, what percentage of the world's oxygen does the Amazon produce?",
                    "options": ["10%", "15%", "20%", "25%"],
                    "correct": "20%"
                },
                {
                    "passage": "The Amazon rainforest, often referred to as the 'lungs of the Earth,' produces approximately 20% of the world's oxygen. This vast ecosystem spans across nine countries in South America and is home to an estimated 10% of all species on Earth. However, deforestation poses a significant threat to this crucial biome, with an area roughly the size of a football field being cleared every minute.",
                    "question": "What is mentioned as a threat to the Amazon?",
                    "options": ["Climate change", "Deforestation", "Pollution", "Overpopulation"],
                    "correct": "Deforestation"
                },
                {
                    "passage": "Artificial intelligence has transformed numerous industries, from healthcare diagnostics to autonomous vehicles. Machine learning algorithms can now detect diseases with accuracy rates surpassing human doctors in certain specialties. Despite these advances, ethical concerns about AI decision-making and job displacement continue to spark debate among policymakers and technologists.",
                    "question": "What does the passage suggest about AI in healthcare?",
                    "options": [
                        "It is completely unreliable",
                        "It can detect diseases very accurately",
                        "It has replaced all doctors",
                        "It is too expensive to implement"
                    ],
                    "correct": "It can detect diseases very accurately"
                }
            ]
        },
        {
            "section_type": "grammar",
            "title": "Structure and Written Expression",
            "instructions": "Choose the best answer to complete each sentence or identify the error.",
            "time_limit_minutes": 15,
            "points_per_question": 1.0,
            "order": 2,
            "questions": [
                {
                    "question": "The committee _____ decided to postpone the meeting until next week.",
                    "options": ["has", "have", "having", "had been"],
                    "correct": "has"
                },
                {
                    "question": "Neither the students nor the teacher _____ aware of the schedule change.",
                    "options": ["were", "was", "are", "been"],
                    "correct": "was"
                },
                {
                    "question": "By the time we arrived, the movie _____.",
                    "options": ["already started", "has already started", "had already started", "already starts"],
                    "correct": "had already started"
                },
                {
                    "question": "She suggested that he _____ more carefully before making a decision.",
                    "options": ["thinks", "thought", "think", "thinking"],
                    "correct": "think"
                }
            ]
        },
        {
            "section_type": "vocabulary",
            "title": "Vocabulary in Context",
            "instructions": "Choose the word or phrase that best completes each sentence.",
            "time_limit_minutes": 10,
            "points_per_question": 1.0,
            "order": 3,
            "questions": [
                {
                    "question": "The scientist's _____ discovery revolutionized the field of medicine.",
                    "options": ["groundbreaking", "underground", "broken", "grounded"],
                    "correct": "groundbreaking"
                },
                {
                    "question": "Despite the _____ evidence, the jury could not reach a verdict.",
                    "options": ["overwhelming", "underwhelming", "whelming", "over"],
                    "correct": "overwhelming"
                },
                {
                    "question": "The company's profits _____ significantly after the new CEO took over.",
                    "options": ["soared", "soured", "sored", "stored"],
                    "correct": "soared"
                }
            ]
        }
    ],
    "IELTS Academic Practice": [
        {
            "section_type": "reading",
            "title": "Academic Reading",
            "instructions": "Read the passages and answer questions 1-10. You have 20 minutes for this section.",
            "time_limit_minutes": 20,
            "points_per_question": 1.0,
            "order": 1,
            "questions": [
                {
                    "passage": "The concept of sustainable development emerged in the 1980s as a response to growing concerns about environmental degradation. The Brundtland Commission defined it as 'development that meets the needs of the present without compromising the ability of future generations to meet their own needs.' This definition has become the cornerstone of international environmental policy.",
                    "question": "When did the concept of sustainable development emerge?",
                    "options": ["1970s", "1980s", "1990s", "2000s"],
                    "correct": "1980s"
                },
                {
                    "passage": "The concept of sustainable development emerged in the 1980s as a response to growing concerns about environmental degradation. The Brundtland Commission defined it as 'development that meets the needs of the present without compromising the ability of future generations to meet their own needs.' This definition has become the cornerstone of international environmental policy.",
                    "question": "According to the passage, sustainable development is about:",
                    "options": [
                        "Maximizing current profits",
                        "Balancing present needs with future needs",
                        "Stopping all development",
                        "Focusing only on the environment"
                    ],
                    "correct": "Balancing present needs with future needs"
                },
                {
                    "passage": "Urban migration continues to reshape demographics worldwide. By 2050, it is estimated that 68% of the world's population will live in urban areas, compared to 55% today. This shift presents both opportunities and challenges for city planners, who must ensure adequate housing, transportation, and services for growing populations.",
                    "question": "What percentage of the world population is expected to live in cities by 2050?",
                    "options": ["55%", "60%", "68%", "75%"],
                    "correct": "68%"
                }
            ]
        },
        {
            "section_type": "writing",
            "title": "Writing Task 1",
            "instructions": "Describe the information presented in the chart. Write at least 150 words.",
            "time_limit_minutes": 20,
            "points_per_question": 5.0,
            "order": 2,
            "questions": [
                {
                    "type": "essay",
                    "prompt": "The bar chart shows the percentage of people using different forms of transport in a city in 2010 and 2020. Summarize the information and make comparisons where relevant.",
                    "word_limit": 150,
                    "criteria": ["Task Achievement", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range"]
                }
            ]
        },
        {
            "section_type": "grammar",
            "title": "Use of English",
            "instructions": "Complete the sentences with the correct form of the words given.",
            "time_limit_minutes": 15,
            "points_per_question": 1.0,
            "order": 3,
            "questions": [
                {
                    "question": "The report highlighted the _____ (important) of investing in renewable energy.",
                    "options": ["importance", "importantly", "important", "importation"],
                    "correct": "importance"
                },
                {
                    "question": "The new policy has _____ (significant) reduced carbon emissions.",
                    "options": ["significant", "significantly", "significance", "signify"],
                    "correct": "significantly"
                }
            ]
        }
    ],
    "Cambridge B2 First": [
        {
            "section_type": "reading",
            "title": "Reading and Use of English - Part 1",
            "instructions": "For questions 1-8, read the text and decide which answer (A, B, C or D) best fits each gap.",
            "time_limit_minutes": 15,
            "points_per_question": 1.0,
            "order": 1,
            "questions": [
                {
                    "passage": "Learning a new language can be a (1)_____ experience, but it requires dedication and practice. Many people find that immersion is the most (2)_____ way to become fluent.",
                    "question": "(1)",
                    "options": ["rewarding", "rewarded", "reward", "rewards"],
                    "correct": "rewarding"
                },
                {
                    "passage": "Learning a new language can be a (1)_____ experience, but it requires dedication and practice. Many people find that immersion is the most (2)_____ way to become fluent.",
                    "question": "(2)",
                    "options": ["effective", "effect", "effectively", "effects"],
                    "correct": "effective"
                },
                {
                    "question": "She _____ to the gym three times a week to stay fit.",
                    "options": ["goes", "go", "going", "gone"],
                    "correct": "goes"
                },
                {
                    "question": "The book, _____ was written in 1984, is still relevant today.",
                    "options": ["which", "who", "what", "whom"],
                    "correct": "which"
                }
            ]
        },
        {
            "section_type": "vocabulary",
            "title": "Reading and Use of English - Part 2",
            "instructions": "For questions 1-8, think of the word which best fits each gap. Use only ONE word in each gap.",
            "time_limit_minutes": 10,
            "points_per_question": 1.0,
            "order": 2,
            "questions": [
                {
                    "question": "I haven't seen him _____ last Monday.",
                    "options": ["since", "for", "from", "during"],
                    "correct": "since"
                },
                {
                    "question": "She is interested _____ learning new languages.",
                    "options": ["in", "on", "at", "for"],
                    "correct": "in"
                },
                {
                    "question": "He apologized _____ being late to the meeting.",
                    "options": ["for", "about", "of", "to"],
                    "correct": "for"
                }
            ]
        },
        {
            "section_type": "grammar",
            "title": "Reading and Use of English - Part 3",
            "instructions": "Use the word given in capitals to form a word that fits in the gap.",
            "time_limit_minutes": 10,
            "points_per_question": 1.0,
            "order": 3,
            "questions": [
                {
                    "question": "The _____ (PERFORM) was absolutely spectacular.",
                    "options": ["performance", "performer", "performing", "performed"],
                    "correct": "performance"
                },
                {
                    "question": "This is an _____ (FORGET) experience that I will treasure forever.",
                    "options": ["unforgettable", "forgetful", "forgettable", "forgotten"],
                    "correct": "unforgettable"
                },
                {
                    "question": "The hotel staff were very _____ (HELP) during our stay.",
                    "options": ["helpful", "helpless", "helping", "helped"],
                    "correct": "helpful"
                }
            ]
        }
    ]
}

def seed_exam_sections():
    """Poblar la tabla de secciones de examen"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("📝 AGREGANDO SECCIONES DE EXÁMENES")
        print("=" * 60)
        
        added = 0
        skipped = 0
        
        exams = ExamSimulator.query.all()
        
        for exam in exams:
            if exam.title in EXAM_SECTIONS:
                sections = EXAM_SECTIONS[exam.title]
                
                for section_data in sections:
                    # Verificar si ya existe
                    existing = ExamSection.query.filter_by(
                        exam_id=exam.id,
                        section_type=section_data["section_type"],
                        title=section_data["title"]
                    ).first()
                    
                    if existing:
                        skipped += 1
                        continue
                    
                    section = ExamSection(
                        exam_id=exam.id,
                        section_type=section_data["section_type"],
                        title=section_data["title"],
                        instructions=section_data["instructions"],
                        questions=section_data["questions"],
                        time_limit_minutes=section_data.get("time_limit_minutes"),
                        points_per_question=section_data.get("points_per_question", 1.0),
                        order=section_data.get("order", 0)
                    )
                    db.session.add(section)
                    added += 1
                    print(f"✓ {exam.title}: {section_data['title']}")
        
        db.session.commit()
        
        print()
        print(f"✅ Secciones agregadas: {added}")
        print(f"⏭️  Omitidas (ya existían): {skipped}")
        print("=" * 60)

if __name__ == "__main__":
    seed_exam_sections()
