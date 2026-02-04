"""
Seed completo de unidades por niveles CEFR
A1, A2, B1, B2, C1, C2 - 12 unidades por nivel = 72 unidades totales
"""
from app import create_app
from app.extensions import db
from app.models import Unit, Topic, GrammarRule, VocabularyCategory, VocabularyItem, WritingPractice

app = create_app()

# ============================================================================
# NIVEL A1 - PRINCIPIANTE (Unidades 1-12)
# ============================================================================
A1_UNITS = [
    {
        "unit_number": 1,
        "title": "Hello! Nice to Meet You",
        "level": "A1",
        "description": "Saludos, presentaciones y información personal básica",
        "topics": [
            {"title": "Greetings", "description": "Hello, Hi, Good morning/afternoon/evening, Goodbye"},
            {"title": "Introductions", "description": "My name is..., I'm from..., Nice to meet you"},
            {"title": "Personal Information", "description": "Name, age, nationality, phone number"}
        ],
        "grammar": [
            {"topic": "Verb TO BE (am/is/are)", "rule": "I am, You are, He/She/It is, We/They are"},
            {"topic": "Subject Pronouns", "rule": "I, you, he, she, it, we, they"},
            {"topic": "Possessive Adjectives", "rule": "my, your, his, her, its, our, their"}
        ],
        "vocabulary": ["Countries", "Nationalities", "Numbers 1-20"],
        "writing": "Hello! My name is [Name]. I am from [Country]. I am [age] years old. Nice to meet you!"
    },
    {
        "unit_number": 2,
        "title": "My Family",
        "level": "A1",
        "description": "Miembros de la familia y descripciones básicas",
        "topics": [
            {"title": "Family Members", "description": "Mother, father, sister, brother, grandparents"},
            {"title": "Physical Description", "description": "Tall, short, young, old"},
            {"title": "Ages", "description": "How old are you? I am... years old"}
        ],
        "grammar": [
            {"topic": "Plural Nouns", "rule": "Add -s/-es: brother → brothers, family → families"},
            {"topic": "Have/Has", "rule": "I have, He/She has"},
            {"topic": "This/That/These/Those", "rule": "Demonstrative pronouns for near/far"}
        ],
        "vocabulary": ["Family members", "Numbers 20-100", "Basic adjectives"],
        "writing": "This is my family. I have a mother and a father. My mother is tall. My father is 45 years old. I have one sister. She is young."
    },
    {
        "unit_number": 3,
        "title": "My Home",
        "level": "A1",
        "description": "Habitaciones de la casa y muebles básicos",
        "topics": [
            {"title": "Rooms", "description": "Kitchen, bedroom, bathroom, living room"},
            {"title": "Furniture", "description": "Table, chair, bed, sofa, TV"},
            {"title": "Where Things Are", "description": "The TV is in the living room"}
        ],
        "grammar": [
            {"topic": "There is/There are", "rule": "There is a bed. There are two chairs."},
            {"topic": "Prepositions of Place", "rule": "in, on, under, next to, between"},
            {"topic": "Articles a/an", "rule": "a table, an apple"}
        ],
        "vocabulary": ["Rooms", "Furniture", "Household items"],
        "writing": "This is my home. There are four rooms. There is a big kitchen. My bedroom is small. There is a bed and a desk in my room."
    },
    {
        "unit_number": 4,
        "title": "Daily Routine",
        "level": "A1",
        "description": "Actividades diarias y la hora",
        "topics": [
            {"title": "Daily Activities", "description": "Wake up, eat breakfast, go to work/school"},
            {"title": "Telling Time", "description": "What time is it? It's 7 o'clock"},
            {"title": "Days of the Week", "description": "Monday, Tuesday, Wednesday..."}
        ],
        "grammar": [
            {"topic": "Simple Present", "rule": "I wake up at 7. She works at 9."},
            {"topic": "Adverbs of Frequency", "rule": "always, usually, sometimes, never"},
            {"topic": "Third Person -s", "rule": "He works, She eats, It rains"}
        ],
        "vocabulary": ["Daily activities", "Times of day", "Days and months"],
        "writing": "I wake up at 7 o'clock. I eat breakfast at 7:30. I go to school at 8:00. I usually study in the morning. I always sleep at 10 PM."
    },
    {
        "unit_number": 5,
        "title": "Food and Drinks",
        "level": "A1",
        "description": "Comidas, bebidas y en el restaurante",
        "topics": [
            {"title": "Food Items", "description": "Bread, rice, chicken, vegetables, fruits"},
            {"title": "Drinks", "description": "Water, coffee, tea, juice, milk"},
            {"title": "At the Restaurant", "description": "Can I have...? I'd like..."}
        ],
        "grammar": [
            {"topic": "Countable/Uncountable Nouns", "rule": "an apple (countable), water (uncountable)"},
            {"topic": "Some/Any", "rule": "I have some bread. I don't have any milk."},
            {"topic": "Would like", "rule": "I'd like a coffee, please."}
        ],
        "vocabulary": ["Food", "Drinks", "Restaurant phrases"],
        "writing": "I like pizza and pasta. I don't like fish. For breakfast, I have some bread and coffee. I'd like some water, please."
    },
    {
        "unit_number": 6,
        "title": "Jobs and Work",
        "level": "A1",
        "description": "Profesiones y lugares de trabajo",
        "topics": [
            {"title": "Common Jobs", "description": "Teacher, doctor, engineer, driver"},
            {"title": "Workplaces", "description": "Office, hospital, school, factory"},
            {"title": "Work Activities", "description": "He teaches. She helps patients."}
        ],
        "grammar": [
            {"topic": "Questions with DO/DOES", "rule": "Do you work? Does she teach?"},
            {"topic": "Short Answers", "rule": "Yes, I do. No, she doesn't."},
            {"topic": "WH-Questions", "rule": "What do you do? Where do you work?"}
        ],
        "vocabulary": ["Jobs", "Workplaces", "Work verbs"],
        "writing": "I am a student. My mother is a teacher. She works at a school. She teaches English. My father is an engineer."
    },
    {
        "unit_number": 7,
        "title": "Shopping",
        "level": "A1",
        "description": "Compras, precios y ropa",
        "topics": [
            {"title": "Clothes", "description": "Shirt, pants, dress, shoes, jacket"},
            {"title": "Colors", "description": "Red, blue, green, black, white"},
            {"title": "Prices", "description": "How much is it? It's $20."}
        ],
        "grammar": [
            {"topic": "How much/How many", "rule": "How much is it? How many do you want?"},
            {"topic": "Adjective Order", "rule": "a beautiful red dress"},
            {"topic": "Can for requests", "rule": "Can I try this on?"}
        ],
        "vocabulary": ["Clothes", "Colors", "Shopping phrases"],
        "writing": "I want to buy a new shirt. This blue shirt is nice. How much is it? It's $25. That's expensive! Can I see the red one?"
    },
    {
        "unit_number": 8,
        "title": "Weather and Seasons",
        "level": "A1",
        "description": "El clima y las estaciones del año",
        "topics": [
            {"title": "Weather", "description": "Sunny, rainy, cloudy, windy, snowy"},
            {"title": "Seasons", "description": "Spring, summer, autumn/fall, winter"},
            {"title": "Temperature", "description": "Hot, warm, cool, cold"}
        ],
        "grammar": [
            {"topic": "Present Continuous", "rule": "It's raining. The sun is shining."},
            {"topic": "What...like?", "rule": "What's the weather like today?"},
            {"topic": "Because", "rule": "I'm wearing a jacket because it's cold."}
        ],
        "vocabulary": ["Weather words", "Seasons", "Temperature"],
        "writing": "Today is sunny and warm. I like summer because it's hot. In winter, it's very cold and it snows. What's the weather like in your country?"
    },
    {
        "unit_number": 9,
        "title": "Transportation",
        "level": "A1",
        "description": "Medios de transporte y direcciones",
        "topics": [
            {"title": "Vehicles", "description": "Car, bus, train, bike, plane"},
            {"title": "Getting Around", "description": "Go by bus, take the train, walk"},
            {"title": "Directions", "description": "Go straight, turn left/right"}
        ],
        "grammar": [
            {"topic": "By + Transport", "rule": "I go to work by bus. I travel by plane."},
            {"topic": "Imperatives", "rule": "Go straight. Turn left. Stop here."},
            {"topic": "Prepositions of Movement", "rule": "to, from, into, out of"}
        ],
        "vocabulary": ["Transport", "Directions", "Places in town"],
        "writing": "I go to school by bus. My father goes to work by car. The train station is near my house. Turn left and go straight."
    },
    {
        "unit_number": 10,
        "title": "Hobbies and Free Time",
        "level": "A1",
        "description": "Pasatiempos y actividades de ocio",
        "topics": [
            {"title": "Hobbies", "description": "Reading, swimming, playing games, cooking"},
            {"title": "Sports", "description": "Football, basketball, tennis, running"},
            {"title": "Free Time Activities", "description": "Watch TV, listen to music, meet friends"}
        ],
        "grammar": [
            {"topic": "Like + -ing", "rule": "I like swimming. She likes reading."},
            {"topic": "Play/Go/Do + Sports", "rule": "play football, go swimming, do yoga"},
            {"topic": "Frequency Expressions", "rule": "every day, once a week, on weekends"}
        ],
        "vocabulary": ["Hobbies", "Sports", "Free time activities"],
        "writing": "I like playing football. I play with my friends every Saturday. I also like reading books. My sister likes swimming. She goes to the pool twice a week."
    },
    {
        "unit_number": 11,
        "title": "Health and Body",
        "level": "A1",
        "description": "El cuerpo humano y la salud básica",
        "topics": [
            {"title": "Body Parts", "description": "Head, arm, leg, hand, foot, eye, ear"},
            {"title": "Health Problems", "description": "Headache, cold, fever, stomachache"},
            {"title": "At the Doctor", "description": "What's wrong? I have a headache."}
        ],
        "grammar": [
            {"topic": "Have for Health", "rule": "I have a headache. He has a cold."},
            {"topic": "Should for Advice", "rule": "You should rest. You should see a doctor."},
            {"topic": "Imperatives for Instructions", "rule": "Take this medicine. Drink water."}
        ],
        "vocabulary": ["Body parts", "Health problems", "Medicine"],
        "writing": "I don't feel well. I have a headache and a fever. I should rest and drink water. My mother says I should see a doctor."
    },
    {
        "unit_number": 12,
        "title": "Celebrations and Holidays",
        "level": "A1",
        "description": "Fiestas, celebraciones y fechas especiales",
        "topics": [
            {"title": "Holidays", "description": "Christmas, New Year, Birthday"},
            {"title": "Celebrations", "description": "Party, gift, cake, decorations"},
            {"title": "Special Days", "description": "Mother's Day, Valentine's Day"}
        ],
        "grammar": [
            {"topic": "Present Continuous for Plans", "rule": "We're having a party tomorrow."},
            {"topic": "Going to", "rule": "I'm going to buy a gift."},
            {"topic": "Ordinal Numbers", "rule": "first, second, third... for dates"}
        ],
        "vocabulary": ["Celebrations", "Months", "Ordinal numbers"],
        "writing": "My birthday is on March 15th. I'm going to have a party. My friends are coming to my house. We're going to eat cake and dance."
    },
]

