"""
Seed para Conversation/ConversationLine - Diálogos interactivos
=================================================================
Migra las 10 conversaciones interactivas (antes hardcodeadas en
routes/conversation.py) a los modelos Conversation y ConversationLine.
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Conversation, ConversationLine

app = create_app()

CONVERSATIONS = [
    {
        'scenario': 'store',
        'title': 'At the Store',
        'description': 'Aprende a comprar productos y preguntar precios en una tienda',
        'metadata': {'user_role': 'Customer', 'system_role': 'Clerk', 'icon': '🛒', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning! Welcome to our store. How can I help you today?'},
            {'speaker': 'user', 'text': None, 'expected': 'Hello, I would like to buy some bread, please.',
             'options': ['Hello, I would like to buy some bread, please.', 'Hi, do you have fresh bread?', 'Good morning, I need some bread.']},
            {'speaker': 'system', 'text': 'Of course! We have fresh bread. Would you like white or whole wheat?'},
            {'speaker': 'user', 'text': None, 'expected': 'I would like whole wheat bread, please.',
             'options': ['I would like whole wheat bread, please.', 'White bread, please.', 'Can I have whole wheat?']},
            {'speaker': 'system', 'text': 'Great choice! Anything else?'},
            {'speaker': 'user', 'text': None, 'expected': 'No, that is all. How much is it?',
             'options': ['No, that is all. How much is it?', 'That would be everything. What is the total?', 'Nothing else, thank you. How much do I owe you?']},
            {'speaker': 'system', 'text': 'That will be 3 dollars, please.'},
            {'speaker': 'user', 'text': None, 'expected': 'Here you go. Thank you very much!',
             'options': ['Here you go. Thank you very much!', 'Here is the money. Thanks!', 'Thank you. Have a nice day!']},
            {'speaker': 'system', 'text': 'Thank you! Have a nice day!'},
        ]
    },
    {
        'scenario': 'directions',
        'title': 'Asking for Directions',
        'description': 'Practica cómo pedir direcciones y entender indicaciones',
        'metadata': {'user_role': 'Tourist', 'system_role': 'Local', 'icon': '🗺️', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! You look a bit lost. Do you need help?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, please. I am looking for the bus station.',
             'options': ['Yes, please. I am looking for the bus station.', 'Hi, where is the bus station?', 'Excuse me, can you help me find the bus station?']},
            {'speaker': 'system', 'text': 'The bus station is two blocks ahead, then turn right.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you. Is it far from here?',
             'options': ['Thank you. Is it far from here?', 'Thanks! How long will it take to get there?', 'I see. Is it a long walk?']},
            {'speaker': 'system', 'text': 'Not at all, about a 5-minute walk.'},
            {'speaker': 'user', 'text': None, 'expected': 'Great, thank you for your help!',
             'options': ['Great, thank you for your help!', 'Perfect, thanks a lot!', 'Wonderful, I appreciate it!']},
            {'speaker': 'system', 'text': 'You are welcome! Good luck!'},
        ]
    },
    {
        'scenario': 'greetings',
        'title': 'Greetings and Introductions',
        'description': 'Conoce a alguien nuevo y preséntate en inglés',
        'metadata': {'user_role': 'You', 'system_role': 'New Friend', 'icon': '👋', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hi there! I am Sarah. Nice to meet you!'},
            {'speaker': 'user', 'text': None, 'expected': 'Nice to meet you too! My name is...',
             'options': ['Nice to meet you too! My name is...', 'Hello Sarah! I am pleased to meet you.', 'Hi! Nice to meet you as well.']},
            {'speaker': 'system', 'text': 'Where are you from?'},
            {'speaker': 'user', 'text': None, 'expected': 'I am from Mexico. And you?',
             'options': ['I am from Mexico. And you?', 'I come from Mexico. What about you?', 'Mexico! Where are you from?']},
            {'speaker': 'system', 'text': 'I am from Canada. What do you do for a living?'},
            {'speaker': 'user', 'text': None, 'expected': 'I am a student. I study computer science.',
             'options': ['I am a student. I study computer science.', 'I work as a programmer.', 'I am studying at the university.']},
            {'speaker': 'system', 'text': 'That sounds interesting! It was nice talking to you!'},
            {'speaker': 'user', 'text': None, 'expected': 'It was nice talking to you too. See you later!',
             'options': ['It was nice talking to you too. See you later!', 'Same here! Goodbye!', 'Nice chatting with you. Take care!']},
        ]
    },
    {
        'scenario': 'restaurant',
        'title': 'At the Restaurant',
        'description': 'Ordena comida, bebidas y pide la cuenta en un restaurante',
        'metadata': {'user_role': 'Customer', 'system_role': 'Waiter', 'icon': '🍽️', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Good evening! Welcome to our restaurant. Do you have a reservation?'},
            {'speaker': 'user', 'text': None, 'expected': 'No, I do not have a reservation. Do you have a table for two?',
             'options': ['No, I do not have a reservation. Do you have a table for two?', 'No reservation. Is there any table available?', 'We did not make a reservation. Can we still get a table?']},
            {'speaker': 'system', 'text': 'Yes, please follow me. Here is the menu. Can I get you something to drink?'},
            {'speaker': 'user', 'text': None, 'expected': 'I would like a glass of water, please.',
             'options': ['I would like a glass of water, please.', 'Can I have some water?', 'Just water for now, thank you.']},
            {'speaker': 'system', 'text': 'Of course! Are you ready to order, or do you need more time?'},
            {'speaker': 'user', 'text': None, 'expected': 'I am ready. I would like the grilled chicken with salad.',
             'options': ['I am ready. I would like the grilled chicken with salad.', 'Yes, I will have the chicken please.', 'Can I get the grilled chicken and a side salad?']},
            {'speaker': 'system', 'text': 'Excellent choice! Would you like any dessert after your meal?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, I will have the chocolate cake, please.',
             'options': ['Yes, I will have the chocolate cake, please.', 'What desserts do you have?', 'No dessert for me, thank you.']},
            {'speaker': 'system', 'text': 'Perfect! Your order will be ready soon.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you very much!',
             'options': ['Thank you very much!', 'Great, thanks!', 'I appreciate it!']},
        ]
    },
    {
        'scenario': 'hotel',
        'title': 'Hotel Check-in',
        'description': 'Registrarte en un hotel y hacer preguntas sobre tu estadía',
        'metadata': {'user_role': 'Guest', 'system_role': 'Receptionist', 'icon': '🏨', 'difficulty': 'Intermediate'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Good afternoon! Welcome to the Grand Hotel. How may I help you?'},
            {'speaker': 'user', 'text': None, 'expected': 'Hello, I have a reservation under the name Johnson.',
             'options': ['Hello, I have a reservation under the name Johnson.', 'Hi, I booked a room online. My name is Johnson.', 'Good afternoon. I would like to check in please.']},
            {'speaker': 'system', 'text': 'Let me check... Yes, I found it. A double room for three nights, correct?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, that is correct.',
             'options': ['Yes, that is correct.', 'That is right.', 'Exactly, three nights.']},
            {'speaker': 'system', 'text': 'I will need your ID and a credit card for the deposit, please.'},
            {'speaker': 'user', 'text': None, 'expected': 'Here you go. Here is my passport and credit card.',
             'options': ['Here you go. Here is my passport and credit card.', 'Sure, here they are.', 'Of course, here is my ID and card.']},
            {'speaker': 'system', 'text': 'Thank you. Your room is on the fifth floor, room 512. Would you like help with your luggage?'},
            {'speaker': 'user', 'text': None, 'expected': 'No, thank you. I can manage. What time is breakfast?',
             'options': ['No, thank you. I can manage. What time is breakfast?', 'Yes, please. And when is breakfast served?', 'I am fine, thanks. Where is the restaurant?']},
            {'speaker': 'system', 'text': 'Breakfast is served from 7 to 10 AM in the restaurant on the ground floor. Enjoy your stay!'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you. Have a nice day!',
             'options': ['Thank you. Have a nice day!', 'Great, thanks for your help!', 'Perfect, thank you very much!']},
        ]
    },
    {
        'scenario': 'airport',
        'title': 'At the Airport',
        'description': 'Facturar equipaje, pasar seguridad y encontrar tu puerta de embarque',
        'metadata': {'user_role': 'Traveler', 'system_role': 'Agent', 'icon': '✈️', 'difficulty': 'Intermediate'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! May I see your passport and boarding pass, please?'},
            {'speaker': 'user', 'text': None, 'expected': 'Of course, here they are.',
             'options': ['Of course, here they are.', 'Sure, here you go.', 'Yes, here is my passport and boarding pass.']},
            {'speaker': 'system', 'text': 'Are you checking any bags today?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, I have one suitcase to check.',
             'options': ['Yes, I have one suitcase to check.', 'Just this one bag.', 'I have one checked bag and one carry-on.']},
            {'speaker': 'system', 'text': 'Please place your bag on the scale. Would you like a window or aisle seat?'},
            {'speaker': 'user', 'text': None, 'expected': 'A window seat, please.',
             'options': ['A window seat, please.', 'I prefer the aisle, please.', 'Do you have any window seats available?']},
            {'speaker': 'system', 'text': 'Here is your boarding pass. Your flight departs from gate B12. Boarding starts at 3:30 PM.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you. Where is gate B12?',
             'options': ['Thank you. Where is gate B12?', 'How do I get to gate B12?', 'Could you tell me how to find gate B12?']},
            {'speaker': 'system', 'text': 'Go through security, then turn left. It is about a 10-minute walk. Have a safe flight!'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you so much. Have a nice day!',
             'options': ['Thank you so much. Have a nice day!', 'Thanks for your help!', 'I appreciate it. Goodbye!']},
        ]
    },
    {
        'scenario': 'doctor',
        'title': "At the Doctor's Office",
        'description': 'Describe tus síntomas y entiende las instrucciones del médico',
        'metadata': {'user_role': 'Patient', 'system_role': 'Doctor', 'icon': '🏥', 'difficulty': 'Intermediate'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! What brings you in today? How are you feeling?'},
            {'speaker': 'user', 'text': None, 'expected': 'Hello, doctor. I have had a headache and fever for three days.',
             'options': ['Hello, doctor. I have had a headache and fever for three days.', 'I am not feeling well. I have a bad headache.', 'I have been sick since Monday with fever and pain.']},
            {'speaker': 'system', 'text': 'I see. Have you taken any medication?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, I have been taking some aspirin, but it does not help much.',
             'options': ['Yes, I have been taking some aspirin, but it does not help much.', 'I tried some pain relievers but they did not work.', 'Only some over-the-counter medicine.']},
            {'speaker': 'system', 'text': 'Do you have any other symptoms like cough, sore throat, or body aches?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, I also have a sore throat and I feel very tired.',
             'options': ['Yes, I also have a sore throat and I feel very tired.', 'My throat hurts and I have no energy.', 'I have been coughing a little and feeling weak.']},
            {'speaker': 'system', 'text': 'It sounds like you might have the flu. I am going to prescribe some medication. Make sure to rest and drink plenty of fluids.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you, doctor. How long until I feel better?',
             'options': ['Thank you, doctor. How long until I feel better?', 'When should I expect to recover?', 'How many days should I rest?']},
            {'speaker': 'system', 'text': 'You should feel better in about a week. If symptoms persist, please come back.'},
            {'speaker': 'user', 'text': None, 'expected': 'I will. Thank you for your help, doctor.',
             'options': ['I will. Thank you for your help, doctor.', 'Okay, I appreciate your help.', 'Thanks so much. I will follow your advice.']},
        ]
    },
    {
        'scenario': 'job_interview',
        'title': 'Job Interview',
        'description': 'Responde preguntas profesionales y destaca tus habilidades',
        'metadata': {'user_role': 'Candidate', 'system_role': 'Interviewer', 'icon': '💼', 'difficulty': 'Advanced'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning! Please have a seat. Thank you for coming. Can you tell me a little about yourself?'},
            {'speaker': 'user', 'text': None, 'expected': 'Good morning! Thank you for having me. I am a software developer with five years of experience.',
             'options': ['Good morning! Thank you for having me. I am a software developer with five years of experience.', 'Hello! I am excited to be here. I have been working in tech for several years.', 'Thanks for the opportunity. I am a passionate programmer with strong skills in web development.']},
            {'speaker': 'system', 'text': 'That sounds great. Why are you interested in this position?'},
            {'speaker': 'user', 'text': None, 'expected': "I am looking for new challenges and I admire your company's innovative projects.",
             'options': ["I am looking for new challenges and I admire your company's innovative projects.", "I want to grow professionally and your company has a great reputation.", "This role aligns perfectly with my career goals and skills."]},
            {'speaker': 'system', 'text': 'What would you say is your greatest strength?'},
            {'speaker': 'user', 'text': None, 'expected': 'I am very organized and I work well under pressure.',
             'options': ['I am very organized and I work well under pressure.', 'I am a quick learner and adapt easily to new technologies.', 'My problem-solving skills are my biggest asset.']},
            {'speaker': 'system', 'text': 'And what about your weaknesses?'},
            {'speaker': 'user', 'text': None, 'expected': 'Sometimes I focus too much on details, but I am working on finding a better balance.',
             'options': ['Sometimes I focus too much on details, but I am working on finding a better balance.', 'I can be a perfectionist, which sometimes slows me down.', 'I am still improving my public speaking skills.']},
            {'speaker': 'system', 'text': 'Where do you see yourself in five years?'},
            {'speaker': 'user', 'text': None, 'expected': 'I hope to be in a leadership role, contributing to major projects.',
             'options': ['I hope to be in a leadership role, contributing to major projects.', 'I see myself growing within the company and taking on more responsibility.', 'I want to become an expert in my field and mentor others.']},
            {'speaker': 'system', 'text': 'Do you have any questions for me?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, what does a typical day look like in this role?',
             'options': ['Yes, what does a typical day look like in this role?', 'What are the opportunities for professional development?', 'Can you tell me more about the team I would be working with?']},
        ]
    },
    {
        'scenario': 'phone_call',
        'title': 'Making a Phone Call',
        'description': 'Haz llamadas telefónicas profesionales y deja mensajes',
        'metadata': {'user_role': 'Caller', 'system_role': 'Receptionist', 'icon': '📞', 'difficulty': 'Intermediate'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Good morning, ABC Company. How may I direct your call?'},
            {'speaker': 'user', 'text': None, 'expected': 'Hello, I would like to speak with Mr. Smith from the sales department, please.',
             'options': ['Hello, I would like to speak with Mr. Smith from the sales department, please.', 'Hi, can you connect me to the sales team?', 'Good morning, I am trying to reach someone in sales.']},
            {'speaker': 'system', 'text': 'May I ask who is calling and what this is regarding?'},
            {'speaker': 'user', 'text': None, 'expected': 'My name is John Davis. I am calling about a product inquiry.',
             'options': ['My name is John Davis. I am calling about a product inquiry.', 'This is John Davis. I have some questions about your services.', 'I am John from XYZ Corp, calling regarding a business matter.']},
            {'speaker': 'system', 'text': 'Thank you, Mr. Davis. Please hold while I transfer your call.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you, I will wait.',
             'options': ['Thank you, I will wait.', 'Sure, no problem.', 'Okay, thanks.']},
            {'speaker': 'system', 'text': 'I am sorry, Mr. Smith is in a meeting right now. Would you like to leave a message or call back later?'},
            {'speaker': 'user', 'text': None, 'expected': 'Could you please ask him to call me back? My number is 555-1234.',
             'options': ['Could you please ask him to call me back? My number is 555-1234.', 'I will call back in an hour. Thank you.', 'Can I leave a message for him to return my call?']},
            {'speaker': 'system', 'text': 'Of course! I will make sure he gets the message. Is there anything else I can help you with?'},
            {'speaker': 'user', 'text': None, 'expected': 'No, that is all. Thank you for your help. Goodbye!',
             'options': ['No, that is all. Thank you for your help. Goodbye!', 'That is everything. Have a nice day!', 'Nothing else, thanks. Bye!']},
        ]
    },
    {
        'scenario': 'shopping_clothes',
        'title': 'Shopping for Clothes',
        'description': 'Compra ropa, pregunta por tallas y usa el probador',
        'metadata': {'user_role': 'Shopper', 'system_role': 'Sales Assistant', 'icon': '👕', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! Welcome to our store. Are you looking for something specific?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, I am looking for a jacket for the winter.',
             'options': ['Yes, I am looking for a jacket for the winter.', 'Hi, do you have any warm jackets?', 'I need a winter coat, please.']},
            {'speaker': 'system', 'text': 'We have a great selection over here. What size do you wear?'},
            {'speaker': 'user', 'text': None, 'expected': 'I usually wear a medium.',
             'options': ['I usually wear a medium.', 'I am a size M.', 'Medium should fit me.']},
            {'speaker': 'system', 'text': 'Here are some options in medium. Would you like to try them on?'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, please. Where are the fitting rooms?',
             'options': ['Yes, please. Where are the fitting rooms?', 'Sure, can I try this one on?', 'I would like to try the blue one.']},
            {'speaker': 'system', 'text': 'The fitting rooms are at the back of the store, on the right.'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you. I will try this one.',
             'options': ['Thank you. I will try this one.', 'Great, I will be right back.', 'Thanks, I will go try it on.']},
            {'speaker': 'system', 'text': 'How does it fit?'},
            {'speaker': 'user', 'text': None, 'expected': 'It fits perfectly! I will take it. How much is it?',
             'options': ['It fits perfectly! I will take it. How much is it?', 'It is a bit tight. Do you have a larger size?', 'I love it! What is the price?']},
            {'speaker': 'system', 'text': 'It is 75 dollars. Would you like to pay by cash or card?'},
            {'speaker': 'user', 'text': None, 'expected': 'I will pay by card, please.',
             'options': ['I will pay by card, please.', 'Cash, please.', 'Do you accept credit cards?']},
        ]
    },
    {
        'scenario': 'taxi',
        'title': 'Taking a Taxi',
        'description': 'Indica tu destino, pregunta el precio y paga el viaje',
        'metadata': {'user_role': 'Passenger', 'system_role': 'Taxi Driver', 'icon': '🚕', 'difficulty': 'Beginner'},
        'dialogue': [
            {'speaker': 'system', 'text': 'Hello! Where would you like to go?'},
            {'speaker': 'user', 'text': None, 'expected': 'Hi, can you take me to the airport, please?',
             'options': ['Hi, can you take me to the airport, please?', 'I need to go to the international airport.', 'To the airport, please.']},
            {'speaker': 'system', 'text': 'Sure! Do you have a flight to catch? I will take the fastest route.'},
            {'speaker': 'user', 'text': None, 'expected': 'Yes, my flight is in two hours. How long will it take?',
             'options': ['Yes, my flight is in two hours. How long will it take?', 'I have plenty of time. No rush.', 'Yes, I need to be there soon. What is the estimated time?']},
            {'speaker': 'system', 'text': 'It should take about 30 minutes, depending on traffic.'},
            {'speaker': 'user', 'text': None, 'expected': 'That sounds good. Thank you.',
             'options': ['That sounds good. Thank you.', 'Perfect, that works for me.', 'Great, let us go.']},
            {'speaker': 'system', 'text': 'Here we are! That will be 25 dollars.'},
            {'speaker': 'user', 'text': None, 'expected': 'Here you go. Keep the change.',
             'options': ['Here you go. Keep the change.', 'Do you accept credit cards?', 'Here is 30 dollars. You can keep the rest.']},
            {'speaker': 'system', 'text': 'Thank you! Have a safe flight!'},
            {'speaker': 'user', 'text': None, 'expected': 'Thank you! Have a nice day!',
             'options': ['Thank you! Have a nice day!', 'Thanks! Goodbye!', 'I appreciate it. Take care!']},
        ]
    },
]


def seed():
    """Insertar las conversaciones interactivas en la DB"""
    print("\n🗣️ Poblando Conversation + ConversationLine...")
    created = 0
    lines_created = 0
    skipped = 0

    for conv in CONVERSATIONS:
        existing = Conversation.query.filter_by(scenario=conv['scenario']).first()
        if existing:
            skipped += 1
            continue

        conversation = Conversation(
            scenario=conv['scenario'],
            title=conv['title'],
            description=conv['description'],
            extra_data=conv['metadata']
        )
        db.session.add(conversation)
        db.session.flush()
        created += 1

        for i, line_data in enumerate(conv['dialogue']):
            line = ConversationLine(
                conversation_id=conversation.id,
                speaker=line_data['speaker'],
                text=line_data.get('text') or '',
                expected=line_data.get('expected'),
                options=line_data.get('options'),
                order=i + 1
            )
            db.session.add(line)
            lines_created += 1

    db.session.commit()
    total = Conversation.query.count()
    total_lines = ConversationLine.query.count()
    print(f"   ✅ Creadas: {created} | Saltadas: {skipped} | Total en DB: {total}")
    print(f"   ✅ Líneas creadas: {lines_created} | Total en DB: {total_lines}")
    return created, lines_created


def main():
    with app.app_context():
        print("=" * 80)
        print("🌱 SEED: Conversation + ConversationLine - Diálogos interactivos")
        print("=" * 80)
        count, lines = seed()
        print(f"\n📊 Total conversaciones en DB: {count}")
        print(f"📊 Total líneas en DB: {lines}")
        print("✅ Seed completado")


if __name__ == '__main__':
    main()
