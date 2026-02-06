#!/usr/bin/env python3
"""
Seed de Lecturas Adicionales - Más lecturas para tener mínimo 1 por unidad
Organizados por nivel CEFR
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import Unit, Reading

app = create_app()

# Lecturas adicionales organizadas por nivel
READINGS_BY_LEVEL = {
    "A1": [
        {
            "title": "My Daily Routine",
            "title_spanish": "Mi Rutina Diaria",
            "content": """Every day, I wake up at 7 o'clock. I get out of bed and go to the bathroom. I brush my teeth and wash my face.

Then, I have breakfast in the kitchen. I usually eat toast and drink orange juice. Sometimes I have cereal with milk.

At 8 o'clock, I leave my house and go to work. I take the bus. The bus ride is about 20 minutes.

I work from 9 to 5. At lunch time, I eat a sandwich. I drink water or coffee.

After work, I go home. I cook dinner and watch TV. At 10 o'clock, I go to bed. I read a book before I sleep.

This is my daily routine. It is simple but I am happy.""",
            "vocabulary": "wake up, bathroom, brush teeth, breakfast, lunch, dinner, work, home",
            "difficulty": "easy"
        },
        {
            "title": "At the Supermarket",
            "title_spanish": "En el Supermercado",
            "content": """Today is Saturday. I go to the supermarket with my mother.

The supermarket is big. There are many things to buy. First, we go to the fruit section. We buy apples, bananas, and oranges. The apples are red and the bananas are yellow.

Then, we go to the vegetable section. We buy tomatoes, carrots, and lettuce. The vegetables are fresh.

Next, we need milk and bread. The milk is in the refrigerator. The bread is near the entrance.

My mother also buys chicken and fish. They are in the meat section. Finally, we buy some snacks: chips and cookies.

We go to the checkout. We pay with a credit card. The total is $45. We put everything in bags and go home.

I like going to the supermarket. I help my mother carry the bags.""",
            "vocabulary": "supermarket, fruit, vegetable, milk, bread, checkout, bags, pay",
            "difficulty": "easy"
        },
        {
            "title": "My Best Friend",
            "title_spanish": "Mi Mejor Amigo/a",
            "content": """I have a best friend. Her name is Laura. She is 25 years old.

Laura has long brown hair and green eyes. She is tall and slim. She is very pretty.

Laura is very kind. She always helps people. She is also funny. We laugh a lot together.

We like to do many things together. We go to the movies. We go shopping. We eat at restaurants. We talk on the phone every day.

Laura works at a school. She is a teacher. She teaches English to children. The children love her.

I am lucky to have a friend like Laura. She is the best friend in the world.""",
            "vocabulary": "friend, kind, funny, movies, shopping, restaurant, teacher, lucky",
            "difficulty": "easy"
        },
        {
            "title": "The Weather Today",
            "title_spanish": "El Clima Hoy",
            "content": """Today the weather is beautiful. The sun is shining. The sky is blue with some white clouds.

It is warm outside. The temperature is 25 degrees. It is not too hot and not too cold. It is perfect weather.

In the morning, it was a little cloudy. But now, at noon, the sun is out. Many people are in the park. Children are playing. Dogs are running.

My friend asks me: "Do you want to go outside?"
I say: "Yes! Let's go to the park!"

We walk to the park. We sit on the grass. We have a picnic. We eat sandwiches and drink lemonade.

I love sunny days like this. They make me happy.

Tomorrow, the weather will be different. It will rain. But today is perfect.""",
            "vocabulary": "weather, sunny, cloudy, warm, temperature, park, picnic, rain",
            "difficulty": "easy"
        },
    ],
    "A2": [
        {
            "title": "A Trip to the Beach",
            "title_spanish": "Un Viaje a la Playa",
            "content": """Last summer, my family and I went to the beach for a week. It was one of the best vacations of my life.

We woke up early in the morning and drove for three hours. When we arrived, I was so excited to see the ocean. The water was blue and beautiful.

We stayed at a small hotel near the beach. Our room had a nice view of the sea. Every morning, we could hear the waves.