# ============================================================================
# NIVEL A2 - ELEMENTARY (Unidades 13-24)
# ============================================================================
A2_UNITS = [
    {
        "unit_number": 13,
        "title": "Childhood Memories",
        "level": "A2",
        "description": "Recuerdos de la infancia y el pasado",
        "topics": [
            {"title": "Childhood Activities", "description": "Play games, go to school, make friends"},
            {"title": "Past Experiences", "description": "When I was young..."},
            {"title": "Memories", "description": "I remember when..."}
        ],
        "grammar": [
            {"topic": "Past Simple (Regular)", "rule": "played, walked, watched - add -ed"},
            {"topic": "Past Simple (Irregular)", "rule": "went, had, was/were, saw, ate"},
            {"topic": "Time Expressions", "rule": "yesterday, last week, ago, when I was..."}
        ],
        "vocabulary": ["Childhood activities", "Past time expressions", "Feelings"],
        "writing": "When I was a child, I lived in a small town. I played with my friends every day. We had a lot of fun. I went to a small school near my house."
    },
    {
        "unit_number": 14,
        "title": "Travel and Vacation",
        "level": "A2",
        "description": "Viajes, vacaciones y turismo",
        "topics": [
            {"title": "Vacation Destinations", "description": "Beach, mountains, city, countryside"},
            {"title": "Travel Plans", "description": "Book a hotel, pack bags, buy tickets"},
            {"title": "At the Airport/Hotel", "description": "Check in, board the plane, room key"}
        ],
        "grammar": [
            {"topic": "Be going to (Future)", "rule": "I'm going to travel to Paris."},
            {"topic": "Will (Predictions)", "rule": "It will be fun. You'll love it."},
            {"topic": "Past Simple Questions", "rule": "Did you visit...? Where did you go?"}
        ],
        "vocabulary": ["Travel", "Accommodation", "Tourist activities"],
        "writing": "Last summer, I went to the beach with my family. We stayed at a nice hotel. The weather was sunny. I swam in the ocean every day. It was amazing!"
    },
    {
        "unit_number": 15,
        "title": "Life Events",
        "level": "A2",
        "description": "Eventos importantes de la vida",
        "topics": [
            {"title": "Milestones", "description": "Graduate, get married, have children"},
            {"title": "Achievements", "description": "Win a prize, pass an exam, learn to drive"},
            {"title": "Changes", "description": "Move to a new city, start a job"}
        ],
        "grammar": [
            {"topic": "Present Perfect Introduction", "rule": "I have graduated. She has gotten married."},
            {"topic": "Ever/Never", "rule": "Have you ever...? I have never..."},
            {"topic": "Just/Already/Yet", "rule": "I've just finished. I haven't started yet."}
        ],
        "vocabulary": ["Life events", "Achievement verbs", "Time markers"],
        "writing": "I have just graduated from university. I have never been to Europe, but I want to go. My sister has already gotten married. She has two children now."
    },
    {
        "unit_number": 16,
        "title": "Entertainment",
        "level": "A2",
        "description": "Entretenimiento, películas y música",
        "topics": [
            {"title": "Movies and TV", "description": "Genres, actors, reviews"},
            {"title": "Music", "description": "Concerts, instruments, favorite songs"},
            {"title": "Books and Reading", "description": "Novels, authors, recommendations"}
        ],
        "grammar": [
            {"topic": "Comparative Adjectives", "rule": "better than, more interesting than"},
            {"topic": "Superlative Adjectives", "rule": "the best, the most exciting"},
            {"topic": "As...as", "rule": "This book is as good as that one."}
        ],
        "vocabulary": ["Movie genres", "Music types", "Entertainment venues"],
        "writing": "I think action movies are more exciting than comedies. The best movie I've ever seen is Inception. It's the most interesting film. My favorite singer is better than any other artist."
    },
    {
        "unit_number": 17,
        "title": "Technology in Daily Life",
        "level": "A2",
        "description": "Tecnología cotidiana y aparatos",
        "topics": [
            {"title": "Devices", "description": "Smartphone, laptop, tablet, smart TV"},
            {"title": "Internet", "description": "Social media, email, online shopping"},
            {"title": "Problems and Solutions", "description": "It doesn't work. I need to charge it."}
        ],
        "grammar": [
            {"topic": "Modal: Can/Can't", "rule": "You can download apps. You can't use it without Wi-Fi."},
            {"topic": "Modal: Have to", "rule": "You have to update the software."},
            {"topic": "Modal: Don't have to", "rule": "You don't have to pay for this app."}
        ],
        "vocabulary": ["Technology", "Internet verbs", "Tech problems"],
        "writing": "I use my smartphone every day. I can send emails, take photos, and browse the internet. Sometimes it doesn't work well. I have to charge it every night."
    },
    {
        "unit_number": 18,
        "title": "Eating Out",
        "level": "A2",
        "description": "Restaurantes y comida internacional",
        "topics": [
            {"title": "Types of Restaurants", "description": "Fast food, Italian, Chinese, vegetarian"},
            {"title": "Ordering Food", "description": "Menu, order, bill, tip"},
            {"title": "Food Preferences", "description": "Spicy, sweet, salty, healthy"}
        ],
        "grammar": [
            {"topic": "Would like vs Want", "rule": "I'd like (polite) vs I want (direct)"},
            {"topic": "Could for Requests", "rule": "Could I have the menu, please?"},
            {"topic": "Too/Enough", "rule": "Too spicy. Not sweet enough."}
        ],
        "vocabulary": ["Restaurant vocabulary", "Food adjectives", "Ordering phrases"],
        "writing": "Last night I went to an Italian restaurant. I ordered pasta and a salad. The pasta was delicious but too salty. The waiter was very friendly. I'd like to go there again."
    },
    {
        "unit_number": 19,
        "title": "Health and Fitness",
        "level": "A2",
        "description": "Ejercicio, dieta y bienestar",
        "topics": [
            {"title": "Exercise", "description": "Gym, running, yoga, cycling"},
            {"title": "Healthy Habits", "description": "Sleep well, eat vegetables, drink water"},
            {"title": "Fitness Goals", "description": "Lose weight, build muscle, feel better"}
        ],
        "grammar": [
            {"topic": "Should/Shouldn't", "rule": "You should exercise. You shouldn't eat junk food."},
            {"topic": "Need to/Don't need to", "rule": "You need to sleep more."},
            {"topic": "Infinitive of Purpose", "rule": "I exercise to stay healthy."}
        ],
        "vocabulary": ["Exercise types", "Healthy/unhealthy habits", "Body and fitness"],
        "writing": "I try to be healthy. I go to the gym twice a week to stay fit. I should eat more vegetables and I shouldn't drink soda. I need to sleep at least 7 hours."
    },
    {
        "unit_number": 20,
        "title": "The Environment",
        "level": "A2",
        "description": "El medio ambiente y problemas ecológicos",
        "topics": [
            {"title": "Environmental Problems", "description": "Pollution, climate change, deforestation"},
            {"title": "Green Actions", "description": "Recycle, save water, use less plastic"},
            {"title": "Nature", "description": "Forests, oceans, animals, plants"}
        ],
        "grammar": [
            {"topic": "First Conditional", "rule": "If we recycle, we will help the planet."},
            {"topic": "Must/Mustn't", "rule": "We must protect nature. We mustn't pollute."},
            {"topic": "Will for Predictions", "rule": "The climate will change."}
        ],
        "vocabulary": ["Environment", "Eco actions", "Nature and wildlife"],
        "writing": "Pollution is a big problem. If we don't act now, the situation will get worse. We must recycle and use less plastic. We mustn't throw trash in the ocean."
    },
    {
        "unit_number": 21,
        "title": "Work and Career",
        "level": "A2",
        "description": "Trabajo, carrera profesional y habilidades",
        "topics": [
            {"title": "Job Skills", "description": "Communication, teamwork, computer skills"},
            {"title": "Job Search", "description": "CV, interview, apply for a job"},
            {"title": "Workplace", "description": "Colleagues, boss, meeting, deadline"}
        ],
        "grammar": [
            {"topic": "Present Perfect for Experience", "rule": "I have worked in sales for 2 years."},
            {"topic": "For/Since", "rule": "for 3 years, since 2020"},
            {"topic": "Can/Could for Ability", "rule": "I can speak English. I could type fast."}
        ],
        "vocabulary": ["Job skills", "CV vocabulary", "Workplace terms"],
        "writing": "I am looking for a new job. I have worked as a receptionist for two years. I can speak English and Spanish. I have experience with computers since 2018."
    },
    {
        "unit_number": 22,
        "title": "Relationships",
        "level": "A2",
        "description": "Relaciones personales y sociales",
        "topics": [
            {"title": "Friendship", "description": "Best friend, make friends, keep in touch"},
            {"title": "Romantic Relationships", "description": "Date, fall in love, get engaged"},
            {"title": "Family Dynamics", "description": "Get along with, argue, support each other"}
        ],
        "grammar": [
            {"topic": "Phrasal Verbs (Relationships)", "rule": "get along, break up, look after"},
            {"topic": "Adverbs of Manner", "rule": "happily, carefully, quickly"},
            {"topic": "Verb + Preposition", "rule": "talk to, listen to, believe in"}
        ],
        "vocabulary": ["Relationship verbs", "Personality adjectives", "Social expressions"],
        "writing": "My best friend is Maria. We get along very well. We've known each other since primary school. We always support each other. We keep in touch every day."
    },
    {
        "unit_number": 23,
        "title": "Cities and Places",
        "level": "A2",
        "description": "Ciudades, lugares y comparaciones",
        "topics": [
            {"title": "City Features", "description": "Buildings, parks, traffic, nightlife"},
            {"title": "City vs Country", "description": "Busy, quiet, crowded, peaceful"},
            {"title": "Famous Places", "description": "Landmarks, tourist attractions, history"}
        ],
        "grammar": [
            {"topic": "Comparatives Review", "rule": "The city is busier than the countryside."},
            {"topic": "Not as...as", "rule": "The village is not as crowded as the city."},
            {"topic": "Superlatives Review", "rule": "Tokyo is the most populated city."}
        ],
        "vocabulary": ["City vocabulary", "Country vocabulary", "Adjectives for places"],
        "writing": "I prefer living in the city because there are more opportunities. However, the countryside is more peaceful and not as polluted as the city. The most beautiful place I've visited is Paris."
    },
    {
        "unit_number": 24,
        "title": "Future Plans and Dreams",
        "level": "A2",
        "description": "Planes futuros, sueños y ambiciones",
        "topics": [
            {"title": "Life Goals", "description": "Career goals, travel dreams, personal growth"},
            {"title": "Making Plans", "description": "Next year, in five years, someday"},
            {"title": "Hopes and Wishes", "description": "I hope to..., I want to..., I'd like to..."}
        ],
        "grammar": [
            {"topic": "Going to vs Will", "rule": "Plans (going to) vs Decisions (will)"},
            {"topic": "Hope/Want/Would like + to", "rule": "I hope to travel. I want to learn."},
            {"topic": "Future Time Expressions", "rule": "next year, in the future, someday"}
        ],
        "vocabulary": ["Goals and ambitions", "Future expressions", "Dream vocabulary"],
        "writing": "I have many plans for the future. Next year, I'm going to learn to drive. In five years, I hope to have a good job. Someday, I'd like to travel around the world."
    },
]

