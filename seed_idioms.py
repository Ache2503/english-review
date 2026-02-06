#!/usr/bin/env python3
"""
Seed de Idioms - Expresiones idiomáticas esenciales para inglés natural
Organizados por nivel CEFR y categoría
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Idiom

app = create_app()

IDIOMS = [
    # ============ A2 LEVEL (Basic Idioms) ============
    # Body parts
    {"expression": "break a leg", "meaning": "Buena suerte (especialmente antes de una actuación)", "spanish_translation": "¡Mucha suerte!", "literal_translation": "Rómpete una pierna", "example_sentence": "You have a job interview? Break a leg!", "example_translation": "¿Tienes una entrevista de trabajo? ¡Mucha suerte!", "origin": "Teatro: se creía que desear buena suerte traía mala suerte", "category": "wishes", "level": "A2"},
    {"expression": "keep an eye on", "meaning": "Vigilar, cuidar algo o alguien", "spanish_translation": "Echar un ojo, vigilar", "literal_translation": "Mantener un ojo en", "example_sentence": "Can you keep an eye on my bag?", "example_translation": "¿Puedes echarle un ojo a mi bolsa?", "origin": "Referencia a observar atentamente", "category": "care", "level": "A2"},
    {"expression": "give someone a hand", "meaning": "Ayudar a alguien", "spanish_translation": "Echar una mano", "literal_translation": "Dar a alguien una mano", "example_sentence": "Could you give me a hand with this box?", "example_translation": "¿Podrías echarme una mano con esta caja?", "origin": "Ofrecer ayuda física con las manos", "category": "help", "level": "A2"},
    {"expression": "all ears", "meaning": "Estar muy atento, listo para escuchar", "spanish_translation": "Soy todo oídos", "literal_translation": "Todo oídos", "example_sentence": "Tell me your idea, I'm all ears.", "example_translation": "Dime tu idea, soy todo oídos.", "origin": "Concentrar toda la atención en escuchar", "category": "communication", "level": "A2"},
    
    # Time
    {"expression": "once in a blue moon", "meaning": "Muy raramente, casi nunca", "spanish_translation": "De vez en cuando, muy raro", "literal_translation": "Una vez en una luna azul", "example_sentence": "I eat fast food once in a blue moon.", "example_translation": "Como comida rápida muy de vez en cuando.", "origin": "Las lunas azules son fenómenos muy raros", "category": "time", "level": "A2"},
    {"expression": "it's about time", "meaning": "Ya era hora", "spanish_translation": "Ya era hora", "literal_translation": "Es sobre tiempo", "example_sentence": "It's about time you arrived!", "example_translation": "¡Ya era hora de que llegaras!", "origin": "Expresión de impaciencia", "category": "time", "level": "A2"},
    
    # ============ B1 LEVEL (Intermediate Idioms) ============
    # Weather
    {"expression": "under the weather", "meaning": "Sentirse mal, enfermo", "spanish_translation": "Sentirse mal, enfermo", "literal_translation": "Bajo el clima", "example_sentence": "I'm feeling under the weather today.", "example_translation": "Me siento mal hoy.", "origin": "Náutico: cuando los marineros se enfermaban iban bajo cubierta", "category": "health", "level": "B1"},
    {"expression": "rain cats and dogs", "meaning": "Llover muy fuerte", "spanish_translation": "Llover a cántaros", "literal_translation": "Llover gatos y perros", "example_sentence": "Take an umbrella, it's raining cats and dogs.", "example_translation": "Lleva paraguas, está lloviendo a cántaros.", "origin": "Posiblemente de la época medieval", "category": "weather", "level": "B1"},
    {"expression": "every cloud has a silver lining", "meaning": "Siempre hay algo positivo en las situaciones malas", "spanish_translation": "No hay mal que por bien no venga", "literal_translation": "Cada nube tiene un borde plateado", "example_sentence": "You lost your job but found a better one. Every cloud has a silver lining.", "example_translation": "Perdiste tu trabajo pero encontraste uno mejor. No hay mal que por bien no venga.", "origin": "La luz del sol detrás de las nubes", "category": "optimism", "level": "B1"},
    
    # Animals
    {"expression": "let the cat out of the bag", "meaning": "Revelar un secreto sin querer", "spanish_translation": "Irse de la lengua", "literal_translation": "Dejar salir al gato de la bolsa", "example_sentence": "Don't let the cat out of the bag about the surprise party.", "example_translation": "No te vayas de la lengua sobre la fiesta sorpresa.", "origin": "Fraude medieval en mercados", "category": "secrets", "level": "B1"},
    {"expression": "kill two birds with one stone", "meaning": "Lograr dos cosas con una sola acción", "spanish_translation": "Matar dos pájaros de un tiro", "literal_translation": "Matar dos pájaros con una piedra", "example_sentence": "I'll visit my mom and do grocery shopping - kill two birds with one stone.", "example_translation": "Visitaré a mi mamá y haré las compras - mataré dos pájaros de un tiro.", "origin": "Eficiencia en la caza", "category": "efficiency", "level": "B1"},
    {"expression": "a piece of cake", "meaning": "Algo muy fácil", "spanish_translation": "Pan comido, muy fácil", "literal_translation": "Un pedazo de pastel", "example_sentence": "The test was a piece of cake.", "example_translation": "El examen fue pan comido.", "origin": "Comer pastel es algo placentero y fácil", "category": "difficulty", "level": "B1"},
    {"expression": "the elephant in the room", "meaning": "Un problema obvio que nadie quiere mencionar", "spanish_translation": "El tema incómodo que nadie quiere tocar", "literal_translation": "El elefante en la habitación", "example_sentence": "Nobody talks about his addiction - it's the elephant in the room.", "example_translation": "Nadie habla de su adicción - es el tema incómodo.", "origin": "Algo tan grande que es imposible ignorar", "category": "problems", "level": "B1"},
    {"expression": "when pigs fly", "meaning": "Nunca (algo imposible)", "spanish_translation": "Cuando las vacas vuelen", "literal_translation": "Cuando los cerdos vuelen", "example_sentence": "He'll clean his room when pigs fly.", "example_translation": "Él limpiará su cuarto cuando las vacas vuelen.", "origin": "Referencia a algo imposible", "category": "impossibility", "level": "B1"},
    
    # Actions
    {"expression": "hit the nail on the head", "meaning": "Dar en el clavo, acertar exactamente", "spanish_translation": "Dar en el clavo", "literal_translation": "Golpear el clavo en la cabeza", "example_sentence": "You hit the nail on the head with that comment.", "example_translation": "Diste en el clavo con ese comentario.", "origin": "Carpintería: golpear el clavo correctamente", "category": "accuracy", "level": "B1"},
    {"expression": "bite off more than you can chew", "meaning": "Tomar más responsabilidades de las que puedes manejar", "spanish_translation": "Abarcar más de lo que puedes", "literal_translation": "Morder más de lo que puedes masticar", "example_sentence": "Taking 6 classes was biting off more than I could chew.", "example_translation": "Tomar 6 clases fue abarcar más de lo que podía.", "origin": "Referencia a comer", "category": "capacity", "level": "B1"},
    {"expression": "get out of hand", "meaning": "Salirse de control", "spanish_translation": "Salirse de control", "literal_translation": "Salirse de la mano", "example_sentence": "The party got out of hand.", "example_translation": "La fiesta se salió de control.", "origin": "Perder el control físico de algo", "category": "control", "level": "B1"},
    
    # ============ B2 LEVEL (Upper-Intermediate Idioms) ============
    # Success/Failure
    {"expression": "the ball is in your court", "meaning": "Es tu turno de tomar acción", "spanish_translation": "La pelota está en tu cancha", "literal_translation": "La pelota está en tu cancha", "example_sentence": "I made an offer, now the ball is in your court.", "example_translation": "Hice una oferta, ahora la pelota está en tu cancha.", "origin": "Tenis: es tu turno de jugar", "category": "decision", "level": "B2"},
    {"expression": "back to the drawing board", "meaning": "Empezar de nuevo desde cero", "spanish_translation": "Volver a empezar desde cero", "literal_translation": "Volver a la mesa de dibujo", "example_sentence": "The plan failed, so it's back to the drawing board.", "example_translation": "El plan falló, así que hay que volver a empezar.", "origin": "Ingeniería: rediseñar cuando algo falla", "category": "restart", "level": "B2"},
    {"expression": "burn the midnight oil", "meaning": "Trabajar o estudiar hasta muy tarde", "spanish_translation": "Quemarse las pestañas", "literal_translation": "Quemar el aceite de medianoche", "example_sentence": "I had to burn the midnight oil to finish the project.", "example_translation": "Tuve que quemarme las pestañas para terminar el proyecto.", "origin": "Antes de la electricidad, se usaba aceite para iluminar", "category": "work", "level": "B2"},
    {"expression": "cut corners", "meaning": "Hacer algo de manera rápida y barata, sin cuidado", "spanish_translation": "Tomar atajos, hacer las cosas a medias", "literal_translation": "Cortar esquinas", "example_sentence": "Don't cut corners on safety.", "example_translation": "No tomes atajos en seguridad.", "origin": "Tomar la ruta más corta", "category": "quality", "level": "B2"},
    
    # Emotions
    {"expression": "get cold feet", "meaning": "Perder el valor, acobardarse", "spanish_translation": "Acobardarse, echarse para atrás", "literal_translation": "Tener pies fríos", "example_sentence": "He got cold feet before the wedding.", "example_translation": "Se acobardó antes de la boda.", "origin": "Soldados con pies congelados no podían luchar", "category": "fear", "level": "B2"},
    {"expression": "over the moon", "meaning": "Extremadamente feliz", "spanish_translation": "En las nubes de felicidad", "literal_translation": "Sobre la luna", "example_sentence": "She was over the moon when she got the job.", "example_translation": "Estaba en las nubes cuando consiguió el trabajo.", "origin": "Canción infantil 'Hey Diddle Diddle'", "category": "happiness", "level": "B2"},
    {"expression": "down in the dumps", "meaning": "Muy triste o deprimido", "spanish_translation": "Por los suelos, deprimido", "literal_translation": "Abajo en los basureros", "example_sentence": "He's been down in the dumps since the breakup.", "example_translation": "Ha estado muy deprimido desde la ruptura.", "origin": "Dumps = melancolía (uso antiguo)", "category": "sadness", "level": "B2"},
    {"expression": "blow off steam", "meaning": "Liberar estrés o frustración", "spanish_translation": "Desahogarse", "literal_translation": "Soltar vapor", "example_sentence": "I go to the gym to blow off steam.", "example_translation": "Voy al gimnasio para desahogarme.", "origin": "Máquinas de vapor liberando presión", "category": "stress", "level": "B2"},
    
    # Money
    {"expression": "break the bank", "meaning": "Costar mucho dinero", "spanish_translation": "Costar un ojo de la cara", "literal_translation": "Romper el banco", "example_sentence": "This vacation won't break the bank.", "example_translation": "Estas vacaciones no costarán un ojo de la cara.", "origin": "Apostar tanto que el casino quiebra", "category": "money", "level": "B2"},
    {"expression": "cost an arm and a leg", "meaning": "Ser muy caro", "spanish_translation": "Costar un ojo de la cara", "literal_translation": "Costar un brazo y una pierna", "example_sentence": "That car cost an arm and a leg.", "example_translation": "Ese carro costó un ojo de la cara.", "origin": "Algo tan valioso como partes del cuerpo", "category": "money", "level": "B2"},
    {"expression": "a dime a dozen", "meaning": "Muy común, sin valor especial", "spanish_translation": "Muy común, hay muchos", "literal_translation": "Una moneda por docena", "example_sentence": "Coffee shops are a dime a dozen in this city.", "example_translation": "Las cafeterías son muy comunes en esta ciudad.", "origin": "Cosas baratas en mercados", "category": "value", "level": "B2"},
    
    # ============ C1 LEVEL (Advanced Idioms) ============
    # Business/Work
    {"expression": "think outside the box", "meaning": "Pensar de manera creativa y no convencional", "spanish_translation": "Pensar fuera de la caja", "literal_translation": "Pensar fuera de la caja", "example_sentence": "We need to think outside the box to solve this.", "example_translation": "Necesitamos pensar de manera creativa para resolver esto.", "origin": "Acertijo de los nueve puntos", "category": "creativity", "level": "B2"},
    {"expression": "get the ball rolling", "meaning": "Empezar algo, iniciar un proyecto", "spanish_translation": "Poner las cosas en marcha", "literal_translation": "Hacer que la pelota ruede", "example_sentence": "Let's get the ball rolling on this project.", "example_translation": "Pongamos en marcha este proyecto.", "origin": "Deportes con pelota", "category": "start", "level": "B2"},
    {"expression": "touch base", "meaning": "Comunicarse brevemente con alguien", "spanish_translation": "Ponerse en contacto", "literal_translation": "Tocar base", "example_sentence": "Let's touch base next week.", "example_translation": "Pongámonos en contacto la próxima semana.", "origin": "Béisbol: tocar las bases", "category": "communication", "level": "C1"},
    {"expression": "on the same page", "meaning": "Tener el mismo entendimiento", "spanish_translation": "Estar en la misma sintonía", "literal_translation": "En la misma página", "example_sentence": "Let's make sure we're all on the same page.", "example_translation": "Asegurémonos de que todos estamos en la misma sintonía.", "origin": "Leer el mismo punto en un libro", "category": "agreement", "level": "B2"},
    {"expression": "in a nutshell", "meaning": "En resumen, brevemente", "spanish_translation": "En pocas palabras", "literal_translation": "En una cáscara de nuez", "example_sentence": "In a nutshell, the project was a success.", "example_translation": "En pocas palabras, el proyecto fue un éxito.", "origin": "Algo tan pequeño que cabe en una cáscara", "category": "summary", "level": "B2"},
    
    # Wisdom
    {"expression": "don't put all your eggs in one basket", "meaning": "No arriesgar todo en una sola opción", "spanish_translation": "No pongas todos los huevos en una canasta", "literal_translation": "No pongas todos tus huevos en una canasta", "example_sentence": "Invest in different stocks - don't put all your eggs in one basket.", "example_translation": "Invierte en diferentes acciones - no pongas todos los huevos en una canasta.", "origin": "Proteger los huevos distribuyéndolos", "category": "wisdom", "level": "B2"},
    {"expression": "actions speak louder than words", "meaning": "Lo que haces importa más que lo que dices", "spanish_translation": "Las acciones valen más que las palabras", "literal_translation": "Las acciones hablan más fuerte que las palabras", "example_sentence": "He says he loves her, but actions speak louder than words.", "example_translation": "Él dice que la ama, pero las acciones valen más que las palabras.", "origin": "Proverbio antiguo", "category": "wisdom", "level": "B1"},
    {"expression": "the best of both worlds", "meaning": "Lo mejor de dos situaciones diferentes", "spanish_translation": "Lo mejor de ambos mundos", "literal_translation": "Lo mejor de ambos mundos", "example_sentence": "Working from home gives me the best of both worlds.", "example_translation": "Trabajar desde casa me da lo mejor de ambos mundos.", "origin": "Combinación ideal", "category": "benefit", "level": "B2"},
    {"expression": "better late than never", "meaning": "Es mejor tarde que nunca", "spanish_translation": "Más vale tarde que nunca", "literal_translation": "Mejor tarde que nunca", "example_sentence": "You finally called! Better late than never.", "example_translation": "¡Por fin llamaste! Más vale tarde que nunca.", "origin": "Proverbio latino", "category": "wisdom", "level": "A2"},
    
    # Relationships
    {"expression": "birds of a feather flock together", "meaning": "Personas similares tienden a juntarse", "spanish_translation": "Dios los cría y ellos se juntan", "literal_translation": "Pájaros del mismo plumaje vuelan juntos", "example_sentence": "They're both artists - birds of a feather flock together.", "example_translation": "Ambos son artistas - Dios los cría y ellos se juntan.", "origin": "Comportamiento de las aves", "category": "relationships", "level": "B2"},
    {"expression": "see eye to eye", "meaning": "Estar de acuerdo completamente", "spanish_translation": "Estar de acuerdo, ver las cosas igual", "literal_translation": "Ver ojo a ojo", "example_sentence": "We don't always see eye to eye.", "example_translation": "No siempre estamos de acuerdo.", "origin": "Mirar directamente al mismo nivel", "category": "agreement", "level": "B2"},
    {"expression": "get along like a house on fire", "meaning": "Llevarse muy bien desde el principio", "spanish_translation": "Llevarse de maravilla", "literal_translation": "Llevarse como una casa en llamas", "example_sentence": "They got along like a house on fire.", "example_translation": "Se llevaron de maravilla.", "origin": "Algo que sucede rápido e intensamente", "category": "relationships", "level": "C1"},
    
    # Miscellaneous Advanced
    {"expression": "the tip of the iceberg", "meaning": "Solo una pequeña parte de un problema mayor", "spanish_translation": "La punta del iceberg", "literal_translation": "La punta del iceberg", "example_sentence": "This scandal is just the tip of the iceberg.", "example_translation": "Este escándalo es solo la punta del iceberg.", "origin": "90% de un iceberg está bajo el agua", "category": "problems", "level": "B2"},
    {"expression": "a blessing in disguise", "meaning": "Algo malo que resulta ser bueno", "spanish_translation": "Una bendición disfrazada", "literal_translation": "Una bendición disfrazada", "example_sentence": "Losing that job was a blessing in disguise.", "example_translation": "Perder ese trabajo fue una bendición disfrazada.", "origin": "Lo bueno oculto en lo malo", "category": "perspective", "level": "B2"},
    {"expression": "barking up the wrong tree", "meaning": "Buscar en el lugar equivocado", "spanish_translation": "Estar equivocado, buscar mal", "literal_translation": "Ladrando al árbol equivocado", "example_sentence": "If you think I took your money, you're barking up the wrong tree.", "example_translation": "Si crees que tomé tu dinero, estás buscando mal.", "origin": "Perros de caza ladrando al árbol equivocado", "category": "mistakes", "level": "C1"},
    {"expression": "add insult to injury", "meaning": "Empeorar una situación ya mala", "spanish_translation": "Para colmo de males", "literal_translation": "Agregar insulto a la herida", "example_sentence": "He fired me and, to add insult to injury, he took credit for my work.", "example_translation": "Me despidió y, para colmo de males, se llevó el crédito de mi trabajo.", "origin": "Fábulas de Esopo", "category": "problems", "level": "C1"},
    {"expression": "go the extra mile", "meaning": "Hacer un esfuerzo adicional", "spanish_translation": "Ir más allá, hacer un esfuerzo extra", "literal_translation": "Ir la milla extra", "example_sentence": "She always goes the extra mile for her customers.", "example_translation": "Ella siempre hace un esfuerzo extra por sus clientes.", "origin": "Sermón de la Montaña en la Biblia", "category": "effort", "level": "B2"},
    {"expression": "keep your chin up", "meaning": "Mantenerse positivo en tiempos difíciles", "spanish_translation": "¡Ánimo! Mantente positivo", "literal_translation": "Mantén tu barbilla arriba", "example_sentence": "Keep your chin up, things will get better.", "example_translation": "¡Ánimo! Las cosas mejorarán.", "origin": "Postura de confianza", "category": "encouragement", "level": "B2"},
    {"expression": "the last straw", "meaning": "El límite final de la paciencia", "spanish_translation": "La gota que derramó el vaso", "literal_translation": "La última paja", "example_sentence": "Coming home late was the last straw.", "example_translation": "Llegar tarde a casa fue la gota que derramó el vaso.", "origin": "Proverbio de la paja que rompe el lomo del camello", "category": "limits", "level": "B2"},
]


def seed_idioms():
    """Agregar idioms a la base de datos"""
    with app.app_context():
        print("="*70)
        print("💬 AGREGANDO IDIOMS (EXPRESIONES IDIOMÁTICAS)")
        print("="*70)
        
        added = 0
        skipped = 0
        
        for idiom_data in IDIOMS:
            # Verificar si ya existe (el modelo usa 'phrase' no 'expression')
            existing = Idiom.query.filter_by(phrase=idiom_data['expression']).first()
            if existing:
                skipped += 1
                continue
            
            # Mapear campos del seed a los campos del modelo
            # Modelo: phrase, meaning, spanish_equivalent, example_sentence, example_translation, origin, category, level, usage_notes
            idiom = Idiom(
                phrase=idiom_data['expression'],
                meaning=idiom_data['meaning'],
                spanish_equivalent=idiom_data['spanish_translation'],
                example_sentence=idiom_data['example_sentence'],
                example_translation=idiom_data['example_translation'],
                origin=idiom_data.get('origin', ''),
                category=idiom_data['category'],
                level=idiom_data['level'],
                usage_notes=f"Traducción literal: {idiom_data.get('literal_translation', '')}"
            )
            db.session.add(idiom)
            added += 1
        
        db.session.commit()
        
        print(f"✅ Idioms agregados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print(f"\n📊 Por nivel:")
        for level in ['A2', 'B1', 'B2', 'C1']:
            count = Idiom.query.filter_by(level=level).count()
            print(f"   {level}: {count}")
        print(f"\n📁 Por categoría:")
        from sqlalchemy import func
        categories = db.session.query(Idiom.category, func.count(Idiom.id)).group_by(Idiom.category).all()
        for cat, count in sorted(categories, key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {cat}: {count}")
        print("="*70)


if __name__ == '__main__':
    seed_idioms()
