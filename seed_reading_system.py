#!/usr/bin/env python
"""Script para poblar la BD con mensajes motivacionales y lecturas de ejemplo"""

import sys
from pathlib import Path

proj_dir = Path(__file__).parent
sys.path.insert(0, str(proj_dir))

from app import create_app, db
from app.models import Unit, MotivationalMessage, Reading

app = create_app('development')

# Mensajes motivacionales genéricos
MOTIVATIONAL_MESSAGES = [
    {
        "title": "Mentalidad de Crecimiento",
        "content": "No necesitas entender todo desde el inicio. La idea es lo más importante. Con la práctica, todo te resultará más claro.",
        "icon": "🧠",
    },
    {
        "title": "Errores son Oportunidades",
        "content": "Cada error es una oportunidad de aprendizaje. Los mejores estudiantes cometen muchos errores. ¡Sigue adelante!",
        "icon": "✨",
    },
    {
        "title": "Progreso Consistente",
        "content": "No importa qué tan lentamente avances, siempre que no pares estás progresando. La consistencia es clave.",
        "icon": "💪",
    },
    {
        "title": "Confianza en Uno Mismo",
        "content": "Ya has aprendido más de lo que crees. Confía en tu progreso y en tu capacidad de aprender.",
        "icon": "🌟",
    },
    {
        "title": "Práctica Deliberada",
        "content": "La práctica perfecta hace al maestro. Enfócate en los puntos débiles, no solo en lo que ya sabes hacer bien.",
        "icon": "🎯",
    },
    {
        "title": "Comparación con Otros",
        "content": "Tu único competidor eres tú mismo. Celebra tu progreso personal, no compares con otros.",
        "icon": "🏆",
    },
    {
        "title": "Tiempo y Paciencia",
        "content": "El idioma toma tiempo. Sé paciente contigo mismo. Cada día es una nueva oportunidad para mejorar.",
        "icon": "⏰",
    },
    {
        "title": "Conecta con la Lengua",
        "content": "Busca contenido que te apasione en inglés: películas, música, blogs. El aprendizaje es más fácil con entusiasmo.",
        "icon": "❤️",
    },
    {
        "title": "Pequeños Pasos",
        "content": "No necesitas dominar todo a la vez. Pequeños pasos consistentes te llevarán lejos. Celebra cada logro.",
        "icon": "👣",
    },
    {
        "title": "Salida de Zona de Confort",
        "content": "Hablar un idioma imperfecto es mejor que no hablar. Salte de tu zona de confort seguro.",
        "icon": "🚀",
    },
]

# Lecturas de ejemplo para Unit 7 (MIND)
UNIT_7_READINGS = [
    {
        "title": "La Felicidad es Diferente para Todos",
        "content": """In our modern world, many people search for happiness but don't know where to look. Some think happiness comes from money and expensive things. Others believe it comes from success and recognition. However, true happiness is different for everyone.

Research shows that happiness comes from simple things: good relationships, physical health, and doing what you love. Studies show that people who spend time with family and friends are happier. Exercise also increases happiness. Most importantly, doing activities that interest you brings real joy.

Many successful people say they used to think money was everything. Now they realize it's not. They found happiness in helping others, learning new things, or spending time in nature. The internet has changed how we think about happiness. We see other people's highlight reels and think their lives are perfect. But nobody's life is perfect. Everyone faces challenges.

The key to happiness is finding what matters to you personally. Maybe it's painting, reading, sports, or teaching. When you focus on what makes YOU happy, not what society tells you should make you happy, life becomes better. Happiness is a journey, not a destination.""",
        "instructions": "Extrae 3-4 oraciones importantes que hablen sobre qué es la felicidad.",
        "difficulty": "beginner",
    },
    {
        "title": "Cómo Internet Cambió Nuestro Cerebro",
        "content": """The internet has changed the way our brains work. Twenty years ago, people had better attention spans. They could read long books and remember details. Today, our brains are used to quick information and constant notifications.

Research from universities shows that heavy internet users have different brain patterns. Their brains become used to receiving small amounts of information quickly. Scientists call this "attention fragmentation." Young people who grew up with smartphones have never experienced different brain patterns.

There are both positive and negative effects. Positive effects: we can learn anything quickly, we can connect with people worldwide, we can solve problems faster. Negative effects: we struggle with deep thinking, we get anxious without our phones, we forget information more easily.

The key is balance. Studies show that people who use the internet but also have periods without devices are happier and think more clearly. Taking breaks from screens helps your brain recover. Some people used to feel lost without their phones, but now they practice digital detox and feel much better.

Your brain is powerful and can adapt. Whether you use technology or avoid it, the choice is yours. The important thing is to be aware of how technology affects your thinking.""",
        "instructions": "Busca 3-4 oraciones que describan cómo cambió el internet nuestro cerebro.",
        "difficulty": "intermediate",
    }
]