# ============================================================================
# NIVEL B1 - INTERMEDIATE (Unidades 25-36)
# ============================================================================
B1_UNITS = [
    {
        "unit_number": 25,
        "title": "Storytelling",
        "level": "B1",
        "description": "Narrativa, contar historias y anécdotas",
        "topics": [
            {"title": "Narrative Techniques", "description": "Setting the scene, building tension, conclusion"},
            {"title": "Interesting Experiences", "description": "Adventures, funny stories, memorable moments"},
            {"title": "Sequencing Events", "description": "First, then, after that, finally"}
        ],
        "grammar": [
            {"topic": "Past Continuous", "rule": "I was walking when it started to rain."},
            {"topic": "Past Simple vs Past Continuous", "rule": "While I was sleeping, the phone rang."},
            {"topic": "Time Clauses", "rule": "when, while, as soon as, before, after"}
        ],
        "vocabulary": ["Narrative expressions", "Sequencing words", "Adjectives for stories"],
        "writing": "I was walking home when something strange happened. While I was crossing the park, I saw a mysterious light in the sky. I stopped and watched it for a few minutes. Then, as soon as it appeared, it vanished."
    },
    {
        "unit_number": 26,
        "title": "Education and Learning",
        "level": "B1",
        "description": "Educación, sistemas educativos y aprendizaje",
        "topics": [
            {"title": "School Systems", "description": "Primary, secondary, university, exams"},
            {"title": "Learning Styles", "description": "Visual, auditory, kinesthetic learners"},
            {"title": "Study Skills", "description": "Take notes, review, memorize, practice"}
        ],
        "grammar": [
            {"topic": "Used to / Would", "rule": "I used to study at night. I would review before exams."},
            {"topic": "Get/Be used to", "rule": "I'm getting used to online classes."},
            {"topic": "Passive Voice (Present)", "rule": "Students are taught by teachers."}
        ],
        "vocabulary": ["Education system", "Academic verbs", "Study techniques"],
        "writing": "When I was a student, I used to study late at night. I would review all my notes before exams. Now, online classes are becoming more common. I'm still getting used to learning from home."
    },
    {
        "unit_number": 27,
        "title": "News and Media",
        "level": "B1",
        "description": "Noticias, medios de comunicación y actualidad",
        "topics": [
            {"title": "Types of Media", "description": "Newspapers, TV news, online news, podcasts"},
            {"title": "News Topics", "description": "Politics, economy, sports, entertainment"},
            {"title": "Fake News", "description": "Reliable sources, fact-checking, bias"}
        ],
        "grammar": [
            {"topic": "Passive Voice (Past)", "rule": "The article was written by a journalist."},
            {"topic": "Reported Speech (Statements)", "rule": "He said that prices had increased."},
            {"topic": "Say vs Tell", "rule": "She said... / She told me..."}
        ],
        "vocabulary": ["Media vocabulary", "News collocations", "Journalism terms"],
        "writing": "According to the news, the economy is improving. It was reported that unemployment has decreased. The president said that new policies would be implemented. However, some sources are not always reliable."
    },
    {
        "unit_number": 28,
        "title": "Culture and Society",
        "level": "B1",
        "description": "Cultura, tradiciones y diferencias culturales",
        "topics": [
            {"title": "Traditions", "description": "Festivals, customs, ceremonies"},
            {"title": "Cultural Differences", "description": "Etiquette, greetings, taboos"},
            {"title": "Globalization", "description": "Cultural exchange, diversity, identity"}
        ],
        "grammar": [
            {"topic": "Defining Relative Clauses", "rule": "A tradition is something that/which people do."},
            {"topic": "Non-defining Relative Clauses", "rule": "Christmas, which is in December, is popular."},
            {"topic": "It is + adjective + infinitive", "rule": "It is important to respect other cultures."}
        ],
        "vocabulary": ["Culture and traditions", "Social customs", "Globalization terms"],
        "writing": "In my country, we celebrate a festival which is called [name]. It is a tradition that has been passed down for generations. It is important to preserve our cultural heritage while being open to other cultures."
    },
    {
        "unit_number": 29,
        "title": "Crime and Law",
        "level": "B1",
        "description": "Crimen, justicia y ley",
        "topics": [
            {"title": "Types of Crime", "description": "Theft, robbery, fraud, cybercrime"},
            {"title": "Justice System", "description": "Police, court, lawyer, judge, prison"},
            {"title": "Safety", "description": "Prevention, security, precautions"}
        ],
        "grammar": [
            {"topic": "Past Perfect", "rule": "The thief had escaped before police arrived."},
            {"topic": "Passive for News", "rule": "The criminal was arrested. The money was stolen."},
            {"topic": "Modal Verbs (Obligation)", "rule": "You must/have to obey the law."}
        ],
        "vocabulary": ["Crime vocabulary", "Legal terms", "Justice system"],
        "writing": "Last week, a robbery took place in the city center. By the time the police arrived, the criminals had already escaped. Fortunately, they were caught the next day. They are now in prison awaiting trial."
    },
    {
        "unit_number": 30,
        "title": "Science and Discovery",
        "level": "B1",
        "description": "Ciencia, descubrimientos e innovación",
        "topics": [
            {"title": "Scientific Method", "description": "Hypothesis, experiment, results, conclusion"},
            {"title": "Famous Discoveries", "description": "Inventions, breakthroughs, scientists"},
            {"title": "Modern Science", "description": "Space exploration, medicine, AI"}
        ],
        "grammar": [
            {"topic": "Present Perfect Continuous", "rule": "Scientists have been researching for years."},
            {"topic": "Passive Voice (Present Perfect)", "rule": "A new cure has been discovered."},
            {"topic": "Future Predictions", "rule": "By 2050, robots will be everywhere."}
        ],
        "vocabulary": ["Science vocabulary", "Research terms", "Technology innovations"],
        "writing": "Scientists have been working on a new vaccine for several years. Recently, important progress has been made. It is believed that this discovery will save millions of lives. The research has been funded by international organizations."
    },
    {
        "unit_number": 31,
        "title": "Money and Finance",
        "level": "B1",
        "description": "Dinero, finanzas personales y economía",
        "topics": [
            {"title": "Personal Finance", "description": "Budget, savings, debt, investments"},
            {"title": "Banking", "description": "Account, loan, credit card, interest"},
            {"title": "Economic Concepts", "description": "Inflation, recession, economy"}
        ],
        "grammar": [
            {"topic": "Second Conditional", "rule": "If I had more money, I would invest it."},
            {"topic": "Wish + Past Simple", "rule": "I wish I had more savings."},
            {"topic": "Unless", "rule": "You won't save money unless you budget."}
        ],
        "vocabulary": ["Finance terms", "Banking vocabulary", "Economic vocabulary"],
        "writing": "If I had a higher salary, I would save more money every month. I wish I had started investing earlier. Unless you control your spending, you won't be able to achieve financial stability."
    },
    {
        "unit_number": 32,
        "title": "Health and Medicine",
        "level": "B1",
        "description": "Salud, medicina y bienestar",
        "topics": [
            {"title": "Health Issues", "description": "Symptoms, diagnosis, treatment, prevention"},
            {"title": "Medical Professionals", "description": "Specialist, surgeon, nurse, therapist"},
            {"title": "Mental Health", "description": "Stress, anxiety, depression, wellbeing"}
        ],
        "grammar": [
            {"topic": "Giving Advice (Should have)", "rule": "You should have gone to the doctor."},
            {"topic": "Modal Verbs (Possibility)", "rule": "It might/could be an allergy."},
            {"topic": "Conditionals for Health", "rule": "If you rest, you'll feel better."}
        ],
        "vocabulary": ["Medical vocabulary", "Symptoms and treatments", "Mental health terms"],
        "writing": "I've been feeling tired lately. It might be stress from work. I should have taken a break earlier. If I don't take care of myself, I could get sick. The doctor recommended that I exercise more."
    },
    {
        "unit_number": 33,
        "title": "Art and Creativity",
        "level": "B1",
        "description": "Arte, creatividad y expresión artística",
        "topics": [
            {"title": "Forms of Art", "description": "Painting, sculpture, photography, music, dance"},
            {"title": "Artists and Works", "description": "Famous artists, masterpieces, styles"},
            {"title": "Creativity", "description": "Inspiration, imagination, self-expression"}
        ],
        "grammar": [
            {"topic": "Gerunds vs Infinitives", "rule": "I enjoy painting. I want to learn photography."},
            {"topic": "Verb Patterns", "rule": "stop/try + gerund vs infinitive (different meanings)"},
            {"topic": "Articles with Art", "rule": "The Mona Lisa (specific) vs Art (general)"}
        ],
        "vocabulary": ["Art forms", "Artistic vocabulary", "Creative expressions"],
        "writing": "I really enjoy painting landscapes. I started learning to draw when I was young. Art allows me to express my feelings. I remember trying oil painting for the first time – it was challenging but rewarding."
    },
    {
        "unit_number": 34,
        "title": "Sports and Competition",
        "level": "B1",
        "description": "Deportes, competición y logros deportivos",
        "topics": [
            {"title": "Sports Events", "description": "Olympics, World Cup, championships"},
            {"title": "Training and Practice", "description": "Coach, training, discipline, motivation"},
            {"title": "Winning and Losing", "description": "Victory, defeat, sportsmanship"}
        ],
        "grammar": [
            {"topic": "Reported Speech (Questions)", "rule": "She asked if I had won."},
            {"topic": "Reported Speech (Commands)", "rule": "The coach told us to practice more."},
            {"topic": "Past Perfect for Narrative", "rule": "He had trained for years before he won."}
        ],
        "vocabulary": ["Sports vocabulary", "Competition terms", "Achievement vocabulary"],
        "writing": "The athlete said that she had trained for ten years. Her coach had told her to never give up. She was asked how she felt about winning. She replied that it was a dream come true."
    },
    {
        "unit_number": 35,
        "title": "Work-Life Balance",
        "level": "B1",
        "description": "Equilibrio trabajo-vida, estrés y bienestar",
        "topics": [
            {"title": "Work Stress", "description": "Burnout, deadlines, pressure, overtime"},
            {"title": "Relaxation", "description": "Hobbies, vacations, meditation, rest"},
            {"title": "Time Management", "description": "Priorities, schedule, productivity"}
        ],
        "grammar": [
            {"topic": "Third Conditional", "rule": "If I had worked less, I would have been happier."},
            {"topic": "Should have / Could have", "rule": "I should have taken a break."},
            {"topic": "Both...and / Neither...nor", "rule": "Both work and rest are important."}
        ],
        "vocabulary": ["Work-life vocabulary", "Stress and relaxation", "Time management"],
        "writing": "If I had known about burnout, I would have taken more breaks. I should have listened to my body. Now I understand that both work and personal time are important. Neither overworking nor being lazy is healthy."
    },
    {
        "unit_number": 36,
        "title": "Global Issues",
        "level": "B1",
        "description": "Problemas globales y desafíos mundiales",
        "topics": [
            {"title": "World Problems", "description": "Poverty, hunger, inequality, war"},
            {"title": "Solutions", "description": "Charity, volunteering, awareness, action"},
            {"title": "Sustainable Development", "description": "Goals, progress, future challenges"}
        ],
        "grammar": [
            {"topic": "Mixed Conditionals", "rule": "If we had acted earlier, the situation would be different now."},
            {"topic": "Passive Voice (Various Tenses)", "rule": "Aid is being sent. Solutions have been proposed."},
            {"topic": "So...that / Such...that", "rule": "The problem is so serious that we must act."}
        ],
        "vocabulary": ["Global issues", "Solutions vocabulary", "International organizations"],
        "writing": "Poverty is such a serious issue that it affects millions of people. If governments had invested more in education years ago, the situation would be better today. Solutions are being discussed at international conferences."
    },
]

