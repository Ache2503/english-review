#!/usr/bin/env python
"""
Script para poblar las explicaciones de unidades y temas.
Cada unidad tendrá su propia explicación detallada.
Cada tema tendrá su propia explicación estructurada.
"""

import sys
from app import create_app
from app.extensions import db
from app.models import (
    Unit, Topic, GrammarRule, UnitExplanation, TopicExplanation
)

# Explicaciones de unidades
UNIT_EXPLANATIONS = {
    7: {
        "title": "Unit 7: MIND (La Mente)",
        "overview": "Explorarás temas sobre la mente, el bienestar mental, la felicidad y cómo funciona nuestro cerebro en la era digital.",
        "learning_objectives": [
            "Entender vocabulario relacionado con la psicología y el bienestar",
            "Hablar sobre emociones y estados mentales",
            "Comprender el impacto de la tecnología en el cerebro",
            "Discutir sobre inteligencia y felicidad"
        ],
        "detailed_explanation": "En esta unidad explorarás la mente humana a través del inglés. Aprenderás vocabulario específico sobre emociones, bienestar y psicología. Comprenderás cómo la tecnología está transformando nuestro cerebro y reflexionarás sobre qué significa ser feliz e inteligente en el mundo moderno.",
        "sections": [
            {
                "title": "Introducción",
                "content": "La mente es uno de los temas más fascinantes que podemos explorar en cualquier idioma. En esta unidad, expandirás tu vocabulario para hablar sobre sentimientos, estados mentales y procesos cerebrales. Descubrirás cómo diferentes culturas entienden la felicidad, la inteligencia y el bienestar mental."
            },
            {
                "title": "Conceptos Clave",
                "content": "1. EMOCIONES Y SENTIMIENTOS: Vocabulario para expresar cómo nos sentimos (happy, sad, anxious, peaceful, etc.)\n2. PROCESOS MENTALES: Cómo pensamos, recordamos y aprendemos\n3. BIENESTAR MENTAL: Estrategias para la salud mental y la felicidad\n4. TECNOLOGÍA Y CEREBRO: Cómo los dispositivos digitales afectan nuestro pensamiento"
            },
            {
                "title": "Aplicación Práctica",
                "content": "Usarás este vocabulario para hablar sobre tu propio bienestar, comprender artículos sobre psicología, discutir sobre hábitos digitales saludables y entender cómo otros piensan y sienten alrededor del mundo."
            }
        ]
    },
    8: {
        "title": "Unit 8: ART (Arte)",
        "overview": "Descubrirás el mundo del arte, la música, el cine y la literatura, expresando tus gustos y opiniones sobre diferentes formas de expresión artística.",
        "learning_objectives": [
            "Expandir vocabulario sobre arte, música y entretenimiento",
            "Expresar opiniones y preferencias sobre obras de arte",
            "Entender críticas y análisis de películas y libros",
            "Hablar sobre gustos personales"
        ],
        "detailed_explanation": "El arte es una ventana a diferentes culturas y formas de pensar. En esta unidad aprenderás a hablar sobre música, películas, literatura y arte visual. Descubrirás nuevas formas de expresar qué te gusta, por qué te gusta, y cómo el arte refleja la sociedad.",
        "sections": [
            {
                "title": "El Lenguaje del Arte",
                "content": "Para hablar de arte efectivamente, necesitas vocabulario específico. Desde géneros musicales hasta técnicas de pintura, desde tipos de películas hasta movimientos literarios. En esta unidad dominarás todas estas categorías."
            },
            {
                "title": "Expresando Gustos",
                "content": "Aprenderás múltiples formas de decir qué te gusta:\n- I love/enjoy/adore...\n- I'm a fan of...\n- I prefer... to...\n- I appreciate... because...\n- I'm not into...\nCada una tiene matices diferentes que harán tu expresión más natural."
            },
            {
                "title": "Análisis y Crítica",
                "content": "Distinguirás entre opiniones simples y análisis profundos. Aprenderás a hablar sobre técnica artística, significado, contexto histórico y impacto cultural. Estas habilidades son esenciales para discusiones académicas y críticas."
            }
        ]
    },
    9: {
        "title": "Unit 9: MONEY (Dinero)",
        "overview": "Explorarás temas sobre dinero, presupuestos, filantropía y cómo diferentes personas manejan sus finanzas.",
        "learning_objectives": [
            "Entender vocabulario financiero en inglés",
            "Hablar sobre gastos, ingresos y ahorros",
            "Comprender donaciones y filantropía",
            "Desarrollar habilidades financieras en inglés"
        ],
        "detailed_explanation": "El dinero es un tema universal pero complejo. En esta unidad aprenderás a hablar sobre finanzas personales, presupuestos y decisiones económicas. Comprenderás cómo diferentes culturas valoran el dinero y la importancia de la filantropía.",
        "sections": [
            {
                "title": "Vocabulario Financiero Básico",
                "content": "Income (ingreso), expense (gasto), budget (presupuesto), savings (ahorros), investment (inversión), debt (deuda). Estos términos te permitirán hablar sobre finanzas de forma clara y profesional."
            },
            {
                "title": "Gestión de Dinero",
                "content": "No es suficiente conocer palabras; necesitas entender conceptos como presupuestación, ahorro y gasto responsable. Aprenderás a aconsejar, analizar y discutir decisiones económicas."
            },
            {
                "title": "Filantropía y Donaciones",
                "content": "Descubrirás cómo habladores de inglés discuten la caridad, el voluntariado y cómo ayudar a otros. Este vocabulario es importante para conversaciones sobre responsabilidad social."
            }
        ]
    },
    10: {
        "title": "Unit 10: SCIENCE AND TECHNOLOGY (Ciencia y Tecnología)",
        "overview": "Sumérgete en el mundo de la ciencia y la tecnología, desde dispositivos cotidianos hasta descubrimientos espaciales.",
        "learning_objectives": [
            "Dominar vocabulario tecnológico y científico",
            "Entender cómo funcionan los dispositivos",
            "Hablar sobre innovación y descubrimientos",
            "Comprender el impacto de la tecnología en la sociedad"
        ],
        "detailed_explanation": "La tecnología y la ciencia son pilares del mundo moderno. En esta unidad expandirás tu vocabulario para hablar sobre dispositivos, sistemas, descubrimientos e innovación. Entenderás cómo diferentes culturas abordan la tecnología y sus implicaciones.",
        "sections": [
            {
                "title": "Dispositivos y Tecnología",
                "content": "Desde smartphones hasta computadoras, desde IoT hasta artificial intelligence. Aprenderás a describir tecnología, sus funciones y cómo usarla. Este vocabulario es esencial en el mundo laboral moderno."
            },
            {
                "title": "Conceptos Científicos",
                "content": "Descubrirás cómo habladores de inglés discuten investigación, experimentos y descubrimientos. Entenderás términos como hypothesis, research, data, conclusion que aparecen en contextos académicos."
            },
            {
                "title": "Impacto Social",
                "content": "Aprenderás a debatir sobre los efectos de la tecnología en la sociedad: ¿nos conecta o nos aísla? ¿Cómo afecta a la privacidad? ¿Qué oportunidades nos ofrece?"
            }
        ]
    },
    11: {
        "title": "Unit 11: NATURAL WORLD (Mundo Natural)",
        "overview": "Explora la belleza del mundo natural, desde maravillas naturales hasta conservación ambiental.",
        "learning_objectives": [
            "Aprender vocabulario sobre naturaleza y animales",
            "Hablar sobre conservación ambiental",
            "Entender problemas ecológicos",
            "Apreciar la biodiversidad"
        ],
        "detailed_explanation": "La naturaleza es inspiradora y urgente. En esta unidad aprenderás a hablar sobre paisajes, animales, ecosistemas y los desafíos ambientales que enfrentamos. Desarrollarás vocabulario para describir la belleza natural y comprender temas de sostenibilidad.",
        "sections": [
            {
                "title": "Vocabulario de la Naturaleza",
                "content": "Bioma, fauna, flora, ecosystem, species, habitat. Estos términos te permiten hablar con precisión sobre el mundo natural. Aprenderás nombres de animales, plantas y características geográficas."
            },
            {
                "title": "Conservación y Sostenibilidad",
                "content": "Entenderás términos como conservation, endangered species, climate change, pollution. Estos son temas críticos en conversaciones globales actuales."
            },
            {
                "title": "Conectando con la Tierra",
                "content": "Explorarás cómo diferentes culturas se relacionan con la naturaleza, respetan el medio ambiente y entienden la sostenibilidad. Reflexionarás sobre tu propia responsabilidad ecológica."
            }
        ]
    },
    12: {
        "title": "Unit 12: MEDIA (Medios de Comunicación)",
        "overview": "Analiza los medios de comunicación, desde noticias online hasta hábitos de televisión y publicidad.",
        "learning_objectives": [
            "Entender vocabulario de medios y comunicación",
            "Analizar noticias críticamente",
            "Hablar sobre hábitos de consumo de medios",
            "Comprender influencia de publicidad"
        ],
        "detailed_explanation": "Los medios moldean cómo entendemos el mundo. En esta unidad aprenderás a hablar críticamente sobre noticias, televisión, redes sociales y publicidad. Desarrollarás habilidades para consumir medios de forma más consciente y analítica.",
        "sections": [
            {
                "title": "Tipos de Medios",
                "content": "News media (periodismo), social media, television, radio, online platforms. Cada medio tiene su propio vocabulario y características. Entenderás cómo cada uno moldea la información."
            },
            {
                "title": "Lectura Crítica de Noticias",
                "content": "Aprenderás a hacer preguntas: ¿Quién escribió esto? ¿Cuál es el sesgo? ¿Dónde está el contexto? Estas habilidades son vitales en la era de la desinformación."
            },
            {
                "title": "Impacto de Medios y Publicidad",
                "content": "Explorarás cómo los medios influyen en nuestras opiniones y comportamientos. Entenderás técnicas publicitarias y cómo los medios reflejan (y crean) la cultura."
            }
        ]
    }
}

