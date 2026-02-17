#!/usr/bin/env python3
"""
Seed de Conversaciones - Diálogos prácticos para aprender inglés conversacional
Organizados por nivel CEFR y situación
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Conversation, ConversationLine

app = create_app()

CONVERSATIONS = [
    # ============ A1 LEVEL - Basic Greetings & Introductions ============
    {
        "title": "Meeting Someone New",
        "title_spanish": "Conociendo a Alguien Nuevo",
        "description": "Basic introductions and greetings",
        "description_spanish": "Presentaciones y saludos básicos",
        "situation": "Two people meeting for the first time at a party",
        "situation_spanish": "Dos personas conociéndose por primera vez en una fiesta",
        "level": "A1",
        "category": "introductions",
        "audio_url": None,
        "lines": [
            {"speaker": "Anna", "text": "Hi! My name is Anna. What's your name?", "translation": "¡Hola! Me llamo Anna. ¿Cómo te llamas?", "notes": "'What's' = What is", "order": 1},
            {"speaker": "Ben", "text": "Hello, Anna. I'm Ben. Nice to meet you.", "translation": "Hola, Anna. Soy Ben. Mucho gusto.", "notes": "'I'm' = I am", "order": 2},
            {"speaker": "Anna", "text": "Nice to meet you too! Where are you from?", "translation": "¡Igualmente! ¿De dónde eres?", "notes": "Pregunta común al conocer gente", "order": 3},
            {"speaker": "Ben", "text": "I'm from Mexico. And you?", "translation": "Soy de México. ¿Y tú?", "notes": "'And you?' es informal para '¿Y tú?'", "order": 4},
            {"speaker": "Anna", "text": "I'm from Spain. How old are you?", "translation": "Soy de España. ¿Cuántos años tienes?", "notes": "", "order": 5},
            {"speaker": "Ben", "text": "I'm 25 years old. What do you do?", "translation": "Tengo 25 años. ¿A qué te dedicas?", "notes": "'What do you do?' = profesión", "order": 6},
            {"speaker": "Anna", "text": "I'm a student. I study English.", "translation": "Soy estudiante. Estudio inglés.", "notes": "", "order": 7},
            {"speaker": "Ben", "text": "That's great! Your English is very good.", "translation": "¡Qué bien! Tu inglés es muy bueno.", "notes": "Un cumplido común", "order": 8},
        ]
    },
    {
        "title": "At the Coffee Shop",
        "title_spanish": "En la Cafetería",
        "description": "Ordering coffee and drinks",
        "description_spanish": "Pidiendo café y bebidas",
        "situation": "A customer ordering at a coffee shop",
        "situation_spanish": "Un cliente haciendo un pedido en una cafetería",
        "level": "A1",
        "category": "shopping",
        "audio_url": None,
        "lines": [
            {"speaker": "Barista", "text": "Good morning! What can I get for you?", "translation": "¡Buenos días! ¿Qué le puedo servir?", "notes": "Frase estándar de servicio", "order": 1},
            {"speaker": "Customer", "text": "Hi! Can I have a coffee, please?", "translation": "¡Hola! ¿Puedo tener un café, por favor?", "notes": "'Can I have...' = forma educada de pedir", "order": 2},
            {"speaker": "Barista", "text": "Of course. What size? Small, medium, or large?", "translation": "Por supuesto. ¿Qué tamaño? ¿Pequeño, mediano o grande?", "notes": "", "order": 3},
            {"speaker": "Customer", "text": "Medium, please. How much is it?", "translation": "Mediano, por favor. ¿Cuánto cuesta?", "notes": "'How much is it?' = precio", "order": 4},
            {"speaker": "Barista", "text": "That's $3.50. Would you like anything else?", "translation": "Son $3.50. ¿Desea algo más?", "notes": "'That's' para indicar precio", "order": 5},
            {"speaker": "Customer", "text": "No, that's all. Thank you.", "translation": "No, eso es todo. Gracias.", "notes": "'That's all' = eso es todo", "order": 6},
            {"speaker": "Barista", "text": "Here you go. Have a nice day!", "translation": "Aquí tiene. ¡Que tenga un buen día!", "notes": "'Here you go' al entregar algo", "order": 7},
            {"speaker": "Customer", "text": "Thanks! You too!", "translation": "¡Gracias! ¡Igualmente!", "notes": "", "order": 8},
        ]
    },
    
    # ============ A2 LEVEL - Daily Life ============
    {
        "title": "Making Plans with a Friend",
        "title_spanish": "Haciendo Planes con un Amigo",
        "description": "Discussing weekend plans",
        "description_spanish": "Discutiendo planes para el fin de semana",
        "situation": "Two friends talking about weekend activities",
        "situation_spanish": "Dos amigos hablando sobre actividades del fin de semana",
        "level": "A2",
        "category": "social",
        "audio_url": None,
        "lines": [
            {"speaker": "Maria", "text": "Hey! What are you doing this weekend?", "translation": "¡Hey! ¿Qué vas a hacer este fin de semana?", "notes": "Presente continuo para planes futuros", "order": 1},
            {"speaker": "Carlos", "text": "I don't have any plans yet. Why?", "translation": "Todavía no tengo planes. ¿Por qué?", "notes": "'yet' = todavía", "order": 2},
            {"speaker": "Maria", "text": "Do you want to go to the movies on Saturday?", "translation": "¿Quieres ir al cine el sábado?", "notes": "'Do you want to...' para invitar", "order": 3},
            {"speaker": "Carlos", "text": "That sounds great! What time?", "translation": "¡Suena genial! ¿A qué hora?", "notes": "'That sounds great!' = aceptar con entusiasmo", "order": 4},
            {"speaker": "Maria", "text": "How about 7 PM? We can have dinner after.", "translation": "¿Qué tal a las 7 PM? Podemos cenar después.", "notes": "'How about...?' para sugerir", "order": 5},
            {"speaker": "Carlos", "text": "Perfect! Where should we meet?", "translation": "¡Perfecto! ¿Dónde nos vemos?", "notes": "'should' para sugerencias", "order": 6},
            {"speaker": "Maria", "text": "Let's meet at the mall entrance at 6:45.", "translation": "Veámonos en la entrada del centro comercial a las 6:45.", "notes": "'Let's' = vamos a", "order": 7},
            {"speaker": "Carlos", "text": "Sounds good! See you on Saturday!", "translation": "¡Suena bien! ¡Nos vemos el sábado!", "notes": "", "order": 8},
            {"speaker": "Maria", "text": "See you! Don't be late!", "translation": "¡Nos vemos! ¡No llegues tarde!", "notes": "'Don't be late' = no llegues tarde", "order": 9},
        ]
    },
    {
        "title": "At the Restaurant",
        "title_spanish": "En el Restaurante",
        "description": "Ordering food at a restaurant",
        "description_spanish": "Ordenando comida en un restaurante",
        "situation": "A couple ordering dinner at a restaurant",
        "situation_spanish": "Una pareja ordenando cena en un restaurante",
        "level": "A2",
        "category": "dining",
        "audio_url": None,
        "lines": [
            {"speaker": "Waiter", "text": "Good evening. Are you ready to order?", "translation": "Buenas noches. ¿Están listos para ordenar?", "notes": "", "order": 1},
            {"speaker": "Lisa", "text": "Yes, I'd like the grilled chicken, please.", "translation": "Sí, me gustaría el pollo a la parrilla, por favor.", "notes": "'I'd like' = forma educada de pedir", "order": 2},
            {"speaker": "Waiter", "text": "And for you, sir?", "translation": "¿Y para usted, señor?", "notes": "", "order": 3},
            {"speaker": "John", "text": "I'll have the pasta with tomato sauce.", "translation": "Yo voy a pedir la pasta con salsa de tomate.", "notes": "'I'll have' = otra forma de pedir", "order": 4},
            {"speaker": "Waiter", "text": "Would you like something to drink?", "translation": "¿Desean algo de tomar?", "notes": "'Would you like...?' muy formal", "order": 5},
            {"speaker": "Lisa", "text": "Can we have a bottle of water, please?", "translation": "¿Podemos tener una botella de agua, por favor?", "notes": "'Can we have' para pedir en grupo", "order": 6},
            {"speaker": "Waiter", "text": "Of course. Anything else?", "translation": "Por supuesto. ¿Algo más?", "notes": "", "order": 7},
            {"speaker": "John", "text": "That's all for now, thank you.", "translation": "Eso es todo por ahora, gracias.", "notes": "", "order": 8},
            {"speaker": "Waiter", "text": "Your order will be ready in about 15 minutes.", "translation": "Su orden estará lista en unos 15 minutos.", "notes": "", "order": 9},
        ]
    },
    {
        "title": "Asking for Directions",
        "title_spanish": "Pidiendo Direcciones",
        "description": "Getting directions to a location",
        "description_spanish": "Obteniendo direcciones a un lugar",
        "situation": "A tourist asking for directions",
        "situation_spanish": "Un turista pidiendo direcciones",
        "level": "A2",
        "category": "travel",
        "audio_url": None,
        "lines": [
            {"speaker": "Tourist", "text": "Excuse me, can you help me?", "translation": "Disculpe, ¿puede ayudarme?", "notes": "'Excuse me' para llamar atención", "order": 1},
            {"speaker": "Local", "text": "Sure, what do you need?", "translation": "Claro, ¿qué necesita?", "notes": "", "order": 2},
            {"speaker": "Tourist", "text": "I'm looking for the train station. Is it far?", "translation": "Estoy buscando la estación de tren. ¿Está lejos?", "notes": "'I'm looking for...' = busco", "order": 3},
            {"speaker": "Local", "text": "No, it's about 10 minutes on foot.", "translation": "No, está a unos 10 minutos a pie.", "notes": "'on foot' = caminando", "order": 4},
            {"speaker": "Tourist", "text": "How do I get there?", "translation": "¿Cómo llego ahí?", "notes": "", "order": 5},
            {"speaker": "Local", "text": "Go straight ahead for two blocks.", "translation": "Vaya derecho por dos cuadras.", "notes": "'straight ahead' = derecho", "order": 6},
            {"speaker": "Local", "text": "Then turn left at the traffic light.", "translation": "Luego gire a la izquierda en el semáforo.", "notes": "'traffic light' = semáforo", "order": 7},
            {"speaker": "Local", "text": "The station is on your right.", "translation": "La estación está a su derecha.", "notes": "'on your right' = a tu derecha", "order": 8},
            {"speaker": "Tourist", "text": "Thank you so much!", "translation": "¡Muchas gracias!", "notes": "", "order": 9},
            {"speaker": "Local", "text": "You're welcome. Have a nice day!", "translation": "De nada. ¡Que tenga un buen día!", "notes": "", "order": 10},
        ]
    },
    
    # ============ B1 LEVEL - Work & Travel ============
    {
        "title": "Job Interview",
        "title_spanish": "Entrevista de Trabajo",
        "description": "A basic job interview conversation",
        "description_spanish": "Una conversación de entrevista de trabajo básica",
        "situation": "A candidate at a job interview",
        "situation_spanish": "Un candidato en una entrevista de trabajo",
        "level": "B1",
        "category": "work",
        "audio_url": None,
        "lines": [
            {"speaker": "Interviewer", "text": "Please, have a seat. Tell me about yourself.", "translation": "Por favor, tome asiento. Cuénteme sobre usted.", "notes": "Pregunta de apertura típica", "order": 1},
            {"speaker": "Candidate", "text": "Thank you. I'm a marketing professional with 5 years of experience.", "translation": "Gracias. Soy un profesional de marketing con 5 años de experiencia.", "notes": "", "order": 2},
            {"speaker": "Interviewer", "text": "What are your main strengths?", "translation": "¿Cuáles son sus principales fortalezas?", "notes": "'strengths' = fortalezas", "order": 3},
            {"speaker": "Candidate", "text": "I'm very organized and I work well under pressure.", "translation": "Soy muy organizado y trabajo bien bajo presión.", "notes": "", "order": 4},
            {"speaker": "Interviewer", "text": "Why do you want to work for our company?", "translation": "¿Por qué quiere trabajar para nuestra empresa?", "notes": "Pregunta crucial en entrevistas", "order": 5},
            {"speaker": "Candidate", "text": "I admire your company's innovation and values.", "translation": "Admiro la innovación y los valores de su empresa.", "notes": "", "order": 6},
            {"speaker": "Candidate", "text": "I believe I can contribute to your team's success.", "translation": "Creo que puedo contribuir al éxito de su equipo.", "notes": "'contribute to' = contribuir a", "order": 7},
            {"speaker": "Interviewer", "text": "Where do you see yourself in five years?", "translation": "¿Dónde se ve en cinco años?", "notes": "Pregunta sobre metas futuras", "order": 8},
            {"speaker": "Candidate", "text": "I see myself growing within the company, possibly in a leadership role.", "translation": "Me veo creciendo dentro de la empresa, posiblemente en un rol de liderazgo.", "notes": "", "order": 9},
            {"speaker": "Interviewer", "text": "Great. Do you have any questions for me?", "translation": "Excelente. ¿Tiene alguna pregunta para mí?", "notes": "Oportunidad para mostrar interés", "order": 10},
            {"speaker": "Candidate", "text": "Yes, what does a typical day look like in this position?", "translation": "Sí, ¿cómo es un día típico en este puesto?", "notes": "", "order": 11},
        ]
    },
    {
        "title": "At the Hotel",
        "title_spanish": "En el Hotel",
        "description": "Checking in and asking about facilities",
        "description_spanish": "Registrándose y preguntando sobre instalaciones",
        "situation": "A guest checking into a hotel",
        "situation_spanish": "Un huésped registrándose en un hotel",
        "level": "B1",
        "category": "travel",
        "audio_url": None,
        "lines": [
            {"speaker": "Receptionist", "text": "Good afternoon. Welcome to Grand Hotel. How may I help you?", "translation": "Buenas tardes. Bienvenido al Hotel Grand. ¿En qué puedo ayudarle?", "notes": "", "order": 1},
            {"speaker": "Guest", "text": "Hi, I have a reservation under the name Johnson.", "translation": "Hola, tengo una reservación a nombre de Johnson.", "notes": "'under the name' = a nombre de", "order": 2},
            {"speaker": "Receptionist", "text": "Let me check... Yes, a double room for three nights, correct?", "translation": "Déjeme verificar... Sí, una habitación doble por tres noches, ¿correcto?", "notes": "", "order": 3},
            {"speaker": "Guest", "text": "That's right. Is breakfast included?", "translation": "Así es. ¿Está incluido el desayuno?", "notes": "", "order": 4},
            {"speaker": "Receptionist", "text": "Yes, breakfast is served from 7 to 10 AM in the restaurant.", "translation": "Sí, el desayuno se sirve de 7 a 10 AM en el restaurante.", "notes": "", "order": 5},
            {"speaker": "Guest", "text": "Great. Does the room have Wi-Fi?", "translation": "Genial. ¿La habitación tiene Wi-Fi?", "notes": "", "order": 6},
            {"speaker": "Receptionist", "text": "Yes, free Wi-Fi is available throughout the hotel.", "translation": "Sí, hay Wi-Fi gratis en todo el hotel.", "notes": "'throughout' = en todo", "order": 7},
            {"speaker": "Guest", "text": "What time is check-out?", "translation": "¿A qué hora es el check-out?", "notes": "", "order": 8},
            {"speaker": "Receptionist", "text": "Check-out is at 11 AM. Here's your key card. Room 405, fourth floor.", "translation": "El check-out es a las 11 AM. Aquí está su tarjeta. Habitación 405, cuarto piso.", "notes": "", "order": 9},
            {"speaker": "Guest", "text": "Thank you. Is there a gym in the hotel?", "translation": "Gracias. ¿Hay un gimnasio en el hotel?", "notes": "", "order": 10},
            {"speaker": "Receptionist", "text": "Yes, on the second floor. It's open 24 hours.", "translation": "Sí, en el segundo piso. Está abierto las 24 horas.", "notes": "", "order": 11},
        ]
    },
    {
        "title": "Doctor's Appointment",
        "title_spanish": "Cita con el Doctor",
        "description": "Describing symptoms to a doctor",
        "description_spanish": "Describiendo síntomas a un doctor",
        "situation": "A patient visiting a doctor",
        "situation_spanish": "Un paciente visitando a un doctor",
        "level": "B1",
        "category": "health",
        "audio_url": None,
        "lines": [
            {"speaker": "Doctor", "text": "Good morning. What seems to be the problem?", "translation": "Buenos días. ¿Cuál parece ser el problema?", "notes": "Pregunta estándar del doctor", "order": 1},
            {"speaker": "Patient", "text": "I've been feeling very tired lately, and I have a headache.", "translation": "Me he sentido muy cansado últimamente, y tengo dolor de cabeza.", "notes": "'lately' = últimamente", "order": 2},
            {"speaker": "Doctor", "text": "How long have you had these symptoms?", "translation": "¿Hace cuánto tiene estos síntomas?", "notes": "Presente perfecto para duración", "order": 3},
            {"speaker": "Patient", "text": "For about a week now.", "translation": "Desde hace una semana.", "notes": "'For' indica duración", "order": 4},
            {"speaker": "Doctor", "text": "Do you have any other symptoms? Fever, cough?", "translation": "¿Tiene otros síntomas? ¿Fiebre, tos?", "notes": "", "order": 5},
            {"speaker": "Patient", "text": "I've had a slight fever, but no cough.", "translation": "He tenido un poco de fiebre, pero no tengo tos.", "notes": "'slight' = leve", "order": 6},
            {"speaker": "Doctor", "text": "Are you taking any medication currently?", "translation": "¿Está tomando algún medicamento actualmente?", "notes": "", "order": 7},
            {"speaker": "Patient", "text": "No, just some vitamins.", "translation": "No, solo algunas vitaminas.", "notes": "", "order": 8},
            {"speaker": "Doctor", "text": "I'm going to prescribe some medicine for you.", "translation": "Le voy a recetar algún medicamento.", "notes": "'prescribe' = recetar", "order": 9},
            {"speaker": "Doctor", "text": "Take one pill twice a day after meals.", "translation": "Tome una pastilla dos veces al día después de las comidas.", "notes": "'twice a day' = dos veces al día", "order": 10},
            {"speaker": "Patient", "text": "How long should I take it?", "translation": "¿Por cuánto tiempo debo tomarlo?", "notes": "", "order": 11},
            {"speaker": "Doctor", "text": "For seven days. If you don't feel better, come back.", "translation": "Por siete días. Si no se siente mejor, regrese.", "notes": "", "order": 12},
        ]
    },
    
    # ============ B2 LEVEL - Professional & Social ============
    {
        "title": "Business Meeting",
        "title_spanish": "Reunión de Negocios",
        "description": "Discussing a project in a business meeting",
        "description_spanish": "Discutiendo un proyecto en una reunión de negocios",
        "situation": "Team members discussing project progress",
        "situation_spanish": "Miembros del equipo discutiendo el progreso del proyecto",
        "level": "B2",
        "category": "work",
        "audio_url": None,
        "lines": [
            {"speaker": "Manager", "text": "Let's get started. Sarah, can you give us an update on the project?", "translation": "Empecemos. Sarah, ¿puedes darnos una actualización del proyecto?", "notes": "'Let's get started' = empecemos", "order": 1},
            {"speaker": "Sarah", "text": "Sure. We've completed 80% of the development phase.", "translation": "Claro. Hemos completado el 80% de la fase de desarrollo.", "notes": "", "order": 2},
            {"speaker": "Sarah", "text": "However, we're facing some challenges with the integration.", "translation": "Sin embargo, estamos enfrentando algunos desafíos con la integración.", "notes": "'However' = sin embargo", "order": 3},
            {"speaker": "Manager", "text": "What kind of challenges?", "translation": "¿Qué tipo de desafíos?", "notes": "", "order": 4},
            {"speaker": "Sarah", "text": "The API isn't compatible with our current system.", "translation": "La API no es compatible con nuestro sistema actual.", "notes": "", "order": 5},
            {"speaker": "Tom", "text": "I think we should consider using a different approach.", "translation": "Creo que deberíamos considerar usar un enfoque diferente.", "notes": "'I think we should' = sugerencia formal", "order": 6},
            {"speaker": "Manager", "text": "What do you have in mind?", "translation": "¿Qué tienes en mente?", "notes": "'What do you have in mind?' = ¿qué propones?", "order": 7},
            {"speaker": "Tom", "text": "We could implement a middleware solution to bridge the gap.", "translation": "Podríamos implementar una solución de middleware para cerrar la brecha.", "notes": "'bridge the gap' = cerrar la brecha", "order": 8},
            {"speaker": "Manager", "text": "That's worth exploring. How would this affect the timeline?", "translation": "Vale la pena explorar eso. ¿Cómo afectaría esto el cronograma?", "notes": "'worth exploring' = vale la pena explorar", "order": 9},
            {"speaker": "Sarah", "text": "It might add about two weeks to the schedule.", "translation": "Podría agregar unas dos semanas al cronograma.", "notes": "'might' = podría (posibilidad)", "order": 10},
            {"speaker": "Manager", "text": "Let's proceed with that plan. Keep me posted on the progress.", "translation": "Procedamos con ese plan. Manténganme informado del progreso.", "notes": "'Keep me posted' = mantenme informado", "order": 11},
        ]
    },
    {
        "title": "Handling a Complaint",
        "title_spanish": "Manejando una Queja",
        "description": "Customer service handling a complaint",
        "description_spanish": "Servicio al cliente manejando una queja",
        "situation": "A customer complaining about a product",
        "situation_spanish": "Un cliente quejándose de un producto",
        "level": "B2",
        "category": "customer service",
        "audio_url": None,
        "lines": [
            {"speaker": "Customer", "text": "I'd like to speak to someone about a problem with my order.", "translation": "Me gustaría hablar con alguien sobre un problema con mi pedido.", "notes": "'I'd like to speak to' = forma educada de solicitar", "order": 1},
            {"speaker": "Agent", "text": "I'm sorry to hear that. I'll be happy to help. What seems to be the issue?", "translation": "Lamento escuchar eso. Estaré feliz de ayudar. ¿Cuál parece ser el problema?", "notes": "'I'm sorry to hear that' = empatía", "order": 2},
            {"speaker": "Customer", "text": "I ordered a laptop last week, but I received the wrong model.", "translation": "Ordené una laptop la semana pasada, pero recibí el modelo equivocado.", "notes": "", "order": 3},
            {"speaker": "Agent", "text": "I apologize for the inconvenience. Can I have your order number, please?", "translation": "Le pido disculpas por el inconveniente. ¿Me puede dar su número de orden, por favor?", "notes": "'I apologize for' = más formal que 'sorry'", "order": 4},
            {"speaker": "Customer", "text": "It's 45892. I've been a loyal customer for years, and this is frustrating.", "translation": "Es 45892. He sido un cliente fiel por años, y esto es frustrante.", "notes": "", "order": 5},
            {"speaker": "Agent", "text": "I completely understand your frustration. Let me look into this right away.", "translation": "Entiendo completamente su frustración. Déjeme investigar esto de inmediato.", "notes": "'look into' = investigar", "order": 6},
            {"speaker": "Agent", "text": "I can see the error. We'll send the correct model immediately.", "translation": "Puedo ver el error. Enviaremos el modelo correcto inmediatamente.", "notes": "", "order": 7},
            {"speaker": "Customer", "text": "What about returning the wrong one?", "translation": "¿Qué hay de devolver el equivocado?", "notes": "", "order": 8},
            {"speaker": "Agent", "text": "We'll arrange a free pickup. You don't need to do anything.", "translation": "Organizaremos una recolección gratuita. Usted no necesita hacer nada.", "notes": "'arrange' = organizar", "order": 9},
            {"speaker": "Agent", "text": "As compensation, I'd like to offer you a 15% discount on your next purchase.", "translation": "Como compensación, me gustaría ofrecerle un 15% de descuento en su próxima compra.", "notes": "'As compensation' = como compensación", "order": 10},
            {"speaker": "Customer", "text": "I appreciate that. Thank you for resolving this so quickly.", "translation": "Lo aprecio. Gracias por resolver esto tan rápido.", "notes": "'I appreciate that' = lo aprecio", "order": 11},
        ]
    },
    {
        "title": "Discussing Current Events",
        "title_spanish": "Discutiendo Eventos Actuales",
        "description": "Friends discussing news and opinions",
        "description_spanish": "Amigos discutiendo noticias y opiniones",
        "situation": "Friends having a casual conversation about news",
        "situation_spanish": "Amigos teniendo una conversación casual sobre noticias",
        "level": "B2",
        "category": "social",
        "audio_url": None,
        "lines": [
            {"speaker": "Alex", "text": "Did you hear about the new climate agreement?", "translation": "¿Escuchaste sobre el nuevo acuerdo climático?", "notes": "'Did you hear about' = ¿te enteraste de?", "order": 1},
            {"speaker": "Rachel", "text": "Yes, I read about it. It's quite significant, isn't it?", "translation": "Sí, leí sobre eso. Es bastante significativo, ¿no?", "notes": "'isn't it?' = tag question", "order": 2},
            {"speaker": "Alex", "text": "I think it's a step in the right direction, but it's not enough.", "translation": "Creo que es un paso en la dirección correcta, pero no es suficiente.", "notes": "", "order": 3},
            {"speaker": "Rachel", "text": "What makes you say that?", "translation": "¿Por qué dices eso?", "notes": "'What makes you say that?' = ¿por qué opinas eso?", "order": 4},
            {"speaker": "Alex", "text": "Well, the targets are too modest given the urgency of the situation.", "translation": "Bueno, los objetivos son muy modestos dada la urgencia de la situación.", "notes": "'given' = dado/dada", "order": 5},
            {"speaker": "Rachel", "text": "That's a fair point. However, getting all countries to agree is challenging.", "translation": "Es un punto válido. Sin embargo, lograr que todos los países estén de acuerdo es desafiante.", "notes": "'That's a fair point' = reconocer un argumento válido", "order": 6},
            {"speaker": "Alex", "text": "True, but I believe we need more ambitious commitments.", "translation": "Cierto, pero creo que necesitamos compromisos más ambiciosos.", "notes": "", "order": 7},
            {"speaker": "Rachel", "text": "I tend to agree with you. What do you think ordinary people can do?", "translation": "Tiendo a estar de acuerdo contigo. ¿Qué crees que pueden hacer las personas comunes?", "notes": "'I tend to agree' = tiendo a estar de acuerdo", "order": 8},
            {"speaker": "Alex", "text": "Every little action counts - reducing waste, using public transport...", "translation": "Cada pequeña acción cuenta - reducir residuos, usar transporte público...", "notes": "", "order": 9},
            {"speaker": "Rachel", "text": "Absolutely. I've been trying to be more conscious about my choices.", "translation": "Absolutamente. He estado tratando de ser más consciente sobre mis decisiones.", "notes": "", "order": 10},
        ]
    },
    
    # ============ C1 LEVEL - Advanced & Academic ============
    {
        "title": "Negotiating a Deal",
        "title_spanish": "Negociando un Trato",
        "description": "Business negotiation between companies",
        "description_spanish": "Negociación comercial entre empresas",
        "situation": "Representatives negotiating a partnership",
        "situation_spanish": "Representantes negociando una asociación",
        "level": "C1",
        "category": "business",
        "audio_url": None,
        "lines": [
            {"speaker": "Mr. Lee", "text": "Thank you for meeting with us today. We're keen to explore potential synergies.", "translation": "Gracias por reunirse con nosotros hoy. Estamos interesados en explorar posibles sinergias.", "notes": "'keen to' = muy interesado en", "order": 1},
            {"speaker": "Ms. Chen", "text": "Likewise. We've reviewed your proposal and it's quite compelling.", "translation": "Igualmente. Hemos revisado su propuesta y es bastante convincente.", "notes": "'compelling' = convincente", "order": 2},
            {"speaker": "Mr. Lee", "text": "We believe this partnership could be mutually beneficial.", "translation": "Creemos que esta asociación podría ser mutuamente beneficiosa.", "notes": "'mutually beneficial' = beneficio mutuo", "order": 3},
            {"speaker": "Ms. Chen", "text": "I agree in principle. However, we have some concerns about the revenue split.", "translation": "Estoy de acuerdo en principio. Sin embargo, tenemos algunas preocupaciones sobre la división de ingresos.", "notes": "'in principle' = en principio", "order": 4},
            {"speaker": "Mr. Lee", "text": "We're open to negotiation on that. What would you consider fair?", "translation": "Estamos abiertos a negociar eso. ¿Qué consideraría justo?", "notes": "'open to negotiation' = abierto a negociar", "order": 5},
            {"speaker": "Ms. Chen", "text": "Given our market reach, we'd propose a 60-40 split in our favor.", "translation": "Dado nuestro alcance de mercado, propondríamos una división 60-40 a nuestro favor.", "notes": "'in our favor' = a nuestro favor", "order": 6},
            {"speaker": "Mr. Lee", "text": "That's a significant shift from our initial offer. Could you elaborate on your reasoning?", "translation": "Ese es un cambio significativo de nuestra oferta inicial. ¿Podría elaborar su razonamiento?", "notes": "'elaborate on' = explicar en detalle", "order": 7},
            {"speaker": "Ms. Chen", "text": "We'd be bringing our existing customer base of 5 million users to the table.", "translation": "Estaríamos trayendo nuestra base de clientes existente de 5 millones de usuarios a la mesa.", "notes": "'bring to the table' = aportar", "order": 8},
            {"speaker": "Mr. Lee", "text": "That's a valid point. What if we meet in the middle at 55-45?", "translation": "Es un punto válido. ¿Qué tal si nos encontramos a la mitad en 55-45?", "notes": "'meet in the middle' = encontrar punto medio", "order": 9},
            {"speaker": "Ms. Chen", "text": "We could consider that if you include exclusivity in certain markets.", "translation": "Podríamos considerar eso si incluyen exclusividad en ciertos mercados.", "notes": "", "order": 10},
            {"speaker": "Mr. Lee", "text": "Let us discuss that internally and get back to you by Friday.", "translation": "Déjenos discutir eso internamente y responderle para el viernes.", "notes": "'get back to you' = responderle/contactarle", "order": 11},
        ]
    },
    {
        "title": "Academic Discussion",
        "title_spanish": "Discusión Académica",
        "description": "University students discussing research",
        "description_spanish": "Estudiantes universitarios discutiendo investigación",
        "situation": "Graduate students in a research seminar",
        "situation_spanish": "Estudiantes de posgrado en un seminario de investigación",
        "level": "C1",
        "category": "academic",
        "audio_url": None,
        "lines": [
            {"speaker": "Professor", "text": "Let's examine the methodology of this study. What are your initial thoughts?", "translation": "Examinemos la metodología de este estudio. ¿Cuáles son sus pensamientos iniciales?", "notes": "", "order": 1},
            {"speaker": "Student 1", "text": "The sample size seems adequate, but I question the selection criteria.", "translation": "El tamaño de la muestra parece adecuado, pero cuestiono los criterios de selección.", "notes": "'I question' = cuestiono (uso académico)", "order": 2},
            {"speaker": "Professor", "text": "Can you elaborate on your concern?", "translation": "¿Puede elaborar su preocupación?", "notes": "", "order": 3},
            {"speaker": "Student 1", "text": "The participants were self-selected, which could introduce significant bias.", "translation": "Los participantes se auto-seleccionaron, lo cual podría introducir sesgo significativo.", "notes": "'self-selected' = auto-seleccionado", "order": 4},
            {"speaker": "Student 2", "text": "That's a valid observation. Additionally, the study lacks a control group.", "translation": "Es una observación válida. Además, el estudio carece de un grupo de control.", "notes": "'lacks' = carece de", "order": 5},
            {"speaker": "Professor", "text": "These are pertinent criticisms. How might we address these limitations?", "translation": "Estas son críticas pertinentes. ¿Cómo podríamos abordar estas limitaciones?", "notes": "'pertinent' = pertinente, relevante", "order": 6},
            {"speaker": "Student 1", "text": "A randomized controlled trial would strengthen the validity of the findings.", "translation": "Un ensayo controlado aleatorizado fortalecería la validez de los hallazgos.", "notes": "'RCT' = ensayo controlado aleatorizado", "order": 7},
            {"speaker": "Student 2", "text": "Though ethically, that might not be feasible in this context.", "translation": "Aunque éticamente, eso podría no ser factible en este contexto.", "notes": "'feasible' = factible", "order": 8},
            {"speaker": "Professor", "text": "Precisely. Research often involves navigating such ethical constraints.", "translation": "Precisamente. La investigación frecuentemente implica navegar tales restricciones éticas.", "notes": "'navigating' = navegar, manejar", "order": 9},
            {"speaker": "Student 1", "text": "Perhaps a quasi-experimental design would be a reasonable compromise.", "translation": "Quizás un diseño cuasi-experimental sería un compromiso razonable.", "notes": "'compromise' = punto medio, compromiso", "order": 10},
            {"speaker": "Professor", "text": "Excellent suggestion. That demonstrates sophisticated methodological thinking.", "translation": "Excelente sugerencia. Eso demuestra un pensamiento metodológico sofisticado.", "notes": "", "order": 11},
        ]
    },
    {
        "title": "Resolving a Misunderstanding",
        "title_spanish": "Resolviendo un Malentendido",
        "description": "Friends clearing up a misunderstanding",
        "description_spanish": "Amigos aclarando un malentendido",
        "situation": "Two friends having an honest conversation",
        "situation_spanish": "Dos amigos teniendo una conversación honesta",
        "level": "C1",
        "category": "relationships",
        "audio_url": None,
        "lines": [
            {"speaker": "Emma", "text": "I've been meaning to talk to you. I feel like there's been some tension between us.", "translation": "He querido hablar contigo. Siento que ha habido algo de tensión entre nosotros.", "notes": "'I've been meaning to' = he querido/tenido la intención de", "order": 1},
            {"speaker": "Sophie", "text": "I've noticed it too. I wasn't sure how to bring it up.", "translation": "También lo he notado. No estaba segura de cómo mencionarlo.", "notes": "'bring it up' = mencionar un tema", "order": 2},
            {"speaker": "Emma", "text": "I think it started after the incident at the party.", "translation": "Creo que empezó después del incidente en la fiesta.", "notes": "", "order": 3},
            {"speaker": "Sophie", "text": "You mean when you left early? I have to admit, I felt a bit hurt.", "translation": "¿Te refieres a cuando te fuiste temprano? Debo admitir que me sentí un poco herida.", "notes": "'I have to admit' = debo admitir", "order": 4},
            {"speaker": "Emma", "text": "I realize now how that might have looked. That wasn't my intention at all.", "translation": "Ahora me doy cuenta de cómo se pudo ver eso. Esa no era mi intención en absoluto.", "notes": "'how that might have looked' = cómo se pudo ver", "order": 5},
            {"speaker": "Sophie", "text": "I assumed you were upset with me for something.", "translation": "Asumí que estabas molesta conmigo por algo.", "notes": "'assumed' = asumí", "order": 6},
            {"speaker": "Emma", "text": "Not at all. I had a family emergency and had to leave urgently.", "translation": "Para nada. Tuve una emergencia familiar y tuve que irme urgentemente.", "notes": "", "order": 7},
            {"speaker": "Emma", "text": "I should have explained at the time. I'm sorry for the confusion.", "translation": "Debí haber explicado en ese momento. Lamento la confusión.", "notes": "'I should have' = debí haber", "order": 8},
            {"speaker": "Sophie", "text": "I'm the one who should apologize for jumping to conclusions.", "translation": "Soy yo quien debería disculparse por sacar conclusiones precipitadas.", "notes": "'jumping to conclusions' = sacar conclusiones precipitadas", "order": 9},
            {"speaker": "Emma", "text": "Let's just agree to communicate more openly in the future.", "translation": "Acordemos simplemente comunicarnos más abiertamente en el futuro.", "notes": "'Let's agree to' = acordemos", "order": 10},
            {"speaker": "Sophie", "text": "Absolutely. I value our friendship too much to let misunderstandings get in the way.", "translation": "Absolutamente. Valoro demasiado nuestra amistad para dejar que los malentendidos se interpongan.", "notes": "'get in the way' = interponerse", "order": 11},
        ]
    },
]


def seed_conversations():
    """Agregar conversaciones a la base de datos"""
    with app.app_context():
        print("="*70)
        print("🗣️ AGREGANDO CONVERSACIONES")
        print("="*70)
        
        conversations_added = 0
        lines_added = 0
        skipped = 0
        
        for conv_data in CONVERSATIONS:
            # El modelo usa 'scenario' como identificador único, creamos uno a partir del title
            scenario_id = conv_data['title'].lower().replace(' ', '_').replace("'", "")
            
            # Verificar si ya existe
            existing = Conversation.query.filter_by(scenario=scenario_id).first()
            if existing:
                skipped += 1
                continue
            
            # El modelo tiene: scenario (unique), title, description
            # No tiene: title_spanish, description_spanish, situation, situation_spanish, level, category, audio_url
            # Combinamos la info en description
            full_description = f"""Level: {conv_data['level']} | Category: {conv_data['category']}