# ============================================================================
# NIVEL B2 - UPPER INTERMEDIATE (Unidades 37-48)
# ============================================================================
B2_UNITS = [
    {
        "unit_number": 37,
        "title": "Communication Skills",
        "level": "B2",
        "description": "Habilidades de comunicación avanzadas",
        "topics": [
            {"title": "Effective Communication", "description": "Clarity, empathy, active listening"},
            {"title": "Body Language", "description": "Gestures, facial expressions, eye contact"},
            {"title": "Conflict Resolution", "description": "Negotiation, compromise, understanding"}
        ],
        "grammar": [
            {"topic": "Cleft Sentences", "rule": "What I need is more time. It was John who called."},
            {"topic": "Emphasis with DO/DOES/DID", "rule": "I do understand your point."},
            {"topic": "Inversion for Emphasis", "rule": "Not only did he apologize, but he also helped."}
        ],
        "vocabulary": ["Communication skills", "Interpersonal vocabulary", "Conflict resolution"],
        "writing": "What makes communication effective is not just what you say, but how you say it. It is body language that often conveys more than words. Not only should we listen carefully, but we should also try to understand the other person's perspective."
    },
    {
        "unit_number": 38,
        "title": "Business and Entrepreneurship",
        "level": "B2",
        "description": "Negocios, emprendimiento y mundo empresarial",
        "topics": [
            {"title": "Starting a Business", "description": "Business plan, funding, marketing"},
            {"title": "Corporate World", "description": "Meetings, presentations, negotiations"},
            {"title": "Leadership", "description": "Management styles, motivation, decision-making"}
        ],
        "grammar": [
            {"topic": "Future Perfect", "rule": "By 2025, we will have expanded globally."},
            {"topic": "Future Continuous", "rule": "This time next year, we'll be launching the product."},
            {"topic": "Formal Language", "rule": "Would you be so kind as to... / I would be grateful if..."}
        ],
        "vocabulary": ["Business terminology", "Entrepreneurship", "Corporate vocabulary"],
        "writing": "By the end of this year, we will have launched our new product line. This time next month, we'll be negotiating with potential investors. I would be grateful if you could review the business proposal at your earliest convenience."
    },
    {
        "unit_number": 39,
        "title": "Psychology and Behavior",
        "level": "B2",
        "description": "Psicología, comportamiento humano y mente",
        "topics": [
            {"title": "Human Behavior", "description": "Motivation, habits, personality"},
            {"title": "Cognitive Psychology", "description": "Memory, perception, decision-making"},
            {"title": "Social Influence", "description": "Peer pressure, conformity, persuasion"}
        ],
        "grammar": [
            {"topic": "Participle Clauses", "rule": "Having studied the subject, I understand it better."},
            {"topic": "Reduced Relative Clauses", "rule": "The theory proposed by Freud... (that was proposed)"},
            {"topic": "Abstract Noun Clauses", "rule": "The fact that humans are social..."}
        ],
        "vocabulary": ["Psychology terms", "Behavior vocabulary", "Cognitive vocabulary"],
        "writing": "Having researched human behavior extensively, psychologists have identified several key factors. The studies conducted by researchers suggest that habits are formed through repetition. The fact that social influence affects our decisions is well documented."
    },
    {
        "unit_number": 40,
        "title": "Environmental Challenges",
        "level": "B2",
        "description": "Desafíos ambientales y sostenibilidad",
        "topics": [
            {"title": "Climate Change", "description": "Global warming, carbon footprint, greenhouse gases"},
            {"title": "Conservation", "description": "Biodiversity, endangered species, ecosystems"},
            {"title": "Sustainable Living", "description": "Renewable energy, zero waste, eco-friendly"}
        ],
        "grammar": [
            {"topic": "Passive Causative", "rule": "We need to have policies changed."},
            {"topic": "Modals of Deduction (Past)", "rule": "The extinction must have been caused by..."},
            {"topic": "Conditionals with Unless/Provided that", "rule": "Unless we act, provided that measures are taken..."}
        ],
        "vocabulary": ["Environmental science", "Sustainability", "Climate vocabulary"],
        "writing": "Unless drastic measures are taken immediately, climate change will continue to accelerate. The damage caused to ecosystems must have been accumulating for decades. We need to have our policies revised and have renewable energy sources implemented on a larger scale."
    },
    {
        "unit_number": 41,
        "title": "Digital Age",
        "level": "B2",
        "description": "Era digital, tecnología e impacto social",
        "topics": [
            {"title": "Social Media Impact", "description": "Influence, privacy, mental health effects"},
            {"title": "Artificial Intelligence", "description": "Automation, ethics, future implications"},
            {"title": "Digital Literacy", "description": "Critical thinking, online safety, information verification"}
        ],
        "grammar": [
            {"topic": "Wish + Past Perfect", "rule": "I wish I had been more careful with my data."},
            {"topic": "Would rather + Perfect", "rule": "I'd rather have studied tech earlier."},
            {"topic": "Subjunctive (Formal)", "rule": "It is essential that users be aware of risks."}
        ],
        "vocabulary": ["Digital technology", "AI terminology", "Cyber vocabulary"],
        "writing": "I wish I had paid more attention to privacy settings earlier. It is essential that all users be educated about online safety. I would rather have grown up with less screen time, but now I need to adapt to the digital world."
    },
    {
        "unit_number": 42,
        "title": "Ethics and Values",
        "level": "B2",
        "description": "Ética, valores morales y dilemas",
        "topics": [
            {"title": "Ethical Dilemmas", "description": "Right vs wrong, moral choices, consequences"},
            {"title": "Personal Values", "description": "Integrity, honesty, respect, fairness"},
            {"title": "Social Responsibility", "description": "Corporate ethics, individual duty, community"}
        ],
        "grammar": [
            {"topic": "Hypothetical Past", "rule": "Had I known the consequences, I would have acted differently."},
            {"topic": "Subjunctive (Wish/Demand)", "rule": "They demanded that he resign."},
            {"topic": "Whether...or", "rule": "Whether we agree or not, ethics matter."}
        ],
        "vocabulary": ["Ethics vocabulary", "Values and principles", "Moral vocabulary"],
        "writing": "Had I been in that situation, I would have made a different choice. Whether people agree or not, ethical considerations should guide our decisions. Many demanded that the company take responsibility for its actions."
    },
    {
        "unit_number": 43,
        "title": "Literature and Writing",
        "level": "B2",
        "description": "Literatura, escritura creativa y análisis literario",
        "topics": [
            {"title": "Literary Analysis", "description": "Themes, symbolism, narrative techniques"},
            {"title": "Writing Styles", "description": "Descriptive, narrative, persuasive, expository"},
            {"title": "Famous Authors", "description": "Classic and contemporary literature"}
        ],
        "grammar": [
            {"topic": "Narrative Tenses Review", "rule": "Past simple, continuous, perfect in stories"},
            {"topic": "Reported Thought", "rule": "She wondered whether... / He realized that..."},
            {"topic": "Literary Present", "rule": "Shakespeare writes about... (for analysis)"}
        ],
        "vocabulary": ["Literary terms", "Writing vocabulary", "Analysis expressions"],
        "writing": "Shakespeare writes about universal themes that remain relevant today. In this novel, the author uses symbolism to convey deeper meanings. The protagonist wondered whether she had made the right choice, as she realized that her actions had consequences."
    },
    {
        "unit_number": 44,
        "title": "Travel and Cultural Exchange",
        "level": "B2",
        "description": "Viajes culturales, inmersión e intercambio",
        "topics": [
            {"title": "Cultural Immersion", "description": "Living abroad, adapting, culture shock"},
            {"title": "Travel Experiences", "description": "Adventure travel, off-the-beaten-path, authentic experiences"},
            {"title": "Global Citizenship", "description": "Cultural awareness, tolerance, respect"}
        ],
        "grammar": [
            {"topic": "Mixed Conditionals (Advanced)", "rule": "If I had learned the language, I would feel more at home now."},
            {"topic": "Inversions (Had/Should/Were)", "rule": "Had I known... / Should you need... / Were I to..."},
            {"topic": "Expressing Regret", "rule": "I regret not having traveled more."}
        ],
        "vocabulary": ["Travel experiences", "Cultural adaptation", "Global citizenship"],
        "writing": "Had I taken the time to learn the local language before moving, I would feel more integrated now. Should you ever decide to live abroad, I would recommend immersing yourself in the culture. I regret not having traveled more in my twenties."
    },
    {
        "unit_number": 45,
        "title": "Innovation and Progress",
        "level": "B2",
        "description": "Innovación, progreso tecnológico y futuro",
        "topics": [
            {"title": "Technological Innovation", "description": "Inventions, disruption, progress"},
            {"title": "Future of Work", "description": "Automation, remote work, new skills"},
            {"title": "Scientific Breakthroughs", "description": "Medical advances, space exploration, biotech"}
        ],
        "grammar": [
            {"topic": "Future in the Past", "rule": "We thought AI would transform... (and it did)"},
            {"topic": "Speculating about Future", "rule": "It's likely/probable that... / There's a good chance..."},
            {"topic": "Be + to + Infinitive", "rule": "The conference is to be held... / This is to change..."}
        ],
        "vocabulary": ["Innovation terms", "Future of work", "Scientific progress"],
        "writing": "Scientists predicted that gene therapy would revolutionize medicine, and it has begun to do so. It's likely that within the next decade, autonomous vehicles will become mainstream. The technology is to transform our daily lives in ways we cannot yet imagine."
    },
    {
        "unit_number": 46,
        "title": "Politics and Society",
        "level": "B2",
        "description": "Política, sociedad y participación ciudadana",
        "topics": [
            {"title": "Political Systems", "description": "Democracy, elections, government"},
            {"title": "Social Issues", "description": "Inequality, discrimination, human rights"},
            {"title": "Civic Participation", "description": "Voting, activism, community engagement"}
        ],
        "grammar": [
            {"topic": "Hedging Language", "rule": "It could be argued that... / It seems that..."},
            {"topic": "Distancing Language", "rule": "It is said that... / According to some..."},
            {"topic": "Concession", "rule": "Although/While/Despite the fact that..."}
        ],
        "vocabulary": ["Political vocabulary", "Social issues", "Civic terms"],
        "writing": "Although democracy is considered the fairest system, it could be argued that it has its limitations. Despite the fact that progress has been made, inequality remains a significant issue. According to recent studies, civic participation among young people is increasing."
    },
    {
        "unit_number": 47,
        "title": "Personal Development",
        "level": "B2",
        "description": "Desarrollo personal, autoconocimiento y crecimiento",
        "topics": [
            {"title": "Self-Improvement", "description": "Goals, habits, mindset, resilience"},
            {"title": "Emotional Intelligence", "description": "Self-awareness, empathy, self-regulation"},
            {"title": "Life Skills", "description": "Critical thinking, problem-solving, adaptability"}
        ],
        "grammar": [
            {"topic": "Verb + Object + Infinitive/Gerund", "rule": "I encouraged him to continue. I saw her leaving."},
            {"topic": "Complex Sentence Structures", "rule": "The more you practice, the better you become."},
            {"topic": "Linking Expressions", "rule": "In addition to / Apart from / Not to mention"}
        ],
        "vocabulary": ["Personal development", "Emotional intelligence", "Life skills"],
        "writing": "The more I work on self-awareness, the better I understand my reactions. In addition to setting clear goals, I have learned to embrace failure as part of growth. I encourage everyone to invest time in personal development, not to mention the importance of emotional intelligence."
    },
    {
        "unit_number": 48,
        "title": "Media and Influence",
        "level": "B2",
        "description": "Medios, influencia y pensamiento crítico",
        "topics": [
            {"title": "Media Literacy", "description": "Critical analysis, bias detection, source evaluation"},
            {"title": "Advertising", "description": "Persuasion techniques, consumer behavior"},
            {"title": "Public Opinion", "description": "Propaganda, manipulation, informed citizenship"}
        ],
        "grammar": [
            {"topic": "Passive Reporting Structures", "rule": "It is believed/thought/said that..."},
            {"topic": "Impersonal Report Structures", "rule": "He is said to be... / They are reported to have..."},
            {"topic": "Emphasis and Focus", "rule": "What the media fails to mention is..."}
        ],
        "vocabulary": ["Media literacy", "Advertising terms", "Critical thinking vocabulary"],
        "writing": "It is widely believed that social media influences public opinion significantly. Advertisers are known to use psychological techniques to persuade consumers. What critical viewers need to understand is that all media has some level of bias."
    },
]

