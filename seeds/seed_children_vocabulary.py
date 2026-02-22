#!/usr/bin/env python3
"""
Seed Script for Children Vocabulary Units
Creates 4 vocabulary units for children: Animals, Colors, Numbers, Food
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import Unit, Topic, VocabularyCategory, VocabularyItem, GrammarRule

def seed_children_units():
    app = create_app()
    
    with app.app_context():
        units_data = [
            {
                "unit_number": 101,
                "title": "Animals - Los Animales",
                "description": "Learn basic animal names in English",
                "detailed_explanation": "This unit introduces children to common animals they can find on a farm and in the wild. Each animal is presented with its name in English, pronunciation, and a simple example sentence.",
                "learning_objectives": ["Learn 10+ animal names", "Practice pronunciation", "Understand simple sentences about animals"],
                "overview": "Farm animals and wild animals vocabulary",
                "age_group": "children",
                "min_age": 4,
                "max_age": 8,
                "cefr_level": "A1",
                "is_children_content": True,
                "topics": [
                    {
                        "title": "Farm Animals",
                        "description": "Animals found on a farm",
                        "key_concepts": ["farm", "animal", "name"],
                        "examples": ["The cow says moo!"],
                        "order": 1,
                        "categories": [
                            {
                                "name": "Farm Animals",
                                "order": 1,
                                "items": [
                                    {"word": "cow", "definition": "Una vaca", "example": "The cow says moo!", "order": 1},
                                    {"word": "pig", "definition": "Un cerdo", "example": "The pig says oink!", "order": 2},
                                    {"word": "chicken", "definition": "Un pollo", "example": "The chicken says cluck!", "order": 3},
                                    {"word": "horse", "definition": "Un caballo", "example": "I can ride a horse!", "order": 4},
                                    {"word": "sheep", "definition": "Una oveja", "example": "The sheep says baa!", "order": 5},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Wild Animals",
                        "description": "Animals found in nature",
                        "key_concepts": ["wild", "forest", "jungle"],
                        "examples": ["The lion is the king of the jungle!"],
                        "order": 2,
                        "categories": [
                            {
                                "name": "Wild Animals",
                                "order": 1,
                                "items": [
                                    {"word": "lion", "definition": "Un león", "example": "The lion is the king!", "order": 1},
                                    {"word": "elephant", "definition": "Un elefante", "example": "The elephant is big!", "order": 2},
                                    {"word": "monkey", "definition": "Un mono", "example": "The monkey eats bananas!", "order": 3},
                                    {"word": "bear", "definition": "Un oso", "example": "The bear loves honey!", "order": 4},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Pets",
                        "description": "Animals we keep at home",
                        "key_concepts": ["pet", "home", "family"],
                        "examples": ["My dog is my best friend!"],
                        "order": 3,
                        "categories": [
                            {
                                "name": "Pets",
                                "order": 1,
                                "items": [
                                    {"word": "dog", "definition": "Un perro", "example": "My dog is friendly!", "order": 1},
                                    {"word": "cat", "definition": "Un gato", "example": "The cat sleeps a lot!", "order": 2},
                                    {"word": "bird", "definition": "Un pájaro", "example": "The bird sings!", "order": 3},
                                    {"word": "fish", "definition": "Un pez", "example": "The fish swims!", "order": 4},
                                ]
                            }
                        ]
                    }
                ],
                "grammar_rules": [
                    {"title": "Animal Sounds", "explanation": "Animals make different sounds", "examples": ["The dog barks. The cat meows."], "order": 1},
                    {"title": "Using 'The'", "explanation": "We use 'the' with animals", "examples": ["The lion", "The cat"], "order": 2},
                ]
            },
            {
                "unit_number": 102,
                "title": "Colors - Los Colores",
                "description": "Learn basic colors in English",
                "detailed_explanation": "This unit teaches children the primary and secondary colors. Each color is presented with its name and fun examples of things that have that color.",
                "learning_objectives": ["Identify 10+ colors", "Describe objects by color", "Use color words in sentences"],
                "overview": "Primary and secondary colors vocabulary",
                "age_group": "children",
                "min_age": 3,
                "max_age": 7,
                "cefr_level": "A1",
                "is_children_content": True,
                "topics": [
                    {
                        "title": "Primary Colors",
                        "description": "Red, Blue, Yellow - the main colors",
                        "key_concepts": ["primary", "color", "mix"],
                        "examples": ["The sky is blue."],
                        "order": 1,
                        "categories": [
                            {
                                "name": "Primary Colors",
                                "order": 1,
                                "items": [
                                    {"word": "red", "definition": "Rojo", "example": "The apple is red!", "order": 1},
                                    {"word": "blue", "definition": "Azul", "example": "The sky is blue!", "order": 2},
                                    {"word": "yellow", "definition": "Amarillo", "example": "The sun is yellow!", "order": 3},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Secondary Colors",
                        "description": "Colors made by mixing primary colors",
                        "key_concepts": ["mix", "secondary", "combine"],
                        "examples": ["Orange is made from red and yellow."],
                        "order": 2,
                        "categories": [
                            {
                                "name": "Secondary Colors",
                                "order": 1,
                                "items": [
                                    {"word": "orange", "definition": "Naranja", "example": "The orange is colorful!", "order": 1},
                                    {"word": "green", "definition": "Verde", "example": "The grass is green!", "order": 2},
                                    {"word": "purple", "definition": "Morado", "example": "The grape is purple!", "order": 3},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "More Colors",
                        "description": "Additional common colors",
                        "key_concepts": ["shade", "light", "dark"],
                        "examples": ["I like pink!"],
                        "order": 3,
                        "categories": [
                            {
                                "name": "More Colors",
                                "order": 1,
                                "items": [
                                    {"word": "pink", "definition": "Rosa", "example": "The flower is pink!", "order": 1},
                                    {"word": "black", "definition": "Negro", "example": "The night is black!", "order": 2},
                                    {"word": "white", "definition": "Blanco", "example": "Snow is white!", "order": 3},
                                    {"word": "brown", "definition": "Marrón", "example": "The bear is brown!", "order": 4},
                                ]
                            }
                        ]
                    }
                ],
                "grammar_rules": [
                    {"title": "Colors as Adjectives", "explanation": "Colors describe nouns", "examples": ["red car", "blue sky"], "order": 1},
                ]
            },
            {
                "unit_number": 103,
                "title": "Numbers - Los Números",
                "description": "Learn to count from 1 to 20",
                "detailed_explanation": "This unit teaches children how to count from 1 to 20. It includes numbers in English with their pronunciation and fun examples using everyday objects.",
                "learning_objectives": ["Count from 1 to 20", "Recognize numbers in writing", "Use numbers in context"],
                "overview": "Numbers 1-20 vocabulary",
                "age_group": "children",
                "min_age": 3,
                "max_age": 6,
                "cefr_level": "A1",
                "is_children_content": True,
                "topics": [
                    {
                        "title": "Numbers 1-10",
                        "description": "Counting from one to ten",
                        "key_concepts": ["count", "number", "digit"],
                        "examples": ["I have one apple!"],
                        "order": 1,
                        "categories": [
                            {
                                "name": "Numbers 1-10",
                                "order": 1,
                                "items": [
                                    {"word": "one", "definition": "Uno", "example": "I have one toy!", "order": 1},
                                    {"word": "two", "definition": "Dos", "example": "Two eyes!", "order": 2},
                                    {"word": "three", "definition": "Tres", "example": "Three bears!", "order": 3},
                                    {"word": "four", "definition": "Cuatro", "example": "Four legs!", "order": 4},
                                    {"word": "five", "definition": "Cinco", "example": "Five fingers!", "order": 5},
                                    {"word": "six", "definition": "Seis", "example": "Six sides!", "order": 6},
                                    {"word": "seven", "definition": "Siete", "example": "Seven days!", "order": 7},
                                    {"word": "eight", "definition": "Ocho", "example": "Eight legs!", "order": 8},
                                    {"word": "nine", "definition": "Nueve", "example": "Nine planets!", "order": 9},
                                    {"word": "ten", "definition": "Diez", "example": "Ten toes!", "order": 10},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Numbers 11-20",
                        "description": "Counting from eleven to twenty",
                        "key_concepts": ["teen", "count", "continue"],
                        "examples": ["I am eleven years old!"],
                        "order": 2,
                        "categories": [
                            {
                                "name": "Numbers 11-20",
                                "order": 1,
                                "items": [
                                    {"word": "eleven", "definition": "Once", "example": "Eleven cookies!", "order": 1},
                                    {"word": "twelve", "definition": "Doce", "example": "Twelve months!", "order": 2},
                                    {"word": "thirteen", "definition": "Trece", "example": "Thirteen!",
                                     "order": 3},
                                    {"word": "fourteen", "definition": "Catorce", "example": "Fourteen!", "order": 4},
                                    {"word": "fifteen", "definition": "Quince", "example": "Fifteen!", "order": 5},
                                    {"word": "sixteen", "definition": "Dieciséis", "example": "Sixteen!", "order": 6},
                                    {"word": "seventeen", "definition": "Diecisiete", "example": "Seventeen!", "order": 7},
                                    {"word": "eighteen", "definition": "Dieciocho", "example": "Eighteen!", "order": 8},
                                    {"word": "nineteen", "definition": "Diecinueve", "example": "Nineteen!", "order": 9},
                                    {"word": "twenty", "definition": "Veinte", "example": "Twenty!", "order": 10},
                                ]
                            }
                        ]
                    }
                ],
                "grammar_rules": [
                    {"title": "How many?", "explanation": "Asking about quantity", "examples": ["How many apples?"], "order": 1},
                ]
            },
            {
                "unit_number": 104,
                "title": "Food - La Comida",
                "description": "Learn basic food words in English",
                "detailed_explanation": "This unit teaches children common food items they eat every day. Foods are organized by meals and categories to make learning easier and more practical.",
                "learning_objectives": ["Learn 15+ food names", "Describe food preferences", "Use food words in sentences"],
                "overview": "Fruits, vegetables, and meals vocabulary",
                "age_group": "children",
                "min_age": 4,
                "max_age": 8,
                "cefr_level": "A1",
                "is_children_content": True,
                "topics": [
                    {
                        "title": "Fruits",
                        "description": "Sweet and healthy fruits",
                        "key_concepts": ["fruit", "sweet", "healthy"],
                        "examples": ["I love apples!"],
                        "order": 1,
                        "categories": [
                            {
                                "name": "Fruits",
                                "order": 1,
                                "items": [
                                    {"word": "apple", "definition": "Manzana", "example": "The apple is red!", "order": 1},
                                    {"word": "banana", "definition": "Plátano", "example": "Bananas are yellow!", "order": 2},
                                    {"word": "orange", "definition": "Naranja", "example": "Oranges are juicy!", "order": 3},
                                    {"word": "grape", "definition": "Uva", "example": "Grapes are small!", "order": 4},
                                    {"word": "strawberry", "definition": "Fresa", "example": "Strawberries are red!", "order": 5},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Vegetables",
                        "description": "Healthy vegetables",
                        "key_concepts": ["vegetable", "healthy", "green"],
                        "examples": ["Eat your vegetables!"],
                        "order": 2,
                        "categories": [
                            {
                                "name": "Vegetables",
                                "order": 1,
                                "items": [
                                    {"word": "carrot", "definition": "Zanahoria", "example": "Carrots are orange!", "order": 1},
                                    {"word": "potato", "definition": "Papa", "example": "Potatoes are yummy!", "order": 2},
                                    {"word": "tomato", "definition": "Tomate", "example": "Tomatoes are red!", "order": 3},
                                    {"word": "lettuce", "definition": "Lechuga", "example": "Lettuce is green!", "order": 4},
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Drinks",
                        "description": "Things we drink",
                        "key_concepts": ["drink", "liquid", "thirsty"],
                        "examples": ["I am thirsty!"],
                        "order": 3,
                        "categories": [
                            {
                                "name": "Drinks",
                                "order": 1,
                                "items": [
                                    {"word": "water", "definition": "Agua", "example": "Water is healthy!", "order": 1},
                                    {"word": "milk", "definition": "Leche", "example": "Milk is white!", "order": 2},
                                    {"word": "juice", "definition": "Jugo", "example": "Juice is sweet!", "order": 3},
                                ]
                            }
                        ]
                    }
                ],
                "grammar_rules": [
                    {"title": "I like...", "explanation": "Expressing food preferences", "examples": ["I like apples.", "I don't like broccoli."], "order": 1},
                    {"title": "Using 'a' or 'some'", "explanation": "Articles with food", "examples": ["an apple", "some milk"], "order": 2},
                ]
            }
        ]

        for unit_data in units_data:
            existing_unit = Unit.query.filter_by(unit_number=unit_data["unit_number"]).first()
            if existing_unit:
                print(f"Unit {unit_data['unit_number']} already exists, skipping...")
                continue

            unit = Unit(
                unit_number=unit_data["unit_number"],
                title=unit_data["title"],
                description=unit_data["description"],
                detailed_explanation=unit_data.get("detailed_explanation"),
                learning_objectives=unit_data.get("learning_objectives"),
                overview=unit_data.get("overview"),
                is_children_content=unit_data.get("is_children_content", False),
                age_group=unit_data.get("age_group"),
                min_age=unit_data.get("min_age"),
                max_age=unit_data.get("max_age"),
                cefr_level=unit_data.get("cefr_level")
            )
            db.session.add(unit)
            db.session.flush()

            print(f"✓ Created Unit: {unit.title}")

            for topic_data in unit_data.get("topics", []):
                topic = Topic(
                    unit_id=unit.id,
                    title=topic_data["title"],
                    description=topic_data.get("description"),
                    key_concepts=topic_data.get("key_concepts"),
                    examples=topic_data.get("examples"),
                    order=topic_data.get("order", 0)
                )
                db.session.add(topic)
                db.session.flush()

                print(f"  ✓ Added topic: {topic.title}")

                for cat_data in topic_data.get("categories", []):
                    category = VocabularyCategory(
                        unit_id=unit.id,
                        topic_id=topic.id,
                        name=cat_data["name"],
                        order=cat_data.get("order", 0)
                    )
                    db.session.add(category)
                    db.session.flush()

                    print(f"    ✓ Added category: {category.name}")

                    for item_data in cat_data.get("items", []):
                        item = VocabularyItem(
                            category_id=category.id,
                            word=item_data["word"],
                            definition=item_data["definition"],
                            example=item_data.get("example"),
                            order=item_data.get("order", 0),
                            image_url=None
                        )
                        db.session.add(item)

            for grammar_data in unit_data.get("grammar_rules", []):
                grammar = GrammarRule(
                    unit_id=unit.id,
                    title=grammar_data["title"],
                    explanation=grammar_data.get("explanation"),
                    examples=grammar_data.get("examples"),
                    order=grammar_data.get("order", 0)
                )
                db.session.add(grammar)

            print(f"  ✓ Added {len(unit_data.get('grammar_rules', []))} grammar rules")

            db.session.flush()

        db.session.commit()
        print("\n✅ All children units created successfully!")

if __name__ == "__main__":
    seed_children_units()