# Explicaciones de temas específicos
TOPIC_EXPLANATIONS = {
    "Felicidad": {
        "sections": [
            {
                "title": "¿Qué es la Felicidad?",
                "content": "La felicidad (happiness) es uno de los sentimientos más buscados en la vida. En diferentes culturas tiene diferentes significados: para algunos es logro material, para otros es paz interior, para otros es conexión social. En esta sección exploramos cómo el inglés nos ayuda a hablar sobre este concepto universal."
            },
            {
                "title": "Vocabulario de Emociones",
                "content": "Happy (feliz), content (satisfecho), joyful (gozoso), cheerful (alegre), blissful (dichoso), delighted (encantado). Cada palabra tiene matices diferentes que permiten expresar niveles distintos de felicidad."
            },
            {
                "title": "Factores de la Felicidad",
                "content": "Relaciones (relationships), logros (achievements), salud (health), propósito (purpose), gratitud (gratitude). Al hablar sobre qué nos hace felices, usamos este vocabulario para expresar qué es importante para nosotros."
            }
        ]
    },
    "Internet y el cerebro": {
        "sections": [
            {
                "title": "Cómo Internet Afecta el Cerebro",
                "content": "Research (investigación) ha mostrado que internet cambia cómo pensamos, recordamos y nos concentramos. Términos como dopamine, attention span, digital addiction son cruciales para esta conversación."
            },
            {
                "title": "Vocabulario Técnico",
                "content": "Neural pathways (caminos neurales), screen time (tiempo de pantalla), cognitive load (carga cognitiva), digital distraction (distracción digital). Estos términos permiten análisis profundos sobre impacto de tecnología."
            },
            {
                "title": "Impacto Social",
                "content": "Debatir sobre si internet nos vuelve más inteligentes o menos atentos, cómo afecta a jóvenes, y cómo mantener equilibrio saludable con la tecnología."
            }
        ]
    },
    "Inteligencia": {
        "sections": [
            {
                "title": "Tipos de Inteligencia",
                "content": "Intelligence (inteligencia) no es solo IQ. Howard Gardner describió múltiples tipos: linguistic, logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal, intrapersonal, naturalistic."
            },
            {
                "title": "Midiendo Inteligencia",
                "content": "IQ test, problem-solving, creativity, adaptability. Diferentes culturas valoran diferentes aspectos de la inteligencia."
            },
            {
                "title": "Inteligencia Emocional",
                "content": "Emotional intelligence (IE) es cada vez más valorada en el mundo laboral moderno. Incluye self-awareness, empathy, social skills, self-regulation."
            }
        ]
    },
    "Gustos musicales": {
        "sections": [
            {
                "title": "Géneros Musicales",
                "content": "Rock, pop, jazz, classical, hip-hop, country, electronic, indie, folk, reggae. Cada género tiene características distintas y culturas asociadas."
            },
            {
                "title": "Describiendo Música",
                "content": "Melody (melodía), rhythm (ritmo), harmony (armonía), beat (pulso), tempo (tempo). Estos términos te permiten describir qué te gusta sobre la música de forma técnica."
            },
            {
                "title": "Argumentando Gustos",
                "content": "I prefer rock because... / I'm not into pop because... / I appreciate classical music for its complexity. Expresar por qué te gusta algo es más interesante que solo decir que te gusta."
            }
        ]
    },
    "Gastos": {
        "sections": [
            {
                "title": "Categorías de Gastos",
                "content": "Housing (vivienda), food (comida), transportation (transporte), entertainment (entretenimiento), utilities (servicios), education (educación). Entender estas categorías es esencial para hablar sobre dinero."
            },
            {
                "title": "Verbos de Dinero",
                "content": "Spend (gastar), cost (costar), afford (poder permitirse), save (ahorrar), invest (invertir), budget (presupuestar). Estos verbos te permiten hablar sobre acciones financieras."
            },
            {
                "title": "Prudencia Financiera",
                "content": "Unnecessary spending (gasto innecesario), impulse purchase (compra impulsiva), financial planning (planificación financiera). Aprender a hablar sobre finanzas inteligentes."
            }
        ]
    },
    "Dispositivos": {
        "sections": [
            {
                "title": "Tecnología Cotidiana",
                "content": "Smartphone, laptop, tablet, smartwatch, headphones, camera. Estos dispositivos están en nuestras vidas diarias y necesitamos vocabulario para hablar sobre ellos."
            },
            {
                "title": "Características y Funciones",
                "content": "Display, processor, battery, memory, storage, camera quality. Al describir dispositivos, necesitas vocabulario técnico pero accesible."
            },
            {
                "title": "Impacto en Nuestras Vidas",
                "content": "Connectivity (conectividad), convenience (conveniencia), distraction (distracción), dependence (dependencia). Estos conceptos permiten reflexionar sobre nuestra relación con la tecnología."
            }
        ]
    },
    "Maravillas naturales": {
        "sections": [
            {
                "title": "Paisajes Espectaculares",
                "content": "Mountains (montañas), waterfalls (cascadas), forests (bosques), beaches (playas), deserts (desiertos), canyons (cañones). El mundo natural ofrece una variedad inmensa de paisajes."
            },
            {
                "title": "Describiendo la Naturaleza",
                "content": "Breathtaking (impresionante), majestic (majestuoso), pristine (prístino), rugged (accidentado), serene (sereno), lush (exuberante). Estos adjetivos enriquecen tu descripción de la naturaleza."
            },
            {
                "title": "Conservación",
                "content": "Muchas maravillas naturales están amenazadas. Términos como endangered, protected status, conservation effort son cruciales en conversaciones modernas."
            }
        ]
    },
    "Noticias online": {
        "sections": [
            {
                "title": "Fuentes de Noticias",
                "content": "News outlet (medio de comunicación), journalist (periodista), editor, publisher (editorial). Entender la estructura de las organizaciones de medios ayuda a analizar noticias críticamente."
            },
            {
                "title": "Tipos de Noticias",
                "content": "Breaking news (noticias de última hora), feature story (reportaje), opinion piece (artículo de opinión), investigative journalism (periodismo investigativo), bias (sesgo)."
            },
            {
                "title": "Lectura Crítica",
                "content": "Source credibility (credibilidad de fuente), fact-checking (verificación de hechos), misinformation (desinformación), fake news. Estas habilidades son vitales hoy."
            }
        ]
    }
}