# ============================================================================
# NIVEL C1 - ADVANCED (Unidades 49-60)
# ============================================================================
C1_UNITS = [
    {
        "unit_number": 49,
        "title": "Academic Writing",
        "level": "C1",
        "description": "Escritura académica y argumentación formal",
        "topics": [
            {"title": "Essay Structure", "description": "Thesis, arguments, evidence, conclusion"},
            {"title": "Citation and Sources", "description": "Referencing, paraphrasing, avoiding plagiarism"},
            {"title": "Critical Analysis", "description": "Evaluating arguments, identifying weaknesses"}
        ],
        "grammar": [
            {"topic": "Nominalization", "rule": "The development of... / The implementation of..."},
            {"topic": "Hedging in Academic Writing", "rule": "It appears that... / Evidence suggests..."},
            {"topic": "Complex Passive Structures", "rule": "Having been analyzed... / It remains to be seen..."}
        ],
        "vocabulary": ["Academic vocabulary", "Research terms", "Argumentation"],
        "writing": "The implementation of new policies has led to significant changes in the sector. Having been analyzed thoroughly, the data suggests that there is a correlation between the variables. It remains to be seen whether these findings can be replicated in different contexts."
    },
    {
        "unit_number": 50,
        "title": "Philosophy and Thought",
        "level": "C1",
        "description": "Filosofía, pensamiento crítico y debate intelectual",
        "topics": [
            {"title": "Philosophical Concepts", "description": "Ethics, existence, knowledge, reality"},
            {"title": "Critical Thinking", "description": "Logic, fallacies, reasoning"},
            {"title": "Intellectual Debate", "description": "Argumentation, counterarguments, synthesis"}
        ],
        "grammar": [
            {"topic": "Conditional Inversion", "rule": "Were one to consider... / Had it not been for..."},
            {"topic": "Subjunctive (Formal/Literary)", "rule": "Be that as it may... / Lest we forget..."},
            {"topic": "Abstract Constructions", "rule": "The notion that... / The extent to which..."}
        ],
        "vocabulary": ["Philosophical terms", "Logic vocabulary", "Abstract concepts"],
        "writing": "Were one to examine the philosophical implications of this theory, one would find profound questions about human existence. Be that as it may, the extent to which these ideas apply to everyday life remains debatable."
    },
    {
        "unit_number": 51,
        "title": "Global Economics",
        "level": "C1",
        "description": "Economía global, mercados y finanzas internacionales",
        "topics": [
            {"title": "Macroeconomics", "description": "GDP, inflation, monetary policy, fiscal policy"},
            {"title": "International Trade", "description": "Globalization, tariffs, trade agreements"},
            {"title": "Financial Markets", "description": "Stock market, investments, risk management"}
        ],
        "grammar": [
            {"topic": "Complex Conditionals", "rule": "If it were not for... / Were the situation to deteriorate..."},
            {"topic": "Qualifying Statements", "rule": "To a certain extent... / With some reservations..."},
            {"topic": "Cause and Effect (Formal)", "rule": "This has resulted in... / Consequently..."}
        ],
        "vocabulary": ["Economic terminology", "Financial terms", "Trade vocabulary"],
        "writing": "Were the central bank to raise interest rates, it would likely result in reduced consumer spending. To a certain extent, globalization has benefited developing economies; however, with some reservations, one must acknowledge the widening wealth gap."
    },
    {
        "unit_number": 52,
        "title": "Legal Systems",
        "level": "C1",
        "description": "Sistemas legales, derechos y jurisprudencia",
        "topics": [
            {"title": "Legal Concepts", "description": "Common law, civil law, constitutional rights"},
            {"title": "International Law", "description": "Treaties, human rights, international courts"},
            {"title": "Legal Proceedings", "description": "Trials, appeals, verdicts, precedents"}
        ],
        "grammar": [
            {"topic": "Legal English Structures", "rule": "Notwithstanding... / In accordance with..."},
            {"topic": "Formal Conditionals", "rule": "Should the defendant be found guilty..."},
            {"topic": "Passive Voice (Formal)", "rule": "The verdict was delivered... / Justice shall be served..."}
        ],
        "vocabulary": ["Legal terminology", "Court vocabulary", "Human rights terms"],
        "writing": "Should the defendant be found guilty, they shall be sentenced in accordance with the applicable statutes. Notwithstanding the arguments presented by the defense, the evidence clearly demonstrates that the law was violated."
    },
    {
        "unit_number": 53,
        "title": "Scientific Research",
        "level": "C1",
        "description": "Investigación científica, metodología y publicación",
        "topics": [
            {"title": "Research Methodology", "description": "Qualitative, quantitative, mixed methods"},
            {"title": "Data Analysis", "description": "Statistics, interpretation, limitations"},
            {"title": "Academic Publishing", "description": "Peer review, journals, conferences"}
        ],
        "grammar": [
            {"topic": "Scientific Passive", "rule": "It was observed that... / Subjects were randomly assigned..."},
            {"topic": "Reporting Research", "rule": "The study found/revealed/demonstrated that..."},
            {"topic": "Hypothetical Scientific Language", "rule": "One might hypothesize that... / It could be posited that..."}
        ],
        "vocabulary": ["Research methodology", "Statistical terms", "Academic publishing"],
        "writing": "The subjects were randomly assigned to either the control or experimental group. It was observed that participants in the treatment condition demonstrated significantly higher scores. One might hypothesize that this effect would be replicated across different demographics."
    },
    {
        "unit_number": 54,
        "title": "Art and Aesthetics",
        "level": "C1",
        "description": "Arte, estética y crítica artística",
        "topics": [
            {"title": "Art Movements", "description": "Impressionism, modernism, contemporary art"},
            {"title": "Aesthetic Theory", "description": "Beauty, meaning, interpretation"},
            {"title": "Art Criticism", "description": "Analysis, evaluation, context"}
        ],
        "grammar": [
            {"topic": "Descriptive Elaboration", "rule": "The painting, characterized by bold strokes..."},
            {"topic": "Appositives", "rule": "Picasso, a pioneer of Cubism, revolutionized..."},
            {"topic": "Relative Clauses (Reduced)", "rule": "The technique employed here... / Works created during this period..."}
        ],
        "vocabulary": ["Art history", "Aesthetic vocabulary", "Critical analysis terms"],
        "writing": "Monet, widely regarded as the father of Impressionism, sought to capture the fleeting effects of light. The technique employed in this piece, characterized by visible brushstrokes and vibrant colors, represents a departure from academic traditions."
    },
    {
        "unit_number": 55,
        "title": "Linguistics and Language",
        "level": "C1",
        "description": "Lingüística, adquisición del lenguaje y sociolingüística",
        "topics": [
            {"title": "Language Acquisition", "description": "First and second language learning, critical period"},
            {"title": "Sociolinguistics", "description": "Dialects, language change, identity"},
            {"title": "Applied Linguistics", "description": "Teaching methods, language policy, translation"}
        ],
        "grammar": [
            {"topic": "Metalinguistic Awareness", "rule": "The term 'X' refers to... / What is meant by..."},
            {"topic": "Citing Theories", "rule": "According to Chomsky... / As Saussure posited..."},
            {"topic": "Discussing Language", "rule": "The use of the subjunctive indicates..."}
        ],
        "vocabulary": ["Linguistics terminology", "Language acquisition", "Sociolinguistic terms"],
        "writing": "According to Chomsky's theory of Universal Grammar, humans are born with an innate capacity for language. What is meant by 'critical period' refers to the age window during which language acquisition occurs most naturally."
    },
    {
        "unit_number": 56,
        "title": "Medical Ethics",
        "level": "C1",
        "description": "Ética médica, bioética y dilemas de salud",
        "topics": [
            {"title": "Bioethics", "description": "Informed consent, patient autonomy, confidentiality"},
            {"title": "Medical Dilemmas", "description": "End-of-life care, genetic testing, organ donation"},
            {"title": "Healthcare Policy", "description": "Access, allocation, public health ethics"}
        ],
        "grammar": [
            {"topic": "Expressing Obligation/Prohibition", "rule": "Physicians are bound to... / It is incumbent upon..."},
            {"topic": "Ethical Conditionals", "rule": "Were a physician to breach confidentiality..."},
            {"topic": "Formal Argumentation", "rule": "It could be contended that... / One might argue..."}
        ],
        "vocabulary": ["Medical ethics", "Bioethics terms", "Healthcare policy"],
        "writing": "It is incumbent upon healthcare providers to respect patient autonomy. Were a physician to disclose confidential information without consent, they would be in violation of ethical standards. One might argue that in certain circumstances, the greater good justifies such disclosure."
    },
    {
        "unit_number": 57,
        "title": "Architecture and Design",
        "level": "C1",
        "description": "Arquitectura, diseño y urbanismo",
        "topics": [
            {"title": "Architectural Styles", "description": "Classical, modern, postmodern, sustainable"},
            {"title": "Urban Planning", "description": "City design, public spaces, infrastructure"},
            {"title": "Design Principles", "description": "Form, function, aesthetics, user experience"}
        ],
        "grammar": [
            {"topic": "Technical Description", "rule": "The structure, designed to withstand... / Featuring X..."},
            {"topic": "Passive for Processes", "rule": "The building was constructed using... / Materials are sourced from..."},
            {"topic": "Purpose Clauses", "rule": "In order that... / So as to... / With a view to..."}
        ],
        "vocabulary": ["Architectural terms", "Design vocabulary", "Urban planning"],
        "writing": "The structure, designed to withstand seismic activity, features an innovative foundation system. Sustainable materials are sourced locally with a view to reducing the carbon footprint. The building was constructed using modular techniques so as to minimize waste."
    },
    {
        "unit_number": 58,
        "title": "Diplomacy and Relations",
        "level": "C1",
        "description": "Diplomacia, relaciones internacionales y negociación",
        "topics": [
            {"title": "International Relations", "description": "Alliances, conflicts, negotiations"},
            {"title": "Diplomatic Language", "description": "Formal communication, protocols, etiquette"},
            {"title": "Conflict Resolution", "description": "Mediation, treaties, peacekeeping"}
        ],
        "grammar": [
            {"topic": "Diplomatic Language", "rule": "We would urge... / It is with regret that..."},
            {"topic": "Formal Subjunctive", "rule": "We recommend that the committee convene..."},
            {"topic": "Diplomatic Hedging", "rule": "It would appear that... / There may be scope for..."}
        ],
        "vocabulary": ["Diplomatic terms", "International relations", "Negotiation vocabulary"],
        "writing": "We would urge all parties to exercise restraint during this sensitive period. It would appear that there may be scope for dialogue. We recommend that the committee convene at the earliest opportunity to address these concerns."
    },
    {
        "unit_number": 59,
        "title": "Environmental Science",
        "level": "C1",
        "description": "Ciencia ambiental, ecología y conservación",
        "topics": [
            {"title": "Ecology", "description": "Ecosystems, biodiversity, food chains"},
            {"title": "Climate Science", "description": "Climate models, projections, mitigation"},
            {"title": "Conservation Biology", "description": "Species protection, habitat restoration, rewilding"}
        ],
        "grammar": [
            {"topic": "Scientific Predictions", "rule": "Models project that... / It is anticipated that..."},
            {"topic": "Discussing Cause/Effect", "rule": "This can be attributed to... / This results in..."},
            {"topic": "Expressing Uncertainty", "rule": "It is not yet clear whether... / The extent to which X affects Y..."}
        ],
        "vocabulary": ["Environmental science", "Ecology terms", "Climate vocabulary"],
        "writing": "Models project that average global temperatures will rise by 2°C by 2050. This can be attributed to increased greenhouse gas emissions. It is not yet clear whether current mitigation efforts will be sufficient to prevent the most severe impacts."
    },
    {
        "unit_number": 60,
        "title": "Advanced Argumentation",
        "level": "C1",
        "description": "Argumentación avanzada, debate y retórica",
        "topics": [
            {"title": "Building Arguments", "description": "Claims, evidence, warrants, rebuttals"},
            {"title": "Rhetorical Strategies", "description": "Ethos, pathos, logos, appeals"},
            {"title": "Debate Skills", "description": "Cross-examination, refutation, synthesis"}
        ],
        "grammar": [
            {"topic": "Concessive Structures", "rule": "While it may be true that... / Granted that..."},
            {"topic": "Strengthening Arguments", "rule": "It is indisputable that... / The evidence overwhelmingly suggests..."},
            {"topic": "Countering Arguments", "rule": "This argument fails to account for... / On the contrary..."}
        ],
        "vocabulary": ["Argumentation", "Rhetorical terms", "Debate vocabulary"],
        "writing": "While it may be true that technological advancement brings certain risks, the evidence overwhelmingly suggests that the benefits outweigh the drawbacks. This argument fails to account for the significant improvements in quality of life that technology has enabled."
    },
]

