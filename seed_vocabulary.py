#!/usr/bin/env python3
"""
Script para poblar VocabularyItem basado en las categorías existentes
y generar flashcards desde el vocabulario
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Unit, VocabularyCategory, VocabularyItem, Flashcard

app = create_app()

# Vocabulario por categoría común
VOCABULARY_TEMPLATES = {
    # Greetings and Basic Expressions
    "Greetings": [
        {"word": "Hello", "definition": "A common greeting", "example": "Hello! How are you?"},
        {"word": "Goodbye", "definition": "Used when leaving", "example": "Goodbye! See you tomorrow."},
        {"word": "Please", "definition": "Used to ask politely", "example": "Can I have water, please?"},
        {"word": "Thank you", "definition": "Expression of gratitude", "example": "Thank you for your help."},
        {"word": "Sorry", "definition": "Expression of apology", "example": "Sorry, I'm late."},
    ],
    
    # Countries and Nationalities
    "Countries": [
        {"word": "country", "definition": "A nation with its own government", "example": "Mexico is a beautiful country."},
        {"word": "city", "definition": "A large town", "example": "New York is a big city."},
        {"word": "language", "definition": "System of communication", "example": "I speak two languages."},
        {"word": "population", "definition": "Number of people in a place", "example": "The population is growing."},
        {"word": "capital", "definition": "Main city of a country", "example": "Paris is the capital of France."},
    ],
    
    "Nationalities": [
        {"word": "American", "definition": "From the United States", "example": "She is American."},
        {"word": "British", "definition": "From Great Britain", "example": "He has a British accent."},
        {"word": "Mexican", "definition": "From Mexico", "example": "Mexican food is delicious."},
        {"word": "Chinese", "definition": "From China", "example": "I'm learning Chinese."},
        {"word": "Spanish", "definition": "From Spain / the language", "example": "Spanish is spoken worldwide."},
    ],
    
    # Family
    "Family members": [
        {"word": "mother", "definition": "Female parent", "example": "My mother is a teacher."},
        {"word": "father", "definition": "Male parent", "example": "My father works in an office."},
        {"word": "sister", "definition": "Female sibling", "example": "I have two sisters."},
        {"word": "brother", "definition": "Male sibling", "example": "My brother is older than me."},
        {"word": "grandmother", "definition": "Mother's or father's mother", "example": "My grandmother bakes cookies."},
    ],
    
    # Numbers
    "Numbers 1-20": [
        {"word": "one", "definition": "The number 1", "example": "I have one cat."},
        {"word": "five", "definition": "The number 5", "example": "There are five apples."},
        {"word": "ten", "definition": "The number 10", "example": "She is ten years old."},
        {"word": "fifteen", "definition": "The number 15", "example": "The class starts in fifteen minutes."},
        {"word": "twenty", "definition": "The number 20", "example": "I have twenty dollars."},
    ],
    
    "Numbers 20-100": [
        {"word": "thirty", "definition": "The number 30", "example": "He is thirty years old."},
        {"word": "fifty", "definition": "The number 50", "example": "The bus comes in fifty minutes."},
        {"word": "seventy", "definition": "The number 70", "example": "My grandfather is seventy."},
        {"word": "hundred", "definition": "The number 100", "example": "I have a hundred books."},
        {"word": "ninety", "definition": "The number 90", "example": "She scored ninety percent."},
    ],
    
    # Home and Rooms
    "Rooms": [
        {"word": "bedroom", "definition": "Room for sleeping", "example": "My bedroom is upstairs."},
        {"word": "kitchen", "definition": "Room for cooking", "example": "I cook in the kitchen."},
        {"word": "bathroom", "definition": "Room with toilet and shower", "example": "The bathroom is clean."},
        {"word": "living room", "definition": "Room for relaxing", "example": "We watch TV in the living room."},
        {"word": "dining room", "definition": "Room for eating meals", "example": "We eat dinner in the dining room."},
    ],
    
    "Furniture": [
        {"word": "bed", "definition": "Furniture for sleeping", "example": "I sleep on a comfortable bed."},
        {"word": "table", "definition": "Furniture with a flat top", "example": "Put the book on the table."},
        {"word": "chair", "definition": "Furniture for sitting", "example": "Please sit on the chair."},
        {"word": "sofa", "definition": "Long comfortable seat", "example": "The sofa is very soft."},
        {"word": "desk", "definition": "Table for working or studying", "example": "I study at my desk."},
    ],
    
    "Household items": [
        {"word": "lamp", "definition": "Device for light", "example": "Turn on the lamp, please."},
        {"word": "clock", "definition": "Device showing time", "example": "The clock says 3 PM."},
        {"word": "television", "definition": "Device for watching programs", "example": "We have a new television."},
        {"word": "refrigerator", "definition": "Appliance for keeping food cold", "example": "The milk is in the refrigerator."},
        {"word": "mirror", "definition": "Glass that reflects images", "example": "I look in the mirror every morning."},
    ],
    
    # Daily Activities
    "Daily activities": [
        {"word": "wake up", "definition": "Stop sleeping", "example": "I wake up at 7 AM."},
        {"word": "go to bed", "definition": "Lie down to sleep", "example": "I go to bed at 10 PM."},
        {"word": "eat breakfast", "definition": "Have morning meal", "example": "I eat breakfast every day."},
        {"word": "take a shower", "definition": "Wash body with water", "example": "I take a shower in the morning."},
        {"word": "brush teeth", "definition": "Clean teeth with brush", "example": "I brush my teeth twice a day."},
    ],
    
    "Times of day": [
        {"word": "morning", "definition": "Early part of day", "example": "I study in the morning."},
        {"word": "afternoon", "definition": "Part of day after noon", "example": "We have class in the afternoon."},
        {"word": "evening", "definition": "Late part of day before night", "example": "I watch TV in the evening."},
        {"word": "night", "definition": "Dark part of day", "example": "I sleep at night."},
        {"word": "midnight", "definition": "12 o'clock at night", "example": "The movie ends at midnight."},
    ],
    
    "Days and months": [
        {"word": "Monday", "definition": "First day of work week", "example": "I start work on Monday."},
        {"word": "Friday", "definition": "Last day of work week", "example": "Friday is my favorite day."},
        {"word": "January", "definition": "First month of year", "example": "January is cold."},
        {"word": "July", "definition": "Seventh month of year", "example": "July is very hot."},
        {"word": "December", "definition": "Last month of year", "example": "December has Christmas."},
    ],
    
    # Food and Drinks
    "Food items": [
        {"word": "bread", "definition": "Baked food from flour", "example": "I eat bread for breakfast."},
        {"word": "rice", "definition": "White grain food", "example": "We have rice with dinner."},
        {"word": "chicken", "definition": "Poultry meat", "example": "I like grilled chicken."},
        {"word": "vegetables", "definition": "Plants eaten as food", "example": "Eat your vegetables!"},
        {"word": "fruit", "definition": "Sweet plant food", "example": "Apples are my favorite fruit."},
    ],
    
    "Drinks": [
        {"word": "water", "definition": "Clear liquid for drinking", "example": "Drink more water."},
        {"word": "coffee", "definition": "Hot brown drink", "example": "I drink coffee every morning."},
        {"word": "tea", "definition": "Hot drink from leaves", "example": "Would you like some tea?"},
        {"word": "juice", "definition": "Drink from fruits", "example": "Orange juice is healthy."},
        {"word": "milk", "definition": "White drink from cows", "example": "I put milk in my cereal."},
    ],
    
    # Shopping and Money
    "Shopping": [
        {"word": "price", "definition": "Cost of something", "example": "What's the price of this?"},
        {"word": "cheap", "definition": "Low cost", "example": "This shirt is cheap."},
        {"word": "expensive", "definition": "High cost", "example": "That car is expensive."},
        {"word": "sale", "definition": "Items at reduced price", "example": "Everything is on sale today."},
        {"word": "discount", "definition": "Reduction in price", "example": "I got a 20% discount."},
    ],
    
    "Money": [
        {"word": "dollar", "definition": "US currency", "example": "This costs ten dollars."},
        {"word": "cash", "definition": "Physical money", "example": "I prefer to pay with cash."},
        {"word": "credit card", "definition": "Plastic payment card", "example": "Do you accept credit cards?"},
        {"word": "bill", "definition": "Paper money / statement of payment due", "example": "I need to pay the bill."},
        {"word": "change", "definition": "Small coins / money returned", "example": "Keep the change."},
    ],
    
    # Work and Jobs
    "Jobs": [
        {"word": "teacher", "definition": "Person who teaches", "example": "My teacher is very nice."},
        {"word": "doctor", "definition": "Medical professional", "example": "I need to see a doctor."},
        {"word": "engineer", "definition": "Person who designs things", "example": "She works as an engineer."},
        {"word": "lawyer", "definition": "Legal professional", "example": "We hired a lawyer."},
        {"word": "nurse", "definition": "Healthcare worker", "example": "The nurse gave me medicine."},
    ],
    
    "Workplace": [
        {"word": "office", "definition": "Place for work", "example": "I work in an office."},
        {"word": "meeting", "definition": "Gathering of people", "example": "We have a meeting at 2 PM."},
        {"word": "deadline", "definition": "Time limit", "example": "The deadline is tomorrow."},
        {"word": "salary", "definition": "Regular payment for work", "example": "He has a good salary."},
        {"word": "colleague", "definition": "Person you work with", "example": "My colleague helped me."},
    ],
    
    # Travel
    "Travel": [
        {"word": "airport", "definition": "Place for planes", "example": "We arrived at the airport."},
        {"word": "passport", "definition": "Travel document", "example": "Don't forget your passport."},
        {"word": "luggage", "definition": "Bags for travel", "example": "Where is your luggage?"},
        {"word": "ticket", "definition": "Document for travel", "example": "I bought a plane ticket."},
        {"word": "reservation", "definition": "Booking", "example": "I made a hotel reservation."},
    ],
    
    "Transportation": [
        {"word": "car", "definition": "Vehicle with four wheels", "example": "I drive my car to work."},
        {"word": "bus", "definition": "Large public vehicle", "example": "The bus comes at 8 AM."},
        {"word": "train", "definition": "Railway vehicle", "example": "We took the train to Paris."},
        {"word": "airplane", "definition": "Flying vehicle", "example": "The airplane was delayed."},
        {"word": "bicycle", "definition": "Two-wheeled vehicle", "example": "I ride my bicycle to school."},
    ],
    
    # Health
    "Health": [
        {"word": "headache", "definition": "Pain in head", "example": "I have a bad headache."},
        {"word": "fever", "definition": "High body temperature", "example": "She has a fever."},
        {"word": "medicine", "definition": "Drug for treatment", "example": "Take your medicine."},
        {"word": "hospital", "definition": "Place for medical care", "example": "He's in the hospital."},
        {"word": "appointment", "definition": "Scheduled meeting", "example": "I have a doctor's appointment."},
    ],
    
    "Body parts": [
        {"word": "head", "definition": "Top part of body", "example": "My head hurts."},
        {"word": "hand", "definition": "End of arm", "example": "Wash your hands."},
        {"word": "foot", "definition": "End of leg", "example": "My foot is sore."},
        {"word": "heart", "definition": "Organ that pumps blood", "example": "Exercise is good for your heart."},
        {"word": "eye", "definition": "Organ for seeing", "example": "She has beautiful eyes."},
    ],
    
    # Weather
    "Weather": [
        {"word": "sunny", "definition": "With sun shining", "example": "It's sunny today."},
        {"word": "cloudy", "definition": "Covered with clouds", "example": "The sky is cloudy."},
        {"word": "rainy", "definition": "With rain falling", "example": "It's rainy outside."},
        {"word": "cold", "definition": "Low temperature", "example": "It's very cold today."},
        {"word": "hot", "definition": "High temperature", "example": "Summer is hot here."},
    ],
    
    # Adjectives
    "Basic adjectives": [
        {"word": "big", "definition": "Large in size", "example": "That's a big house."},
        {"word": "small", "definition": "Little in size", "example": "I have a small car."},
        {"word": "good", "definition": "Of high quality", "example": "This is good food."},
        {"word": "bad", "definition": "Of low quality", "example": "That was a bad movie."},
        {"word": "new", "definition": "Recently made", "example": "I bought a new phone."},
    ],
    
    # Verbs
    "Common verbs": [
        {"word": "be", "definition": "To exist", "example": "I am a student."},
        {"word": "have", "definition": "To possess", "example": "I have a car."},
        {"word": "do", "definition": "To perform action", "example": "What do you do?"},
        {"word": "go", "definition": "To move somewhere", "example": "I go to work."},
        {"word": "come", "definition": "To arrive", "example": "Please come here."},
    ],
    
    "Action verbs": [
        {"word": "run", "definition": "To move fast on feet", "example": "I run every morning."},
        {"word": "walk", "definition": "To move on feet", "example": "I walk to school."},
        {"word": "eat", "definition": "To consume food", "example": "We eat dinner at 7."},
        {"word": "drink", "definition": "To consume liquid", "example": "I drink water daily."},
        {"word": "sleep", "definition": "To rest", "example": "I sleep 8 hours."},
    ],
}

# Default vocabulary for categories without specific templates
DEFAULT_VOCABULARY = [
    {"word": "example", "definition": "Something that illustrates", "example": "Here is an example."},
    {"word": "practice", "definition": "Regular exercise of an activity", "example": "Practice makes perfect."},
    {"word": "study", "definition": "To learn", "example": "I study every day."},
    {"word": "learn", "definition": "To gain knowledge", "example": "I want to learn English."},
    {"word": "understand", "definition": "To comprehend", "example": "I understand now."},
]


def seed_vocabulary():
    """Agregar vocabulario a las categorías existentes"""
    with app.app_context():
        print("="*70)
        print("AGREGANDO VOCABULARIO A LAS CATEGORÍAS")
        print("="*70)
        
        categories = VocabularyCategory.query.all()
        vocab_added = 0
        vocab_skipped = 0
        
        for cat in categories:
            # Verificar si ya tiene vocabulario
            existing = VocabularyItem.query.filter_by(category_id=cat.id).count()
            if existing > 0:
                vocab_skipped += existing
                continue
            
            # Buscar vocabulario para esta categoría
            vocab_list = None
            for key in VOCABULARY_TEMPLATES:
                if key.lower() in cat.category_name.lower() or cat.category_name.lower() in key.lower():
                    vocab_list = VOCABULARY_TEMPLATES[key]
                    break
            
            if not vocab_list:
                # Usar vocabulario por defecto
                vocab_list = DEFAULT_VOCABULARY
            
            # Agregar vocabulario
            for idx, word_data in enumerate(vocab_list):
                item = VocabularyItem(
                    category_id=cat.id,
                    word=word_data['word'],
                    definition=word_data['definition'],
                    example=word_data.get('example', ''),
                    order=idx
                )
                db.session.add(item)
                vocab_added += 1
        
        db.session.commit()
        print(f"✓ Vocabulario agregado: {vocab_added}")
        print(f"- Omitido (ya existía): {vocab_skipped}")
        
        # Ahora crear flashcards desde vocabulario
        print("\n" + "="*70)
        print("CREANDO FLASHCARDS DESDE VOCABULARIO")
        print("="*70)
        
        flashcards_added = 0
        flashcards_skipped = 0
        
        vocab_items = VocabularyItem.query.all()
        
        for item in vocab_items:
            # Obtener unit_id desde la categoría
            category = VocabularyCategory.query.get(item.category_id)
            if not category:
                continue
            
            # Verificar si ya existe flashcard
            existing = Flashcard.query.filter_by(
                unit_id=category.unit_id,
                front=item.word
            ).first()
            
            if existing:
                flashcards_skipped += 1
                continue
            
            flashcard = Flashcard(
                unit_id=category.unit_id,
                front=item.word,
                back=item.definition,
                example=item.example,
                difficulty='beginner',
                order=item.order
            )
            db.session.add(flashcard)
            flashcards_added += 1
        
        db.session.commit()
        print(f"✓ Flashcards creadas: {flashcards_added}")
        print(f"- Omitidas (ya existían): {flashcards_skipped}")
        
        print("\n" + "="*70)
        print("✅ ¡VOCABULARIO Y FLASHCARDS COMPLETADOS!")
        print("="*70)


if __name__ == '__main__':
    seed_vocabulary()
