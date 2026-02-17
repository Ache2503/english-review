#!/usr/bin/env python3
"""
Seed para explicaciones de temas (TopicExplanation)
Explicaciones detalladas y secciones para cada topic
"""

from app import create_app, db
from app.models import Topic, TopicExplanation

# Explicaciones por topic
TOPIC_EXPLANATIONS = {
    "Felicidad": [
        {
            "section_title": "Vocabulario Clave",
            "content": """**Happiness Vocabulary:**

- **joy** /dʒɔɪ/ - alegría intensa
- **contentment** /kənˈtentmənt/ - satisfacción tranquila  
- **well-being** /ˌwel ˈbiːɪŋ/ - bienestar general
- **cheerful** /ˈtʃɪrfəl/ - alegre, animado
- **blissful** /ˈblɪsfəl/ - dichoso, muy feliz
- **grateful** /ˈɡreɪtfəl/ - agradecido
- **fulfilled** /fʊlˈfɪld/ - realizado, satisfecho

**Expresiones comunes:**
- "on cloud nine" = muy feliz
- "over the moon" = encantado
- "in high spirits" = de buen ánimo""",
            "order": 1
        },
        {
            "section_title": "Gramática en Contexto",
            "content": """**Present Simple para hábitos de felicidad:**

- I **exercise** every morning because it makes me happy.
- She **practices** gratitude daily.

**Present Perfect para experiencias:**

- I **have learned** that happiness comes from within.
- They **have discovered** the importance of relationships.

**Conditionals para hablar de causas:**

- If I **spend** time with friends, I **feel** happier.
- When you **help** others, you **experience** joy.""",
            "order": 2
        },
        {
            "section_title": "Errores Comunes",
            "content": """❌ **Incorrecto:** "I am very satisfy with my life."
✅ **Correcto:** "I am very **satisfied** with my life."

❌ **Incorrecto:** "The happiness is important."
✅ **Correcto:** "**Happiness** is important." (sin artículo)

❌ **Incorrecto:** "I feel me happy."
✅ **Correcto:** "I feel happy." (sin pronombre reflexivo)

❌ **Incorrecto:** "She is more happier now."
✅ **Correcto:** "She is **happier** now." (no doble comparativo)""",
            "order": 3
        }
    ],
    "Internet y el cerebro": [
        {
            "section_title": "Vocabulario Técnico",
            "content": """**Brain & Internet Vocabulary:**

- **attention span** - capacidad de atención
- **multitasking** - hacer varias tareas a la vez
- **dopamine** /ˈdoʊpəmiːn/ - dopamina
- **neural pathways** - conexiones neuronales
- **cognitive** /ˈkɒɡnɪtɪv/ - cognitivo
- **scroll** /skroʊl/ - desplazarse (en pantalla)
- **addictive** /əˈdɪktɪv/ - adictivo

**Collocations:**
- social media **addiction**
- digital **detox**
- screen **time**""",
            "order": 1
        },
        {
            "section_title": "Estructuras para Opiniones",
            "content": """**Expresar opiniones sobre tecnología:**

- **I believe** that social media affects our concentration.
- **In my opinion**, we should limit screen time.
- **It seems to me** that the internet changes how we think.
- **I'm convinced** that digital detox is beneficial.

**Para contrastar ideas:**

- **On one hand**, the internet provides information. **On the other hand**, it can be distracting.
- **While** technology has benefits, **it also** has drawbacks.""",
            "order": 2
        }
    ],
    "Inteligencia": [
        {
            "section_title": "Tipos de Inteligencia",
            "content": """**Vocabulary for Intelligence Types:**

- **IQ** (Intelligence Quotient) - coeficiente intelectual
- **emotional intelligence (EQ)** - inteligencia emocional
- **creative** /kriˈeɪtɪv/ - creativo
- **analytical** /ˌænəˈlɪtɪkəl/ - analítico
- **problem-solving** - resolución de problemas
- **gifted** /ˈɡɪftɪd/ - dotado, con talento
- **brilliant** /ˈbrɪljənt/ - brillante

**Howard Gardner's Multiple Intelligences:**
- linguistic, logical-mathematical, spatial
- musical, bodily-kinesthetic, interpersonal
- intrapersonal, naturalistic""",
            "order": 1
        }
    ],
    "Gustos musicales": [
        {
            "section_title": "Vocabulario Musical",
            "content": """**Music Vocabulary:**

- **genre** /ˈʒɑːnrə/ - género musical
- **melody** /ˈmelədi/ - melodía
- **rhythm** /ˈrɪðəm/ - ritmo
- **lyrics** /ˈlɪrɪks/ - letra de canción
- **tune** /tjuːn/ - melodía, canción
- **catchy** /ˈkætʃi/ - pegadizo
- **beat** /biːt/ - ritmo, pulso

**Music Genres:**
pop, rock, jazz, classical, hip-hop, reggae, electronic, folk, country, R&B""",
            "order": 1
        },
        {
            "section_title": "Expresar Preferencias",
            "content": """**Talking about music preferences:**

- I'm **really into** jazz these days.
- I **can't stand** heavy metal.
- Rock music **grows on you** after a while.
- This song **is stuck in my head**.
- I'm **a big fan of** classical music.

**Comparisons:**

- I **prefer** jazz **to** pop.
- I **like** indie music **better than** mainstream.
- Classical is **not as energetic as** electronic music.""",
            "order": 2
        }
    ],
    "Arte inusual": [
        {
            "section_title": "Art Vocabulary",
            "content": """**Unusual Art Terms:**

- **installation art** - arte de instalación
- **performance art** - arte performático
- **avant-garde** /ˌævɒ̃ ˈɡɑːrd/ - vanguardista
- **abstract** /ˈæbstrækt/ - abstracto
- **controversial** /ˌkɒntrəˈvɜːʃəl/ - polémico
- **thought-provoking** - que invita a la reflexión
- **unconventional** - poco convencional

**Describing art:**
- striking, bold, innovative, bizarre, quirky""",
            "order": 1
        }
    ],
    "Películas y libros": [
        {
            "section_title": "Vocabulary for Reviews",
            "content": """**Film & Book Vocabulary:**

- **plot** /plɒt/ - trama
- **character development** - desarrollo de personajes
- **twist** /twɪst/ - giro inesperado
- **gripping** /ˈɡrɪpɪŋ/ - absorbente
- **page-turner** - libro que no puedes dejar
- **blockbuster** - éxito taquillero
- **bestseller** - éxito de ventas

**Genres:**
thriller, romance, sci-fi, documentary, biography, horror, comedy, drama""",
            "order": 1
        },
        {
            "section_title": "Giving Reviews",
            "content": """**Structures for reviews:**

**Positive:**
- It's **worth watching/reading**.
- I **highly recommend** it.
- I **couldn't put it down**.
- The ending **blew my mind**.

**Negative:**
- It was a bit **disappointing**.
- The plot was **predictable**.
- I **wouldn't recommend** it.
- It **didn't live up to** the hype.""",
            "order": 2
        }
    ],
    "Gastos": [
        {
            "section_title": "Money Vocabulary",
            "content": """**Spending & Money Terms:**

- **budget** /ˈbʌdʒɪt/ - presupuesto
- **expenses** /ɪkˈspensɪz/ - gastos
- **savings** /ˈseɪvɪŋz/ - ahorros
- **debt** /det/ - deuda
- **investment** /ɪnˈvestmənt/ - inversión
- **afford** /əˈfɔːrd/ - permitirse
- **splurge** /splɜːrdʒ/ - derrochar

**Useful expressions:**
- to be **broke** = estar sin dinero
- to **live paycheck to paycheck** = vivir al día
- to **tighten one's belt** = ajustarse el cinturón""",
            "order": 1
        }
    ],
    "Filantropía": [
        {
            "section_title": "Charity Vocabulary",
            "content": """**Philanthropy & Giving:**

- **donate** /doʊˈneɪt/ - donar
- **volunteer** /ˌvɒlənˈtɪr/ - voluntario/voluntariar
- **charity** /ˈtʃærəti/ - caridad, organización benéfica
- **non-profit** - sin fines de lucro
- **fundraising** - recaudación de fondos
- **altruism** /ˈæltruːɪzəm/ - altruismo
- **generous** /ˈdʒenərəs/ - generoso

**Collocations:**
- to **make a donation**
- to **raise awareness**
- to **give back** to the community""",
            "order": 1
        }
    ],
    "Dispositivos": [
        {
            "section_title": "Device Vocabulary",
            "content": """**Tech Devices:**

- **smartphone** - teléfono inteligente
- **tablet** /ˈtæblət/ - tableta
- **laptop** - portátil
- **smartwatch** - reloj inteligente
- **wireless** /ˈwaɪərləs/ - inalámbrico
- **charger** /ˈtʃɑːrdʒər/ - cargador
- **gadget** /ˈɡædʒɪt/ - dispositivo

**Common verbs:**
- to **sync** devices
- to **update** software
- to **back up** data
- to **reboot** / **restart**""",
            "order": 1
        }
    ],
    "El espacio": [
        {
            "section_title": "Space Vocabulary",
            "content": """**Space & Astronomy:**

- **universe** /ˈjuːnɪvɜːrs/ - universo
- **galaxy** /ˈɡæləksi/ - galaxia
- **astronaut** /ˈæstrənɔːt/ - astronauta
- **spacecraft** - nave espacial
- **satellite** /ˈsætəlaɪt/ - satélite
- **orbit** /ˈɔːrbɪt/ - órbita
- **black hole** - agujero negro
- **solar system** - sistema solar

**Space exploration terms:**
- rocket launch, space station, Mars mission, lunar landing""",
            "order": 1
        }
    ],
    "Maravillas naturales": [
        {
            "section_title": "Nature Vocabulary",
            "content": """**Natural Wonders:**

- **waterfall** /ˈwɔːtərfɔːl/ - cascada
- **canyon** /ˈkænjən/ - cañón
- **glacier** /ˈɡleɪʃər/ - glaciar
- **volcano** /vɒlˈkeɪnoʊ/ - volcán
- **reef** /riːf/ - arrecife
- **breathtaking** - impresionante
- **majestic** /məˈdʒestɪk/ - majestuoso
- **stunning** /ˈstʌnɪŋ/ - impresionante

**Famous wonders:**
- Grand Canyon, Great Barrier Reef, Northern Lights, Victoria Falls""",
            "order": 1
        }
    ],
    "Contaminación plástica": [
        {
            "section_title": "Environmental Vocabulary",
            "content": """**Plastic Pollution Terms:**

- **pollution** /pəˈluːʃən/ - contaminación
- **recycling** /riːˈsaɪklɪŋ/ - reciclaje
- **biodegradable** - biodegradable
- **single-use plastic** - plástico de un solo uso
- **microplastics** - microplásticos
- **landfill** /ˈlændfɪl/ - vertedero
- **sustainable** /səˈsteɪnəbəl/ - sostenible

**Environmental actions:**
- to **reduce** consumption
- to **reuse** items
- to **recycle** materials
- to **ban** plastic bags""",
            "order": 1
        }
    ],
    "Noticias online": [
        {
            "section_title": "News Media Vocabulary",
            "content": """**Online News Terms:**

- **headline** /ˈhedlaɪn/ - titular
- **breaking news** - noticias de última hora
- **reliable source** - fuente confiable
- **fake news** - noticias falsas
- **clickbait** - ciberanzuelo
- **viral** /ˈvaɪrəl/ - viral
- **journalist** /ˈdʒɜːrnəlɪst/ - periodista

**News verbs:**
- to **report** on
- to **cover** a story
- to **broadcast** news
- to **go viral**""",
            "order": 1
        }
    ],
    "Hábitos de TV": [
        {
            "section_title": "TV Watching Vocabulary",
            "content": """**Television Terms:**

- **binge-watch** - ver muchos episodios seguidos
- **streaming service** - servicio de streaming
- **episode** /ˈepɪsoʊd/ - episodio
- **season** /ˈsiːzən/ - temporada
- **series** /ˈsɪriːz/ - serie
- **reality show** - programa de telerrealidad
- **documentary** - documental

**Expressions:**
- "I'm hooked on this show" = estoy enganchado
- "No spoilers!" = ¡no cuentes el final!
- "It's binge-worthy" = vale la pena verlo de corrido""",
            "order": 1
        }
    ],
    "Publicidad": [
        {
            "section_title": "Advertising Vocabulary",
            "content": """**Advertising Terms:**

- **advertisement/ad** - anuncio
- **commercial** /kəˈmɜːrʃəl/ - comercial (TV)
- **brand** /brænd/ - marca
- **slogan** /ˈsloʊɡən/ - eslogan
- **target audience** - público objetivo
- **campaign** /kæmˈpeɪn/ - campaña
- **influencer** - influencer

**Advertising verbs:**
- to **promote** a product
- to **endorse** a brand
- to **sponsor** an event
- to **advertise** services""",
            "order": 1
        }
    ]
}