# ============================================================================
# NIVEL C2 - MASTERY (Unidades 61-72)
# ============================================================================
C2_UNITS = [
    {
        "unit_number": 61,
        "title": "Nuance and Subtlety",
        "level": "C2",
        "description": "Matices del lenguaje, sutilezas y registro",
        "topics": [
            {"title": "Register and Tone", "description": "Formal, informal, ironic, humorous"},
            {"title": "Connotation", "description": "Word choice, implied meaning, emotional impact"},
            {"title": "Idiomatic Mastery", "description": "Fixed expressions, collocations, native-like usage"}
        ],
        "grammar": [
            {"topic": "Subtle Modal Distinctions", "rule": "might vs may, should vs ought to, nuanced will"},
            {"topic": "Pragmatic Particles", "rule": "Well, you see, actually, as it were"},
            {"topic": "Ellipsis and Substitution", "rule": "If so... / If not... / Do so..."}
        ],
        "vocabulary": ["Nuanced vocabulary", "Idiomatic expressions", "Register markers"],
        "writing": "One might, as it were, suggest that the distinction between these terms is rather more subtle than it initially appears. Well, you see, language is not merely a matter of grammar but of understanding what is implied rather than stated."
    },
    {
        "unit_number": 62,
        "title": "Literary Analysis",
        "level": "C2",
        "description": "Análisis literario profundo y crítica",
        "topics": [
            {"title": "Literary Devices", "description": "Allegory, irony, symbolism, stream of consciousness"},
            {"title": "Critical Theory", "description": "Feminist, postcolonial, psychoanalytic approaches"},
            {"title": "Textual Analysis", "description": "Close reading, interpretation, intertextuality"}
        ],
        "grammar": [
            {"topic": "Complex Relative Structures", "rule": "That which we call... / The extent to which..."},
            {"topic": "Inversion for Style", "rule": "Rarely does one encounter... / Never before had..."},
            {"topic": "Periodic Sentences", "rule": "After years of struggle, countless setbacks, and... he finally..."}
        ],
        "vocabulary": ["Literary criticism", "Critical theory terms", "Analytical vocabulary"],
        "writing": "Rarely does one encounter a work so rich in allegorical meaning. That which Conrad portrays on the surface—a journey into Africa—reveals, upon closer examination, a psychological descent into the human psyche itself."
    },
    {
        "unit_number": 63,
        "title": "Sociolinguistic Variation",
        "level": "C2",
        "description": "Variación sociolingüística, dialectos y cambio lingüístico",
        "topics": [
            {"title": "Language Variation", "description": "Regional, social, and stylistic variation"},
            {"title": "Language and Identity", "description": "Code-switching, language attitudes, prestige"},
            {"title": "Language Change", "description": "Historical development, neologisms, language death"}
        ],
        "grammar": [
            {"topic": "Dialectal Features", "rule": "Understanding and recognizing non-standard forms"},
            {"topic": "Historical Grammar", "rule": "Archaic forms: thee, thou, wherefore, hitherto"},
            {"topic": "Code-switching Patterns", "rule": "Intra-sentential, inter-sentential switches"}
        ],
        "vocabulary": ["Sociolinguistics", "Dialectology", "Language variation"],
        "writing": "The extent to which speakers code-switch varies considerably according to social context. Hitherto, linguists had focused primarily on structural aspects; nowadays, the social dimensions of language are recognized as equally significant."
    },
    {
        "unit_number": 64,
        "title": "Philosophical Discourse",
        "level": "C2",
        "description": "Discurso filosófico y análisis conceptual",
        "topics": [
            {"title": "Epistemology", "description": "Knowledge, truth, belief, justification"},
            {"title": "Ontology", "description": "Being, existence, reality, essence"},
            {"title": "Phenomenology", "description": "Consciousness, experience, perception"}
        ],
        "grammar": [
            {"topic": "Abstract Nominalization", "rule": "The beingness of... / The very act of perceiving..."},
            {"topic": "Philosophical Conditionals", "rule": "Were existence to precede essence..."},
            {"topic": "Qualifying Complexity", "rule": "Insofar as... / Qua... / As such..."}
        ],
        "vocabulary": ["Philosophical terminology", "Epistemology", "Ontology"],
        "writing": "Insofar as consciousness constitutes the very foundation of our experience, one cannot speak of reality qua reality without acknowledging the subjective dimension. Were existence to precede essence, as Sartre contended, then we would be, as such, condemned to freedom."
    },
    {
        "unit_number": 65,
        "title": "Advanced Translation",
        "level": "C2",
        "description": "Traducción avanzada, equivalencia y adaptación cultural",
        "topics": [
            {"title": "Translation Theory", "description": "Equivalence, fidelity, domestication, foreignization"},
            {"title": "Cultural Adaptation", "description": "Localization, transcreation, cultural references"},
            {"title": "Specialized Translation", "description": "Literary, legal, medical, technical"}
        ],
        "grammar": [
            {"topic": "Untranslatable Structures", "rule": "Understanding culturally-bound expressions"},
            {"topic": "Preserving Style", "rule": "Maintaining register, tone, and voice across languages"},
            {"topic": "Compensatory Techniques", "rule": "Dealing with linguistic asymmetries"}
        ],
        "vocabulary": ["Translation studies", "Localization", "Equivalence types"],
        "writing": "The challenge facing the translator lies not merely in converting words but in conveying meaning across cultural boundaries. Insofar as certain expressions resist direct translation, compensatory strategies must be employed to preserve the author's intended effect."
    },
    {
        "unit_number": 66,
        "title": "Rhetoric and Persuasion",
        "level": "C2",
        "description": "Retórica, persuasión y discurso público",
        "topics": [
            {"title": "Classical Rhetoric", "description": "Aristotelian appeals, arrangement, style"},
            {"title": "Modern Persuasion", "description": "Media influence, propaganda, advertising"},
            {"title": "Political Discourse", "description": "Speeches, debates, public communication"}
        ],
        "grammar": [
            {"topic": "Rhetorical Devices", "rule": "Anaphora, antithesis, chiasmus, tricolon"},
            {"topic": "Emotional Appeal", "rule": "Evocative language, imagery, narrative"},
            {"topic": "Logical Structure", "rule": "Syllogistic reasoning, enthymemes, rebuttals"}
        ],
        "vocabulary": ["Rhetorical terms", "Persuasion techniques", "Political discourse"],
        "writing": "Not through force, but through reason; not through imposition, but through inspiration; not through fear, but through hope—this is how lasting change is achieved. The greatest orators understood that to move the heart, one must first engage the mind."
    },
    {
        "unit_number": 67,
        "title": "Cognitive Science",
        "level": "C2",
        "description": "Ciencia cognitiva, mente y procesamiento",
        "topics": [
            {"title": "Cognitive Processes", "description": "Attention, memory, reasoning, decision-making"},
            {"title": "Neuroscience", "description": "Brain structures, neural pathways, plasticity"},
            {"title": "Artificial Cognition", "description": "AI, machine learning, cognitive modeling"}
        ],
        "grammar": [
            {"topic": "Scientific Precision", "rule": "Operationalizing concepts, defining variables"},
            {"topic": "Hypothesis Formation", "rule": "If X, then Y; controlling for Z..."},
            {"topic": "Reporting Findings", "rule": "The data indicate... / Results suggest..."}
        ],
        "vocabulary": ["Cognitive science", "Neuroscience terms", "AI vocabulary"],
        "writing": "The data indicate that working memory capacity, controlling for individual differences in attention, significantly predicts performance on complex reasoning tasks. These findings suggest that cognitive resources are allocated in a hierarchical manner."
    },
    {
        "unit_number": 68,
        "title": "Ethics in Practice",
        "level": "C2",
        "description": "Ética aplicada, casos complejos y toma de decisiones",
        "topics": [
            {"title": "Applied Ethics", "description": "Business ethics, professional ethics, environmental ethics"},
            {"title": "Ethical Frameworks", "description": "Utilitarianism, deontology, virtue ethics"},
            {"title": "Case Studies", "description": "Complex scenarios, stakeholder analysis, moral reasoning"}
        ],
        "grammar": [
            {"topic": "Hypothetical Scenarios", "rule": "Were one to find oneself in such a situation..."},
            {"topic": "Moral Language", "rule": "One is morally obligated to... / It is incumbent upon..."},
            {"topic": "Balancing Considerations", "rule": "On the one hand... on the other... ultimately..."}
        ],
        "vocabulary": ["Applied ethics", "Moral philosophy", "Professional ethics"],
        "writing": "Were one to find oneself in a position where truth-telling would cause significant harm, would one be morally obligated to lie? On the one hand, deontological ethics would suggest that honesty is a categorical imperative; on the other, consequentialist reasoning would weigh the outcomes."
    },
    {
        "unit_number": 69,
        "title": "Discourse Analysis",
        "level": "C2",
        "description": "Análisis del discurso, pragmática y comunicación",
        "topics": [
            {"title": "Pragmatics", "description": "Speech acts, implicature, presupposition"},
            {"title": "Critical Discourse Analysis", "description": "Power, ideology, social practices"},
            {"title": "Conversation Analysis", "description": "Turn-taking, repair, adjacency pairs"}
        ],
        "grammar": [
            {"topic": "Speech Act Theory", "rule": "Performative utterances, illocutionary force"},
            {"topic": "Implicature", "rule": "What is said vs. what is meant"},
            {"topic": "Discourse Markers", "rule": "Function in organizing and signaling discourse"}
        ],
        "vocabulary": ["Discourse analysis", "Pragmatics", "Conversation analysis"],
        "writing": "The utterance 'It's cold in here' functions not merely as a statement of temperature but as an indirect request—an illocutionary act with perlocutionary intent. What is implicated far exceeds what is stated explicitly."
    },
    {
        "unit_number": 70,
        "title": "Academic Discourse",
        "level": "C2",
        "description": "Discurso académico, convenciones y géneros",
        "topics": [
            {"title": "Academic Genres", "description": "Research articles, dissertations, reviews"},
            {"title": "Academic Conventions", "description": "Structure, citation, argumentation"},
            {"title": "Scholarly Debate", "description": "Responding to criticism, building on others' work"}
        ],
        "grammar": [
            {"topic": "Citation Integration", "rule": "Smith (2020) argues that... / As noted by Smith (2020)..."},
            {"topic": "Positioning the Author", "rule": "This study contributes to... / We depart from..."},
            {"topic": "Metadiscourse", "rule": "As will be shown... / This section explores..."}
        ],
        "vocabulary": ["Academic writing", "Scholarly discourse", "Research vocabulary"],
        "writing": "This study contributes to the growing body of literature on X by examining Y. As will be shown in the following sections, our findings challenge the conventional understanding of Z. We depart from previous research in our theoretical framing."
    },
    {
        "unit_number": 71,
        "title": "Cross-Cultural Communication",
        "level": "C2",
        "description": "Comunicación intercultural, negociación y malentendidos",
        "topics": [
            {"title": "Cultural Dimensions", "description": "Hofstede's dimensions, high/low context cultures"},
            {"title": "Intercultural Competence", "description": "Awareness, sensitivity, adaptability"},
            {"title": "Misunderstandings", "description": "Sources of confusion, repair strategies"}
        ],
        "grammar": [
            {"topic": "Cultural Hedging", "rule": "In my culture... / Where I come from..."},
            {"topic": "Clarification Strategies", "rule": "What I mean by that is... / Let me put it another way..."},
            {"topic": "Diplomatic Reformulation", "rule": "Perhaps what we're trying to say is..."}
        ],
        "vocabulary": ["Intercultural communication", "Cultural dimensions", "Communication strategies"],
        "writing": "In high-context cultures, what remains unsaid often carries as much meaning as explicit statements. Perhaps what we're trying to say is that effective cross-cultural communication requires not only linguistic competence but also cultural intelligence."
    },
    {
        "unit_number": 72,
        "title": "Mastery Integration",
        "level": "C2",
        "description": "Integración de todas las habilidades a nivel de dominio nativo",
        "topics": [
            {"title": "Native-like Fluency", "description": "Spontaneity, naturalness, automaticity"},
            {"title": "Stylistic Range", "description": "Adapting to any context, audience, or purpose"},
            {"title": "Creative Expression", "description": "Wit, wordplay, eloquence, originality"}
        ],
        "grammar": [
            {"topic": "Complete Flexibility", "rule": "Moving seamlessly between styles and registers"},
            {"topic": "Creative Grammar", "rule": "Breaking rules for effect, playing with language"},
            {"topic": "Idiomatic Precision", "rule": "Using the exact right expression for the context"}
        ],
        "vocabulary": ["Full range of vocabulary", "Stylistic choices", "Creative expression"],
        "writing": "Having traversed the full spectrum of linguistic competence—from the tentative first words of a beginner to the nuanced expression of the advanced speaker—one arrives at a point where language is no longer a tool but an extension of thought itself."
    },
]

