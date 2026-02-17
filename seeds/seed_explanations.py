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

# Explicaciones de temas específicos - Actualizados para coincidir con la BD
TOPIC_EXPLANATIONS = {
    # === A1 TOPICS ===
    "Clothes": {
        "sections": [
            {
                "title": "Vocabulario de Ropa",
                "content": "Shirt (camisa), pants/trousers (pantalones), dress (vestido), skirt (falda), shoes (zapatos), jacket (chaqueta), coat (abrigo), hat (sombrero), socks (calcetines), underwear (ropa interior). Este vocabulario básico te permite hablar sobre lo que llevas puesto."
            },
            {
                "title": "Describiendo Ropa",
                "content": "Big/small, long/short, tight/loose, comfortable, stylish, casual, formal. Usa estos adjetivos para describir cómo te queda la ropa: 'This shirt is too tight' o 'These shoes are very comfortable'."
            },
            {
                "title": "Comprando Ropa",
                "content": "Can I try this on? / What size is this? / Do you have this in blue? / How much does it cost? Frases esenciales para ir de compras en países de habla inglesa."
            }
        ]
    },
    "Weather": {
        "sections": [
            {
                "title": "Condiciones Climáticas",
                "content": "Sunny (soleado), cloudy (nublado), rainy (lluvioso), windy (ventoso), snowy (nevado), foggy (neblinoso), stormy (tormentoso). Vocabulario esencial para hablar sobre el clima."
            },
            {
                "title": "Expresiones del Clima",
                "content": "It's hot/cold/warm/cool. It's raining/snowing. The sun is shining. It's pouring (llueve a cántaros). There's a storm coming. Aprende a describir el tiempo atmosférico."
            },
            {
                "title": "Conversación sobre el Clima",
                "content": "En inglés, hablar del clima es muy común para iniciar conversaciones: 'Nice weather, isn't it?' / 'Terrible day, right?' Es una forma educada de romper el hielo."
            }
        ]
    },
    "Hobbies": {
        "sections": [
            {
                "title": "Pasatiempos Comunes",
                "content": "Reading (leer), swimming (nadar), playing sports (hacer deportes), cooking (cocinar), gardening (jardinería), painting (pintar), playing music (tocar música), watching movies (ver películas)."
            },
            {
                "title": "Hablando de Gustos",
                "content": "I like/love/enjoy + gerund: 'I love reading books' / 'I enjoy playing tennis'. Para negativos: 'I don't like cooking' / 'I hate waking up early'."
            },
            {
                "title": "Preguntas sobre Hobbies",
                "content": "What do you like to do in your free time? / Do you have any hobbies? / What are you into? / How often do you...? Preguntas útiles para conocer a alguien."
            }
        ]
    },
    "Body Parts": {
        "sections": [
            {
                "title": "Partes del Cuerpo",
                "content": "Head (cabeza), face (cara), eyes (ojos), nose (nariz), mouth (boca), ears (orejas), arms (brazos), hands (manos), fingers (dedos), legs (piernas), feet (pies), back (espalda)."
            },
            {
                "title": "Describiendo Personas",
                "content": "She has blue eyes. He has long hair. They are tall/short. She has a beautiful smile. Usa 'have/has' para describir características físicas."
            },
            {
                "title": "En el Médico",
                "content": "My head hurts. I have a stomachache. My arm is broken. I feel dizzy. Vocabulario esencial para describir problemas de salud y visitar al doctor."
            }
        ]
    },
    # === A2-B1 TOPICS ===
    "Sports": {
        "sections": [
            {
                "title": "Deportes Populares",
                "content": "Football/Soccer, basketball, tennis, swimming, running, cycling, volleyball, golf, baseball, rugby. Cada deporte tiene su propio vocabulario específico."
            },
            {
                "title": "Vocabulario Deportivo",
                "content": "Match/game (partido), team (equipo), player (jugador), coach (entrenador), score (puntuación), win/lose/draw (ganar/perder/empatar), championship (campeonato)."
            },
            {
                "title": "Hablando de Deportes",
                "content": "I play tennis. I go swimming. I do yoga. Nota: usamos 'play' para deportes de equipo, 'go' para actividades terminadas en -ing, y 'do' para artes marciales y yoga."
            }
        ]
    },
    "Conservation": {
        "sections": [
            {
                "title": "Vocabulario Ambiental",
                "content": "Environment (medio ambiente), pollution (contaminación), recycling (reciclaje), climate change (cambio climático), renewable energy (energía renovable), endangered species (especies en peligro)."
            },
            {
                "title": "Acciones Ecológicas",
                "content": "Reduce, reuse, recycle. Save water/energy. Use public transport. Plant trees. Avoid plastic. Frases para hablar sobre cómo cuidar el planeta."
            },
            {
                "title": "Problemas Ambientales",
                "content": "Deforestation (deforestación), global warming (calentamiento global), ocean pollution (contaminación oceánica), extinction (extinción). Vocabulario para discutir problemas ecológicos."
            }
        ]
    },
    "Artificial Intelligence": {
        "sections": [
            {
                "title": "Conceptos Básicos de IA",
                "content": "Artificial Intelligence (IA), machine learning (aprendizaje automático), algorithm (algoritmo), data (datos), neural network (red neuronal), automation (automatización)."
            },
            {
                "title": "Aplicaciones de IA",
                "content": "Virtual assistants (asistentes virtuales), self-driving cars (coches autónomos), facial recognition (reconocimiento facial), chatbots, recommendation systems (sistemas de recomendación)."
            },
            {
                "title": "Debate sobre IA",
                "content": "Will AI replace jobs? Is AI dangerous? Can machines think? Vocabulario y estructuras para debatir sobre el impacto de la inteligencia artificial en la sociedad."
            }
        ]
    },
    "Climate Change": {
        "sections": [
            {
                "title": "Causas del Cambio Climático",
                "content": "Greenhouse gases (gases de efecto invernadero), carbon emissions (emisiones de carbono), fossil fuels (combustibles fósiles), deforestation (deforestación)."
            },
            {
                "title": "Efectos del Cambio Climático",
                "content": "Rising sea levels (aumento del nivel del mar), extreme weather (clima extremo), droughts (sequías), floods (inundaciones), melting ice caps (derretimiento de glaciares)."
            },
            {
                "title": "Soluciones",
                "content": "Renewable energy, carbon neutrality, sustainable development, international agreements. Vocabulario para discutir soluciones al cambio climático."
            }
        ]
    },
    # === B2-C1 TOPICS ===
    "Advertising": {
        "sections": [
            {
                "title": "Vocabulario Publicitario",
                "content": "Advertisement/ad (anuncio), commercial (comercial de TV), billboard (valla publicitaria), brand (marca), slogan, target audience (público objetivo), campaign (campaña)."
            },
            {
                "title": "Técnicas Publicitarias",
                "content": "Emotional appeal, celebrity endorsement, product placement, social media marketing, influencer marketing. Técnicas que las marcas usan para venderte productos."
            },
            {
                "title": "Análisis Crítico",
                "content": "What message is this ad sending? Who is the target audience? What techniques are being used? Preguntas para analizar publicidad críticamente."
            }
        ]
    },
    "Critical Analysis": {
        "sections": [
            {
                "title": "Pensamiento Crítico",
                "content": "Analyze (analizar), evaluate (evaluar), interpret (interpretar), argue (argumentar), conclude (concluir). Verbos esenciales para el análisis crítico."
            },
            {
                "title": "Estructuras de Análisis",
                "content": "The author argues that... / This suggests... / However, one could argue... / In conclusion... Frases académicas para presentar análisis."
            },
            {
                "title": "Evaluando Fuentes",
                "content": "Is this source reliable? What is the author's bias? Is the evidence sufficient? Preguntas clave para evaluar información críticamente."
            }
        ]
    },
    "Creativity": {
        "sections": [
            {
                "title": "¿Qué es la Creatividad?",
                "content": "Creativity (creatividad), imagination (imaginación), innovation (innovación), originality (originalidad), inspiration (inspiración). Vocabulario para hablar sobre el proceso creativo."
            },
            {
                "title": "Expresión Creativa",
                "content": "Art, music, writing, design, photography, dance. Diferentes formas de expresar creatividad y el vocabulario asociado a cada una."
            },
            {
                "title": "Fomentando la Creatividad",
                "content": "Think outside the box. Brainstorm ideas. Take risks. Learn from failure. Expresiones para hablar sobre cómo desarrollar la creatividad."
            }
        ]
    },
    "Banking": {
        "sections": [
            {
                "title": "Vocabulario Bancario",
                "content": "Account (cuenta), savings (ahorros), checking account (cuenta corriente), loan (préstamo), interest (interés), mortgage (hipoteca), credit card (tarjeta de crédito)."
            },
            {
                "title": "Transacciones",
                "content": "Deposit (depositar), withdraw (retirar), transfer (transferir), pay (pagar), balance (saldo). Verbos esenciales para operaciones bancarias."
            },
            {
                "title": "En el Banco",
                "content": "I'd like to open an account. / Can I withdraw $100? / What's my balance? / I need to apply for a loan. Frases útiles para visitar un banco."
            }
        ]
    },
    # === C1-C2 TOPICS ===
    "Cognitive Psychology": {
        "sections": [
            {
                "title": "Procesos Cognitivos",
                "content": "Memory (memoria), attention (atención), perception (percepción), reasoning (razonamiento), decision-making (toma de decisiones). Procesos mentales fundamentales."
            },
            {
                "title": "Teorías Cognitivas",
                "content": "Information processing, schema theory, cognitive load theory. Teorías que explican cómo pensamos y aprendemos."
            },
            {
                "title": "Aplicaciones",
                "content": "Learning strategies, memory techniques, mindfulness, cognitive behavioral therapy. Aplicaciones prácticas de la psicología cognitiva."
            }
        ]
    },
    "Bioethics": {
        "sections": [
            {
                "title": "Dilemas Bioéticos",
                "content": "Euthanasia, genetic engineering, cloning, organ donation, stem cell research. Temas controvertidos que requieren vocabulario especializado."
            },
            {
                "title": "Argumentación Ética",
                "content": "It's morally acceptable because... / The ethical implications are... / From a utilitarian perspective... Estructuras para debatir temas éticos."
            },
            {
                "title": "Perspectivas",
                "content": "Medical ethics, religious views, legal considerations, patient rights. Diferentes perspectivas para analizar dilemas bioéticos."
            }
        ]
    },
    "Art Movements": {
        "sections": [
            {
                "title": "Movimientos Artísticos",
                "content": "Renaissance, Baroque, Impressionism, Expressionism, Cubism, Surrealism, Pop Art, Contemporary Art. Historia del arte a través de sus movimientos."
            },
            {
                "title": "Características",
                "content": "Style (estilo), technique (técnica), composition (composición), color palette (paleta de colores), subject matter (temática). Vocabulario para describir arte."
            },
            {
                "title": "Análisis Artístico",
                "content": "This painting represents... / The artist conveys... / The use of light suggests... Frases para analizar obras de arte."
            }
        ]
    },
    "Academic Conventions": {
        "sections": [
            {
                "title": "Escritura Académica",
                "content": "Thesis statement (tesis), argument (argumento), evidence (evidencia), citation (cita), bibliography (bibliografía). Elementos esenciales de escritura académica."
            },
            {
                "title": "Registro Formal",
                "content": "It is argued that... / Research indicates... / According to... / In conclusion... Lenguaje formal para contextos académicos."
            },
            {
                "title": "Estructuras",
                "content": "Introduction, body paragraphs, conclusion. Topic sentence, supporting details, transition words. Estructura de ensayos académicos."
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