# Lecturas para Unit 8 (ART)
UNIT_8_READINGS = [
    {
        "title": "El Poder de la Música en Nuestras Vidas",
        "content": """Music is one of humanity's greatest gifts. For thousands of years, people have used music to express emotions, tell stories, and connect with others. Every culture has its own unique music and instruments that tell its history.

Different types of music affect our brains differently. Classical music helps people concentrate and relax. Jazz is energetic and improves creative thinking. Rock music makes people feel powerful and motivated. Pop music brings joy and happiness. Studies show that listening to your favorite music reduces stress and anxiety.

Many people don't realize that music teaches us about other cultures. When you listen to music from different countries, you learn about their traditions, values, and history. A traditional Chinese instrument sounds different from an African drum, but both express human emotion beautifully.

Playing a musical instrument is also incredibly powerful. If you learn guitar, piano, or violin, you're training your brain. Musicians have stronger connections in their brains than non-musicians. They're also better at problem-solving and languages.

Whether you listen to music or play it, the benefits are clear. Music brings people together, heals emotions, and makes life more beautiful. Start exploring different types of music today.""",
        "instructions": "Extrae 3 oraciones sobre los beneficios de la música.",
        "difficulty": "beginner",
    }
]

def seed_motivational_messages():
    """Poblar mensajes motivacionales"""
    print("Agregando mensajes motivacionales...")
    
    for msg_data in MOTIVATIONAL_MESSAGES:
        existing = MotivationalMessage.query.filter_by(
            title=msg_data['title']
        ).first()
        
        if not existing:
            msg = MotivationalMessage(
                title=msg_data['title'],
                content=msg_data['content'],
                icon=msg_data['icon'],
                is_active=True,
                order=len(MotivationalMessage.query.all())
            )
            db.session.add(msg)
    
    db.session.commit()
    print(f"✓ {len(MOTIVATIONAL_MESSAGES)} mensajes motivacionales agregados")


def seed_readings():
    """Poblar lecturas de ejemplo"""
    print("Agregando lecturas de ejemplo...")
    
    # Unit 7 readings
    unit_7 = Unit.query.filter_by(unit_number=7).first()
    if unit_7:
        for idx, reading_data in enumerate(UNIT_7_READINGS):
            existing = Reading.query.filter_by(
                unit_id=unit_7.id,
                title=reading_data['title']
            ).first()
            
            if not existing:
                reading = Reading(
                    unit_id=unit_7.id,
                    title=reading_data['title'],
                    content=reading_data['content'],
                    instructions=reading_data['instructions'],
                    difficulty=reading_data['difficulty'],
                    order=idx
                )
                db.session.add(reading)
        
        db.session.commit()
        print(f"✓ {len(UNIT_7_READINGS)} lecturas para Unit 7 agregadas")
    
    # Unit 8 readings
    unit_8 = Unit.query.filter_by(unit_number=8).first()
    if unit_8:
        for idx, reading_data in enumerate(UNIT_8_READINGS):
            existing = Reading.query.filter_by(
                unit_id=unit_8.id,
                title=reading_data['title']
            ).first()
            
            if not existing:
                reading = Reading(
                    unit_id=unit_8.id,
                    title=reading_data['title'],
                    content=reading_data['content'],
                    instructions=reading_data['instructions'],
                    difficulty=reading_data['difficulty'],
                    order=idx
                )
                db.session.add(reading)
        
        db.session.commit()
        print(f"✓ {len(UNIT_8_READINGS)} lecturas para Unit 8 agregadas")


if __name__ == '__main__':
    with app.app_context():
        print("=" * 60)
        print("AGREGANDO SISTEMA DE LECTURA Y MENSAJES MOTIVACIONALES")
        print("=" * 60)
        
        seed_motivational_messages()
        seed_readings()
        
        print("\n" + "=" * 60)
        print("✅ Sistema de lectura poblado exitosamente!")
        print("=" * 60)