During the day, we did many activities. We swam in the ocean and built sandcastles. My brother and I played beach volleyball. We also went for long walks along the shore.

In the evening, we watched the sunset. The sky turned orange and pink. It was so beautiful. Then we went to restaurants and tried different seafood.

On the last day, I didn't want to leave. I took many photos to remember this trip. I can't wait to go back next summer.

The beach is my favorite place. I feel so relaxed there.""",
            "vocabulary": "vacation, ocean, waves, sunset, sandcastle, seafood, relaxed, memories",
            "difficulty": "easy"
        },
        {
            "title": "Learning to Cook",
            "title_spanish": "Aprendiendo a Cocinar",
            "content": """When I was young, I didn't know how to cook. I always ate at restaurants or bought prepared food. But last year, I decided to learn.

At first, it was difficult. I burned my first dish. The pasta was too soft and the sauce was too salty. But I didn't give up.

I started watching cooking videos on the internet. I also bought a cookbook with easy recipes. Every weekend, I practiced a new dish.

Now, I can cook many things. I can make pasta, rice, and salads. I can bake chicken and fish. My specialty is vegetable soup.

Cooking is not just about food. It is also about creativity. I like to experiment with different ingredients and flavors.

My friends and family enjoy my cooking. Last week, I made dinner for my parents. They were very impressed. "This is delicious!" my mother said.

I am proud of my progress. Cooking has become my new hobby. It is relaxing and rewarding. Plus, it saves money!

Next month, I want to learn to make desserts. I will start with chocolate cake.""",
            "vocabulary": "cook, recipe, ingredients, practice, specialty, creativity, impressed, hobby",
            "difficulty": "medium"
        },
        {
            "title": "My First Job",
            "title_spanish": "Mi Primer Trabajo",
            "content": """I got my first job when I was 18 years old. I worked at a coffee shop near my university.

The job interview was scary. I was very nervous. But the manager was nice and asked simple questions. "Why do you want to work here?" she asked. I said, "I love coffee and I want to learn customer service."

On my first day, I learned how to use the coffee machine. It was complicated at first. I made many mistakes. But my coworkers helped me.

The best part of the job was meeting new people. Many regular customers came every day. I learned their names and their favorite drinks. "Good morning, the usual?" I would ask.

The worst part was waking up early. I started work at 6 AM! But I got used to it.

I worked there for two years. I learned many important things: how to be responsible, how to work in a team, and how to handle stress.

When I left the job, my manager said, "You were a great employee." That made me feel proud.

Now I have a different job, but I will always remember my first one.""",
            "vocabulary": "interview, nervous, customer service, coworker, regular, responsible, stress, employee",
            "difficulty": "medium"
        },
        {
            "title": "Pets and Animals",
            "title_spanish": "Mascotas y Animales",
            "content": """I love animals. I have had different pets throughout my life.

When I was a child, I had a goldfish. His name was Bubbles. He was orange and swam all day in his little bowl. I fed him every morning. Unfortunately, he only lived for one year.

Then, my parents got me a hamster. Her name was Fluffy. She was small and soft. She lived in a cage with a wheel. She ran on the wheel all night! It was noisy, but I loved watching her.

Now, I have a dog named Max. He is a golden retriever. He is big, friendly, and full of energy. We go for walks twice a day. He loves playing fetch in the park.

Having a pet is a big responsibility. You need to feed them, clean after them, and take them to the vet. But they give you so much love in return.

Studies show that pets are good for your health. They reduce stress and make you happier. I agree completely.

In the future, I want to adopt a cat too. I think Max and a cat could be good friends. What do you think?""",
            "vocabulary": "pet, goldfish, hamster, cage, responsibility, vet, adopt, stress",
            "difficulty": "medium"
        },
    ],
    "B1": [
        {
            "title": "The Benefits of Exercise",
            "title_spanish": "Los Beneficios del Ejercicio",
            "content": """Exercise is one of the best things you can do for your health. It doesn't matter how old you are or what shape you're in – physical activity can make a positive difference in your life.