def init_app():
    """Inicializar la aplicación"""
    app = create_app()
    return app


def populate_unit_explanations(app):
    """Poblar explicaciones de unidades"""
    count = 0
    
    for unit_number, explanation_data in UNIT_EXPLANATIONS.items():
        unit = Unit.query.filter_by(unit_number=unit_number).first()
        
        if not unit:
            print(f"⚠️ Unidad {unit_number} no encontrada")
            continue
        
        # Actualizar datos de la unidad
        unit.overview = explanation_data["overview"]
        unit.detailed_explanation = explanation_data["detailed_explanation"]
        unit.learning_objectives = explanation_data["learning_objectives"]
        
        # Crear explicaciones por sección
        for order, section in enumerate(explanation_data.get("sections", []), 1):
            existing = UnitExplanation.query.filter_by(
                unit_id=unit.id,
                section_title=section["title"]
            ).first()
            
            if not existing:
                explanation = UnitExplanation(
                    unit_id=unit.id,
                    section_title=section["title"],
                    content=section["content"],
                    order=order
                )
                db.session.add(explanation)
                count += 1
        
        db.session.commit()
    
    print(f"✓ {count} secciones de explicación de unidades agregadas")


def populate_topic_explanations(app):
    """Poblar explicaciones de temas"""
    count = 0
    
    for topic_name, explanation_data in TOPIC_EXPLANATIONS.items():
        topics = Topic.query.filter_by(title=topic_name).all()
        
        if not topics:
            print(f"⚠️ Tema '{topic_name}' no encontrado")
            continue
        
        for topic in topics:
            # Actualizar datos del tema si lo tiene
            if "key_concepts" in explanation_data:
                topic.key_concepts = explanation_data.get("key_concepts")
            if "common_mistakes" in explanation_data:
                topic.common_mistakes = explanation_data.get("common_mistakes")
            
            # Crear explicaciones por sección
            for order, section in enumerate(explanation_data.get("sections", []), 1):
                existing = TopicExplanation.query.filter_by(
                    topic_id=topic.id,
                    section_title=section["title"]
                ).first()
                
                if not existing:
                    explanation = TopicExplanation(
                        topic_id=topic.id,
                        section_title=section["title"],
                        content=section["content"],
                        order=order
                    )
                    db.session.add(explanation)
                    count += 1
            
            db.session.commit()
    
    print(f"✓ {count} secciones de explicación de temas agregadas")


def main():
    """Ejecutar poblado de explicaciones"""
    try:
        print("\n🎓 Iniciando poblado de explicaciones...\n")
        
        # Crear aplicación e inicializar
        app = init_app()
        
        with app.app_context():
            # Crear tablas si no existen
            db.create_all()
            print("✓ Tablas de explicaciones creadas/verificadas\n")
            
            populate_unit_explanations(app)
            print()
            populate_topic_explanations(app)
        
        print("\n✅ Explicaciones pobladas exitosamente!\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
