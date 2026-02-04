from flask import Blueprint, render_template, abort, request, session, redirect, url_for
from flask_login import login_required, current_user
import Levenshtein
from app.extensions import db
from app.models import Conversation, ConversationLine, ConversationPractice, AlternativeResponse, ResponsePattern
from datetime import datetime

conversation_bp = Blueprint('conversation', __name__, url_prefix='/conversation')

# Conversaciones de ejemplo (puedes migrar a BD después)
conversations = {
    'store': {
        'title': 'At the Store',
        'description': 'Aprende a comprar productos y preguntar precios en una tienda',
        'user_role': 'Customer',
        'system_role': 'Clerk',
        'icon': '🛒',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning! Welcome to our store. How can I help you today?'},
            {'speaker': 'user', 'expected': 'Hello, I would like to buy some bread, please.', 
             'options': ['Hello, I would like to buy some bread, please.', 'Hi, do you have fresh bread?', 'Good morning, I need some bread.']},
            {'speaker': 'system', 'text': 'Of course! We have fresh bread. Would you like white or whole wheat?'},
            {'speaker': 'user', 'expected': 'I would like whole wheat bread, please.',
             'options': ['I would like whole wheat bread, please.', 'White bread, please.', 'Can I have whole wheat?']},
            {'speaker': 'system', 'text': 'Great choice! Anything else?'},
            {'speaker': 'user', 'expected': 'No, that is all. How much is it?',
             'options': ['No, that is all. How much is it?', 'That would be everything. What is the total?', 'Nothing else, thank you. How much do I owe you?']},
            {'speaker': 'system', 'text': 'That will be 3 dollars, please.'},
            {'speaker': 'user', 'expected': 'Here you go. Thank you very much!',
             'options': ['Here you go. Thank you very much!', 'Here is the money. Thanks!', 'Thank you. Have a nice day!']},
            {'speaker': 'system', 'text': 'Thank you! Have a nice day!'},
        ]
    },
    'directions': {
        'title': 'Asking for Directions',
        'description': 'Practica cómo pedir direcciones y entender indicaciones',
        'user_role': 'Tourist',
        'system_role': 'Local',
        'icon': '🗺️',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! You look a bit lost. Do you need help?'},
            {'speaker': 'user', 'expected': 'Yes, please. I am looking for the bus station.',
             'options': ['Yes, please. I am looking for the bus station.', 'Hi, where is the bus station?', 'Excuse me, can you help me find the bus station?']},
            {'speaker': 'system', 'text': 'The bus station is two blocks ahead, then turn right.'},
            {'speaker': 'user', 'expected': 'Thank you. Is it far from here?',
             'options': ['Thank you. Is it far from here?', 'Thanks! How long will it take to get there?', 'I see. Is it a long walk?']},
            {'speaker': 'system', 'text': 'Not at all, about a 5-minute walk.'},
            {'speaker': 'user', 'expected': 'Great, thank you for your help!',
             'options': ['Great, thank you for your help!', 'Perfect, thanks a lot!', 'Wonderful, I appreciate it!']},
            {'speaker': 'system', 'text': 'You are welcome! Good luck!'},
        ]
    },
    'greetings': {
        'title': 'Greetings and Introductions',
        'description': 'Conoce a alguien nuevo y preséntate en inglés',
        'user_role': 'You',
        'system_role': 'New Friend',
        'icon': '👋',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hi there! I am Sarah. Nice to meet you!'},
            {'speaker': 'user', 'expected': 'Nice to meet you too! My name is...',
             'options': ['Nice to meet you too! My name is...', 'Hello Sarah! I am pleased to meet you.', 'Hi! Nice to meet you as well.']},
            {'speaker': 'system', 'text': 'Where are you from?'},
            {'speaker': 'user', 'expected': 'I am from Mexico. And you?',
             'options': ['I am from Mexico. And you?', 'I come from Mexico. What about you?', 'Mexico! Where are you from?']},
            {'speaker': 'system', 'text': 'I am from Canada. What do you do for a living?'},
            {'speaker': 'user', 'expected': 'I am a student. I study computer science.',
             'options': ['I am a student. I study computer science.', 'I work as a programmer.', 'I am studying at the university.']},
            {'speaker': 'system', 'text': 'That sounds interesting! It was nice talking to you!'},
            {'speaker': 'user', 'expected': 'It was nice talking to you too. See you later!',
             'options': ['It was nice talking to you too. See you later!', 'Same here! Goodbye!', 'Nice chatting with you. Take care!']},
        ]
    },
    'restaurant': {
        'title': 'At the Restaurant',
        'description': 'Ordena comida, bebidas y pide la cuenta en un restaurante',
        'user_role': 'Customer',
        'system_role': 'Waiter',
        'icon': '🍽️',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Good evening! Welcome to our restaurant. Do you have a reservation?'},
            {'speaker': 'user', 'expected': 'No, I do not have a reservation. Do you have a table for two?',
             'options': ['No, I do not have a reservation. Do you have a table for two?', 'No reservation. Is there any table available?', 'We did not make a reservation. Can we still get a table?']},
            {'speaker': 'system', 'text': 'Yes, please follow me. Here is the menu. Can I get you something to drink?'},
            {'speaker': 'user', 'expected': 'I would like a glass of water, please.',
             'options': ['I would like a glass of water, please.', 'Can I have some water?', 'Just water for now, thank you.']},
            {'speaker': 'system', 'text': 'Of course! Are you ready to order, or do you need more time?'},
            {'speaker': 'user', 'expected': 'I am ready. I would like the grilled chicken with salad.',
             'options': ['I am ready. I would like the grilled chicken with salad.', 'Yes, I will have the chicken please.', 'Can I get the grilled chicken and a side salad?']},
            {'speaker': 'system', 'text': 'Excellent choice! Would you like any dessert after your meal?'},
            {'speaker': 'user', 'expected': 'Yes, I will have the chocolate cake, please.',
             'options': ['Yes, I will have the chocolate cake, please.', 'What desserts do you have?', 'No dessert for me, thank you.']},
            {'speaker': 'system', 'text': 'Perfect! Your order will be ready soon.'},
            {'speaker': 'user', 'expected': 'Thank you very much!',
             'options': ['Thank you very much!', 'Great, thanks!', 'I appreciate it!']},
        ]
    },
    'hotel': {
        'title': 'Hotel Check-in',
        'description': 'Registrarte en un hotel y hacer preguntas sobre tu estadía',
        'user_role': 'Guest',
        'system_role': 'Receptionist',
        'icon': '🏨',
        'difficulty': 'Intermediate',
        'dialogue': [
            {'speaker': 'system', 'text': 'Good afternoon! Welcome to the Grand Hotel. How may I help you?'},
            {'speaker': 'user', 'expected': 'Hello, I have a reservation under the name Johnson.',
             'options': ['Hello, I have a reservation under the name Johnson.', 'Hi, I booked a room online. My name is Johnson.', 'Good afternoon. I would like to check in please.']},
            {'speaker': 'system', 'text': 'Let me check... Yes, I found it. A double room for three nights, correct?'},
            {'speaker': 'user', 'expected': 'Yes, that is correct.',
             'options': ['Yes, that is correct.', 'That is right.', 'Exactly, three nights.']},
            {'speaker': 'system', 'text': 'I will need your ID and a credit card for the deposit, please.'},
            {'speaker': 'user', 'expected': 'Here you go. Here is my passport and credit card.',
             'options': ['Here you go. Here is my passport and credit card.', 'Sure, here they are.', 'Of course, here is my ID and card.']},
            {'speaker': 'system', 'text': 'Thank you. Your room is on the fifth floor, room 512. Would you like help with your luggage?'},
            {'speaker': 'user', 'expected': 'No, thank you. I can manage. What time is breakfast?',
             'options': ['No, thank you. I can manage. What time is breakfast?', 'Yes, please. And when is breakfast served?', 'I am fine, thanks. Where is the restaurant?']},
            {'speaker': 'system', 'text': 'Breakfast is served from 7 to 10 AM in the restaurant on the ground floor. Enjoy your stay!'},
            {'speaker': 'user', 'expected': 'Thank you. Have a nice day!',
             'options': ['Thank you. Have a nice day!', 'Great, thanks for your help!', 'Perfect, thank you very much!']},
        ]
    },
    'airport': {
        'title': 'At the Airport',
        'description': 'Facturar equipaje, pasar seguridad y encontrar tu puerta de embarque',
        'user_role': 'Traveler',
        'system_role': 'Agent',
        'icon': '✈️',
        'difficulty': 'Intermediate',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! May I see your passport and boarding pass, please?'},
            {'speaker': 'user', 'expected': 'Of course, here they are.',
             'options': ['Of course, here they are.', 'Sure, here you go.', 'Yes, here is my passport and boarding pass.']},
            {'speaker': 'system', 'text': 'Are you checking any bags today?'},
            {'speaker': 'user', 'expected': 'Yes, I have one suitcase to check.',
             'options': ['Yes, I have one suitcase to check.', 'Just this one bag.', 'I have one checked bag and one carry-on.']},
            {'speaker': 'system', 'text': 'Please place your bag on the scale. Would you like a window or aisle seat?'},
            {'speaker': 'user', 'expected': 'A window seat, please.',
             'options': ['A window seat, please.', 'I prefer the aisle, please.', 'Do you have any window seats available?']},
            {'speaker': 'system', 'text': 'Here is your boarding pass. Your flight departs from gate B12. Boarding starts at 3:30 PM.'},
            {'speaker': 'user', 'expected': 'Thank you. Where is gate B12?',
             'options': ['Thank you. Where is gate B12?', 'How do I get to gate B12?', 'Could you tell me how to find gate B12?']},
            {'speaker': 'system', 'text': 'Go through security, then turn left. It is about a 10-minute walk. Have a safe flight!'},
            {'speaker': 'user', 'expected': 'Thank you so much. Have a nice day!',
             'options': ['Thank you so much. Have a nice day!', 'Thanks for your help!', 'I appreciate it. Goodbye!']},
        ]
    },
    'doctor': {
        'title': 'At the Doctor\'s Office',
        'description': 'Describe tus síntomas y entiende las instrucciones del médico',
        'user_role': 'Patient',
        'system_role': 'Doctor',
        'icon': '🏥',
        'difficulty': 'Intermediate',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! What brings you in today? How are you feeling?'},
            {'speaker': 'user', 'expected': 'Hello, doctor. I have had a headache and fever for three days.',
             'options': ['Hello, doctor. I have had a headache and fever for three days.', 'I am not feeling well. I have a bad headache.', 'I have been sick since Monday with fever and pain.']},
            {'speaker': 'system', 'text': 'I see. Have you taken any medication?'},
            {'speaker': 'user', 'expected': 'Yes, I have been taking some aspirin, but it does not help much.',
             'options': ['Yes, I have been taking some aspirin, but it does not help much.', 'I tried some pain relievers but they did not work.', 'Only some over-the-counter medicine.']},
            {'speaker': 'system', 'text': 'Do you have any other symptoms like cough, sore throat, or body aches?'},
            {'speaker': 'user', 'expected': 'Yes, I also have a sore throat and I feel very tired.',
             'options': ['Yes, I also have a sore throat and I feel very tired.', 'My throat hurts and I have no energy.', 'I have been coughing a little and feeling weak.']},
            {'speaker': 'system', 'text': 'It sounds like you might have the flu. I am going to prescribe some medication. Make sure to rest and drink plenty of fluids.'},
            {'speaker': 'user', 'expected': 'Thank you, doctor. How long until I feel better?',
             'options': ['Thank you, doctor. How long until I feel better?', 'When should I expect to recover?', 'How many days should I rest?']},
            {'speaker': 'system', 'text': 'You should feel better in about a week. If symptoms persist, please come back.'},
            {'speaker': 'user', 'expected': 'I will. Thank you for your help, doctor.',
             'options': ['I will. Thank you for your help, doctor.', 'Okay, I appreciate your help.', 'Thanks so much. I will follow your advice.']},
        ]
    },
    'job_interview': {
        'title': 'Job Interview',
        'description': 'Responde preguntas profesionales y destaca tus habilidades',
        'user_role': 'Candidate',
        'system_role': 'Interviewer',
        'icon': '💼',
        'difficulty': 'Advanced',
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning! Please have a seat. Thank you for coming. Can you tell me a little about yourself?'},
            {'speaker': 'user', 'expected': 'Good morning! Thank you for having me. I am a software developer with five years of experience.',
             'options': ['Good morning! Thank you for having me. I am a software developer with five years of experience.', 'Hello! I am excited to be here. I have been working in tech for several years.', 'Thanks for the opportunity. I am a passionate programmer with strong skills in web development.']},
            {'speaker': 'system', 'text': 'That sounds great. Why are you interested in this position?'},
            {'speaker': 'user', 'expected': 'I am looking for new challenges and I admire your company\'s innovative projects.',
             'options': ['I am looking for new challenges and I admire your company\'s innovative projects.', 'I want to grow professionally and your company has a great reputation.', 'This role aligns perfectly with my career goals and skills.']},
            {'speaker': 'system', 'text': 'What would you say is your greatest strength?'},
            {'speaker': 'user', 'expected': 'I am very organized and I work well under pressure.',
             'options': ['I am very organized and I work well under pressure.', 'I am a quick learner and adapt easily to new technologies.', 'My problem-solving skills are my biggest asset.']},
            {'speaker': 'system', 'text': 'And what about your weaknesses?'},
            {'speaker': 'user', 'expected': 'Sometimes I focus too much on details, but I am working on finding a better balance.',
             'options': ['Sometimes I focus too much on details, but I am working on finding a better balance.', 'I can be a perfectionist, which sometimes slows me down.', 'I am still improving my public speaking skills.']},
            {'speaker': 'system', 'text': 'Where do you see yourself in five years?'},
            {'speaker': 'user', 'expected': 'I hope to be in a leadership role, contributing to major projects.',
             'options': ['I hope to be in a leadership role, contributing to major projects.', 'I see myself growing within the company and taking on more responsibility.', 'I want to become an expert in my field and mentor others.']},
            {'speaker': 'system', 'text': 'Do you have any questions for me?'},
            {'speaker': 'user', 'expected': 'Yes, what does a typical day look like in this role?',
             'options': ['Yes, what does a typical day look like in this role?', 'What are the opportunities for professional development?', 'Can you tell me more about the team I would be working with?']},
        ]
    },
    'phone_call': {
        'title': 'Making a Phone Call',
        'description': 'Haz llamadas telefónicas profesionales y deja mensajes',
        'user_role': 'Caller',
        'system_role': 'Receptionist',
        'icon': '📞',
        'difficulty': 'Intermediate',
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning, ABC Company. How may I direct your call?'},
            {'speaker': 'user', 'expected': 'Hello, I would like to speak with Mr. Smith from the sales department, please.',
             'options': ['Hello, I would like to speak with Mr. Smith from the sales department, please.', 'Hi, can you connect me to the sales team?', 'Good morning, I am trying to reach someone in sales.']},
            {'speaker': 'system', 'text': 'May I ask who is calling and what this is regarding?'},
            {'speaker': 'user', 'expected': 'My name is John Davis. I am calling about a product inquiry.',
             'options': ['My name is John Davis. I am calling about a product inquiry.', 'This is John Davis. I have some questions about your services.', 'I am John from XYZ Corp, calling regarding a business matter.']},
            {'speaker': 'system', 'text': 'Thank you, Mr. Davis. Please hold while I transfer your call.'},
            {'speaker': 'user', 'expected': 'Thank you, I will wait.',
             'options': ['Thank you, I will wait.', 'Sure, no problem.', 'Okay, thanks.']},
            {'speaker': 'system', 'text': 'I am sorry, Mr. Smith is in a meeting right now. Would you like to leave a message or call back later?'},
            {'speaker': 'user', 'expected': 'Could you please ask him to call me back? My number is 555-1234.',
             'options': ['Could you please ask him to call me back? My number is 555-1234.', 'I will call back in an hour. Thank you.', 'Can I leave a message for him to return my call?']},
            {'speaker': 'system', 'text': 'Of course! I will make sure he gets the message. Is there anything else I can help you with?'},
            {'speaker': 'user', 'expected': 'No, that is all. Thank you for your help. Goodbye!',
             'options': ['No, that is all. Thank you for your help. Goodbye!', 'That is everything. Have a nice day!', 'Nothing else, thanks. Bye!']},
        ]
    },
    'shopping_clothes': {
        'title': 'Shopping for Clothes',
        'description': 'Compra ropa, pregunta por tallas y usa el probador',
        'user_role': 'Shopper',
        'system_role': 'Sales Assistant',
        'icon': '👕',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! Welcome to our store. Are you looking for something specific?'},
            {'speaker': 'user', 'expected': 'Yes, I am looking for a jacket for the winter.',
             'options': ['Yes, I am looking for a jacket for the winter.', 'Hi, do you have any warm jackets?', 'I need a winter coat, please.']},
            {'speaker': 'system', 'text': 'We have a great selection over here. What size do you wear?'},
            {'speaker': 'user', 'expected': 'I usually wear a medium.',
             'options': ['I usually wear a medium.', 'I am a size M.', 'Medium should fit me.']},
            {'speaker': 'system', 'text': 'Here are some options in medium. Would you like to try them on?'},
            {'speaker': 'user', 'expected': 'Yes, please. Where are the fitting rooms?',
             'options': ['Yes, please. Where are the fitting rooms?', 'Sure, can I try this one on?', 'I would like to try the blue one.']},
            {'speaker': 'system', 'text': 'The fitting rooms are at the back of the store, on the right.'},
            {'speaker': 'user', 'expected': 'Thank you. I will try this one.',
             'options': ['Thank you. I will try this one.', 'Great, I will be right back.', 'Thanks, I will go try it on.']},
            {'speaker': 'system', 'text': 'How does it fit?'},
            {'speaker': 'user', 'expected': 'It fits perfectly! I will take it. How much is it?',
             'options': ['It fits perfectly! I will take it. How much is it?', 'It is a bit tight. Do you have a larger size?', 'I love it! What is the price?']},
            {'speaker': 'system', 'text': 'It is 75 dollars. Would you like to pay by cash or card?'},
            {'speaker': 'user', 'expected': 'I will pay by card, please.',
             'options': ['I will pay by card, please.', 'Cash, please.', 'Do you accept credit cards?']},
        ]
    },
    'taxi': {
        'title': 'Taking a Taxi',
        'description': 'Indica tu destino, pregunta el precio y paga el viaje',
        'user_role': 'Passenger',
        'system_role': 'Taxi Driver',
        'icon': '🚕',
        'difficulty': 'Beginner',
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! Where would you like to go?'},
            {'speaker': 'user', 'expected': 'Hi, can you take me to the airport, please?',
             'options': ['Hi, can you take me to the airport, please?', 'I need to go to the international airport.', 'To the airport, please.']},
            {'speaker': 'system', 'text': 'Sure! Do you have a flight to catch? I will take the fastest route.'},
            {'speaker': 'user', 'expected': 'Yes, my flight is in two hours. How long will it take?',
             'options': ['Yes, my flight is in two hours. How long will it take?', 'I have plenty of time. No rush.', 'Yes, I need to be there soon. What is the estimated time?']},
            {'speaker': 'system', 'text': 'It should take about 30 minutes, depending on traffic.'},
            {'speaker': 'user', 'expected': 'That sounds good. Thank you.',
             'options': ['That sounds good. Thank you.', 'Perfect, that works for me.', 'Great, let us go.']},
            {'speaker': 'system', 'text': 'Here we are! That will be 25 dollars.'},
            {'speaker': 'user', 'expected': 'Here you go. Keep the change.',
             'options': ['Here you go. Keep the change.', 'Do you accept credit cards?', 'Here is 30 dollars. You can keep the rest.']},
            {'speaker': 'system', 'text': 'Thank you! Have a safe flight!'},
            {'speaker': 'user', 'expected': 'Thank you! Have a nice day!',
             'options': ['Thank you! Have a nice day!', 'Thanks! Goodbye!', 'I appreciate it. Take care!']},
        ]
    },
}

