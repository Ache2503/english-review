#!/usr/bin/env python3
"""
Seed de Phrasal Verbs - Verbos frasales esenciales para inglés natural
Organizados por nivel CEFR
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import PhrasalVerb

app = create_app()

PHRASAL_VERBS = [
    # ============ A1-A2 LEVEL (Beginner) ============
    # GET
    {"verb": "get", "particle": "up", "full_form": "get up", "meaning": "Levantarse de la cama", "spanish_translation": "levantarse", "is_separable": False, "example_sentence": "I get up at 7 AM every day.", "example_translation": "Me levanto a las 7 AM todos los días.", "category": "daily routine", "level": "A1"},
    {"verb": "get", "particle": "on", "full_form": "get on", "meaning": "Subirse a (transporte)", "spanish_translation": "subirse a", "is_separable": False, "example_sentence": "Get on the bus at the next stop.", "example_translation": "Súbete al autobús en la próxima parada.", "category": "transportation", "level": "A1"},
    {"verb": "get", "particle": "off", "full_form": "get off", "meaning": "Bajarse de (transporte)", "spanish_translation": "bajarse de", "is_separable": False, "example_sentence": "I get off at the train station.", "example_translation": "Me bajo en la estación de tren.", "category": "transportation", "level": "A1"},
    {"verb": "get", "particle": "back", "full_form": "get back", "meaning": "Regresar, volver", "spanish_translation": "regresar", "is_separable": False, "example_sentence": "What time did you get back home?", "example_translation": "¿A qué hora regresaste a casa?", "category": "movement", "level": "A2"},
    {"verb": "get", "particle": "along", "full_form": "get along", "meaning": "Llevarse bien con alguien", "spanish_translation": "llevarse bien", "is_separable": False, "example_sentence": "I get along well with my colleagues.", "example_translation": "Me llevo bien con mis colegas.", "category": "relationship", "level": "A2"},
    
    # LOOK
    {"verb": "look", "particle": "for", "full_form": "look for", "meaning": "Buscar algo", "spanish_translation": "buscar", "is_separable": False, "example_sentence": "I'm looking for my keys.", "example_translation": "Estoy buscando mis llaves.", "category": "action", "level": "A1"},
    {"verb": "look", "particle": "at", "full_form": "look at", "meaning": "Mirar algo", "spanish_translation": "mirar", "is_separable": False, "example_sentence": "Look at this picture!", "example_translation": "¡Mira esta foto!", "category": "action", "level": "A1"},
    {"verb": "look", "particle": "after", "full_form": "look after", "meaning": "Cuidar de", "spanish_translation": "cuidar", "is_separable": False, "example_sentence": "She looks after her little brother.", "example_translation": "Ella cuida a su hermano pequeño.", "category": "care", "level": "A2"},
    {"verb": "look", "particle": "forward to", "full_form": "look forward to", "meaning": "Esperar con ansias", "spanish_translation": "esperar con ansias", "is_separable": False, "example_sentence": "I look forward to meeting you.", "example_translation": "Espero con ansias conocerte.", "category": "feeling", "level": "A2"},
    {"verb": "look", "particle": "up", "full_form": "look up", "meaning": "Buscar (información)", "spanish_translation": "buscar (info)", "is_separable": True, "example_sentence": "I looked up the word in the dictionary.", "example_translation": "Busqué la palabra en el diccionario.", "category": "action", "level": "A2"},
    
    # TURN
    {"verb": "turn", "particle": "on", "full_form": "turn on", "meaning": "Encender", "spanish_translation": "encender", "is_separable": True, "example_sentence": "Turn on the light, please.", "example_translation": "Enciende la luz, por favor.", "category": "action", "level": "A1"},
    {"verb": "turn", "particle": "off", "full_form": "turn off", "meaning": "Apagar", "spanish_translation": "apagar", "is_separable": True, "example_sentence": "Don't forget to turn off the TV.", "example_translation": "No olvides apagar la televisión.", "category": "action", "level": "A1"},
    {"verb": "turn", "particle": "up", "full_form": "turn up", "meaning": "Subir el volumen / aparecer", "spanish_translation": "subir volumen", "is_separable": True, "example_sentence": "Can you turn up the music?", "example_translation": "¿Puedes subir la música?", "category": "action", "level": "A2"},
    {"verb": "turn", "particle": "down", "full_form": "turn down", "meaning": "Bajar el volumen / rechazar", "spanish_translation": "bajar volumen", "is_separable": True, "example_sentence": "Please turn down the volume.", "example_translation": "Por favor baja el volumen.", "category": "action", "level": "A2"},
    
    # PUT
    {"verb": "put", "particle": "on", "full_form": "put on", "meaning": "Ponerse (ropa)", "spanish_translation": "ponerse", "is_separable": True, "example_sentence": "Put on your jacket, it's cold.", "example_translation": "Ponte la chaqueta, hace frío.", "category": "clothing", "level": "A1"},
    {"verb": "put", "particle": "away", "full_form": "put away", "meaning": "Guardar en su lugar", "spanish_translation": "guardar", "is_separable": True, "example_sentence": "Put away your toys.", "example_translation": "Guarda tus juguetes.", "category": "action", "level": "A2"},
    {"verb": "put", "particle": "off", "full_form": "put off", "meaning": "Posponer", "spanish_translation": "posponer", "is_separable": True, "example_sentence": "Don't put off your homework.", "example_translation": "No pospongas tu tarea.", "category": "time", "level": "A2"},
    
    # TAKE
    {"verb": "take", "particle": "off", "full_form": "take off", "meaning": "Quitarse (ropa) / despegar", "spanish_translation": "quitarse", "is_separable": True, "example_sentence": "Take off your shoes at the door.", "example_translation": "Quítate los zapatos en la puerta.", "category": "clothing", "level": "A1"},
    {"verb": "take", "particle": "out", "full_form": "take out", "meaning": "Sacar", "spanish_translation": "sacar", "is_separable": True, "example_sentence": "Take out your notebook.", "example_translation": "Saca tu cuaderno.", "category": "action", "level": "A1"},
    {"verb": "take", "particle": "care of", "full_form": "take care of", "meaning": "Cuidar de", "spanish_translation": "cuidar de", "is_separable": False, "example_sentence": "I take care of my grandmother.", "example_translation": "Cuido a mi abuela.", "category": "care", "level": "A2"},
    
    # ============ B1 LEVEL (Intermediate) ============
    # GIVE
    {"verb": "give", "particle": "up", "full_form": "give up", "meaning": "Rendirse, dejar de intentar", "spanish_translation": "rendirse", "is_separable": True, "example_sentence": "Never give up on your dreams.", "example_translation": "Nunca te rindas con tus sueños.", "category": "motivation", "level": "B1"},
    {"verb": "give", "particle": "back", "full_form": "give back", "meaning": "Devolver", "spanish_translation": "devolver", "is_separable": True, "example_sentence": "Give me back my book.", "example_translation": "Devuélveme mi libro.", "category": "action", "level": "B1"},
    
    # COME
    {"verb": "come", "particle": "up with", "full_form": "come up with", "meaning": "Inventar, idear", "spanish_translation": "inventar, idear", "is_separable": False, "example_sentence": "She came up with a great idea.", "example_translation": "Ella se le ocurrió una gran idea.", "category": "thinking", "level": "B1"},
    {"verb": "come", "particle": "across", "full_form": "come across", "meaning": "Encontrar por casualidad", "spanish_translation": "encontrar por casualidad", "is_separable": False, "example_sentence": "I came across an old photo.", "example_translation": "Encontré una foto vieja por casualidad.", "category": "discovery", "level": "B1"},
    
    # GO
    {"verb": "go", "particle": "on", "full_form": "go on", "meaning": "Continuar", "spanish_translation": "continuar", "is_separable": False, "example_sentence": "Please go on with your story.", "example_translation": "Por favor continúa con tu historia.", "category": "action", "level": "B1"},
    {"verb": "go", "particle": "out", "full_form": "go out", "meaning": "Salir (socialmente)", "spanish_translation": "salir", "is_separable": False, "example_sentence": "Let's go out for dinner.", "example_translation": "Salgamos a cenar.", "category": "social", "level": "A2"},
    {"verb": "go", "particle": "through", "full_form": "go through", "meaning": "Revisar / experimentar algo difícil", "spanish_translation": "revisar, pasar por", "is_separable": False, "example_sentence": "She's going through a difficult time.", "example_translation": "Está pasando por un momento difícil.", "category": "experience", "level": "B1"},
    
    # BREAK
    {"verb": "break", "particle": "down", "full_form": "break down", "meaning": "Descomponerse, averiarse", "spanish_translation": "descomponerse", "is_separable": False, "example_sentence": "My car broke down yesterday.", "example_translation": "Mi carro se descompuso ayer.", "category": "problem", "level": "B1"},
    {"verb": "break", "particle": "up", "full_form": "break up", "meaning": "Terminar una relación", "spanish_translation": "terminar (relación)", "is_separable": False, "example_sentence": "They broke up last month.", "example_translation": "Terminaron el mes pasado.", "category": "relationship", "level": "B1"},
    
    # WORK
    {"verb": "work", "particle": "out", "full_form": "work out", "meaning": "Hacer ejercicio / resolver", "spanish_translation": "ejercitarse, resolver", "is_separable": False, "example_sentence": "I work out at the gym every day.", "example_translation": "Hago ejercicio en el gimnasio todos los días.", "category": "health", "level": "B1"},
    {"verb": "work", "particle": "on", "full_form": "work on", "meaning": "Trabajar en algo", "spanish_translation": "trabajar en", "is_separable": False, "example_sentence": "I'm working on a new project.", "example_translation": "Estoy trabajando en un nuevo proyecto.", "category": "work", "level": "B1"},
    
    # FIGURE
    {"verb": "figure", "particle": "out", "full_form": "figure out", "meaning": "Resolver, entender", "spanish_translation": "resolver, entender", "is_separable": True, "example_sentence": "I can't figure out this problem.", "example_translation": "No puedo resolver este problema.", "category": "thinking", "level": "B1"},
    
    # FILL
    {"verb": "fill", "particle": "out", "full_form": "fill out", "meaning": "Llenar (formulario)", "spanish_translation": "llenar", "is_separable": True, "example_sentence": "Please fill out this form.", "example_translation": "Por favor llena este formulario.", "category": "action", "level": "B1"},
    {"verb": "fill", "particle": "in", "full_form": "fill in", "meaning": "Completar información", "spanish_translation": "completar", "is_separable": True, "example_sentence": "Fill in the blanks.", "example_translation": "Llena los espacios en blanco.", "category": "action", "level": "B1"},
    
    # FIND
    {"verb": "find", "particle": "out", "full_form": "find out", "meaning": "Descubrir, averiguar", "spanish_translation": "descubrir", "is_separable": True, "example_sentence": "I need to find out the truth.", "example_translation": "Necesito descubrir la verdad.", "category": "discovery", "level": "B1"},
    
    # ============ B2 LEVEL (Upper-Intermediate) ============
    # CARRY
    {"verb": "carry", "particle": "on", "full_form": "carry on", "meaning": "Continuar, seguir adelante", "spanish_translation": "continuar", "is_separable": False, "example_sentence": "Carry on with your work.", "example_translation": "Continúa con tu trabajo.", "category": "action", "level": "B2"},
    {"verb": "carry", "particle": "out", "full_form": "carry out", "meaning": "Llevar a cabo, ejecutar", "spanish_translation": "llevar a cabo", "is_separable": True, "example_sentence": "We need to carry out the plan.", "example_translation": "Necesitamos llevar a cabo el plan.", "category": "action", "level": "B2"},
    
    # BRING
    {"verb": "bring", "particle": "up", "full_form": "bring up", "meaning": "Mencionar un tema / criar", "spanish_translation": "mencionar, criar", "is_separable": True, "example_sentence": "Don't bring up that topic.", "example_translation": "No menciones ese tema.", "category": "communication", "level": "B2"},
    {"verb": "bring", "particle": "about", "full_form": "bring about", "meaning": "Causar, provocar", "spanish_translation": "causar", "is_separable": True, "example_sentence": "The new law brought about many changes.", "example_translation": "La nueva ley causó muchos cambios.", "category": "cause", "level": "B2"},
    
    # SET
    {"verb": "set", "particle": "up", "full_form": "set up", "meaning": "Establecer, instalar", "spanish_translation": "establecer", "is_separable": True, "example_sentence": "Let's set up a meeting.", "example_translation": "Organicemos una reunión.", "category": "organization", "level": "B2"},
    {"verb": "set", "particle": "off", "full_form": "set off", "meaning": "Partir, empezar un viaje", "spanish_translation": "partir", "is_separable": False, "example_sentence": "We set off early in the morning.", "example_translation": "Partimos temprano en la mañana.", "category": "travel", "level": "B2"},
    
    # PICK
    {"verb": "pick", "particle": "up", "full_form": "pick up", "meaning": "Recoger, levantar / aprender", "spanish_translation": "recoger, aprender", "is_separable": True, "example_sentence": "I'll pick you up at 8.", "example_translation": "Te recogeré a las 8.", "category": "action", "level": "B1"},
    {"verb": "pick", "particle": "out", "full_form": "pick out", "meaning": "Elegir, seleccionar", "spanish_translation": "elegir", "is_separable": True, "example_sentence": "Pick out a nice dress for the party.", "example_translation": "Elige un lindo vestido para la fiesta.", "category": "choice", "level": "B2"},
    
    # RUN
    {"verb": "run", "particle": "out of", "full_form": "run out of", "meaning": "Quedarse sin", "spanish_translation": "quedarse sin", "is_separable": False, "example_sentence": "We ran out of milk.", "example_translation": "Nos quedamos sin leche.", "category": "shortage", "level": "B1"},
    {"verb": "run", "particle": "into", "full_form": "run into", "meaning": "Encontrarse con (por casualidad)", "spanish_translation": "encontrarse con", "is_separable": False, "example_sentence": "I ran into my old friend yesterday.", "example_translation": "Me encontré con mi viejo amigo ayer.", "category": "meeting", "level": "B2"},
    
    # CALL
    {"verb": "call", "particle": "off", "full_form": "call off", "meaning": "Cancelar", "spanish_translation": "cancelar", "is_separable": True, "example_sentence": "They called off the meeting.", "example_translation": "Cancelaron la reunión.", "category": "cancellation", "level": "B2"},
    {"verb": "call", "particle": "back", "full_form": "call back", "meaning": "Devolver la llamada", "spanish_translation": "devolver llamada", "is_separable": True, "example_sentence": "I'll call you back later.", "example_translation": "Te devuelvo la llamada después.", "category": "communication", "level": "B1"},
    
    # ============ C1 LEVEL (Advanced) ============
    # COME
    {"verb": "come", "particle": "down to", "full_form": "come down to", "meaning": "Reducirse a", "spanish_translation": "reducirse a", "is_separable": False, "example_sentence": "It all comes down to money.", "example_translation": "Todo se reduce al dinero.", "category": "conclusion", "level": "C1"},
    
    # HOLD
    {"verb": "hold", "particle": "up", "full_form": "hold up", "meaning": "Retrasar / asaltar", "spanish_translation": "retrasar", "is_separable": True, "example_sentence": "Traffic held us up for an hour.", "example_translation": "El tráfico nos retrasó una hora.", "category": "delay", "level": "C1"},
    {"verb": "hold", "particle": "on", "full_form": "hold on", "meaning": "Esperar / agarrarse", "spanish_translation": "esperar", "is_separable": False, "example_sentence": "Hold on, I'll be right back.", "example_translation": "Espera, ya regreso.", "category": "waiting", "level": "B1"},
    
    # MAKE
    {"verb": "make", "particle": "up", "full_form": "make up", "meaning": "Inventar / reconciliarse / maquillarse", "spanish_translation": "inventar, reconciliarse", "is_separable": True, "example_sentence": "Don't make up excuses.", "example_translation": "No inventes excusas.", "category": "action", "level": "B2"},
    {"verb": "make", "particle": "up for", "full_form": "make up for", "meaning": "Compensar", "spanish_translation": "compensar", "is_separable": False, "example_sentence": "I'll make up for lost time.", "example_translation": "Compensaré el tiempo perdido.", "category": "compensation", "level": "C1"},
    
    # PUT
    {"verb": "put", "particle": "up with", "full_form": "put up with", "meaning": "Tolerar, aguantar", "spanish_translation": "tolerar", "is_separable": False, "example_sentence": "I can't put up with this noise.", "example_translation": "No puedo tolerar este ruido.", "category": "tolerance", "level": "B2"},
    
    # LOOK
    {"verb": "look", "particle": "into", "full_form": "look into", "meaning": "Investigar", "spanish_translation": "investigar", "is_separable": False, "example_sentence": "The police are looking into the case.", "example_translation": "La policía está investigando el caso.", "category": "investigation", "level": "B2"},
    {"verb": "look", "particle": "down on", "full_form": "look down on", "meaning": "Menospreciar", "spanish_translation": "menospreciar", "is_separable": False, "example_sentence": "Don't look down on others.", "example_translation": "No menosprecies a otros.", "category": "attitude", "level": "C1"},
    
    # GET
    {"verb": "get", "particle": "over", "full_form": "get over", "meaning": "Superar, recuperarse de", "spanish_translation": "superar", "is_separable": False, "example_sentence": "It took time to get over the breakup.", "example_translation": "Tomó tiempo superar la ruptura.", "category": "recovery", "level": "B2"},
    {"verb": "get", "particle": "away with", "full_form": "get away with", "meaning": "Salirse con la suya", "spanish_translation": "salirse con la suya", "is_separable": False, "example_sentence": "He got away with cheating.", "example_translation": "Se salió con la suya haciendo trampa.", "category": "consequence", "level": "C1"},
    {"verb": "get", "particle": "rid of", "full_form": "get rid of", "meaning": "Deshacerse de", "spanish_translation": "deshacerse de", "is_separable": False, "example_sentence": "I need to get rid of old clothes.", "example_translation": "Necesito deshacerme de ropa vieja.", "category": "disposal", "level": "B2"},
    
    # TURN
    {"verb": "turn", "particle": "out", "full_form": "turn out", "meaning": "Resultar", "spanish_translation": "resultar", "is_separable": False, "example_sentence": "Everything turned out well.", "example_translation": "Todo resultó bien.", "category": "result", "level": "B2"},
    
    # TAKE
    {"verb": "take", "particle": "after", "full_form": "take after", "meaning": "Parecerse a", "spanish_translation": "parecerse a", "is_separable": False, "example_sentence": "She takes after her mother.", "example_translation": "Ella se parece a su madre.", "category": "family", "level": "B2"},
    {"verb": "take", "particle": "over", "full_form": "take over", "meaning": "Hacerse cargo, tomar control", "spanish_translation": "hacerse cargo", "is_separable": True, "example_sentence": "He took over the company.", "example_translation": "Él tomó control de la empresa.", "category": "control", "level": "B2"},
    {"verb": "take", "particle": "up", "full_form": "take up", "meaning": "Empezar un hobby / ocupar espacio", "spanish_translation": "empezar, ocupar", "is_separable": True, "example_sentence": "I took up painting last year.", "example_translation": "Empecé a pintar el año pasado.", "category": "hobby", "level": "B2"},
]


def seed_phrasal_verbs():
    """Agregar phrasal verbs a la base de datos"""
    with app.app_context():
        print("="*70)
        print("🔤 AGREGANDO PHRASAL VERBS")
        print("="*70)
        
        added = 0
        skipped = 0
        
        for pv_data in PHRASAL_VERBS:
            # Verificar si ya existe
            existing = PhrasalVerb.query.filter_by(full_form=pv_data['full_form']).first()
            if existing:
                skipped += 1
                continue
            
            pv = PhrasalVerb(
                verb=pv_data['verb'],
                particle=pv_data['particle'],
                full_form=pv_data['full_form'],
                meaning=pv_data['meaning'],
                spanish_translation=pv_data['spanish_translation'],
                is_separable=pv_data['is_separable'],
                example_sentence=pv_data['example_sentence'],
                example_translation=pv_data['example_translation'],
                category=pv_data['category'],
                level=pv_data['level']
            )
            db.session.add(pv)
            added += 1
        
        db.session.commit()
        
        print(f"✅ Phrasal verbs agregados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print(f"\n📊 Por nivel:")
        for level in ['A1', 'A2', 'B1', 'B2', 'C1']:
            count = PhrasalVerb.query.filter_by(level=level).count()
            print(f"   {level}: {count}")
        print(f"\n📊 Por verbo base:")
        from sqlalchemy import func
        verbs = db.session.query(PhrasalVerb.verb, func.count(PhrasalVerb.id)).group_by(PhrasalVerb.verb).all()
        for verb, count in sorted(verbs, key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {verb}: {count}")
        print("="*70)


if __name__ == '__main__':
    seed_phrasal_verbs()
