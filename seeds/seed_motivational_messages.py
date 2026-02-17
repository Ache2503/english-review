#!/usr/bin/env python3
"""
Seed para mensajes motivacionales
Mensajes psicológicos para mantener la motivación del estudiante
"""

from app import create_app, db
from app.models import MotivationalMessage

MOTIVATIONAL_MESSAGES = [
    # Mindset - Mentalidad de crecimiento
    {
        "title": "mindset",
        "content": "Los errores no son fracasos, son oportunidades de aprendizaje. Cada error te acerca más a dominar el inglés.",
        "icon": "🧠",
        "order": 1
    },
    {
        "title": "mindset",
        "content": "Tu cerebro es como un músculo: mientras más practicas, más fuerte se vuelve tu inglés.",
        "icon": "💪",
        "order": 2
    },
    {
        "title": "mindset",
        "content": "No existe 'no soy bueno para los idiomas'. Solo existe 'todavía no lo domino'.",
        "icon": "🌱",
        "order": 3
    },
    {
        "title": "mindset",
        "content": "La confusión es parte del aprendizaje. Si algo te parece difícil, significa que estás creciendo.",
        "icon": "🎯",
        "order": 4
    },
    
    # Progression - Progreso
    {
        "title": "progression",
        "content": "Cada palabra nueva que aprendes es un ladrillo más en tu castillo del inglés. ¡Sigue construyendo!",
        "icon": "🏰",
        "order": 1
    },
    {
        "title": "progression",
        "content": "Hace un mes no sabías lo que sabes hoy. Imagina lo que sabrás en un mes más.",
        "icon": "📈",
        "order": 2
    },
    {
        "title": "progression",
        "content": "El progreso no siempre es visible día a día, pero mira atrás y verás cuánto has avanzado.",
        "icon": "🔭",
        "order": 3
    },
    {
        "title": "progression",
        "content": "Pequeños pasos diarios llevan a grandes destinos. ¡Hoy diste otro paso!",
        "icon": "👣",
        "order": 4
    },
    
    # Effort - Esfuerzo
    {
        "title": "effort",
        "content": "La práctica constante supera al talento natural. Tu dedicación es tu superpoder.",
        "icon": "⚡",
        "order": 1
    },
    {
        "title": "effort",
        "content": "15 minutos de práctica diaria son más efectivos que 2 horas una vez por semana.",
        "icon": "⏰",
        "order": 2
    },
    {
        "title": "effort",
        "content": "El esfuerzo que pones hoy es la fluidez que tendrás mañana.",
        "icon": "🌟",
        "order": 3
    },
    {
        "title": "effort",
        "content": "Cada sesión de estudio es una inversión en tu futuro. ¡Vale la pena!",
        "icon": "💎",
        "order": 4
    },
    
    # Celebration - Celebración de logros
    {
        "title": "celebration",
        "content": "¡Excelente trabajo! Completar una lección es un logro real. Celébralo.",
        "icon": "🎉",
        "order": 1
    },
    {
        "title": "celebration",
        "content": "¡Lo lograste! Cada ejercicio completado te hace mejor.",
        "icon": "🏆",
        "order": 2
    },
    {
        "title": "celebration",
        "content": "¡Increíble dedicación! Estar aquí practicando ya te distingue.",
        "icon": "⭐",
        "order": 3
    },
    {
        "title": "celebration",
        "content": "¡Muy bien! Tu constancia está dando frutos.",
        "icon": "🌻",
        "order": 4
    },
    
    # Encouragement - Ánimo
    {
        "title": "encouragement",
        "content": "¿Te sientes estancado? Es normal. Justo antes del avance viene la meseta.",
        "icon": "🌈",
        "order": 1
    },
    {
        "title": "encouragement",
        "content": "No te compares con otros. Tu único competidor es la versión de ayer.",
        "icon": "🪞",
        "order": 2
    },
    {
        "title": "encouragement",
        "content": "Miles de personas han aprendido inglés. Tú también puedes. Es cuestión de tiempo.",
        "icon": "🌍",
        "order": 3
    },
    {
        "title": "encouragement",
        "content": "El día que domines el inglés, recordarás este momento con orgullo.",
        "icon": "🏅",
        "order": 4
    },
    
    # Practical Tips - Consejos prácticos
    {
        "title": "tips",
        "content": "Tip: Habla en voz alta mientras practicas. Tu cerebro aprende mejor cuando usas múltiples sentidos.",
        "icon": "💡",
        "order": 1
    },
    {
        "title": "tips",
        "content": "Tip: Escucha música o podcasts en inglés. La exposición constante acelera tu aprendizaje.",
        "icon": "🎧",
        "order": 2
    },
    {
        "title": "tips",
        "content": "Tip: Cambia el idioma de tu teléfono a inglés. Pequeños cambios hacen grandes diferencias.",
        "icon": "📱",
        "order": 3
    },
    {
        "title": "tips",
        "content": "Tip: Piensa en inglés durante el día. No traduzcas, ¡crea pensamientos directamente!",
        "icon": "💭",
        "order": 4
    },
    
    # Fun Facts - Datos curiosos
    {
        "title": "fun_fact",
        "content": "Fun fact: El inglés tiene más de 170,000 palabras, pero con 3,000 puedes entender el 95% de textos cotidianos.",
        "icon": "📚",
        "order": 1
    },
    {
        "title": "fun_fact",
        "content": "Fun fact: 'Set' es la palabra con más definiciones en inglés: ¡más de 430!",
        "icon": "🤯",
        "order": 2
    },
    {
        "title": "fun_fact",
        "content": "Fun fact: El inglés es el idioma oficial de la aviación y el espacio.",
        "icon": "✈️",
        "order": 3
    },
    {
        "title": "fun_fact",
        "content": "Fun fact: Shakespeare inventó más de 1,700 palabras que usamos hoy.",
        "icon": "🎭",
        "order": 4
    },
]

def seed_motivational_messages():
    """Poblar la tabla de mensajes motivacionales"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("🌟 AGREGANDO MENSAJES MOTIVACIONALES")
        print("=" * 60)
        
        added = 0
        skipped = 0
        
        for msg in MOTIVATIONAL_MESSAGES:
            # Verificar si ya existe
            existing = MotivationalMessage.query.filter_by(
                title=msg["title"],
                content=msg["content"]
            ).first()
            
            if existing:
                skipped += 1
                continue
            
            message = MotivationalMessage(
                title=msg["title"],
                content=msg["content"],
                icon=msg.get("icon", "💬"),
                unit_id=msg.get("unit_id"),
                order=msg.get("order", 0),
                is_active=True
            )
            db.session.add(message)
            added += 1
        
        db.session.commit()
        
        # Contar por categoría
        categories = {}
        for msg in MOTIVATIONAL_MESSAGES:
            cat = msg["title"]
            categories[cat] = categories.get(cat, 0) + 1
        
        print(f"✅ Mensajes agregados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print()
        print("📂 Por categoría:")
        for cat, count in categories.items():
            print(f"   - {cat}: {count}")
        print("=" * 60)

if __name__ == "__main__":
    seed_motivational_messages()