There are many types of exercise to choose from. Some people prefer cardiovascular activities like running, swimming, or cycling. These exercises strengthen your heart and lungs. Others enjoy strength training with weights, which builds muscle and increases bone density.

The benefits of regular exercise are numerous. First, it helps you maintain a healthy weight. When you exercise, you burn calories and build muscle. This combination helps prevent obesity and related diseases.

Second, exercise improves your mental health. Physical activity releases chemicals called endorphins in your brain. These are often called "feel-good" hormones because they reduce stress and anxiety. Many people find that exercise is as effective as medication for treating mild depression.

Third, exercise boosts your energy levels. Although it might seem counterintuitive, using energy through exercise actually gives you more energy throughout the day. Regular exercisers often report sleeping better at night too.

You don't need to spend hours at the gym to see benefits. Health experts recommend at least 150 minutes of moderate activity per week. That's just 30 minutes a day, five days a week. Even small changes, like taking the stairs instead of the elevator, can make a difference.

Start small and gradually increase your activity level. Find an exercise you enjoy, so it doesn't feel like a chore. Your future self will thank you.""",
            "vocabulary": "cardiovascular, strength training, endorphins, obesity, counterintuitive, moderate, chore",
            "difficulty": "medium"
        },
        {
            "title": "Social Media: Pros and Cons",
            "title_spanish": "Redes Sociales: Pros y Contras",
            "content": """Social media has become an integral part of modern life. Platforms like Instagram, Twitter, and TikTok connect billions of people worldwide. But is this connection always positive?

On the positive side, social media keeps us connected with friends and family, regardless of distance. You can share photos, videos, and updates instantly. Long-lost friends can reconnect, and people with similar interests can form communities.

Social media is also a powerful tool for businesses. Companies can reach customers directly and build their brands. Small businesses especially benefit, as they can compete with larger corporations without huge advertising budgets.

Furthermore, social media has given voice to social movements. Activists use these platforms to raise awareness about important issues, from climate change to human rights.

However, there are significant downsides. Many people spend too much time scrolling through feeds, which can lead to addiction. Studies have linked excessive social media use to increased rates of depression and anxiety, particularly among young people.

There's also the problem of misinformation. False news spreads quickly on social media, and it's often difficult to distinguish fact from fiction. This has serious implications for democracy and public health.

Privacy is another concern. Social media companies collect vast amounts of personal data, which raises questions about security and consent.

The key is balance. Social media can be a useful tool when used mindfully. Set time limits, be critical of what you read, and remember that the curated images you see don't represent reality. Real-life connections remain more valuable than virtual ones.""",
            "vocabulary": "integral, platform, activists, misinformation, implications, consent, curated, mindfully",
            "difficulty": "medium"
        },
        {
            "title": "The History of Coffee",
            "title_spanish": "La Historia del Café",
            "content": """Coffee is one of the world's most popular beverages, consumed by millions of people every day. But few people know the fascinating history behind this beloved drink.

Legend has it that coffee was discovered in Ethiopia around the 9th century. A goat herder named Kaldi noticed that his goats became very energetic after eating berries from a certain tree. Curious, he tried the berries himself and felt the same stimulating effect. He had discovered the coffee plant.

From Ethiopia, coffee spread to Yemen and the Arabian Peninsula. By the 15th century, coffeehouses were popular gathering places in the Middle East. They became centers for conversation, chess, and political discussion.

Coffee arrived in Europe in the 17th century and quickly became fashionable. However, some people were suspicious of the new drink. Clergy in Italy even called it the "bitter invention of Satan"! Fortunately, Pope Clement VIII tried coffee and liked it so much that he gave it papal approval.

Coffeehouses soon appeared across Europe. In England, they were called "penny universities" because for the price of a coffee, people could engage in intellectual discussion. Many famous businesses, including Lloyd's of London insurance company, started in coffeehouses.

The coffee industry transformed entire economies. Today, coffee is grown in more than 70 countries, mainly in Latin America, Africa, and Southeast Asia. Brazil is the world's largest producer.

Coffee culture continues to evolve. From espresso bars in Italy to specialty coffee shops worldwide, coffee remains at the center of social life. The next time you enjoy your morning cup, remember you're participating in a tradition that spans centuries.""",
            "vocabulary": "beverage, legend, stimulating, coffeehouse, clergy, papal, intellectual, specialty",
            "difficulty": "hard"
        },
        {
            "title": "Remote Work: The New Normal",
            "title_spanish": "Trabajo Remoto: La Nueva Normalidad",
            "content": """The global pandemic of 2020 forced companies worldwide to rapidly adopt remote work. What started as a temporary measure has become a permanent shift for many organizations.

Before the pandemic, remote work was relatively rare. Only about 5% of workers regularly worked from home. The pandemic changed everything overnight. Suddenly, millions of people set up home offices and learned to use video conferencing tools.

For many workers, remote work has been liberating. They save time and money on commuting. They have more flexibility to manage personal responsibilities. Parents can be more present for their children. Many report higher productivity when working in a quiet home environment.

Companies have also seen benefits. They can reduce expensive office space and access talent from anywhere in the world. Employees aren't limited by geography when job hunting.

However, remote work isn't without challenges. Many people struggle with isolation and loneliness. Without casual office interactions, it's harder to build relationships with colleagues. Some find it difficult to separate work from personal life when both happen in the same space.

There are also concerns about company culture and collaboration. Spontaneous conversations at the coffee machine can lead to creative ideas. These moments are hard to replicate virtually.

The future likely lies in hybrid models, where employees split time between home and office. This approach aims to combine the benefits of both while minimizing the drawbacks.

Whatever form it takes, flexible work is here to stay. The traditional nine-to-five office routine may never fully return.""",
            "vocabulary": "pandemic, adopt, commuting, liberating, productivity, isolation, hybrid, spontaneous",
            "difficulty": "hard"
        },
    ],
    "B2": [
        {
            "title": "Artificial Intelligence in Everyday Life",
            "title_spanish": "Inteligencia Artificial en la Vida Cotidiana",
            "content": """Artificial intelligence, or AI, is no longer science fiction. It's deeply embedded in our daily lives, often in ways we don't even notice.

Every time you use a virtual assistant like Siri or Alexa, you're interacting with AI. These systems use natural language processing to understand your voice commands and respond appropriately. They're constantly learning from interactions, becoming more accurate over time.

AI powers the recommendation algorithms on Netflix, Spotify, and Amazon. These platforms analyze your behavior – what you watch, listen to, or buy – to suggest content you might enjoy. The accuracy of these recommendations is remarkable, though some argue they create "filter bubbles" that limit our exposure to diverse perspectives.

In healthcare, AI is revolutionizing diagnosis and treatment. Machine learning algorithms can analyze medical images and detect diseases like cancer with accuracy comparable to – and sometimes exceeding – human doctors. AI-powered systems are also accelerating drug discovery by analyzing molecular data at unprecedented speeds.

Self-driving cars rely heavily on AI. They use computer vision to interpret their surroundings, make decisions in real-time, and navigate safely. While fully autonomous vehicles aren't yet mainstream, advanced driver assistance features are increasingly common.

However, the rise of AI raises important ethical questions. Algorithms can perpetuate bias if they're trained on biased data. AI systems making decisions about hiring, lending, or criminal justice must be carefully monitored for fairness.

There are also concerns about job displacement. As AI becomes more capable, many routine jobs may be automated. This will require workers to adapt and acquire new skills.

The future with AI holds both tremendous potential and significant challenges. How we navigate this transition will shape society for generations to come.""",
            "vocabulary": "embedded, virtual assistant, algorithms, filter bubbles, revolutionizing, autonomous, perpetuate, displacement",
            "difficulty": "hard"
        },
        {
            "title": "Climate Change: Understanding the Crisis",
            "title_spanish": "Cambio Climático: Entendiendo la Crisis",
            "content": """Climate change is one of the defining challenges of our time. The scientific evidence is overwhelming: human activities are warming the planet at an unprecedented rate, with far-reaching consequences.

Since the Industrial Revolution, the burning of fossil fuels has released billions of tons of carbon dioxide into the atmosphere. These greenhouse gases trap heat, causing global temperatures to rise. The average global temperature has increased by approximately 1.1°C compared to pre-industrial levels.

The effects of this warming are already visible. Extreme weather events – hurricanes, droughts, wildfires, and floods – are becoming more frequent and intense. Polar ice caps are melting, causing sea levels to rise and threatening coastal communities.

Biodiversity is suffering too. Many species cannot adapt quickly enough to changing conditions. Coral reefs, home to a quarter of marine life, are bleaching and dying as ocean temperatures rise and waters become more acidic.

The consequences extend to human society. Agricultural patterns are disrupted, affecting food security. Climate refugees are forced to flee their homes due to environmental degradation. Health impacts include increased respiratory diseases and the spread of tropical infections to new areas.

Addressing climate change requires urgent, coordinated action. The Paris Agreement aims to limit warming to 1.5°C, but current commitments fall short. Transitioning to renewable energy, improving efficiency, and protecting forests are essential steps.

Individual actions matter too. Reducing consumption, choosing sustainable products, eating less meat, and using public transportation can all contribute. Perhaps most importantly, citizens must demand stronger action from governments and businesses.

The next decade is crucial. The choices we make now will determine the future of our planet.""",
            "vocabulary": "unprecedented, greenhouse gases, biodiversity, bleaching, degradation, coordinated, sustainable, crucial",
            "difficulty": "hard"
        },
        {
            "title": "The Psychology of Habits",
            "title_spanish": "La Psicología de los Hábitos",
            "content": """Habits are the invisible architecture of our lives. Research suggests that up to 40% of our daily actions are not conscious decisions but habits – automatic behaviors triggered by specific cues.

Understanding how habits work is key to changing them. According to psychologists, every habit consists of three components: a cue, a routine, and a reward. The cue triggers the behavior, the routine is the behavior itself, and the reward is what makes the behavior worth remembering.

For example, consider the habit of checking your phone first thing in the morning. The cue is waking up. The routine is reaching for your phone. The reward is the dopamine hit from seeing new notifications. Understanding this loop is the first step toward changing it.

Bad habits are notoriously difficult to break. This is because they're wired into our neural pathways. The more we repeat a behavior, the stronger these pathways become. That's why willpower alone often fails – you're fighting against your own brain.

Successful habit change typically involves replacing the routine while keeping the same cue and reward. If stress (cue) leads you to snack (routine) for comfort (reward), you might replace snacking with taking a short walk, which can provide similar stress relief.

Creating new habits requires repetition and patience. Research suggests it takes an average of 66 days for a new behavior to become automatic, though this varies widely. Starting small increases the chances of success. Want to exercise more? Begin with just five minutes a day.

Environment design is also crucial. If you want to read more, keep books visible and your phone out of reach. If you want to eat healthier, don't keep junk food in the house. Make good habits easy and bad habits difficult.

The compounding effect of small habits is remarkable. Improving by just 1% each day leads to extraordinary results over time. As the saying goes, "We are what we repeatedly do.""",
            "vocabulary": "invisible, triggered, dopamine, neural pathways, willpower, compounding, repetition, extraordinary",
            "difficulty": "hard"
        },
    ],
    "C1": [
        {
            "title": "The Paradox of Choice",
            "title_spanish": "La Paradoja de la Elección",
            "content": """In modern consumer societies, we are bombarded with choices. From dozens of varieties of cereal in supermarkets to hundreds of streaming options, abundance has become the norm. Conventional wisdom suggests that more choice equals more freedom and satisfaction. But is this assumption valid?

Psychologist Barry Schwartz argues that excessive choice can actually be debilitating. His research demonstrates that while some choice is undoubtedly better than none, there's a point where additional options become counterproductive. He calls this phenomenon the "paradox of choice."

Consider the famous jam study by Sheena Iyengar. Shoppers were presented with either 6 or 24 varieties of jam. While more people stopped at the larger display, those who encountered the smaller selection were ten times more likely to actually purchase jam. The abundance of options led to decision paralysis.

The psychological mechanisms behind this are revealing. With numerous options, evaluating alternatives becomes cognitively exhausting. Even after making a decision, doubts linger. "Did I choose the best one? What if another option would have been better?" This counterfactual thinking diminishes satisfaction with our choices.

Schwartz distinguishes between "maximizers" who seek the optimal choice and "satisficers" who choose what's good enough. Maximizers, despite often making objectively better choices, report less satisfaction. The pursuit of perfection becomes its own burden.

The implications extend beyond consumer choices to major life decisions: careers, partners, living locations. Having more options can lead to perpetual dissatisfaction and the fear of missing out – now enshrined in the acronym FOMO.

So what's the solution? Schwartz recommends embracing "good enough" decisions, limiting our options deliberately, practicing gratitude for what we have, and lowering expectations. In essence, learning to appreciate rather than optimize.

In an age of infinite possibilities, the ability to choose decisively and be content with our choices may be one of the most valuable skills we can cultivate.""",
            "vocabulary": "paradox, debilitating, counterproductive, paralysis, cognitively, counterfactual, maximizers, enshrined",
            "difficulty": "hard"
        },
        {
            "title": "The Future of Work in the Age of Automation",
            "title_spanish": "El Futuro del Trabajo en la Era de la Automatización",
            "content": """The automation of work is not a new phenomenon. From the agricultural revolution to the industrial revolution to the digital revolution, technology has continuously transformed how humans earn their living. Yet the current wave of automation, driven by advances in artificial intelligence and robotics, may be qualitatively different.

Previous technological shifts generally displaced specific types of work while creating new categories of employment. The automobile eliminated jobs for blacksmiths and stable hands but created millions of jobs in manufacturing, repair, and transportation services. The net effect on employment was often positive.

Today's AI systems, however, can perform cognitive tasks that were once considered exclusively human. Machine learning algorithms can analyze legal documents, diagnose diseases, compose music, and write articles. The range of activities that could potentially be automated is expanding rapidly.

Economic research suggests that 47% of US jobs are at high risk of automation in the coming decades. Jobs with routine, predictable tasks are most vulnerable, including many white-collar professions. Paradoxically, some manual jobs requiring physical dexterity and situational judgment – plumbers, caregivers, construction workers – may prove more resistant to automation than roles requiring analytical skills.

The distribution of impacts will likely be uneven. Low-skilled workers may find fewer opportunities as entry-level positions are automated. High-skilled workers who can leverage AI as a tool may see their productivity and earnings increase. This could exacerbate existing inequality.

Societies will need to adapt their institutions. Education systems must focus on skills that complement rather than compete with AI: creativity, emotional intelligence, ethical reasoning, and adaptability. Social safety nets may require expansion or reinvention, with some proposing universal basic income as a response to potential widespread displacement.

Ultimately, the future is not predetermined. The same technologies that threaten jobs can create new opportunities and increase prosperity. How we navigate this transition – through policy choices, educational investments, and social adaptations – will determine whether automation becomes a force for shared flourishing or deepening division.""",
            "vocabulary": "qualitatively, displaced, cognitive, paradoxically, dexterity, exacerbate, complement, predetermined",
            "difficulty": "hard"
        },
    ],
    "C2": [
        {
            "title": "The Nature of Consciousness: Philosophy Meets Neuroscience",
            "title_spanish": "La Naturaleza de la Conciencia: Filosofía y Neurociencia",
            "content": """Few questions have puzzled humanity as persistently as the nature of consciousness. What gives rise to subjective experience? How does the electrochemical activity of neurons generate the vivid inner life that each of us knows intimately? This is what philosopher David Chalmers famously termed "the hard problem of consciousness."

Contemporary neuroscience has made remarkable strides in identifying the neural correlates of consciousness – the brain states associated with specific conscious experiences. We can observe which regions activate when someone sees red, feels pain, or experiences an emotion. Yet correlation is not explanation. Knowing which neurons fire tells us little about why there is subjective experience at all.

Consider the thought experiment of "philosophical zombies" – hypothetical beings physically identical to humans but lacking inner experience. They would behave exactly as we do, respond to stimuli appropriately, even claim to be conscious, but there would be "nobody home." The fact that such beings seem conceivable suggests that consciousness cannot be logically derived from physical properties alone.

Materialists respond that consciousness will eventually be explained by increasingly sophisticated neuroscience, just as life was demystified by molecular biology. Perhaps our intuition that consciousness is special is simply mistaken – a remnant of dualistic thinking. Daniel Dennett provocatively argues that the hard problem is an illusion generated by our conceptual confusion about the nature of mind.

Alternative theories abound. Integrated Information Theory proposes that consciousness is a fundamental property of systems that integrate information in specific ways – potentially extending to non-biological entities. Panpsychism suggests that consciousness is a basic feature of reality, present to some degree in all matter. These ideas, once dismissed as mysticism, are receiving serious consideration from mainstream philosophers and scientists.

The question of machine consciousness adds urgency to these debates. As AI systems become more sophisticated, will they eventually experience something? If so, will we recognize it? Our inability to detect consciousness directly means we might create suffering entities without awareness.

Whatever the resolution, the investigation of consciousness remains one of the most profound intellectual challenges of our age, sitting at the intersection of philosophy, neuroscience, physics, and computer science.""",
            "vocabulary": "electrochemical, correlates, conceivable, materialists, demystified, dualistic, panpsychism, entities",
            "difficulty": "hard"
        },
    ]
}