def calculate_score(similarity):
    """Calcular puntaje basado en similitud"""
    if similarity > 0.85:
        return 100
    elif similarity > 0.7:
        return 80
    elif similarity > 0.5:
        return 60
    elif similarity > 0.3:
        return 40
    else:
        return 20

def get_feedback(similarity, expected, alternative_match=None):
    """Generar retroalimentación basada en similitud"""
    if alternative_match:
        return {
            'type': 'success', 
            'message': '¡Excelente! Tu respuesta es válida y natural.', 
            'suggestion': f'También podrías decir: "{expected}"',
            'learned': True
        }
    if similarity > 0.85:
        return {'type': 'success', 'message': '¡Excelente! Tu respuesta es muy natural.', 'suggestion': None}
    elif similarity > 0.7:
        return {'type': 'good', 'message': '¡Muy bien! Casi perfecto.', 'suggestion': f'Una forma ideal sería: "{expected}"'}
    elif similarity > 0.5:
        return {'type': 'ok', 'message': 'Bien, pero se puede mejorar.', 'suggestion': f'Intenta algo como: "{expected}"'}
    else:
        return {'type': 'needs_work', 'message': 'Sigue practicando.', 'suggestion': f'La respuesta esperada era: "{expected}"'}


def detect_pattern_type(text):
    """Detectar el tipo de patrón de una respuesta"""
    text_lower = text.lower()
    if any(word in text_lower for word in ['hello', 'hi', 'good morning', 'good afternoon', 'good evening']):
        return 'greeting'
    elif any(word in text_lower for word in ['thank', 'thanks', 'appreciate']):
        return 'thanks'
    elif any(word in text_lower for word in ['goodbye', 'bye', 'see you', 'take care']):
        return 'farewell'
    elif any(word in text_lower for word in ['please', 'could you', 'would you', 'can you']):
        return 'request'
    elif '?' in text:
        return 'question'
    elif any(word in text_lower for word in ['sorry', 'excuse me', 'pardon']):
        return 'apology'
    elif any(word in text_lower for word in ['yes', 'sure', 'of course', 'certainly']):
        return 'affirmation'
    elif any(word in text_lower for word in ['no', 'not', "don't", "can't"]):
        return 'negation'
    return 'general'


