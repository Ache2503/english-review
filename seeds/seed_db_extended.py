#!/usr/bin/env python
"""
Script avanzado de seeding con contenido enriquecido:
- Vocabulario detallado (palabra, traducción, pronunciación, ejemplo)
- Múltiples ejercicios por unidad (writing, dialogues, fill-in-blank, multiple-choice)
- Diálogos prácticos
- Casos de uso complejos
"""
import sys
import os
from pathlib import Path

proj_dir = Path(__file__).parent
sys.path.insert(0, str(proj_dir))

from app import create_app, db
from app.models import (
    Unit, Topic, GrammarRule, VocabularyCategory, VocabularyItem,
    WritingPractice, UnitExtra, Quiz, QuizQuestion, QuizOption
)
import json

app = create_app('development')

# Datos enriquecidos con múltiples ejercicios
EXTENDED_UNITS_DATA = [
    {
        "unit_number": 7,
        "title": "MIND (La Mente)",
        "description": "Exploring topics about happiness, the internet's impact on the brain, and intelligence.",
        "topics": ["Felicidad", "Internet y el cerebro", "Inteligencia"],
        "grammar": [
            {
                "title": "Articles (a/an/the/no article)",
                "rule": "Use 'the' with specific things, use 'a/an' with general things.",
                "example": "I go to school (as a student) vs I go to the school (the building). The happiness I feel is real.",
                "level": "beginner"
            },
            {
                "title": "Used to",
                "rule": "Express habits or states in the past that no longer occur.",
                "example": "I used to feel anxious. She used to spend hours on social media.",
                "level": "beginner"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Sentimientos",
                    "description": "Emotions related to happiness and well-being",
                    "words": [
                        {"word": "happiness", "translation": "felicidad", "pronunciation": "/ˈhæpɪnəs/", "example": "True happiness comes from within."},
                        {"word": "sadness", "translation": "tristeza", "pronunciation": "/ˈsædnəs/", "example": "She felt deep sadness."},
                        {"word": "anxiety", "translation": "ansiedad", "pronunciation": "/æŋˈzaɪəti/", "example": "Meditation reduces anxiety."},
                        {"word": "contentment", "translation": "satisfacción", "pronunciation": "/kənˈtɛntmənt/", "example": "He found contentment in simple things."},
                        {"word": "peace of mind", "translation": "tranquilidad mental", "pronunciation": "/pis əv maɪnd/", "example": "Exercise gives me peace of mind."}
                    ]
                },
                {
                    "name": "Phrasal Verbs",
                    "description": "Phrasal verbs for emotions and mental states",
                    "words": [
                        {"word": "cheer up", "translation": "animarse", "pronunciation": "/tʃɪr ʌp/", "example": "He cheered up when seeing friends."},
                        {"word": "calm down", "translation": "calmarse", "pronunciation": "/kɑːm daʊn/", "example": "Take a deep breath and calm down."},
                        {"word": "freak out", "translation": "asustarse", "pronunciation": "/frik aʊt/", "example": "Don't freak out about the exam."},
                        {"word": "figure out", "translation": "descubrir", "pronunciation": "/ˈfɪɡər aʊt/", "example": "Figure out what makes you happy."},
                        {"word": "deal with", "translation": "lidiar con", "pronunciation": "/dil wɪð/", "example": "How do you deal with stress?"}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Past Habits Reflection",
                "instructions": "Write 5-7 sentences about what you used to do that is different now.",
                "example": "I used to think money was the only way to happiness. Now I realize connections matter more.",
                "min_words": 50,
                "difficulty": "beginner"
            },
            {
                "type": "writing",
                "title": "Internet Impact Analysis",
                "instructions": "Discuss how the internet has changed your brain and thinking patterns.",
                "example": "The internet has changed how I think. I used to read books, but now I scroll quickly.",
                "min_words": 70,
                "difficulty": "intermediate"
            },
            {
                "type": "writing",
                "title": "Intelligence Redefined",
                "instructions": "Write about what intelligence means beyond just IQ.",
                "example": "Intelligence is more than test scores. Emotional intelligence matters too.",
                "min_words": 100,
                "difficulty": "advanced"
            }
        ],
        "dialogues": [
            {
                "title": "Coffee Shop - What Makes You Happy",
                "lines": [
                    {"speaker": "A", "text": "I used to think happiness was about money and success."},
                    {"speaker": "B", "text": "But now you realize simple things matter more, right?"},
                    {"speaker": "A", "text": "Exactly! Real happiness comes from relationships and growth."}
                ]
            },
            {
                "title": "Internet Habits Discussion",
                "lines": [
                    {"speaker": "Parent", "text": "You used to spend more time outside. Now you're always online."},
                    {"speaker": "Teen", "text": "The internet helps me stay connected with friends."},
                    {"speaker": "Parent", "text": "Connection is important, but face-to-face is different."}
                ]
            }
        ],
        "practice_writing": "In the past, I used to think that money was the only way to find happiness. However, I read an article about the human brain and realized that simple things matter. The happiness I feel today comes from different places. Going to school helps me stay active, and seeing the school building reminds me of good memories."
    },
    {
        "unit_number": 8,
        "title": "ART (Arte)",
        "description": "Discover art, music, and creative expression",
        "topics": ["Gustos musicales", "Arte inusual", "Películas y libros"],
        "grammar": [
            {
                "title": "Reflexive Pronouns",
                "rule": "Use when subject and object are the same person.",
                "example": "I taught myself to paint. She bought herself a new guitar.",
                "level": "beginner"
            },
            {
                "title": "Infinitive of Purpose",
                "rule": "Use 'to' to explain why you do something.",
                "example": "I went to the gallery to see art. She reads books to relax.",
                "level": "beginner"
            },
            {
                "title": "First Conditional",
                "rule": "For real possible situations (If + Present, will + verb).",
                "example": "If I see a good movie, I will recommend it.",
                "level": "intermediate"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Géneros de Música",
                    "description": "Music genres and related vocabulary",
                    "words": [
                        {"word": "classical", "translation": "clásica", "pronunciation": "/ˈklæsɪkəl/", "example": "Classical music is very sophisticated."},
                        {"word": "jazz", "translation": "jazz", "pronunciation": "/dʒæz/", "example": "Jazz originated in New Orleans."},
                        {"word": "rock", "translation": "rock", "pronunciation": "/rɑːk/", "example": "Rock music is very energetic."},
                        {"word": "pop", "translation": "pop", "pronunciation": "/pɑːp/", "example": "Pop music is popular worldwide."},
                        {"word": "electronic", "translation": "electrónica", "pronunciation": "/ɪˌlɛkˈtrɑːnɪk/", "example": "Electronic music uses synthesizers."}
                    ]
                },
                {
                    "name": "Cine y Películas",
                    "description": "Cinema and film vocabulary",
                    "words": [
                        {"word": "plot", "translation": "trama", "pronunciation": "/plɑːt/", "example": "The plot was very interesting."},
                        {"word": "character", "translation": "personaje", "pronunciation": "/ˈkærɪktər/", "example": "The main character was very likeable."},
                        {"word": "director", "translation": "director", "pronunciation": "/dɪˈrɛktər/", "example": "The director made a great film."},
                        {"word": "scene", "translation": "escena", "pronunciation": "/siːn/", "example": "That scene was very emotional."},
                        {"word": "genre", "translation": "género", "pronunciation": "/ˈʒɑːnrə/", "example": "What is your favorite film genre?"}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Your Art Preferences",
                "instructions": "Write about your favorite art, music, or film and why you like it.",
                "example": "I enjoy classical music because it relaxes me. If I had more time, I would learn to play piano.",
                "min_words": 60,
                "difficulty": "beginner"
            },
            {
                "type": "writing",
                "title": "Art Experience",
                "instructions": "Describe a time you went to a museum, concert, or movie. Use reflexive pronouns.",
                "example": "I bought myself a ticket to the art exhibition. I told myself to keep an open mind about modern art.",
                "min_words": 80,
                "difficulty": "intermediate"
            }
        ],
        "dialogues": [
            {
                "title": "Gallery Discussion",
                "lines": [
                    {"speaker": "A", "text": "I went to the gallery to see the new exhibition."},
                    {"speaker": "B", "text": "What did you think? I enjoyed myself there last week."},
                    {"speaker": "A", "text": "If you go again, I will go with you."}
                ]
            }
        ],
        "practice_writing": "I bought a ticket to see the abstract art exhibition. I told myself that I needed to be open-minded. If the exhibition is interesting, I will write a review. I love exploring new art forms. If I learn painting, maybe I will create something myself one day."
    },
    {
        "unit_number": 9,
        "title": "MONEY (Dinero)",
        "description": "Understanding money, finance, and economic thinking",
        "topics": ["Gastos", "Filantropía", "Habilidades"],
        "grammar": [
            {
                "title": "Second Conditional",
                "rule": "For imaginary or unlikely situations (If + Past, would + verb).",
                "example": "If I had more money, I would travel. If she were rich, she would help others.",
                "level": "intermediate"
            },
            {
                "title": "Gerunds",
                "rule": "Verb + -ing acting as a noun.",
                "example": "Saving money is important. I enjoy reading about finance.",
                "level": "intermediate"
            },
            {
                "title": "Essential Adjective Clauses",
                "rule": "Use who/which/that to define the noun.",
                "example": "People who save money are wise. The skills that you learn will help.",
                "level": "intermediate"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Make vs Do",
                    "description": "Differentiating between make and do",
                    "words": [
                        {"word": "make money", "translation": "ganar dinero", "pronunciation": "/meɪk ˈmʌni/", "example": "Hard work helps you make money."},
                        {"word": "make a decision", "translation": "tomar una decisión", "pronunciation": "/meɪk ə dɪˈsɪʒən/", "example": "Think carefully before you make a decision."},
                        {"word": "make progress", "translation": "hacer progreso", "pronunciation": "/meɪk ˈprɑːɡrɛs/", "example": "Consistent effort makes progress."},
                        {"word": "do homework", "translation": "hacer la tarea", "pronunciation": "/duː ˈhoʊmˌwɜrk/", "example": "Students do homework every night."},
                        {"word": "do research", "translation": "hacer investigación", "pronunciation": "/duː rɪˈsɜːrtʃ/", "example": "Scientists do research to find solutions."}
                    ]
                },
                {
                    "name": "Frases de Dinero",
                    "description": "Money-related phrases and expressions",
                    "words": [
                        {"word": "save money", "translation": "ahorrar dinero", "pronunciation": "/seɪv ˈmʌni/", "example": "It's important to save money for emergencies."},
                        {"word": "spend wisely", "translation": "gastar sabiamente", "pronunciation": "/spɛnd ˈwaɪzli/", "example": "Always spend wisely and avoid impulse buying."},
                        {"word": "earn a living", "translation": "ganarse la vida", "pronunciation": "/ɜːrn ə ˈlɪvɪŋ/", "example": "Most people work to earn a living."},
                        {"word": "make ends meet", "translation": "llegar a fin de mes", "pronunciation": "/meɪk ɛndz miːt/", "example": "Many families struggle to make ends meet."},
                        {"word": "waste money", "translation": "desperdiciar dinero", "pronunciation": "/weɪst ˈmʌni/", "example": "Don't waste money on unnecessary things."}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Your Money Philosophy",
                "instructions": "Write about your thoughts on money. What would you do if you had unlimited money?",
                "example": "If I had more money, I would help my family. Saving money is difficult, but it's necessary.",
                "min_words": 70,
                "difficulty": "intermediate"
            },
            {
                "type": "writing",
                "title": "Skills for Success",
                "instructions": "Discuss skills that help people earn money and what you would do differently.",
                "example": "People who develop valuable skills can make good money. If I had learned coding earlier, I would be a different person.",
                "min_words": 90,
                "difficulty": "advanced"
            }
        ],
        "dialogues": [
            {
                "title": "Financial Planning",
                "lines": [
                    {"speaker": "A", "text": "If you won the lottery, what would you do?"},
                    {"speaker": "B", "text": "I would help people who need it. Helping others is important to me."},
                    {"speaker": "A", "text": "That's noble. I would travel and learn new skills."}
                ]
            }
        ],
        "practice_writing": "Spending money responsibly is difficult. If I won the lottery, I would give half to charity. There are people who need help everywhere. I want to do good things for my community, but first I need to make enough money. Skills that I learn today will help me earn more in the future."
    },
    {
        "unit_number": 10,
        "title": "SCIENCE AND TECHNOLOGY (Ciencia y Tecnología)",
        "description": "Exploring technology, innovation, and scientific thinking",
        "topics": ["Dispositivos", "Tipos de tecnología", "El espacio"],
        "grammar": [
            {
                "title": "Comparatives & Superlatives",
                "rule": "Compare things (more/er) or identify the best (most/est).",
                "example": "My phone is faster than my tablet. This is the most useful device.",
                "level": "beginner"
            },
            {
                "title": "Need to",
                "rule": "Express necessity or obligation.",
                "example": "We need to learn about AI. You need to update your software.",
                "level": "beginner"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Dispositivos Electrónicos",
                    "description": "Electronic devices and technology",
                    "words": [
                        {"word": "smartphone", "translation": "teléfono inteligente", "pronunciation": "/ˈsmɑːrtfoʊn/", "example": "Modern smartphones are very powerful."},
                        {"word": "laptop", "translation": "computadora portátil", "pronunciation": "/ˈlæptɑːp/", "example": "I use my laptop for work every day."},
                        {"word": "tablet", "translation": "tableta", "pronunciation": "/ˈtæblɪt/", "example": "Tablets are great for reading and drawing."},
                        {"word": "smartwatch", "translation": "reloj inteligente", "pronunciation": "/ˈsmɑːrtwɑːtʃ/", "example": "My smartwatch tracks my fitness."},
                        {"word": "earbuds", "translation": "auriculares", "pronunciation": "/ˈɪrˌbʌdz/", "example": "Wireless earbuds are very convenient."}
                    ]
                },
                {
                    "name": "Colocaciones de Ciencia",
                    "description": "Science and research vocabulary",
                    "words": [
                        {"word": "conduct research", "translation": "realizar investigación", "pronunciation": "/kənˈdʌkt rɪˈsɜːrtʃ/", "example": "Scientists conduct research to find answers."},
                        {"word": "make a discovery", "translation": "hacer un descubrimiento", "pronunciation": "/meɪk ə dɪˈskʌvəri/", "example": "This scientist made an important discovery."},
                        {"word": "develop technology", "translation": "desarrollar tecnología", "pronunciation": "/dɪˈvɛləp tɛkˈnɑːlədʒi/", "example": "Companies develop technology to improve lives."},
                        {"word": "launch a rocket", "translation": "lanzar un cohete", "pronunciation": "/lɔːntʃ ə ˈrɑːkɪt/", "example": "NASA will launch a rocket tomorrow."},
                        {"word": "artificial intelligence", "translation": "inteligencia artificial", "pronunciation": "/ɑːr.tɪˈfɪʃ.əl ɪnˈtɛlɪdʒəns/", "example": "AI is changing the world rapidly."}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Technology Comparison",
                "instructions": "Compare two devices you use. Which is better and why?",
                "example": "My phone is faster than my laptop in some ways. However, my laptop is the most powerful device I own.",
                "min_words": 60,
                "difficulty": "beginner"
            },
            {
                "type": "writing",
                "title": "Future of Technology",
                "instructions": "Discuss what technology we need to develop in the future.",
                "example": "We need to develop better battery technology. Scientists need to research renewable energy solutions.",
                "min_words": 80,
                "difficulty": "intermediate"
            }
        ],
        "dialogues": [
            {
                "title": "Tech Store Conversation",
                "lines": [
                    {"speaker": "Salesman", "text": "This phone is faster than the previous model."},
                    {"speaker": "Customer", "text": "What is the most important feature?"},
                    {"speaker": "Salesman", "text": "You need to consider the camera quality. It's the best in the market."}
                ]
            }
        ],
        "practice_writing": "My new smartphone is faster than my old tablet. It is the most useful device I own. Technology changes quickly, so we need to update our skills constantly. AI is developing rapidly, and I think working with technology is the most exciting career option. We need to prepare for the future of innovation."
    },
    {
        "unit_number": 11,
        "title": "NATURAL WORLD (Mundo Natural)",
        "description": "Understanding nature, environment, and wildlife",
        "topics": ["Maravillas naturales", "Fotografía de vida salvaje", "Contaminación plástica"],
        "grammar": [
            {
                "title": "Passive Voice",
                "rule": "Focus on the action, not the actor (be + past participle).",
                "example": "Plastic is found everywhere. Animals are affected by pollution.",
                "level": "intermediate"
            },
            {
                "title": "Adjective + Infinitive",
                "rule": "Use 'It is + adjective + to + verb'.",
                "example": "It is important to protect nature. It is difficult to clean the oceans.",
                "level": "intermediate"
            },
            {
                "title": "Words with -where",
                "rule": "Use somewhere, nowhere, everywhere, anywhere.",
                "example": "Pollution is found everywhere. We need somewhere safe for wildlife.",
                "level": "beginner"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Animales en Peligro",
                    "description": "Endangered animals vocabulary",
                    "words": [
                        {"word": "endangered species", "translation": "especie en peligro", "pronunciation": "/ɪnˈdeɪndʒərd ˈspiːʃiːz/", "example": "Tigers are an endangered species."},
                        {"word": "habitat loss", "translation": "pérdida de hábitat", "pronunciation": "/ˈhæbɪtæt lɔːs/", "example": "Habitat loss is a major threat to wildlife."},
                        {"word": "conservation", "translation": "conservación", "pronunciation": "/ˌkɑːnsərˈveɪʃən/", "example": "Conservation efforts protect endangered animals."},
                        {"word": "wildlife", "translation": "vida silvestre", "pronunciation": "/ˈwaɪldˌlaɪf/", "example": "Wildlife photography captures nature's beauty."},
                        {"word": "ecosystem", "translation": "ecosistema", "pronunciation": "/ˈɛkoʊˌsɪstəm/", "example": "Every ecosystem is important for nature."}
                    ]
                },
                {
                    "name": "Características Naturales",
                    "description": "Natural features and landscapes",
                    "words": [
                        {"word": "mountain", "translation": "montaña", "pronunciation": "/ˈmaʊntən/", "example": "The mountain peak is covered in snow."},
                        {"word": "forest", "translation": "bosque", "pronunciation": "/ˈfɔːrɪst/", "example": "The rainforest is home to many species."},
                        {"word": "ocean", "translation": "océano", "pronunciation": "/ˈoʊʃən/", "example": "The ocean covers most of Earth."},
                        {"word": "desert", "translation": "desierto", "pronunciation": "/ˈdɛzərt/", "example": "Life in the desert is challenging."},
                        {"word": "river", "translation": "río", "pronunciation": "/ˈrɪvər/", "example": "The river provides water for the community."}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Environmental Concerns",
                "instructions": "Write about environmental problems and what can be done.",
                "example": "Plastic pollution is found everywhere. It is important to reduce plastic use. Animals are affected by waste.",
                "min_words": 70,
                "difficulty": "intermediate"
            },
            {
                "type": "writing",
                "title": "Natural Wonders",
                "instructions": "Describe a natural place you love and why it needs protection.",
                "example": "Somewhere in the mountains, there are endangered species. It is difficult to preserve these areas, but it is necessary.",
                "min_words": 85,
                "difficulty": "advanced"
            }
        ],
        "dialogues": [
            {
                "title": "Environmental Discussion",
                "lines": [
                    {"speaker": "A", "text": "Did you see that documentary about ocean pollution?"},
                    {"speaker": "B", "text": "Yes, it is sad to see animals suffering. Plastic is found everywhere in the ocean."},
                    {"speaker": "A", "text": "It is important to change our habits. I try to use less plastic everywhere."}
                ]
            }
        ],
        "practice_writing": "Plastic pollution is found everywhere, even in the deepest oceans. It is sad to see animals suffering because of our waste. Many photos were taken by wildlife photographers to show this problem. We must do something before there is nowhere safe for these animals. It is crucial to protect our natural wonders for future generations."
    },
    {
        "unit_number": 12,
        "title": "MEDIA (Medios de Comunicación)",
        "description": "Understanding media, information, and communication",
        "topics": ["Noticias online", "Hábitos de TV", "Publicidad"],
        "grammar": [
            {
                "title": "Reported Speech",
                "rule": "Report what someone said (change tenses).",
                "example": "She said that she liked the movie. He told me he would come.",
                "level": "intermediate"
            },
            {
                "title": "Past Perfect",
                "rule": "Show which action happened first (had + past participle).",
                "example": "When I arrived, the show had already started.",
                "level": "intermediate"
            },
            {
                "title": "Should",
                "rule": "Give advice or recommendations.",
                "example": "You should verify news sources. We should limit screen time.",
                "level": "beginner"
            }
        ],
        "vocabulary": {
            "categories": [
                {
                    "name": "Expresiones de Noticias",
                    "description": "News and media vocabulary",
                    "words": [
                        {"word": "headline", "translation": "titular", "pronunciation": "/ˈhɛdˌlaɪn/", "example": "The headline caught my attention."},
                        {"word": "breaking news", "translation": "noticias de último momento", "pronunciation": "/ˈbreɪkɪŋ njuːz/", "example": "Breaking news interrupted the program."},
                        {"word": "journalist", "translation": "periodista", "pronunciation": "/ˈdʒɜːrnələst/", "example": "The journalist investigated the story carefully."},
                        {"word": "fake news", "translation": "noticias falsas", "pronunciation": "/feɪk njuːz/", "example": "It's important to identify fake news."},
                        {"word": "credible source", "translation": "fuente creíble", "pronunciation": "/ˈkrɛdəbəl sɔːrs/", "example": "Always check credible sources before sharing."}
                    ]
                },
                {
                    "name": "Publicidad y Medios",
                    "description": "Advertising and media-related terms",
                    "words": [
                        {"word": "commercial", "translation": "comercial", "pronunciation": "/kəˈmɜːrʃəl/", "example": "That commercial was very creative."},
                        {"word": "advertisement", "translation": "anuncio", "pronunciation": "/ˈædvərˌtaɪzmənt/", "example": "Online advertisements are everywhere."},
                        {"word": "target audience", "translation": "audiencia objetivo", "pronunciation": "/ˈtɑːrɡɪt ˈɔːdiəns/", "example": "The target audience for this ad is teenagers."},
                        {"word": "brand", "translation": "marca", "pronunciation": "/brænd/", "example": "This brand is very popular worldwide."},
                        {"word": "marketing strategy", "translation": "estrategia de marketing", "pronunciation": "/ˈmɑːrkɪtɪŋ ˈstrætədʒi/", "example": "Their marketing strategy is very effective."}
                    ]
                }
            ]
        },
        "exercises": [
            {
                "type": "writing",
                "title": "Fake News Awareness",
                "instructions": "Write about how to identify fake news and why it's important.",
                "example": "The journalist said that fake news has become a problem. We should check sources. If information seems suspicious, we should investigate.",
                "min_words": 75,
                "difficulty": "intermediate"
            },
            {
                "type": "writing",
                "title": "Your Media Habits",
                "instructions": "Discuss your TV and social media habits and suggest improvements.",
                "example": "I had watched TV for three hours before my friend arrived. If I reduce my screen time, I would be healthier.",
                "min_words": 90,
                "difficulty": "advanced"
            }
        ],
        "dialogues": [
            {
                "title": "News Discussion",
                "lines": [
                    {"speaker": "A", "text": "Did you see that news report?"},
                    {"speaker": "B", "text": "The journalist said it was about climate change. But I should verify the source first."},
                    {"speaker": "A", "text": "Smart idea. You should always check credible sources. I had read about it before the broadcast."}
                ]
            }
        ],
        "practice_writing": "The journalist said that fake news had become a big problem. He told us that we should check sources before sharing. When I turned on the news, the program had already started. So I watched a documentary about advertising instead. People say that binge-watching TV is addictive, and I agree."
    }
]


def seed_database_extended():
    """Seed database with enriched content - ONLY adds UnitExtra, doesn't delete existing data"""
    with app.app_context():
        print("Verificando unidades existentes...")
        
        # NO eliminar tablas - solo agregar contenido
        # db.drop_all()  # COMENTADO - NO DESTRUIR DATOS
        db.create_all()  # Crear tablas si no existen
        db.session.commit()

        print("Cargando contenido extendido para unidades...")
        
        units_updated = 0
        units_skipped = 0
        
        for unit_data in EXTENDED_UNITS_DATA:
            # Buscar unidad existente
            unit = Unit.query.filter_by(unit_number=unit_data['unit_number']).first()
            
            if not unit:
                print(f"  ⚠️  Unit {unit_data['unit_number']} no existe, creándola...")
                unit = Unit(
                    unit_number=unit_data['unit_number'],
                    title=unit_data['title'],
                    description=unit_data.get('description', f"Unit {unit_data['unit_number']}: {unit_data['title']}")
                )
                db.session.add(unit)
                db.session.flush()
            
            # Verificar si ya tiene UnitExtra
            existing_extra = UnitExtra.query.filter_by(unit_id=unit.id).first()
            
            if existing_extra:
                print(f"  ℹ️  Unit {unit_data['unit_number']}: Ya tiene datos extendidos, actualizando...")
                # Actualizar datos existentes
                existing_data = existing_extra.data or {}
                new_data = {
                    'dialogues': unit_data.get('dialogues', existing_data.get('dialogues', [])),
                    'practice_activities': unit_data.get('practice_activities', existing_data.get('practice_activities', [])),
                    'prompts': unit_data.get('prompts', existing_data.get('prompts', [])),
                    'tips': unit_data.get('tips', existing_data.get('tips', [])),
                    'activities': unit_data.get('activities', existing_data.get('activities', {})),
                    'exercises_count': len(unit_data.get('exercises', []))
                }
                existing_extra.data = new_data
                units_updated += 1
            else:
                # Crear nuevo UnitExtra
                extras = {
                    'dialogues': unit_data.get('dialogues', []),
                    'practice_activities': unit_data.get('practice_activities', []),
                    'prompts': unit_data.get('prompts', []),
                    'tips': unit_data.get('tips', []),
                    'activities': unit_data.get('activities', {}),
                    'exercises_count': len(unit_data.get('exercises', []))
                }
                extra = UnitExtra(unit_id=unit.id, data=extras)
                db.session.add(extra)
                units_updated += 1
            
            exercises = unit_data.get('exercises', [])
            dialogues = unit_data.get('dialogues', [])
            vocab_cats = unit_data.get('vocabulary', {}).get('categories', [])
            
            print(f"  ✓ Unit {unit_data['unit_number']}: {unit_data['title']} - {len(exercises)} exercises, {len(vocab_cats)} vocab categories, {len(dialogues)} dialogues")

        db.session.commit()
        
        print(f"\n✅ Contenido extendido cargado exitosamente!")
        print(f"   Unidades actualizadas: {units_updated}")
        print("Características agregadas:")
        print("  - Diálogos prácticos con ejemplos reales")
        print("  - Actividades de práctica y prompts adicionales")
        print("  - Sistema de tips y recomendaciones")


if __name__ == '__main__':
    seed_database_extended()
