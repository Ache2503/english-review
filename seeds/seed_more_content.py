#!/usr/bin/env python3
"""
Script para agregar más lecturas, mensajes motivacionales y vocabulario.
Ejecutar: python seed_more_content.py
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Unit, Reading, MotivationalMessage, VocabularyCategory, VocabularyItem

EXTRA_MESSAGES = [
    {
        "title": "Enfoque en el Proceso",
        "content": "No busques perfección inmediata. Enfócate en mejorar cada día un poco más.",
        "icon": "🪴",
    },
    {
        "title": "Autoempatía",
        "content": "Si hoy te equivocas, no pasa nada. Estás entrenando tu cerebro, no tomando un examen final.",
        "icon": "🤝",
    },
    {
        "title": "Micro‑metas",
        "content": "Divide el aprendizaje en pasos pequeños. 5 nuevas palabras hoy es mejor que 0.",
        "icon": "🎯",
    },
    {
        "title": "Confianza en tu Voz",
        "content": "Hablar imperfecto es normal. Tu cerebro aprende cuando practicas en voz alta.",
        "icon": "🗣️",
    },
    {
        "title": "Lectura Estratégica",
        "content": "No necesitas entender cada palabra. Enfócate en la idea principal.",
        "icon": "📌",
    },
    {
        "title": "Constancia",
        "content": "Un poco cada día vence a mucho una sola vez. La disciplina gana.",
        "icon": "📅",
    },
    {
        "title": "Mentalidad Positiva",
        "content": "Si te cuesta, significa que estás avanzando. Lo fácil no cambia tu nivel.",
        "icon": "💡",
    },
    {
        "title": "Curiosidad",
        "content": "Explora temas que te gusten en inglés. La curiosidad acelera el aprendizaje.",
        "icon": "🔍",
    },
]

EXTRA_READINGS = {
    7: [
        {
            "title": "La Atención Plena y la Mente",
            "content": """Mindfulness is the practice of paying attention to the present moment. Many people live in the past or worry about the future. This creates anxiety and stress. Mindfulness teaches us to focus on what is happening right now: our breathing, our body, and our thoughts. When you practice mindfulness, you notice your thoughts without judging them. This helps you control your reactions. Studies show that people who practice mindfulness sleep better and feel more calm. It is not about stopping thoughts. It is about observing them. You can start with just five minutes a day. Sit quietly, breathe slowly, and notice how you feel. Over time, your mind becomes clearer and more focused.""",
            "instructions": "Extrae 3-4 oraciones sobre qué es el mindfulness y sus beneficios.",
            "difficulty": "intermediate",
        }
    ],
    8: [
        {
            "title": "El Arte de Contar Historias",
            "content": """Storytelling is a powerful form of art. A good story creates emotion, teaches lessons, and connects people. When we hear stories, our brains activate areas related to feeling and memory. This is why we remember stories more than facts. In movies, books, and music, storytelling helps us understand different lives. A story about a child in another country can teach us empathy. Storytelling also helps us explain our own experiences. When you tell a story, you organize your ideas and feelings. Great artists and speakers use stories to inspire change. You do not need to be a writer to be a storyteller. Everyone has a story worth sharing.""",
            "instructions": "Extrae 3-4 oraciones sobre por qué contar historias es importante.",
            "difficulty": "intermediate",
        }
    ],
    9: [
        {
            "title": "El Ahorro Inteligente en la Vida Diaria",
            "content": """Saving money does not always require a high salary. Many people can save by changing small habits. For example, cooking at home instead of eating out can save a lot. Another method is to track your spending every week. When you see where your money goes, you can make better choices. Some people use the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings. Even saving a small amount consistently builds a habit. Over time, this habit creates financial security. Saving is not only about money. It is about control and peace of mind. When you have savings, you feel less stress. You can handle emergencies without panic.""",
            "instructions": "Extrae 3-4 oraciones sobre hábitos de ahorro.",
            "difficulty": "beginner",
        }
    ],
    10: [
        {
            "title": "Tecnología Verde y Futuro Sostenible",
            "content": """Green technology helps reduce pollution and save energy. Solar panels convert sunlight into electricity. Wind turbines create clean energy from wind. Electric cars reduce the use of gasoline. These technologies are becoming cheaper and more efficient. Governments and companies invest billions in green innovation. This creates new jobs and new skills. Green technology also changes how cities work. Smart traffic systems reduce congestion. Energy‑efficient buildings use less electricity. The future of technology is not only faster; it is cleaner and more responsible. If we want a healthier planet, we need to support green solutions.""",
            "instructions": "Extrae 3-4 oraciones sobre tecnología verde.",
            "difficulty": "intermediate",
        }
    ],
    11: [
        {
            "title": "Bosques y Clima",
            "content": """Forests are essential for the planet. They absorb carbon dioxide and produce oxygen. When forests are destroyed, more CO2 stays in the air. This increases global warming. Forests are also home to millions of species. Deforestation threatens animals and plants. Many communities depend on forests for food and water. Protecting forests is one of the fastest ways to fight climate change. Reforestation programs plant new trees and restore ecosystems. Every tree matters. When people protect forests, they protect the future.""",
            "instructions": "Extrae 3-4 oraciones sobre la importancia de los bosques.",
            "difficulty": "beginner",
        }
    ],
    12: [
        {
            "title": "Movilidad Urbana Inteligente",
            "content": """Cities are redesigning transportation to reduce traffic and pollution. Many cities are building bike lanes and improving public transport. Electric buses and trains reduce emissions. Some cities use smart traffic lights to manage flow. This reduces time wasted in traffic. When transportation is efficient, people have more time and less stress. Urban mobility also improves health because walking and cycling are common. The best cities prioritize people, not cars. A well‑designed city makes life easier for everyone.""",
            "instructions": "Extrae 3-4 oraciones sobre movilidad urbana.",
            "difficulty": "intermediate",
        }
    ],
}

EXTRA_VOCAB = [
    # Unit 7
    {"unit": 7, "category": "Sentimientos", "word": "anxious", "definition": "sentirse ansioso o nervioso", "example": "I feel anxious before exams."},
    {"unit": 7, "category": "Sentimientos", "word": "relieved", "definition": "aliviado", "example": "She felt relieved after the test."},
    {"unit": 7, "category": "Sentimientos", "word": "confident", "definition": "confiado", "example": "I feel confident today."},
    {"unit": 7, "category": "Sentimientos", "word": "overwhelmed", "definition": "abrumado", "example": "He felt overwhelmed at work."},
    {"unit": 7, "category": "Phrasal Verbs", "word": "calm down", "definition": "calmarse", "example": "Take a deep breath and calm down."},
    {"unit": 7, "category": "Phrasal Verbs", "word": "cheer up", "definition": "animarse", "example": "Music helps me cheer up."},
    {"unit": 7, "category": "Phrasal Verbs", "word": "think over", "definition": "pensar cuidadosamente", "example": "I need to think over the decision."},
    {"unit": 7, "category": "Phrasal Verbs", "word": "deal with", "definition": "lidiar con", "example": "She can deal with stress."},
    # Unit 8
    {"unit": 8, "category": "Géneros de Música", "word": "classical", "definition": "música clásica", "example": "Classical music helps me focus."},
    {"unit": 8, "category": "Géneros de Música", "word": "jazz", "definition": "jazz", "example": "Jazz is creative and energetic."},
    {"unit": 8, "category": "Géneros de Música", "word": "hip-hop", "definition": "hip‑hop", "example": "Hip-hop is popular worldwide."},
    {"unit": 8, "category": "Géneros de Música", "word": "soundtrack", "definition": "banda sonora", "example": "The soundtrack was amazing."},
    {"unit": 8, "category": "Cine y Películas", "word": "plot", "definition": "trama", "example": "The plot was very interesting."},
    {"unit": 8, "category": "Cine y Películas", "word": "character", "definition": "personaje", "example": "My favorite character is the hero."},
    {"unit": 8, "category": "Cine y Películas", "word": "director", "definition": "director", "example": "The director won an award."},
    {"unit": 8, "category": "Cine y Películas", "word": "scene", "definition": "escena", "example": "That scene was emotional."},
    # Unit 9
    {"unit": 9, "category": "Make vs Do", "word": "make a decision", "definition": "tomar una decisión", "example": "I need to make a decision."},
    {"unit": 9, "category": "Make vs Do", "word": "do business", "definition": "hacer negocios", "example": "They do business internationally."},
    {"unit": 9, "category": "Make vs Do", "word": "make progress", "definition": "hacer progreso", "example": "We made progress this week."},
    {"unit": 9, "category": "Make vs Do", "word": "do research", "definition": "hacer investigación", "example": "They do research at the lab."},
    {"unit": 9, "category": "Frases de Dinero", "word": "save up", "definition": "ahorrar para algo", "example": "I save up for a new phone."},
    {"unit": 9, "category": "Frases de Dinero", "word": "pay back", "definition": "devolver dinero", "example": "I'll pay you back tomorrow."},
    {"unit": 9, "category": "Frases de Dinero", "word": "cut costs", "definition": "reducir gastos", "example": "We need to cut costs."},
    {"unit": 9, "category": "Frases de Dinero", "word": "on a budget", "definition": "con presupuesto limitado", "example": "I'm on a budget this month."},
    # Unit 10
    {"unit": 10, "category": "Dispositivos Electrónicos", "word": "headphones", "definition": "auriculares", "example": "I use headphones to listen to music."},
    {"unit": 10, "category": "Dispositivos Electrónicos", "word": "charger", "definition": "cargador", "example": "My phone needs a charger."},
    {"unit": 10, "category": "Dispositivos Electrónicos", "word": "smartwatch", "definition": "reloj inteligente", "example": "My smartwatch tracks my steps."},
    {"unit": 10, "category": "Dispositivos Electrónicos", "word": "tablet", "definition": "tableta", "example": "I read on my tablet."},
    {"unit": 10, "category": "Colocaciones de Ciencia", "word": "run experiments", "definition": "realizar experimentos", "example": "Scientists run experiments in labs."},
    {"unit": 10, "category": "Colocaciones de Ciencia", "word": "collect data", "definition": "recopilar datos", "example": "We collect data every day."},
    {"unit": 10, "category": "Colocaciones de Ciencia", "word": "test a hypothesis", "definition": "probar una hipótesis", "example": "They test a hypothesis."},
    {"unit": 10, "category": "Colocaciones de Ciencia", "word": "conduct research", "definition": "realizar investigación", "example": "We conduct research in space."},
    # Unit 11
    {"unit": 11, "category": "Animales en Peligro", "word": "habitat", "definition": "hábitat", "example": "The forest is its natural habitat."},
    {"unit": 11, "category": "Animales en Peligro", "word": "endangered", "definition": "en peligro de extinción", "example": "The tiger is endangered."},
    {"unit": 11, "category": "Animales en Peligro", "word": "conservation", "definition": "conservación", "example": "Conservation protects wildlife."},
    {"unit": 11, "category": "Animales en Peligro", "word": "wildlife", "definition": "vida silvestre", "example": "Wildlife needs protection."},
    {"unit": 11, "category": "Características Naturales", "word": "waterfall", "definition": "cascada", "example": "We visited a beautiful waterfall."},
    {"unit": 11, "category": "Características Naturales", "word": "mountain range", "definition": "cordillera", "example": "The Andes is a mountain range."},
    {"unit": 11, "category": "Características Naturales", "word": "river basin", "definition": "cuenca del río", "example": "The river basin is large."},
    {"unit": 11, "category": "Características Naturales", "word": "coastline", "definition": "línea costera", "example": "The coastline is rocky."},
    # Unit 12
    {"unit": 12, "category": "Expresiones de Noticias", "word": "breaking news", "definition": "noticia de última hora", "example": "Breaking news is on TV."},
    {"unit": 12, "category": "Expresiones de Noticias", "word": "headline", "definition": "titular", "example": "The headline was surprising."},
    {"unit": 12, "category": "Expresiones de Noticias", "word": "press release", "definition": "comunicado de prensa", "example": "They issued a press release."},
    {"unit": 12, "category": "Expresiones de Noticias", "word": "coverage", "definition": "cobertura (mediática)", "example": "The event got wide coverage."},
    {"unit": 12, "category": "Publicidad y Medios", "word": "advertisement", "definition": "anuncio", "example": "The advertisement was creative."},
    {"unit": 12, "category": "Publicidad y Medios", "word": "audience", "definition": "audiencia", "example": "The audience was large."},
    {"unit": 12, "category": "Publicidad y Medios", "word": "campaign", "definition": "campaña", "example": "The campaign was successful."},
    {"unit": 12, "category": "Publicidad y Medios", "word": "brand", "definition": "marca", "example": "The brand is well known."},
]


def seed_more_messages():
    print("Agregando más mensajes motivacionales...")
    added = 0
    for msg in EXTRA_MESSAGES:
        existing = MotivationalMessage.query.filter_by(title=msg["title"]).first()
        if not existing:
            db.session.add(MotivationalMessage(
                title=msg["title"],
                content=msg["content"],
                icon=msg.get("icon"),
                is_active=True,
                order=len(MotivationalMessage.query.all())
            ))
            added += 1
    db.session.commit()
    print(f"✓ Mensajes agregados: {added}")


def seed_more_readings():
    print("Agregando más lecturas...")
    added = 0
    for unit_number, readings in EXTRA_READINGS.items():
        unit = Unit.query.filter_by(unit_number=unit_number).first()
        if not unit:
            continue
        current_max = db.session.query(db.func.max(Reading.order)).filter_by(unit_id=unit.id).scalar() or 0
        for idx, data in enumerate(readings, start=1):
            existing = Reading.query.filter_by(unit_id=unit.id, title=data["title"]).first()
            if existing:
                continue
            reading = Reading(
                unit_id=unit.id,
                title=data["title"],
                content=data["content"],
                instructions=data["instructions"],
                difficulty=data["difficulty"],
                order=current_max + idx
            )
            db.session.add(reading)
            added += 1
    db.session.commit()
    print(f"✓ Lecturas agregadas: {added}")


def seed_more_vocab():
    print("Agregando más vocabulario...")
    added = 0
    skipped = 0

    for item in EXTRA_VOCAB:
        unit = Unit.query.filter_by(unit_number=item["unit"]).first()
        if not unit:
            skipped += 1
            continue

        category = VocabularyCategory.query.filter_by(unit_id=unit.id, category_name=item["category"]).first()
        if not category:
            category = VocabularyCategory.query.filter_by(unit_id=unit.id).order_by(VocabularyCategory.order).first()
        if not category:
            skipped += 1
            continue

        existing = VocabularyItem.query.filter_by(category_id=category.id, word=item["word"]).first()
        if existing:
            skipped += 1
            continue

        vocab = VocabularyItem(
            category_id=category.id,
            word=item["word"],
            definition=item["definition"],
            example=item["example"],
            order=0
        )
        db.session.add(vocab)
        added += 1

    db.session.commit()
    print(f"✓ Vocabulario agregado: {added}")
    print(f"- Omitidos: {skipped}")


def main():
    app = create_app('development')
    with app.app_context():
        print("=" * 70)
        print("AGREGANDO CONTENIDO EXTRA (LECTURAS, MENSAJES, VOCABULARIO)")
        print("=" * 70)
        seed_more_readings()
        seed_more_messages()
        seed_more_vocab()
        print("=" * 70)
        print("✅ CONTENIDO EXTRA AGREGADO")


if __name__ == '__main__':
    main()