Situation: {conv_data['situation']}
Situación: {conv_data['situation_spanish']}

{conv_data['description']} / {conv_data['description_spanish']}"""
            
            conversation = Conversation(
                scenario=scenario_id,
                title=conv_data['title'],
                description=full_description
            )
            db.session.add(conversation)
            db.session.flush()  # Para obtener el ID
            
            conversations_added += 1
            
            # Agregar las líneas de diálogo
            # El modelo tiene: conversation_id, speaker, text, order
            # No tiene: translation, notes (los añadimos al texto)
            for line_data in conv_data['lines']:
                # Incluimos la traducción en el texto para mantener la info
                text_with_translation = f"{line_data['text']}"
                if line_data.get('notes'):
                    text_with_translation += f" [{line_data['notes']}]"
                text_with_translation += f"\n📝 {line_data['translation']}"
                
                line = ConversationLine(
                    conversation_id=conversation.id,
                    speaker=line_data['speaker'],
                    text=text_with_translation,
                    order=line_data['order']
                )
                db.session.add(line)
                lines_added += 1
        
        db.session.commit()
        
        print(f"✅ Conversaciones agregadas: {conversations_added}")
        print(f"✅ Líneas de diálogo agregadas: {lines_added}")
        print(f"⏭️  Omitidas (ya existían): {skipped}")
        
        # Mostrar resumen
        total_convs = Conversation.query.count()
        total_lines = ConversationLine.query.count()
        print(f"\n📊 Total conversaciones: {total_convs}")
        print(f"📊 Total líneas de diálogo: {total_lines}")
        print(f"📊 Promedio líneas por conversación: {total_lines/max(total_convs,1):.1f}")
        print("="*70)


if __name__ == '__main__':
    seed_conversations()
