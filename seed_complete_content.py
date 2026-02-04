"""
Script para poblar contenido completo de todas las unidades
============================================================
- 5 lecturas por unidad
- 10+ palabras de vocabulario por unidad
- Flashcards
- Ejercicios de oraciones
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import (
    Unit, Reading, VocabularyCategory, VocabularyItem, 
    Flashcard, SentenceExercise
)
import random

app = create_app()

# ============================================================================
# CONTENIDO POR NIVEL - LECTURAS
# ============================================================================

READINGS_BY_LEVEL = {
    'A1': {
        'word_count': (80, 150),
        'templates': [
            {
                'title': 'My Daily Routine',
                'content': '''Every day I wake up at 7 o'clock. I get out of bed and go to the bathroom. I brush my teeth and wash my face. Then I have breakfast. I usually eat bread with butter and drink coffee.

After breakfast, I get dressed for work. I leave my house at 8:30. I take the bus to work. The bus ride takes about 20 minutes. I arrive at work at 9 o'clock.

I work until 5 o'clock in the afternoon. After work, I go home. I have dinner with my family. We talk about our day. In the evening, I watch TV or read a book. I go to bed at 10 o'clock.''',
                'questions': [
                    {'question': 'What time does the person wake up?', 'answer': '7 o\'clock', 'options': ['6 o\'clock', '7 o\'clock', '8 o\'clock', '9 o\'clock']},
                    {'question': 'How does the person go to work?', 'answer': 'By bus', 'options': ['By car', 'By bus', 'By train', 'On foot']},
                    {'question': 'What does the person do in the evening?', 'answer': 'Watch TV or read', 'options': ['Exercise', 'Work', 'Watch TV or read', 'Sleep']}
                ]
            },
            {
                'title': 'My Family',
                'content': '''I have a wonderful family. There are five people in my family: my father, my mother, my sister, my brother, and me. My father is 45 years old. He is a doctor. He works at a hospital in the city.

My mother is 42 years old. She is a teacher. She teaches English at a school. My sister is 20 years old. She is a student at university. She studies medicine. My brother is 15 years old. He goes to high school.

I am 25 years old. I work at a bank. On weekends, we all have dinner together. We love spending time as a family.''',
                'questions': [
                    {'question': 'How many people are in the family?', 'answer': 'Five', 'options': ['Three', 'Four', 'Five', 'Six']},
                    {'question': 'What is the father\'s job?', 'answer': 'Doctor', 'options': ['Teacher', 'Doctor', 'Engineer', 'Driver']},
                    {'question': 'What does the sister study?', 'answer': 'Medicine', 'options': ['English', 'Law', 'Medicine', 'Business']}
                ]
            },
            {
                'title': 'My Home',
                'content': '''I live in a small apartment in the city. It has two bedrooms, a living room, a kitchen, and a bathroom. The apartment is on the third floor. It is not very big, but it is comfortable.

My bedroom is my favorite room. It has a bed, a desk, and a wardrobe. There is a window with a nice view of the park. I like to sit near the window and read.

The kitchen is small but modern. We have a refrigerator, a stove, and a microwave. There is a small table with four chairs. We eat breakfast there every morning.''',
                'questions': [
                    {'question': 'Where is the apartment located?', 'answer': 'In the city', 'options': ['In the country', 'In the city', 'By the beach', 'In the mountains']},
                    {'question': 'How many bedrooms are there?', 'answer': 'Two', 'options': ['One', 'Two', 'Three', 'Four']},
                    {'question': 'What floor is the apartment on?', 'answer': 'Third floor', 'options': ['First floor', 'Second floor', 'Third floor', 'Fourth floor']}
                ]
            },
            {
                'title': 'At the Supermarket',
                'content': '''Today I go to the supermarket. I need to buy food for the week. I take my shopping list with me. On the list I have: milk, bread, eggs, cheese, fruit, and vegetables.

First, I go to the fruit section. I buy apples, bananas, and oranges. Then I get some vegetables: tomatoes, lettuce, and carrots. Next, I go to the dairy section for milk and cheese.

At the checkout, I pay with my credit card. The total is $45. The cashier gives me a receipt. I put everything in my bags and walk home. Shopping takes about one hour.''',
                'questions': [
                    {'question': 'What does the person take to the supermarket?', 'answer': 'A shopping list', 'options': ['Money', 'A shopping list', 'A friend', 'A car']},
                    {'question': 'How much does the person pay?', 'answer': '$45', 'options': ['$35', '$45', '$55', '$65']},
                    {'question': 'How does the person pay?', 'answer': 'With credit card', 'options': ['With cash', 'With credit card', 'With check', 'With coins']}
                ]
            },
            {
                'title': 'My Best Friend',
                'content': '''My best friend's name is Emma. She is 24 years old. We have been friends for 10 years. We met at school when we were 14.

Emma has long brown hair and green eyes. She is very kind and funny. She always makes me laugh. She works as a nurse at the local hospital. She helps sick people every day.

We meet every weekend. Sometimes we go to the cinema. Sometimes we go shopping or have coffee. She is a very good friend. I am lucky to have her.''',
                'questions': [
                    {'question': 'How long have they been friends?', 'answer': '10 years', 'options': ['5 years', '10 years', '15 years', '20 years']},
                    {'question': 'What is Emma\'s job?', 'answer': 'Nurse', 'options': ['Doctor', 'Teacher', 'Nurse', 'Secretary']},
                    {'question': 'How often do they meet?', 'answer': 'Every weekend', 'options': ['Every day', 'Every weekend', 'Once a month', 'Rarely']}
                ]
            },
            {
                'title': 'The Weather Today',
                'content': '''Today the weather is beautiful. The sun is shining and the sky is blue. It is warm outside. The temperature is 25 degrees Celsius. It is a perfect day to go outside.

In the morning, there were some clouds. But now the sky is clear. There is a gentle breeze. The trees are moving slowly in the wind. Birds are singing in the trees.

I think I will go to the park today. I can have a picnic with my friends. We can play games and enjoy the sunshine. I love sunny days like this.''',
                'questions': [
                    {'question': 'What is the weather like today?', 'answer': 'Sunny and warm', 'options': ['Rainy', 'Sunny and warm', 'Cold', 'Snowy']},
                    {'question': 'What is the temperature?', 'answer': '25 degrees', 'options': ['15 degrees', '20 degrees', '25 degrees', '30 degrees']},
                    {'question': 'What does the person plan to do?', 'answer': 'Go to the park', 'options': ['Stay home', 'Go to work', 'Go to the park', 'Go shopping']}
                ]
            },
            {
                'title': 'My Favorite Food',
                'content': '''My favorite food is pizza. I love pizza with cheese and tomato sauce. Sometimes I add vegetables like mushrooms and peppers. I don't like pizza with anchovies.

I usually eat pizza on Friday nights. My family and I order pizza from the restaurant near our house. They make delicious pizza. The crust is thin and crispy.

Besides pizza, I also like pasta and salads. I try to eat healthy food during the week. But on weekends, I enjoy a nice pizza. Food is one of the best things in life!''',
                'questions': [
                    {'question': 'What is the person\'s favorite food?', 'answer': 'Pizza', 'options': ['Pasta', 'Pizza', 'Salad', 'Soup']},
                    {'question': 'What doesn\'t the person like on pizza?', 'answer': 'Anchovies', 'options': ['Cheese', 'Mushrooms', 'Anchovies', 'Tomatoes']},
                    {'question': 'When does the person usually eat pizza?', 'answer': 'Friday nights', 'options': ['Monday mornings', 'Wednesday afternoons', 'Friday nights', 'Every day']}
                ]
            },
            {
                'title': 'Taking the Bus',
                'content': '''I take the bus to work every day. The bus stop is near my house. I walk for about 5 minutes to get there. The bus comes every 15 minutes.

I usually take the 8:15 bus. It is not very crowded at that time. I find a seat and sit down. The journey takes about 30 minutes. During the ride, I listen to music or read the news on my phone.

The bus drops me near my office. I walk for 2 more minutes to reach the building. Taking the bus is convenient and cheap. I pay $2 for each ride.''',
                'questions': [
                    {'question': 'How long is the walk to the bus stop?', 'answer': '5 minutes', 'options': ['2 minutes', '5 minutes', '10 minutes', '15 minutes']},
                    {'question': 'How long is the bus journey?', 'answer': '30 minutes', 'options': ['15 minutes', '20 minutes', '30 minutes', '45 minutes']},
                    {'question': 'How much is the bus fare?', 'answer': '$2', 'options': ['$1', '$2', '$3', '$5']}
                ]
            }
        ]
    },
    'A2': {
        'word_count': (150, 250),
        'templates': [
            {
                'title': 'My Last Vacation',
                'content': '''Last summer, I went on vacation to Barcelona, Spain. It was my first time visiting Europe. I was very excited about the trip. I traveled with my best friend, and we stayed for two weeks.

We stayed in a small hotel in the city center. The hotel was clean and comfortable. From our room, we could see the famous La Rambla street. Every morning, we had breakfast at a café nearby.

During our trip, we visited many places. We saw the beautiful Sagrada Familia church. It was amazing! We also went to the beach and swam in the Mediterranean Sea. The water was warm and blue.

One day, we took a day trip to Montserrat, a mountain near Barcelona. The views were incredible. We also tried many Spanish dishes. My favorite was paella, a rice dish with seafood.

I loved Barcelona. The people were friendly, and the weather was perfect. I want to go back someday. It was the best vacation of my life.''',
                'questions': [
                    {'question': 'Where did the person go on vacation?', 'answer': 'Barcelona, Spain', 'options': ['Paris, France', 'Barcelona, Spain', 'Rome, Italy', 'London, UK']},
                    {'question': 'How long was the vacation?', 'answer': 'Two weeks', 'options': ['One week', 'Two weeks', 'Three weeks', 'One month']},
                    {'question': 'What was the person\'s favorite food?', 'answer': 'Paella', 'options': ['Pizza', 'Paella', 'Pasta', 'Tacos']}
                ]
            },
            {
                'title': 'Learning to Drive',
                'content': '''When I was 18 years old, I decided to learn how to drive. I was nervous but excited at the same time. My parents signed me up for driving lessons at a local school.

My driving instructor was a patient woman named Maria. She taught me the basics first: how to start the car, how to use the mirrors, and how to brake. At first, everything felt very difficult.

During my first lesson, I was very scared. I drove very slowly. I had problems with parking. But Maria was always calm and encouraging. She said, "Don't worry, everyone makes mistakes at the beginning."

After three months of lessons, I felt ready for the test. I practiced every weekend with my father. On the day of the test, I was nervous. But I remembered everything Maria taught me.

I passed the test on my first try! I was so happy. Now I drive everywhere. Learning to drive was challenging, but it gave me freedom and independence.''',
                'questions': [
                    {'question': 'How old was the person when they started learning?', 'answer': '18 years old', 'options': ['16 years old', '17 years old', '18 years old', '20 years old']},
                    {'question': 'Who was the driving instructor?', 'answer': 'Maria', 'options': ['Anna', 'Maria', 'Sarah', 'Linda']},
                    {'question': 'How long did the lessons take?', 'answer': 'Three months', 'options': ['One month', 'Two months', 'Three months', 'Six months']}
                ]
            },
            {
                'title': 'A Day at the Beach',
                'content': '''Last Saturday, my friends and I went to the beach. The weather was perfect – sunny with a light breeze. We left early in the morning to avoid traffic. It took us about an hour to get there.

When we arrived, we found a nice spot on the sand. We put up our umbrella and laid out our towels. The beach was not too crowded. We could hear the waves crashing on the shore.

First, we went swimming. The water was cold at first, but we got used to it quickly. We played in the waves and tried to catch them. It was so much fun! After swimming, we played beach volleyball.

At lunchtime, we had a picnic. We brought sandwiches, fruits, and cold drinks. We sat under the umbrella and watched people pass by. Some children were building sandcastles nearby.

In the afternoon, I took a walk along the shore. I collected some beautiful seashells. The sunset was amazing – the sky turned orange and pink. We stayed until it got dark. It was a perfect day!''',
                'questions': [
                    {'question': 'How long did it take to get to the beach?', 'answer': 'About an hour', 'options': ['30 minutes', 'About an hour', 'Two hours', 'Three hours']},
                    {'question': 'What game did they play on the beach?', 'answer': 'Beach volleyball', 'options': ['Soccer', 'Beach volleyball', 'Frisbee', 'Tennis']},
                    {'question': 'What did the person collect on the walk?', 'answer': 'Seashells', 'options': ['Stones', 'Seashells', 'Flowers', 'Sticks']}
                ]
            },
            {
                'title': 'My New Smartphone',
                'content': '''Last month, I bought a new smartphone. My old phone was three years old and very slow. It was time for an upgrade. I researched different models online before making my decision.

I went to the electronics store with my brother. He knows a lot about technology and helped me choose. We compared several phones. In the end, I chose a mid-range model with a good camera.

The phone has many useful features. The screen is bigger than my old phone. The battery lasts all day without charging. I can take beautiful photos and videos. The phone also has a fingerprint scanner for security.

Setting up the new phone was easy. I transferred all my contacts and photos from my old device. I downloaded my favorite apps like WhatsApp, Instagram, and Spotify. It only took about an hour to set everything up.

I have had my new phone for a month now, and I am very happy with it. It works much faster than my old one. The camera is especially impressive. I recommend this phone to anyone looking for a good option.''',
                'questions': [
                    {'question': 'How old was the old phone?', 'answer': 'Three years old', 'options': ['One year old', 'Two years old', 'Three years old', 'Four years old']},
                    {'question': 'Who helped choose the new phone?', 'answer': 'Brother', 'options': ['Father', 'Friend', 'Brother', 'Mother']},
                    {'question': 'How long did setup take?', 'answer': 'About an hour', 'options': ['30 minutes', 'About an hour', 'Two hours', 'All day']}
                ]
            },
            {
                'title': 'Working from Home',
                'content': '''Since last year, I have been working from home. At first, it was strange not going to the office every day. But now I am used to it, and I actually prefer it.

I have set up a small office in my bedroom. I have a desk, a comfortable chair, and a good computer. I also have a bookshelf with all my work materials. Good lighting is important, so I sit near the window.

My daily routine is different now. I wake up at 8 o'clock, but I don't have to commute. I save about two hours every day! I start work at 9 and take a break for lunch at 1 o'clock.

There are some challenges. Sometimes it's hard to focus because of distractions at home. I try to keep a regular schedule and take short breaks. I also make sure to exercise every day.

The best part is the flexibility. I can do laundry during my breaks. I spend more time with my family. Working from home has changed my life in many positive ways.''',
                'questions': [
                    {'question': 'Where is the home office located?', 'answer': 'In the bedroom', 'options': ['In the living room', 'In the bedroom', 'In the kitchen', 'In the garage']},
                    {'question': 'How much time is saved from not commuting?', 'answer': 'About two hours', 'options': ['One hour', 'About two hours', 'Three hours', 'Four hours']},
                    {'question': 'What time does work start?', 'answer': '9 o\'clock', 'options': ['8 o\'clock', '9 o\'clock', '10 o\'clock', '11 o\'clock']}
                ]
            },
            {
                'title': 'A Visit to the Doctor',
                'content': '''Last week, I wasn't feeling well. I had a headache and a sore throat. I also felt very tired. After two days, I decided to visit the doctor.

I called the clinic and made an appointment for the next day. When I arrived, I gave my name to the receptionist. She asked me to fill out a form and wait in the waiting room.

After about 15 minutes, the nurse called my name. She took me to a small room. She checked my temperature and blood pressure. Then the doctor came in. She asked me about my symptoms.

The doctor examined my throat and listened to my chest. She said I had a mild infection. She prescribed some medicine and told me to rest for a few days. She also recommended drinking lots of fluids.

I went to the pharmacy and got my medicine. After taking it for three days, I felt much better. I'm glad I went to the doctor. It's important to take care of your health.''',
                'questions': [
                    {'question': 'What symptoms did the person have?', 'answer': 'Headache and sore throat', 'options': ['Stomachache', 'Headache and sore throat', 'Back pain', 'Toothache']},
                    {'question': 'How long did the person wait?', 'answer': 'About 15 minutes', 'options': ['5 minutes', 'About 15 minutes', '30 minutes', 'One hour']},
                    {'question': 'What was the diagnosis?', 'answer': 'A mild infection', 'options': ['Flu', 'A mild infection', 'Allergy', 'Cold']}
                ]
            }
        ]
    },
    'B1': {
        'word_count': (250, 400),
        'templates': [
            {
                'title': 'The Importance of Learning Languages',
                'content': '''In today's globalized world, learning foreign languages has become more important than ever before. Many people study English, Spanish, Mandarin, or other languages to improve their career prospects and connect with people from different cultures.

There are several reasons why learning a new language is beneficial. First, it can help you in your professional life. Many companies work internationally and need employees who can communicate in multiple languages. Knowing another language can make you stand out in job interviews and lead to better opportunities.

Second, learning languages is good for your brain. Studies have shown that bilingual people have better memory and cognitive abilities. The process of learning and switching between languages keeps the brain active and healthy. Some researchers even suggest that it may delay the onset of dementia in older people.

Third, knowing another language allows you to experience other cultures more deeply. When you can speak the local language while traveling, you can have more meaningful conversations with people. You can understand their customs, read their literature, and watch their films without subtitles.

Of course, learning a language takes time and effort. You need to practice regularly and be patient with yourself. There will be times when you make mistakes or feel frustrated. But if you keep going, you will eventually see progress. The rewards of speaking another language are definitely worth the effort.

Many resources are available today for language learners. You can take classes, use apps, watch videos, or find a conversation partner online. The key is to find methods that work for you and stick with them.''',
                'questions': [
                    {'question': 'According to the text, why is language learning good for your brain?', 'answer': 'It improves memory and cognitive abilities', 'options': ['It helps you sleep better', 'It improves memory and cognitive abilities', 'It makes you more creative', 'It reduces stress']},
                    {'question': 'What does the text say about bilingual people and dementia?', 'answer': 'It may be delayed', 'options': ['They never get it', 'It may be delayed', 'It has no effect', 'It causes dementia']},
                    {'question': 'What is the key to success in language learning?', 'answer': 'Find methods that work and stick with them', 'options': ['Take expensive courses', 'Find methods that work and stick with them', 'Move to another country', 'Study 10 hours daily']}
                ]
            },
            {
                'title': 'Climate Change and Our Future',
                'content': '''Climate change is one of the biggest challenges facing our planet today. Scientists around the world agree that the Earth's temperature is rising due to human activities. This is causing many problems that affect everyone.

The main cause of climate change is the burning of fossil fuels like coal, oil, and gas. When we burn these fuels for energy, they release carbon dioxide and other greenhouse gases into the atmosphere. These gases trap heat from the sun, causing the planet to warm up. This is called the greenhouse effect.

The effects of climate change are already visible. Glaciers and ice caps are melting, causing sea levels to rise. Many coastal cities may be at risk of flooding in the future. Weather patterns are becoming more extreme, with more hurricanes, droughts, and heat waves.

Climate change also affects wildlife and ecosystems. Many species are struggling to adapt to the changing conditions. Some animals are moving to new areas to find suitable habitats. Others face the risk of extinction if they cannot adapt quickly enough.

However, there is still hope. Governments, businesses, and individuals can take action to reduce greenhouse gas emissions. Renewable energy sources like solar and wind power are becoming more affordable. Many countries are setting targets to reduce their carbon footprint and protect the environment.

Each of us can also make a difference. We can reduce our energy consumption, use public transport, recycle, and eat less meat. Small changes, when adopted by millions of people, can have a big impact.

The fight against climate change requires global cooperation. We must work together to create a sustainable future for the next generations.''',
                'questions': [
                    {'question': 'What is the main cause of climate change according to the text?', 'answer': 'Burning of fossil fuels', 'options': ['Deforestation', 'Burning of fossil fuels', 'Overpopulation', 'Natural causes']},
                    {'question': 'What is causing sea levels to rise?', 'answer': 'Melting glaciers and ice caps', 'options': ['More rain', 'Melting glaciers and ice caps', 'Ocean pollution', 'Earthquakes']},
                    {'question': 'What examples of renewable energy does the text mention?', 'answer': 'Solar and wind power', 'options': ['Nuclear and hydro', 'Solar and wind power', 'Natural gas', 'Biomass']}
                ]
            },
            {
                'title': 'The Digital Revolution in Education',
                'content': '''The way we learn has changed dramatically over the past few decades. Technology has transformed education, making it more accessible and interactive than ever before. Today, students can access knowledge from anywhere in the world with just a few clicks.

Online learning platforms have grown rapidly in recent years. Websites like Coursera, Khan Academy, and Duolingo offer courses on almost any subject imaginable. Students can learn at their own pace, pausing and rewinding videos when they need to review something. Many of these resources are free or much cheaper than traditional education.

The COVID-19 pandemic accelerated this trend. When schools and universities closed, millions of students had to switch to online learning. While this transition was challenging for many, it also showed the potential of digital education. Teachers and students discovered new ways to collaborate and communicate online.

However, digital education is not without its challenges. Not everyone has access to reliable internet or devices. This digital divide can create inequality in education opportunities. Students in rural areas or developing countries may be left behind.

Another concern is the lack of social interaction in online learning. Traditional classrooms provide opportunities for students to interact with their peers and develop social skills. Some students feel isolated when learning online and miss the community aspect of school.

Despite these challenges, the future of education will likely be a blend of traditional and digital methods. Technology can supplement classroom learning, providing additional resources and personalized learning experiences. The key is to use technology as a tool to enhance education, not replace human connection entirely.

Teachers will continue to play an important role in guiding students and providing support. The best education systems will combine the strengths of both approaches to create the best learning outcomes for students.''',
                'questions': [
                    {'question': 'What platforms are mentioned as examples of online learning?', 'answer': 'Coursera, Khan Academy, and Duolingo', 'options': ['YouTube and Netflix', 'Coursera, Khan Academy, and Duolingo', 'Facebook and Instagram', 'Wikipedia and Google']},
                    {'question': 'What event accelerated the growth of online learning?', 'answer': 'The COVID-19 pandemic', 'options': ['The internet invention', 'The COVID-19 pandemic', 'Economic crisis', 'Climate change']},
                    {'question': 'What is the "digital divide" mentioned in the text?', 'answer': 'Inequality in access to technology', 'options': ['Different types of devices', 'Inequality in access to technology', 'Age differences', 'Language barriers']}
                ]
            },
            {
                'title': 'The Psychology of Habits',
                'content': '''We all have habits – routines and behaviors that we do automatically without thinking. Some habits are helpful, like brushing our teeth or exercising regularly. Others are not so good, like eating too much junk food or spending too much time on social media. Understanding how habits work can help us change them.

According to research, habits are formed through a loop that has three parts: the cue, the routine, and the reward. The cue is a trigger that tells your brain to start the habit. The routine is the behavior itself. The reward is what you get from the behavior, which makes your brain want to repeat it.

For example, consider the habit of checking your phone first thing in the morning. The cue might be waking up and seeing your phone on the bedside table. The routine is picking up the phone and scrolling through notifications. The reward is the feeling of connection or the dopamine hit from seeing new messages.

To change a bad habit, you need to understand its loop. You cannot simply eliminate a habit; you need to replace it with a new one. Keep the same cue and reward, but change the routine. For instance, if stress (cue) makes you eat chocolate (routine) to feel calm (reward), you could try going for a walk instead when you feel stressed.

Starting new habits requires repetition. Research suggests it takes about 66 days on average to form a new habit. Start small and be consistent. If you want to start exercising, begin with just 10 minutes a day instead of an hour.

Making your new habits easy and your bad habits hard can also help. If you want to eat healthier, keep fruits on the counter and hide the cookies. If you want to exercise, lay out your workout clothes the night before.

Remember, change takes time and patience. Be kind to yourself when you slip up, and keep trying.''',
                'questions': [
                    {'question': 'What are the three parts of the habit loop?', 'answer': 'Cue, routine, and reward', 'options': ['Start, middle, end', 'Cue, routine, and reward', 'Beginning, action, result', 'Trigger, behavior, outcome']},
                    {'question': 'How long does it typically take to form a new habit?', 'answer': 'About 66 days', 'options': ['21 days', 'About 66 days', '30 days', '100 days']},
                    {'question': 'What does the text suggest for changing a bad habit?', 'answer': 'Replace the routine, keep the cue and reward', 'options': ['Just stop doing it', 'Replace the routine, keep the cue and reward', 'Change everything', 'Ignore the habit']}
                ]
            },
            {
                'title': 'The Gig Economy',
                'content': '''The world of work is changing. More and more people are leaving traditional full-time jobs to work in the "gig economy." This term refers to a labor market where short-term, flexible jobs are common, and companies hire independent workers for specific projects or tasks.

The gig economy includes various types of work. Freelancers offer their skills to multiple clients, working on projects like writing, design, or programming. Ride-share drivers work for companies like Uber and Lyft. Delivery workers bring food and packages to people's doors. These workers are usually classified as independent contractors, not employees.

There are several reasons why the gig economy has grown. Technology has made it easier to connect workers with opportunities through apps and websites. Many people value the flexibility of choosing when and where to work. For some, gig work provides extra income alongside their regular job.

However, the gig economy also has downsides. Independent workers often lack benefits like health insurance, paid vacation, and retirement plans that traditional employees receive. Their income can be unpredictable, varying from week to week. There is also less job security, as they can be "deactivated" from platforms with little notice.

The legal status of gig workers is a subject of debate. Some argue that these workers should be classified as employees and receive the same protections. Others believe that the flexibility of independent work is what makes it attractive and should be preserved.

Companies benefit from the gig economy because they can adjust their workforce based on demand. They don't have to pay for benefits or deal with the costs of full-time employees. This can make their services cheaper for consumers.

The future of work will likely include more gig opportunities. The challenge for society is to ensure that these workers are treated fairly while maintaining the flexibility that makes gig work appealing.''',
                'questions': [
                    {'question': 'What does "gig economy" refer to?', 'answer': 'A labor market with short-term, flexible jobs', 'options': ['Music industry jobs', 'A labor market with short-term, flexible jobs', 'Traditional office work', 'Government jobs']},
                    {'question': 'What classification do gig workers usually have?', 'answer': 'Independent contractors', 'options': ['Full-time employees', 'Part-time employees', 'Independent contractors', 'Volunteers']},
                    {'question': 'What is a downside of gig work mentioned in the text?', 'answer': 'Lack of benefits like health insurance', 'options': ['Too much flexibility', 'Lack of benefits like health insurance', 'High salaries', 'Too many clients']}
                ]
            }
        ]
    },
    'B2': {
        'word_count': (400, 600),
        'templates': [
            {
                'title': 'The Ethics of Artificial Intelligence',
                'content': '''Artificial intelligence (AI) is transforming every aspect of our lives, from the way we work to how we interact with technology. As these systems become more sophisticated, important ethical questions are emerging that society must address.

One of the primary concerns is algorithmic bias. AI systems learn from data, and if that data contains biases, the AI will perpetuate and sometimes amplify those biases. For example, facial recognition systems have been shown to be less accurate for people with darker skin tones, and hiring algorithms have been found to discriminate against women. These biases can have real-world consequences, affecting people's access to opportunities and justice.

Privacy is another significant ethical issue. AI systems often require vast amounts of personal data to function effectively. Companies and governments collect information about our browsing habits, purchasing decisions, location, and even our facial features. There are legitimate concerns about how this data is used, stored, and protected. The potential for surveillance and the erosion of privacy is a major worry for civil liberties advocates.

The impact of AI on employment raises ethical questions as well. Automation powered by AI threatens to displace workers in many industries, from manufacturing to customer service to even professional fields like law and medicine. While new jobs will be created, the transition may be difficult for many workers, particularly those without the skills needed for the new economy.

There is also the question of accountability. When an AI system makes a mistake that causes harm – such as a self-driving car accident or an incorrect medical diagnosis – who is responsible? The developer? The company? The user? Current legal frameworks are not well-equipped to handle these questions.

Some researchers warn about the long-term risks of developing highly advanced AI systems. The concept of superintelligent AI – machines that surpass human intelligence – raises existential questions. While this may seem like science fiction, many experts believe we should begin thinking about these scenarios now.

To address these ethical challenges, various approaches are being proposed. Some advocate for government regulation of AI development and deployment. Others call for industry self-regulation and the adoption of ethical guidelines. Many emphasize the importance of transparency – ensuring that AI systems are explainable and their decision-making processes can be understood.

Ultimately, the goal should be to develop AI that benefits humanity while minimizing potential harms. This requires ongoing dialogue between technologists, policymakers, ethicists, and the public.''',
                'questions': [
                    {'question': 'What is "algorithmic bias" according to the text?', 'answer': 'AI systems perpetuating biases from their training data', 'options': ['Computer errors', 'AI systems perpetuating biases from their training data', 'Slow processing speed', 'User preferences']},
                    {'question': 'What example of AI bias is mentioned?', 'answer': 'Facial recognition being less accurate for darker skin tones', 'options': ['Voice recognition problems', 'Facial recognition being less accurate for darker skin tones', 'Language translation errors', 'Navigation mistakes']},
                    {'question': 'What does the text say about accountability for AI mistakes?', 'answer': 'Current legal frameworks cannot handle these questions well', 'options': ['Developers are always responsible', 'Current legal frameworks cannot handle these questions well', 'Users must accept all responsibility', 'There are clear laws about this']}
                ]
            },
            {
                'title': 'The Science of Sleep',
                'content': '''Sleep is one of the most fundamental aspects of human biology, yet many people don't fully understand its importance or the complex processes that occur while we rest. Modern research has revealed that sleep is not simply a passive state but an active period essential for physical and mental health.

The sleep cycle consists of several stages that repeat throughout the night. Non-REM sleep includes three stages, progressing from light sleep to deep sleep. During deep sleep, the body repairs tissues, builds bone and muscle, and strengthens the immune system. REM (rapid eye movement) sleep is when most dreaming occurs and is crucial for cognitive functions like memory consolidation and learning.

A typical adult needs seven to nine hours of sleep per night, though individual needs vary. Children and teenagers require more sleep, while older adults may need slightly less. However, the quality of sleep is just as important as quantity. Sleep that is frequently interrupted or that doesn't include enough deep sleep and REM sleep may leave you feeling tired even after spending adequate time in bed.

Sleep deprivation has serious consequences. In the short term, it impairs concentration, decision-making, and reaction time, increasing the risk of accidents. Chronic sleep deprivation has been linked to numerous health problems, including obesity, diabetes, cardiovascular disease, and mental health disorders like depression and anxiety. Studies have also shown that insufficient sleep weakens the immune system, making people more susceptible to infections.

Several factors affect sleep quality. The circadian rhythm, our internal body clock, regulates when we feel sleepy and when we feel alert. Exposure to light, particularly blue light from screens, can disrupt this rhythm by suppressing the production of melatonin, a hormone that promotes sleep. Caffeine, alcohol, and heavy meals close to bedtime can also interfere with sleep.

Creating a sleep-friendly environment is important. A cool, dark, and quiet bedroom is ideal. Many sleep experts recommend establishing a consistent sleep schedule, going to bed and waking up at the same times even on weekends. A relaxing bedtime routine, such as reading or taking a warm bath, can signal to the body that it's time to sleep.

Despite our understanding of sleep's importance, modern society often works against good sleep habits. Long work hours, 24/7 entertainment, and the pressure to be constantly connected all contribute to sleep deprivation. Prioritizing sleep is one of the most important things we can do for our health and well-being.''',
                'questions': [
                    {'question': 'What happens during deep (non-REM) sleep?', 'answer': 'The body repairs tissues and strengthens the immune system', 'options': ['Dreams occur', 'The body repairs tissues and strengthens the immune system', 'The brain is inactive', 'Metabolism stops']},
                    {'question': 'How much sleep do typical adults need?', 'answer': 'Seven to nine hours', 'options': ['Five to six hours', 'Seven to nine hours', 'Ten to twelve hours', 'Four to five hours']},
                    {'question': 'What hormone promotes sleep that can be disrupted by blue light?', 'answer': 'Melatonin', 'options': ['Dopamine', 'Serotonin', 'Melatonin', 'Cortisol']}
                ]
            },
            {
                'title': 'Globalization: Benefits and Challenges',
                'content': '''Globalization, the process of increasing interconnection between countries through trade, investment, technology, and cultural exchange, has been one of the defining phenomena of the past century. While it has brought significant benefits, it has also created challenges that require careful consideration.

The economic benefits of globalization are substantial. Free trade has allowed countries to specialize in producing goods and services where they have a comparative advantage, leading to greater efficiency and lower prices for consumers. Multinational corporations have spread technology and knowledge across borders, helping developing countries modernize their economies. Global supply chains have made it possible to produce complex products more efficiently by sourcing components from different countries.

For developing nations, globalization has opened access to foreign markets and investment. Many countries have seen rapid economic growth and poverty reduction as they integrated into the global economy. China's transformation from a predominantly agricultural economy to the world's manufacturing powerhouse is perhaps the most dramatic example.

However, globalization has also created significant challenges. In developed countries, competition from low-wage countries has led to job losses in manufacturing sectors. Communities dependent on these industries have experienced economic decline and social problems. While economists point out that overall wealth increases through trade, the benefits have not been evenly distributed, contributing to rising inequality within countries.

Cultural impacts are also debated. Some argue that globalization threatens local cultures and traditions as Western products and media dominate global markets. The spread of English as a global language, while facilitating communication, may come at the expense of linguistic diversity. On the other hand, cultural exchange can enrich societies and promote understanding between different peoples.

Environmental concerns are another dimension of the globalization debate. The expansion of international trade has increased transportation and production, contributing to carbon emissions and climate change. Critics argue that current trade rules prioritize economic growth over environmental protection. However, global cooperation is also necessary to address environmental challenges that transcend national boundaries.

The COVID-19 pandemic exposed vulnerabilities in global supply chains and raised questions about the wisdom of depending on distant countries for essential goods like medical supplies. Some argue for reshoring production or at least diversifying supply chains to reduce risks.

As we look to the future, the challenge is to preserve the benefits of global economic integration while addressing its shortcomings. This may require new approaches to trade agreements that include stronger protections for workers and the environment, as well as domestic policies that help those who are negatively affected by globalization.''',
                'questions': [
                    {'question': 'What economic benefit of globalization is mentioned for consumers?', 'answer': 'Lower prices', 'options': ['Higher quality only', 'Lower prices', 'More variety but higher prices', 'Better customer service']},
                    {'question': 'Which country is cited as an example of rapid economic transformation?', 'answer': 'China', 'options': ['India', 'Brazil', 'China', 'Mexico']},
                    {'question': 'What concern about globalization did the COVID-19 pandemic highlight?', 'answer': 'Vulnerabilities in global supply chains', 'options': ['Cultural exchange', 'Vulnerabilities in global supply chains', 'Language barriers', 'Currency differences']}
                ]
            }
        ]
    },
    'C1': {
        'word_count': (500, 800),
        'templates': [
            {
                'title': 'The Neuroscience of Decision Making',
                'content': '''Human decision making is a fascinating and complex process that has captivated researchers across multiple disciplines, from psychology and economics to neuroscience and philosophy. Our understanding of how we make choices has evolved significantly over the past century, challenging traditional assumptions about human rationality and revealing the intricate interplay between emotion and reason.

Classical economic theory assumed that humans are rational actors who carefully weigh the costs and benefits of each option before making decisions that maximize their utility. However, behavioral economists and psychologists have demonstrated that our decision-making processes are subject to numerous cognitive biases and heuristics that can lead us astray.

The work of Daniel Kahneman, who received the Nobel Prize in Economics for his contributions to behavioral economics, has been particularly influential. Kahneman proposed that we have two systems of thinking: System 1, which is fast, automatic, and intuitive; and System 2, which is slow, deliberate, and analytical. Most of our daily decisions are made by System 1, which relies on mental shortcuts that are usually effective but can sometimes lead to systematic errors.

Neuroscience has provided deeper insights into the mechanisms underlying decision making. Brain imaging studies have shown that different regions of the brain are involved in different aspects of choice. The prefrontal cortex, which is involved in planning and reasoning, plays a key role in deliberative decisions. The amygdala, associated with emotional processing, is crucial for decisions involving risk and fear. The striatum, part of the brain's reward system, is activated when we anticipate rewards.

One of the most significant findings has been the essential role of emotion in decision making. Antonio Damasio's somatic marker hypothesis suggests that emotions and bodily sensations guide our decisions by helping us quickly evaluate options based on past experiences. Patients with damage to the emotional centers of the brain, while retaining their cognitive abilities, often make poor decisions, suggesting that pure reason is insufficient for effective choice.

The concept of bounded rationality, introduced by Herbert Simon, recognizes that our decision-making abilities are limited by the information we have, the cognitive limitations of our minds, and the time available to make decisions. Rather than optimizing, we often "satisfice" – choosing an option that is good enough rather than spending excessive resources searching for the best possible outcome.

Understanding the psychological and neural bases of decision making has practical implications. In fields such as medicine, law, and finance, awareness of cognitive biases can help professionals make better judgments. The design of choice architectures – the way options are presented – can nudge people toward decisions that are in their best interest while still preserving their freedom to choose.

As research continues to unravel the mysteries of human choice, we gain not only scientific knowledge but also practical tools for improving decisions at individual and societal levels. The integration of insights from psychology, neuroscience, and economics promises a more nuanced understanding of this fundamental aspect of human experience.''',
                'questions': [
                    {'question': 'According to Kahneman, what characterizes System 2 thinking?', 'answer': 'Slow, deliberate, and analytical', 'options': ['Fast and automatic', 'Slow, deliberate, and analytical', 'Emotional and intuitive', 'Random and unpredictable']},
                    {'question': 'What is the somatic marker hypothesis about?', 'answer': 'How emotions and bodily sensations guide decisions', 'options': ['How logic determines choices', 'How emotions and bodily sensations guide decisions', 'How education affects decision making', 'How culture shapes preferences']},
                    {'question': 'What does "satisficing" mean according to the text?', 'answer': 'Choosing an option that is good enough rather than optimal', 'options': ['Always making the best decision', 'Choosing an option that is good enough rather than optimal', 'Making decisions randomly', 'Avoiding all decisions']}
                ]
            },
            {
                'title': 'The Future of Urban Planning',
                'content': '''As the world becomes increasingly urbanized, with projections indicating that over two-thirds of the global population will live in cities by 2050, the challenges and opportunities of urban planning have never been more significant. The decisions made today about how cities are designed, built, and governed will shape the quality of life for billions of people and determine our collective ability to address pressing global challenges such as climate change, social inequality, and public health.

Historically, urban planning has undergone significant paradigm shifts. The modernist planning of the mid-twentieth century, with its emphasis on functional zoning and automobile-oriented design, created urban environments that, while efficient in some respects, often resulted in sterile cityscapes, sprawling suburbs, and communities dependent on cars. In response, planners have increasingly embraced principles of walkability, mixed-use development, and transit-oriented design that prioritize human-scale environments and reduce carbon footprints.

The concept of the "15-minute city" has gained traction in recent years, particularly following the COVID-19 pandemic. This approach proposes that all essential services – work, shopping, education, healthcare, and leisure – should be accessible within a 15-minute walk or bike ride from one's home. Paris, under Mayor Anne Hidalgo, has been at the forefront of implementing this vision, transforming streets to prioritize pedestrians and cyclists while reducing car access.

Smart city technologies offer both promise and peril for urban futures. Sensors, data analytics, and connected infrastructure can improve efficiency in everything from traffic management to energy distribution. However, concerns about surveillance, data privacy, and the digital divide must be carefully addressed. The risk of creating technology-dependent cities that exclude those without access or digital literacy is real.

Sustainable urban planning increasingly incorporates nature-based solutions. Green infrastructure – including urban forests, green roofs, rain gardens, and bioswales – can address multiple challenges simultaneously, from managing stormwater and reducing heat island effects to improving air quality and providing spaces for recreation and biodiversity. Singapore's approach to becoming a "city in a garden" demonstrates how even densely built environments can integrate substantial greenery.

Housing affordability remains one of the most pressing challenges for cities worldwide. The financialization of housing, where properties are treated as investment assets rather than homes, has contributed to rising prices and displacement of long-term residents. Innovative approaches such as community land trusts, co-housing, and inclusionary zoning are being explored to ensure that cities remain accessible to people of all income levels.

The governance of cities is also evolving. Metropolitan regions often extend beyond traditional municipal boundaries, requiring new forms of regional coordination. Participatory planning processes that engage citizens in decision-making are becoming more common, enabled by both in-person engagement and digital tools. The challenge is to make these processes genuinely inclusive rather than dominated by the usual voices.

Climate change presents existential challenges for urban planning. Cities must simultaneously mitigate their contributions to greenhouse gas emissions and adapt to the impacts that are already locked in. This includes preparing for sea-level rise, extreme heat events, flooding, and other climate-related hazards. The costs of inaction are enormous, making investment in resilient infrastructure a necessity rather than a luxury.

Looking ahead, the cities that thrive will likely be those that can balance multiple objectives: economic vitality, environmental sustainability, social equity, and quality of life. There is no single model that works everywhere, as local contexts vary enormously. However, the exchange of ideas and best practices across cities, facilitated by networks and international organizations, can accelerate learning and innovation.

The future of urban planning is not just a technical matter but fundamentally a political and ethical one. The choices we make reflect our values and priorities. By reimagining what cities can be, we have the opportunity to create urban environments that are not only more sustainable but also more just and humane.''',
                'questions': [
                    {'question': 'What is the "15-minute city" concept?', 'answer': 'All essential services accessible within a 15-minute walk or bike ride', 'options': ['A city that takes 15 minutes to cross', 'All essential services accessible within a 15-minute walk or bike ride', 'A city planning process that takes 15 minutes', 'Cities with 15-minute work days']},
                    {'question': 'What concern about smart city technologies is mentioned?', 'answer': 'Surveillance, privacy, and the digital divide', 'options': ['They are too expensive', 'Surveillance, privacy, and the digital divide', 'They use too much electricity', 'They are difficult to maintain']},
                    {'question': 'What does "financialization of housing" mean?', 'answer': 'Treating properties as investment assets rather than homes', 'options': ['Making housing free', 'Treating properties as investment assets rather than homes', 'Building more affordable housing', 'Government ownership of housing']}
                ]
            }
        ]
    },
    'C2': {
        'word_count': (700, 1000),
        'templates': [
            {
                'title': 'The Philosophy of Consciousness',
                'content': '''The nature of consciousness remains one of the most profound and persistent puzzles in philosophy, psychology, and neuroscience. Despite remarkable advances in our understanding of the brain, the subjective experience of being aware – what philosophers call phenomenal consciousness or qualia – continues to elude satisfactory explanation, giving rise to what David Chalmers famously termed the "hard problem of consciousness."

The hard problem can be framed as follows: even if we could explain all the objective, functional aspects of consciousness – how the brain processes information, controls behavior, and gives rise to verbal reports about experience – we would still face the question of why there is something it is like to be conscious. Why doesn't all this neural activity occur "in the dark," without any accompanying subjective experience? This explanatory gap between objective physical processes and subjective experience poses a formidable challenge to purely physicalist accounts of the mind.

Various philosophical positions have been developed to address this problem. Reductive physicalism maintains that consciousness will ultimately be explained in terms of brain processes, just as water was explained in terms of H₂O molecules. On this view, the apparent gap between physical and mental explanations will close as our scientific understanding advances. Critics object that no matter how complete our knowledge of neural correlates becomes, we still won't have bridged the explanatory gap to subjective experience.

Non-reductive physicalism, or property dualism, accepts that consciousness is ultimately physical but holds that mental properties are emergent properties that cannot be reduced to or predicted from lower-level physical properties alone. This position preserves the unity of the natural world while acknowledging the distinctive character of conscious experience. However, critics question whether emergence is anything more than a label for our current ignorance and whether it can provide a genuine explanation.

Dualist positions, following Descartes, maintain that consciousness is fundamentally non-physical. Substance dualism holds that mind and body are distinct substances that interact. While this resonates with our intuitive sense of being more than mere matter, it faces the notorious interaction problem: how can a non-physical substance causally influence physical processes? The historical failure to specify any mechanism for such interaction has led most contemporary philosophers to reject this view.

Panpsychism, which has experienced a recent revival, proposes that consciousness is a fundamental feature of reality, present to some degree in all matter. On this view, human consciousness is a complex combination of more basic forms of consciousness. While counterintuitive, panpsychism avoids both the explanatory gap of physicalism and the interaction problem of dualism. Critics question whether the combination problem – how micro-experiences combine to form unified macro-experience – is any more tractable than the hard problem itself.

Illusionist accounts, championed by philosophers like Daniel Dennett and Keith Frankish, take a deflationary approach. They argue that phenomenal consciousness, as typically conceived, is an illusion. We are radically mistaken about the nature of our own experience. What seems like irreducible qualia can actually be explained in terms of representations that the brain creates. While this approach dissolves rather than solves the hard problem, critics argue that it simply cannot account for the undeniable reality of our subjective experience.

Integrated Information Theory (IIT), developed by neuroscientist Giulio Tononi, attempts to mathematize consciousness. It proposes that consciousness is identical to a particular kind of integrated information, measured by the quantity φ (phi). A system is conscious to the degree that its information is integrated in a way that the whole is greater than the sum of its parts. IIT makes interesting predictions, such as that certain simple systems might be slightly conscious while some complex but modular systems might not be conscious at all.

Global Workspace Theory (GWT), associated with Bernard Baars, offers a functional theory of consciousness. It compares consciousness to a spotlight on a theater stage: conscious contents are those that are broadcast widely across the brain, making information available to many different processes simultaneously. While GWT successfully explains many features of conscious cognition, critics argue it addresses the easy problems of consciousness rather than the hard problem of subjective experience.

Higher-Order Theories propose that a mental state becomes conscious when it is the target of a higher-order mental state – essentially, when we have a thought about the thought. Variations include higher-order thought theories and higher-order perception theories. While they offer a promising account of the difference between conscious and unconscious mental states, they have been criticized for making consciousness seem too cognitively demanding.

The empirical study of consciousness has made significant progress through identifying neural correlates of consciousness (NCCs) – the specific brain processes associated with particular conscious experiences. However, correlation is not causation, and finding NCCs doesn't directly address the hard problem. Experiments on phenomena like binocular rivalry, change blindness, and blindsight continue to refine our understanding of the boundary between conscious and unconscious processing.

The question of animal consciousness raises important ethical implications. If consciousness is not uniquely human, what moral status should we accord to other sentient beings? Similarly, the possibility of machine consciousness raises questions about the moral status of artificial intelligence systems.

As we stand at the frontier of consciousness science and philosophy, intellectual humility is warranted. The problem may require conceptual revolutions comparable to those that transformed physics in the twentieth century. Or it may be that some aspects of consciousness will remain forever beyond our grasp, a true mystery at the heart of existence.''',
                'questions': [
                    {'question': 'What is the "hard problem" of consciousness?', 'answer': 'Explaining why there is subjective experience', 'options': ['Understanding how the brain functions', 'Explaining why there is subjective experience', 'Mapping neural connections', 'Studying brain diseases']},
                    {'question': 'What does panpsychism propose?', 'answer': 'Consciousness is a fundamental feature present in all matter', 'options': ['Consciousness is an illusion', 'Only humans are conscious', 'Consciousness is a fundamental feature present in all matter', 'Consciousness requires language']},
                    {'question': 'What does Integrated Information Theory measure consciousness with?', 'answer': 'The quantity φ (phi)', 'options': ['Brain size', 'Number of neurons', 'The quantity φ (phi)', 'Reaction time']}
                ]
            }
        ]
    }
}

# ============================================================================
# VOCABULARIO POR NIVEL
# ============================================================================

VOCABULARY_BY_LEVEL = {
    'A1': {
        'categories': {
            'Greetings': ['hello', 'goodbye', 'good morning', 'good night', 'hi', 'bye', 'see you', 'nice to meet you', 'how are you', 'fine'],
            'Family': ['mother', 'father', 'sister', 'brother', 'grandmother', 'grandfather', 'aunt', 'uncle', 'cousin', 'parents'],
            'Numbers': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],
            'Colors': ['red', 'blue', 'green', 'yellow', 'black', 'white', 'orange', 'purple', 'pink', 'brown'],
            'Days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'Food': ['bread', 'water', 'milk', 'egg', 'apple', 'rice', 'chicken', 'fish', 'vegetables', 'fruit'],
            'House': ['bedroom', 'bathroom', 'kitchen', 'living room', 'door', 'window', 'table', 'chair', 'bed', 'sofa'],
            'Body': ['head', 'eyes', 'ears', 'nose', 'mouth', 'hand', 'arm', 'leg', 'foot', 'body'],
            'Clothes': ['shirt', 'pants', 'dress', 'shoes', 'hat', 'jacket', 'socks', 'skirt', 'coat', 'sweater'],
            'Weather': ['sunny', 'rainy', 'cloudy', 'cold', 'hot', 'windy', 'snow', 'rain', 'sun', 'cloud']
        }
    },
    'A2': {
        'categories': {
            'Travel': ['airport', 'hotel', 'passport', 'ticket', 'luggage', 'suitcase', 'reservation', 'flight', 'destination', 'vacation'],
            'Work': ['office', 'meeting', 'boss', 'colleague', 'salary', 'interview', 'resume', 'employee', 'company', 'business'],
            'Technology': ['computer', 'phone', 'internet', 'email', 'website', 'password', 'download', 'upload', 'message', 'app'],
            'Health': ['doctor', 'medicine', 'hospital', 'pain', 'headache', 'fever', 'appointment', 'prescription', 'illness', 'treatment'],
            'Shopping': ['price', 'discount', 'receipt', 'cash', 'credit card', 'customer', 'sale', 'change', 'size', 'brand'],
            'Entertainment': ['movie', 'concert', 'theater', 'museum', 'festival', 'show', 'ticket', 'performance', 'exhibition', 'gallery'],
            'Restaurant': ['menu', 'waiter', 'bill', 'reservation', 'appetizer', 'dessert', 'tip', 'order', 'dish', 'cuisine'],
            'Sports': ['soccer', 'basketball', 'tennis', 'swimming', 'running', 'team', 'match', 'score', 'player', 'coach'],
            'Environment': ['pollution', 'recycle', 'energy', 'nature', 'climate', 'forest', 'ocean', 'wildlife', 'environment', 'conservation'],
            'Emotions': ['happy', 'sad', 'angry', 'excited', 'worried', 'surprised', 'bored', 'scared', 'nervous', 'confident']
        }
    },
    'B1': {
        'categories': {
            'Education': ['degree', 'course', 'lecture', 'assignment', 'deadline', 'research', 'thesis', 'graduate', 'scholarship', 'curriculum'],
            'Media': ['journalist', 'headline', 'article', 'broadcast', 'interview', 'press', 'coverage', 'editorial', 'reporter', 'publication'],
            'Society': ['community', 'citizen', 'government', 'election', 'policy', 'democracy', 'rights', 'society', 'culture', 'tradition'],
            'Finance': ['budget', 'investment', 'savings', 'loan', 'interest', 'debt', 'income', 'expense', 'tax', 'economy'],
            'Science': ['experiment', 'theory', 'discovery', 'research', 'evidence', 'hypothesis', 'analysis', 'data', 'conclusion', 'laboratory'],
            'Art': ['painting', 'sculpture', 'exhibition', 'gallery', 'artist', 'masterpiece', 'portrait', 'landscape', 'contemporary', 'classical'],
            'Career': ['promotion', 'experience', 'qualification', 'achievement', 'responsibility', 'teamwork', 'leadership', 'management', 'performance', 'goal'],
            'Law': ['lawyer', 'judge', 'court', 'trial', 'evidence', 'witness', 'verdict', 'sentence', 'crime', 'justice'],
            'Global Issues': ['poverty', 'inequality', 'immigration', 'refugee', 'discrimination', 'human rights', 'development', 'crisis', 'conflict', 'cooperation'],
            'Psychology': ['behavior', 'emotion', 'motivation', 'stress', 'anxiety', 'personality', 'therapy', 'consciousness', 'perception', 'memory']
        }
    },
    'B2': {
        'categories': {
            'Business': ['entrepreneur', 'strategy', 'negotiation', 'stakeholder', 'merger', 'acquisition', 'corporation', 'revenue', 'market share', 'competitive advantage'],
            'Philosophy': ['ethics', 'morality', 'existence', 'consciousness', 'truth', 'reality', 'perception', 'knowledge', 'belief', 'reasoning'],
            'Environment': ['sustainability', 'carbon footprint', 'renewable energy', 'biodiversity', 'ecosystem', 'deforestation', 'conservation', 'emissions', 'greenhouse gases', 'climate change'],
            'Literature': ['novel', 'narrative', 'protagonist', 'metaphor', 'symbolism', 'plot', 'theme', 'genre', 'fiction', 'prose'],
            'Politics': ['legislation', 'constitution', 'democracy', 'diplomacy', 'sovereignty', 'parliament', 'bureaucracy', 'reform', 'ideology', 'advocacy'],
            'Technology': ['algorithm', 'artificial intelligence', 'automation', 'cybersecurity', 'innovation', 'interface', 'software', 'hardware', 'database', 'network'],
            'Medicine': ['diagnosis', 'symptom', 'chronic', 'acute', 'therapy', 'vaccine', 'immune system', 'clinical trial', 'pharmaceutical', 'surgery'],
            'Communication': ['persuasion', 'rhetoric', 'discourse', 'articulate', 'eloquent', 'negotiate', 'mediate', 'convey', 'interpret', 'nuance'],
            'Academic': ['hypothesis', 'methodology', 'analysis', 'synthesis', 'critique', 'peer review', 'citation', 'dissertation', 'abstract', 'journal'],
            'Social Issues': ['marginalization', 'empowerment', 'systemic', 'institutional', 'advocacy', 'activism', 'solidarity', 'inclusion', 'diversity', 'equity']
        }
    },
    'C1': {
        'categories': {
            'Academic Writing': ['substantiate', 'elucidate', 'corroborate', 'delineate', 'extrapolate', 'juxtapose', 'scrutinize', 'synthesize', 'articulate', 'postulate'],
            'Legal': ['jurisprudence', 'litigation', 'adjudicate', 'precedent', 'statute', 'injunction', 'tort', 'liability', 'plaintiff', 'defendant'],
            'Economics': ['macroeconomics', 'microeconomics', 'fiscal policy', 'monetary policy', 'inflation', 'deflation', 'recession', 'commodity', 'liquidity', 'speculation'],
            'Philosophy': ['epistemology', 'ontology', 'phenomenology', 'existentialism', 'empiricism', 'rationalism', 'pragmatism', 'relativism', 'determinism', 'free will'],
            'Science': ['paradigm', 'empirical', 'quantitative', 'qualitative', 'correlation', 'causation', 'variable', 'replicate', 'validity', 'reliability'],
            'Arts': ['avant-garde', 'aesthetic', 'juxtaposition', 'minimalism', 'expressionism', 'surrealism', 'cubism', 'renaissance', 'baroque', 'neoclassical'],
            'Linguistics': ['syntax', 'semantics', 'pragmatics', 'morphology', 'phonology', 'discourse', 'register', 'dialect', 'sociolinguistics', 'psycholinguistics'],
            'Medicine': ['prognosis', 'etiology', 'pathology', 'epidemiology', 'pharmacology', 'oncology', 'cardiology', 'neurology', 'psychiatry', 'immunology'],
            'Research': ['longitudinal', 'cross-sectional', 'ethnographic', 'phenomenological', 'grounded theory', 'meta-analysis', 'triangulation', 'saturation', 'generalizability', 'reflexivity'],
            'Rhetoric': ['ethos', 'pathos', 'logos', 'syllogism', 'fallacy', 'premise', 'inference', 'deduction', 'induction', 'refutation']
        }
    },
    'C2': {
        'categories': {
            'Advanced Rhetoric': ['circumlocution', 'periphrasis', 'litotes', 'meiosis', 'hyperbole', 'antithesis', 'chiasmus', 'anacoluthon', 'aposiopesis', 'zeugma'],
            'Philosophy': ['hermeneutics', 'dialectic', 'teleology', 'deontology', 'consequentialism', 'solipsism', 'nihilism', 'hedonism', 'stoicism', 'transcendentalism'],
            'Literary Criticism': ['intertextuality', 'deconstruction', 'postmodernism', 'structuralism', 'semiotics', 'narratology', 'formalism', 'new criticism', 'reader response', 'cultural studies'],
            'Linguistics': ['deixis', 'anaphora', 'cataphora', 'prosody', 'suprasegmental', 'illocutionary', 'perlocutionary', 'implicature', 'presupposition', 'entailment'],
            'Cognitive Science': ['metacognition', 'proprioception', 'synesthesia', 'aphasia', 'agnosia', 'confabulation', 'heuristic', 'schema', 'prototype', 'exemplar'],
            'Research Methods': ['hermeneutic circle', 'bracketing', 'thick description', 'verstehen', 'double hermeneutic', 'paradigm shift', 'falsifiability', 'operationalization', 'construct validity', 'internal validity'],
            'Ethics': ['deontological', 'utilitarian', 'virtue ethics', 'moral relativism', 'moral absolutism', 'metaethics', 'normative ethics', 'applied ethics', 'bioethics', 'environmental ethics'],
            'Political Philosophy': ['libertarianism', 'communitarianism', 'egalitarianism', 'republicanism', 'cosmopolitanism', 'social contract', 'veil of ignorance', 'distributive justice', 'procedural justice', 'restorative justice'],
            'Epistemology': ['foundationalism', 'coherentism', 'reliabilism', 'internalism', 'externalism', 'skepticism', 'fallibilism', 'contextualism', 'virtue epistemology', 'social epistemology'],
            'Aesthetics': ['sublime', 'kitsch', 'mimesis', 'catharsis', 'formalism', 'intentionalism', 'anti-essentialism', 'institutional theory', 'aesthetic experience', 'aesthetic judgment']
        }
    }
}


def get_level(unit_num):
    """Determina el nivel CEFR basado en el número de unidad"""
    if unit_num <= 12: return 'A1'
    elif unit_num <= 24: return 'A2'
    elif unit_num <= 36: return 'B1'
    elif unit_num <= 48: return 'B2'
    elif unit_num <= 60: return 'C1'
    else: return 'C2'


def generate_reading_for_unit(unit, level_data, used_titles):
    """Genera una lectura adaptada para una unidad específica"""
    templates = level_data['templates']
    
    # Buscar una plantilla no usada o menos usada
    available = [t for t in templates if t['title'] not in used_titles]
    if not available:
        available = templates
    
    template = random.choice(available)
    used_titles.add(template['title'])
    
    # Personalizar el título con el tema de la unidad
    unit_topic = unit.title.split(':')[-1].strip() if ':' in unit.title else unit.title
    custom_title = f"{template['title']} - {unit_topic}"
    
    return template, custom_title


def seed_readings_for_unit(unit):
    """Añade lecturas a una unidad"""
    level = get_level(unit.unit_number)
    level_data = READINGS_BY_LEVEL.get(level)
    
    if not level_data:
        return 0
    
    existing = Reading.query.filter_by(unit_id=unit.id).count()
    needed = max(0, 5 - existing)
    
    if needed == 0:
        return 0
    
    used_titles = {r.title for r in Reading.query.filter_by(unit_id=unit.id).all()}
    added = 0
    
    for i in range(needed):
        template, custom_title = generate_reading_for_unit(unit, level_data, used_titles)
        
        # Evitar duplicados exactos
        if Reading.query.filter_by(unit_id=unit.id, title=custom_title).first():
            custom_title = f"{custom_title} ({i+1})"
        
        reading = Reading(
            unit_id=unit.id,
            title=custom_title,
            content=template['content'],
            difficulty=level,
            order=existing + i + 1
        )
        db.session.add(reading)
        
        added += 1
    
    return added


def seed_vocabulary_for_unit(unit):
    """Añade vocabulario a una unidad"""
    level = get_level(unit.unit_number)
    level_vocab = VOCABULARY_BY_LEVEL.get(level)
    
    if not level_vocab:
        return 0
    
    # Verificar vocabulario existente
    existing_categories = VocabularyCategory.query.filter_by(unit_id=unit.id).all()
    existing_count = sum(
        VocabularyItem.query.filter_by(category_id=cat.id).count() 
        for cat in existing_categories
    )
    
    if existing_count >= 10:
        return 0
    
    categories = list(level_vocab['categories'].items())
    
    # Seleccionar 2 categorías para la unidad
    selected = random.sample(categories, min(2, len(categories)))
    added = 0
    
    for cat_name, words in selected:
        # Crear o buscar categoría
        category = VocabularyCategory.query.filter_by(
            unit_id=unit.id, 
            category_name=cat_name
        ).first()
        
        if not category:
            category = VocabularyCategory(
                unit_id=unit.id,
                category_name=cat_name,
                description=f"Vocabulary related to {cat_name.lower()}"
            )
            db.session.add(category)
            db.session.flush()
        
        # Añadir palabras
        existing_words = {v.word for v in VocabularyItem.query.filter_by(category_id=category.id).all()}
        
        for word in words:
            if word not in existing_words:
                vocab_item = VocabularyItem(
                    category_id=category.id,
                    word=word,
                    definition=f"A word meaning {word}",
                    example=f"Example: This is a {word}.",
                    pronunciation=f"/{word}/"
                )
                db.session.add(vocab_item)
                added += 1
                existing_words.add(word)
    
    return added


def seed_flashcards_for_unit(unit):
    """Añade flashcards basados en vocabulario"""
    level = get_level(unit.unit_number)
    level_vocab = VOCABULARY_BY_LEVEL.get(level)
    
    if not level_vocab:
        return 0
    
    existing = Flashcard.query.filter_by(unit_id=unit.id).count()
    if existing >= 8:
        return 0
    
    categories = list(level_vocab['categories'].items())
    selected = random.sample(categories, min(1, len(categories)))
    added = 0
    
    for cat_name, words in selected:
        for word in random.sample(words, min(8 - existing, len(words))):
            if not Flashcard.query.filter_by(unit_id=unit.id, front=word).first():
                flashcard = Flashcard(
                    unit_id=unit.id,
                    front=word,
                    back=f"Definition of {word}",
                    example=f"Example sentence with {word}.",
                    difficulty=level
                )
                db.session.add(flashcard)
                added += 1
                
                if added >= 8:
                    break
    
    return added


def seed_exercises_for_unit(unit):
    """Añade ejercicios de oraciones"""
    level = get_level(unit.unit_number)
    
    existing = SentenceExercise.query.filter_by(unit_id=unit.id).count()
    if existing >= 6:
        return 0
    
    # Ejercicios genéricos por nivel
    exercises_templates = {
        'A1': [
            {'sentence': 'I ___ a student.', 'answer': 'am', 'hint': 'verb to be'},
            {'sentence': 'She ___ to school every day.', 'answer': 'goes', 'hint': 'present simple'},
            {'sentence': 'They ___ playing football.', 'answer': 'are', 'hint': 'present continuous'},
            {'sentence': 'He ___ a car.', 'answer': 'has', 'hint': 'have/has'},
            {'sentence': 'We ___ English.', 'answer': 'speak', 'hint': 'present simple'},
            {'sentence': 'The book is ___ the table.', 'answer': 'on', 'hint': 'preposition'}
        ],
        'A2': [
            {'sentence': 'I ___ to the cinema yesterday.', 'answer': 'went', 'hint': 'past simple'},
            {'sentence': 'She was ___ when I called.', 'answer': 'sleeping', 'hint': 'past continuous'},
            {'sentence': 'He is ___ than his brother.', 'answer': 'taller', 'hint': 'comparative'},
            {'sentence': 'They will ___ tomorrow.', 'answer': 'arrive', 'hint': 'future simple'},
            {'sentence': 'I have ___ eaten lunch.', 'answer': 'already', 'hint': 'adverb'},
            {'sentence': 'She ___ to come to the party.', 'answer': 'wants', 'hint': 'verb + infinitive'}
        ],
        'B1': [
            {'sentence': 'I ___ been waiting for an hour.', 'answer': 'have', 'hint': 'present perfect continuous'},
            {'sentence': 'If I ___ rich, I would travel.', 'answer': 'were', 'hint': 'second conditional'},
            {'sentence': 'The book ___ was written by Dickens is famous.', 'answer': 'which/that', 'hint': 'relative clause'},
            {'sentence': 'She said she ___ help me.', 'answer': 'would', 'hint': 'reported speech'},
            {'sentence': 'The car ___ repaired yesterday.', 'answer': 'was', 'hint': 'passive voice'},
            {'sentence': 'I wish I ___ more time.', 'answer': 'had', 'hint': 'wish + past'}
        ],
        'B2': [
            {'sentence': 'If I had known, I ___ have come.', 'answer': 'would', 'hint': 'third conditional'},
            {'sentence': 'By next year, I ___ have finished.', 'answer': 'will', 'hint': 'future perfect'},
            {'sentence': 'I ___ rather you didn\'t smoke.', 'answer': 'would', 'hint': 'would rather'},
            {'sentence': 'Not only ___ she smart, but also hardworking.', 'answer': 'is', 'hint': 'inversion'},
            {'sentence': 'It\'s time we ___ home.', 'answer': 'went', 'hint': 'it\'s time + past'},
            {'sentence': 'He insisted ___ paying the bill.', 'answer': 'on', 'hint': 'verb + preposition'}
        ],
        'C1': [
            {'sentence': 'Had I known, I ___ told you.', 'answer': 'would have', 'hint': 'conditional inversion'},
            {'sentence': '___ as it may seem, it\'s true.', 'answer': 'Strange', 'hint': 'concessive clause'},
            {'sentence': 'The proposal ___ approved by the board.', 'answer': 'was', 'hint': 'passive'},
            {'sentence': 'It is essential that he ___ on time.', 'answer': 'be', 'hint': 'subjunctive'},
            {'sentence': '___ to his efforts, we succeeded.', 'answer': 'Thanks/Due', 'hint': 'complex preposition'},
            {'sentence': 'Little ___ he know what awaited him.', 'answer': 'did', 'hint': 'negative inversion'}
        ],
        'C2': [
            {'sentence': 'Were it not ___ his help, we would have failed.', 'answer': 'for', 'hint': 'formal conditional'},
            {'sentence': 'The extent ___ which this is true is debatable.', 'answer': 'to', 'hint': 'complex relative'},
            {'sentence': 'It is ___ that he arrived late again.', 'answer': 'typical', 'hint': 'cleft sentence'},
            {'sentence': '___ notwithstanding, we proceeded.', 'answer': 'This', 'hint': 'formal transition'},
            {'sentence': 'Be that as it ___, we must continue.', 'answer': 'may', 'hint': 'fixed expression'},
            {'sentence': 'He was, ___ speak, the life of the party.', 'answer': 'so to', 'hint': 'hedging expression'}
        ]
    }
    
    templates = exercises_templates.get(level, exercises_templates['A1'])
    added = 0
    
    for ex in templates:
        if added >= (6 - existing):
            break
        
        if not SentenceExercise.query.filter_by(
            unit_id=unit.id, 
            prompt=ex['sentence']
        ).first():
            exercise = SentenceExercise(
                unit_id=unit.id,
                exercise_type='fill_blank',
                instruction=f"Complete the sentence with the correct word. Hint: {ex.get('hint', '')}",
                prompt=ex['sentence'],
                correct_answer=ex['answer'],
                grammar_focus=ex.get('hint', ''),
                difficulty=level
            )
            db.session.add(exercise)
            added += 1
    
    return added


def main():
    """Ejecutar el seed completo"""
    with app.app_context():
        print("=" * 80)
        print("🚀 POBLANDO CONTENIDO COMPLETO PARA TODAS LAS UNIDADES")
        print("=" * 80)
        
        units = Unit.query.order_by(Unit.unit_number).all()
        
        total_readings = 0
        total_vocab = 0
        total_flashcards = 0
        total_exercises = 0
        
        current_level = ''
        
        for unit in units:
            level = get_level(unit.unit_number)
            
            if level != current_level:
                print(f"\n📚 Procesando nivel {level}...")
                current_level = level
            
            # Añadir contenido
            r = seed_readings_for_unit(unit)
            v = seed_vocabulary_for_unit(unit)
            f = seed_flashcards_for_unit(unit)
            e = seed_exercises_for_unit(unit)
            
            total_readings += r
            total_vocab += v
            total_flashcards += f
            total_exercises += e
            
            if r + v + f + e > 0:
                print(f"  Unit {unit.unit_number}: +{r} lecturas, +{v} vocab, +{f} flash, +{e} ejerc.")
        
        db.session.commit()
        
        print("\n" + "=" * 80)
        print("✅ RESUMEN DE CONTENIDO AGREGADO:")
        print(f"   📖 Lecturas: {total_readings}")
        print(f"   📚 Vocabulario: {total_vocab}")
        print(f"   🃏 Flashcards: {total_flashcards}")
        print(f"   ✍️ Ejercicios: {total_exercises}")
        print("=" * 80)
        
        # Estadísticas finales
        print("\n📊 ESTADÍSTICAS FINALES:")
        total_r = Reading.query.count()
        total_v = VocabularyItem.query.count()
        total_f = Flashcard.query.count()
        total_e = SentenceExercise.query.count()
        
        print(f"   📖 Total lecturas: {total_r}")
        print(f"   📚 Total vocabulario: {total_v}")
        print(f"   🃏 Total flashcards: {total_f}")
        print(f"   ✍️ Total ejercicios: {total_e}")


if __name__ == '__main__':
    main()