def find_alternative_match(user_input, scenario, step):
    """Buscar coincidencias con respuestas alternativas guardadas"""
    alternatives = AlternativeResponse.query.filter_by(
        scenario=scenario, 
        step=step
    ).filter(
        AlternativeResponse.times_used >= 2  # Solo usar alternativas usadas más de una vez
    ).all()
    
    for alt in alternatives:
        similarity = Levenshtein.ratio(user_input.lower(), alt.alternative_text.lower())
        if similarity > 0.85:
            return alt
    return None


def find_cross_scenario_match(user_input):
    """Buscar si la respuesta coincide con patrones de otros escenarios"""
    # Buscar patrones similares en la base de datos
    patterns = ResponsePattern.query.all()
    
    for pattern in patterns:
        similarity = Levenshtein.ratio(user_input.lower(), pattern.pattern_text.lower())
        if similarity > 0.8:
            return {
                'pattern': pattern,
                'similarity': similarity,
                'applicable_scenarios': pattern.applicable_scenarios or []
            }
    return None


def save_alternative_response(user_input, scenario, step, expected, similarity, user_id=None):
    """Guardar una respuesta alternativa válida del usuario"""
    # Verificar si ya existe esta alternativa
    existing = AlternativeResponse.query.filter_by(
        scenario=scenario,
        step=step,
        alternative_text=user_input
    ).first()
    
    if existing:
        # Incrementar el contador de uso
        existing.times_used += 1
        db.session.commit()
        return existing
    
    # Crear nueva alternativa si la similitud es razonable (entre 0.4 y 0.85)
    if 0.4 <= similarity <= 0.85:
        new_alt = AlternativeResponse(
            scenario=scenario,
            step=step,
            original_expected=expected,
            alternative_text=user_input,
            similarity_score=similarity,
            created_by_user_id=user_id
        )
        db.session.add(new_alt)
        db.session.commit()
        return new_alt
    return None