def seed_units():
    """Seed all CEFR level units to the database"""
    with app.app_context():
        # Count existing units
        existing = Unit.query.count()
        print(f"📊 Unidades existentes: {existing}")
        
        if existing > 0:
            print("¿Desea eliminar las unidades existentes y crear las nuevas? (s/n)")
            response = input().strip().lower()
            if response != 's':
                print("❌ Operación cancelada.")
                return
            
            # Delete all related data using TRUNCATE CASCADE
            db.session.execute(db.text("TRUNCATE TABLE units CASCADE"))
            db.session.commit()
            print("🗑️ Datos anteriores eliminados.")
        
        # Combine all levels
        all_units = A1_UNITS + A2_UNITS + B1_UNITS + B2_UNITS + C1_UNITS + C2_UNITS
        
        unit_count = 0
        topic_count = 0
        grammar_count = 0
        vocab_count = 0
        writing_count = 0
        
        for unit_data in all_units:
            # Create Unit
            unit = Unit(
                unit_number=unit_data["unit_number"],
                title=f"{unit_data['level']} - Unit {unit_data['unit_number']}: {unit_data['title']}",
                description=unit_data["description"],
                learning_objectives=[f"Nivel {unit_data['level']}", unit_data["description"]]
            )
            db.session.add(unit)
            db.session.flush()  # Get the ID
            unit_count += 1
            
            # Create Topics
            for i, topic_data in enumerate(unit_data.get("topics", [])):
                topic = Topic(
                    unit_id=unit.id,
                    title=topic_data["title"],
                    description=topic_data["description"],
                    order=i
                )
                db.session.add(topic)
                topic_count += 1
            
            # Create Grammar Rules
            for grammar_data in unit_data.get("grammar", []):
                grammar = GrammarRule(
                    unit_id=unit.id,
                    topic=grammar_data["topic"],
                    rule=grammar_data["rule"],
                    examples=[]
                )
                db.session.add(grammar)
                grammar_count += 1
            
            # Create Vocabulary Categories
            for vocab_name in unit_data.get("vocabulary", []):
                vocab_cat = VocabularyCategory(
                    unit_id=unit.id,
                    category_name=vocab_name
                )
                db.session.add(vocab_cat)
                vocab_count += 1
            
            # Create Writing Practice
            if unit_data.get("writing"):
                writing = WritingPractice(
                    unit_id=unit.id,
                    title=f"Writing Practice - {unit_data['title']}",
                    instructions=f"Practice writing about {unit_data['title']}. Use the grammar and vocabulary from this unit.",
                    example_text=unit_data["writing"],
                    difficulty=unit_data["level"].lower() if unit_data["level"] in ["A1", "A2"] else "intermediate"
                )
                db.session.add(writing)
                writing_count += 1
        
        db.session.commit()
        
        print("\n" + "="*50)
        print("✅ SEED COMPLETADO EXITOSAMENTE")
        print("="*50)
        print(f"📚 Unidades creadas: {unit_count}")
        print(f"   • A1 (Beginner): 12 unidades")
        print(f"   • A2 (Elementary): 12 unidades")
        print(f"   • B1 (Intermediate): 12 unidades")
        print(f"   • B2 (Upper-Intermediate): 12 unidades")
        print(f"   • C1 (Advanced): 12 unidades")
        print(f"   • C2 (Mastery): 12 unidades")
        print(f"📖 Temas creados: {topic_count}")
        print(f"📝 Reglas gramaticales: {grammar_count}")
        print(f"📗 Categorías de vocabulario: {vocab_count}")
        print(f"✍️ Ejercicios de escritura: {writing_count}")
        print("="*50)


if __name__ == "__main__":
    seed_units()