def seed_topic_explanations():
    """Poblar la tabla de explicaciones de temas"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("📚 AGREGANDO EXPLICACIONES DE TEMAS")
        print("=" * 60)
        
        added = 0
        skipped = 0
        
        topics = Topic.query.all()
        
        for topic in topics:
            if topic.title in TOPIC_EXPLANATIONS:
                explanations = TOPIC_EXPLANATIONS[topic.title]
                
                for exp_data in explanations:
                    # Verificar si ya existe
                    existing = TopicExplanation.query.filter_by(
                        topic_id=topic.id,
                        section_title=exp_data["section_title"]
                    ).first()
                    
                    if existing:
                        skipped += 1
                        continue
                    
                    explanation = TopicExplanation(
                        topic_id=topic.id,
                        section_title=exp_data["section_title"],
                        content=exp_data["content"],
                        visual_aids=exp_data.get("visual_aids"),
                        order=exp_data.get("order", 0)
                    )
                    db.session.add(explanation)
                    added += 1
                    print(f"✓ {topic.title}: {exp_data['section_title']}")
        
        db.session.commit()
        
        print()
        print(f"✅ Explicaciones agregadas: {added}")
        print(f"⏭️  Omitidas (ya existían): {skipped}")
        print("=" * 60)

if __name__ == "__main__":
    seed_topic_explanations()