def save_or_update_pattern(text, pattern_type, scenario):
    """Guardar o actualizar un patrón de respuesta"""
    # Buscar patrón similar existente
    existing_patterns = ResponsePattern.query.filter_by(pattern_type=pattern_type).all()
    
    for pattern in existing_patterns:
        similarity = Levenshtein.ratio(text.lower(), pattern.pattern_text.lower())
        if similarity > 0.85:
            # Actualizar patrón existente
            pattern.usage_count += 1
            if pattern.applicable_scenarios:
                if scenario not in pattern.applicable_scenarios:
                    pattern.applicable_scenarios = pattern.applicable_scenarios + [scenario]
            else:
                pattern.applicable_scenarios = [scenario]
            db.session.commit()
            return pattern
    
    # Crear nuevo patrón
    new_pattern = ResponsePattern(
        pattern_text=text,
        pattern_type=pattern_type,
        applicable_scenarios=[scenario]
    )
    db.session.add(new_pattern)
    db.session.commit()
    return new_pattern


def get_learned_options(scenario, step):
    """Obtener opciones aprendidas de la base de datos"""
    alternatives = AlternativeResponse.query.filter_by(
        scenario=scenario,
        step=step
    ).filter(
        AlternativeResponse.times_used >= 3  # Solo mostrar alternativas populares
    ).order_by(
        AlternativeResponse.times_used.desc()
    ).limit(2).all()
    
    return [alt.alternative_text for alt in alternatives]