def seed_additional_readings():
    """Agregar lecturas adicionales a la base de datos"""
    with app.app_context():
        print("="*70)
        print("📚 AGREGANDO LECTURAS ADICIONALES")
        print("="*70)
        
        # Mapeo de nivel a rango de unit_number (asumiendo 12 unidades por nivel)
        LEVEL_RANGES = {
            "A1": (1, 12),
            "A2": (13, 24),
            "B1": (25, 36),
            "B2": (37, 48),
            "C1": (49, 60),
            "C2": (61, 72)
        }
        
        readings_added = 0
        skipped = 0
        
        for level, readings in READINGS_BY_LEVEL.items():
            # Obtener unidades de este nivel por unit_number
            start_num, end_num = LEVEL_RANGES.get(level, (1, 12))
            units = Unit.query.filter(
                Unit.unit_number >= start_num,
                Unit.unit_number <= end_num
            ).all()
            
            if not units:
                print(f"⚠️ No se encontraron unidades para nivel {level} (units {start_num}-{end_num})")
                continue
            
            for idx, reading_data in enumerate(readings):
                # Asignar a una unidad (rotando entre las disponibles)
                unit = units[idx % len(units)]
                
                # Verificar si ya existe
                existing = Reading.query.filter_by(title=reading_data['title']).first()
                if existing:
                    skipped += 1
                    continue
                
                # El modelo Reading tiene: unit_id, title, content, difficulty, instructions, order
                # No tiene: title_spanish, vocabulary
                # Añadimos el vocabulario y título en español a las instrucciones
                instructions_text = f"📘 {reading_data['title_spanish']}\n\n"
                instructions_text += f"Vocabulary: {reading_data.get('vocabulary', '')}"
                
                reading = Reading(
                    unit_id=unit.id,
                    title=reading_data['title'],
                    content=reading_data['content'],
                    difficulty=reading_data.get('difficulty', 'medium'),
                    instructions=instructions_text
                )
                db.session.add(reading)
                readings_added += 1
        
        db.session.commit()
        
        # Contar lecturas totales por nivel
        print(f"\n✅ Lecturas agregadas: {readings_added}")
        print(f"⏭️  Omitidas (ya existían): {skipped}")
        
        print(f"\n📊 Total de lecturas por nivel:")
        for level, (start_num, end_num) in LEVEL_RANGES.items():
            # Contar lecturas de unidades de este nivel
            count = db.session.query(Reading).join(Unit).filter(
                Unit.unit_number >= start_num,
                Unit.unit_number <= end_num
            ).count()
            print(f"   {level}: {count}")
        
        total = Reading.query.count()
        units_count = Unit.query.count()
        print(f"\n📈 Promedio: {total/max(units_count,1):.1f} lecturas por unidad")
        print("="*70)


if __name__ == '__main__':
    seed_additional_readings()