@conversation_bp.route('/')
def list():
    return render_template(
        'conversation_list.html',
        conversations=conversations
    )


@conversation_bp.route('/<scenario>', methods=['GET', 'POST'])
def detail(scenario):
    conversation = conversations.get(scenario)
    if not conversation:
        abort(404)

    # Inicializar sesión para este escenario
    session_key = f'conversation_{scenario}'
    if session_key not in session or request.args.get('restart'):
        session[session_key] = {
            'step': 0,
            'history': [],
            'scores': [],
            'completed': False
        }

    conv_state = session[session_key]
    dialogue = conversation['dialogue']
    current_step = conv_state['step']
    
    # Variables para la plantilla
    system_message = None
    user_prompt = None
    is_completed = conv_state['completed']
    final_score = None
    
    if request.method == 'POST' and not is_completed:
        user_sentence = request.form.get('user_sentence', '').strip()
        
        # Encontrar la respuesta esperada del usuario
        expected = None
        step_index = None
        for i, line in enumerate(dialogue):
            if i == current_step and line['speaker'] == 'user':
                expected = line['expected']
                step_index = i
                break
        
        if expected:
            # Calcular similitud con la respuesta esperada
            similarity = Levenshtein.ratio(user_sentence.lower(), expected.lower())
            
            # Buscar coincidencia con respuestas alternativas aprendidas
            alternative_match = find_alternative_match(user_sentence, scenario, current_step)
            
            # Buscar coincidencia con patrones de otros escenarios
            cross_match = find_cross_scenario_match(user_sentence)
            
            # Determinar el puntaje y feedback
            if alternative_match:
                # La respuesta coincide con una alternativa aprendida
                score = 90
                feedback = get_feedback(similarity, expected, alternative_match=alternative_match)
                # Incrementar uso de la alternativa
                alternative_match.times_used += 1
                db.session.commit()
            else:
                score = calculate_score(similarity)
                feedback = get_feedback(similarity, expected)
            
            # Si la respuesta es razonable pero diferente, guardarla como alternativa
            user_id = current_user.id if current_user.is_authenticated else None
            if 0.4 <= similarity <= 0.85 and len(user_sentence) > 5:
                save_alternative_response(user_sentence, scenario, current_step, expected, similarity, user_id)
                
                # Detectar y guardar el patrón
                pattern_type = detect_pattern_type(user_sentence)
                save_or_update_pattern(user_sentence, pattern_type, scenario)
            
            # Agregar info de cross-match al feedback si aplica
            if cross_match and not alternative_match:
                feedback['cross_scenario'] = {
                    'message': f'Tu respuesta también funcionaría en: {", ".join(cross_match["applicable_scenarios"][:3])}',
                    'pattern_type': cross_match['pattern']['pattern_type']
                }
            
            # Obtener el mensaje del sistema que precedía este turno del usuario
            system_msg_for_history = None
            for k in range(current_step - 1, -1, -1):
                if dialogue[k]['speaker'] == 'system':
                    system_msg_for_history = dialogue[k]['text']
                    break
            
            # Guardar en historial
            conv_state['history'].append({
                'step': current_step,
                'system_msg': system_msg_for_history,
                'user_input': user_sentence,
                'expected': expected,
                'similarity': round(similarity * 100, 1),
                'score': score,
                'feedback': feedback,
                'learned_match': alternative_match is not None,
                'cross_match': cross_match is not None
            })
            conv_state['scores'].append(score)
            
            # Avanzar al siguiente paso
            conv_state['step'] = current_step + 1
            current_step = conv_state['step']
        
        # Verificar si la conversación ha terminado
        if current_step >= len(dialogue):
            conv_state['completed'] = True
            is_completed = True
    
    # Obtener el mensaje actual del sistema
    if not is_completed:
        for i, line in enumerate(dialogue):
            if i >= current_step:
                if line['speaker'] == 'system':
                    system_message = line['text']
                    # Buscar el siguiente turno del usuario
                    for j in range(i + 1, len(dialogue)):
                        if dialogue[j]['speaker'] == 'user':
                            user_prompt = dialogue[j].get('expected', '')
                            conv_state['step'] = j
                            break
                    break
                elif line['speaker'] == 'user' and i == current_step:
                    # Buscar el mensaje del sistema anterior
                    for k in range(i - 1, -1, -1):
                        if dialogue[k]['speaker'] == 'system':
                            system_message = dialogue[k]['text']
                            break
                    user_prompt = line.get('expected', '')
                    break
    
    # Calcular puntaje final y guardar si está completado
    if is_completed and conv_state['scores']:
        final_score = round(sum(conv_state['scores']) / len(conv_state['scores']), 1)
        
        # Guardar en la base de datos si el usuario está autenticado y no se ha guardado aún
        if current_user.is_authenticated and not conv_state.get('saved'):
            practice = ConversationPractice(
                user_id=current_user.id,
                scenario=scenario,
                final_score=final_score,
                total_responses=len(conv_state['history']),
                practice_data=conv_state['history']
            )
            db.session.add(practice)
            db.session.commit()
            conv_state['saved'] = True
    
    # Obtener opciones de respuesta para el paso actual
    response_options = []
    learned_options = []
    if not is_completed:
        for i, line in enumerate(dialogue):
            if i == current_step and line['speaker'] == 'user':
                response_options = line.get('options', [])
                # Obtener opciones aprendidas de la base de datos
                learned_options = get_learned_options(scenario, current_step)
                break
    
    session[session_key] = conv_state
    
    return render_template(
        'conversation_detail.html',
        conversation=conversation,
        scenario=scenario,
        system_message=system_message,
        history=conv_state['history'],
        is_completed=is_completed,
        final_score=final_score,
        current_step=current_step,
        total_steps=len([d for d in dialogue if d['speaker'] == 'user']),
        response_options=response_options,
        learned_options=learned_options
    )
