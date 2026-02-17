#!/usr/bin/env python3
"""
Script para agregar lecturas a todas las unidades del sistema.
Ejecutar: python seed_all_readings.py
"""

import os
import sys

# Agregar el directorio padre al path para importar app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Reading, Unit

def add_readings():
    """Agrega lecturas a todas las unidades."""
    
    app = create_app()
    with app.app_context():
        print("=" * 70)
        print("AGREGANDO LECTURAS A TODAS LAS UNIDADES")
        print("=" * 70)
        
        # Unit 7 - MIND (La Mente)
        unit7_readings = [
            {
                "title": "La Felicidad es Diferente para Todos",
                "content": """Happiness means different things to different people. Some people find happiness in money, while others find it in simple moments with family. In today's world, social media shows us perfect lives that don't really exist. We compare ourselves to others and feel sad. But real happiness comes from inside. It comes from doing things we love, helping others, and being grateful for what we have. Research shows that practicing gratitude every day makes us happier. Even small things like drinking a good coffee or walking in nature can bring joy. Happiness is not about having everything. It's about appreciating what you already have. When you stop comparing your life with others, you start to see your own happiness.""",
                "difficulty": "beginner",
                "instructions": "Extract 3-5 key sentences that explain what happiness really is.",
                "order": 1
            },
            {
                "title": "Cómo Internet Cambió Nuestro Cerebro",
                "content": """The internet has changed how our brains work. Twenty years ago, we memorized phone numbers and addresses. Now, we Google everything. Our brains have adapted to this new way of living. We are good at finding information, but we are worse at remembering things. Scientists say we spend too much time on screens. This affects our ability to concentrate. When we read a book without checking our phones, we can't focus for more than a few minutes. Our brains have become used to quick, short pieces of information. This is called "continuous partial attention." However, the internet has also made learning easier. We can watch educational videos, take online courses, and read articles about anything. The key is balance. We need to use technology wisely. Our brains are powerful, but they need rest. If we don't give them time offline, we will lose important skills like deep thinking and creativity.""",
                "difficulty": "intermediate",
                "instructions": "Extract the main ideas about how the internet affects our brains.",
                "order": 2
            },
            {
                "title": "Inteligencia Emocional vs Inteligencia Académica",
                "content": """Intelligence is not just about getting good grades in school. There is something called emotional intelligence. People with high emotional intelligence understand their feelings and the feelings of others. They can manage stress better. They have better relationships. Studies show that emotional intelligence is more important for success in life than academic intelligence. A person with good grades but poor social skills might struggle at work. A person who understands people, listens well, and shows empathy will do better. This doesn't mean academic intelligence is not important. Both are necessary. But in today's world, we focus too much on grades and test scores. We forget to teach children how to manage anger, how to be kind, and how to communicate. Emotional intelligence can be learned. You can develop it at any age. Start by being aware of your feelings. Notice when you are angry, sad, or anxious. Ask yourself why you feel this way. Then, practice controlling your reactions. This is the first step to developing emotional intelligence.""",
                "difficulty": "intermediate",
                "instructions": "What are the key differences between emotional and academic intelligence? Extract relevant sentences.",
                "order": 3
            }
        ]
        
        # Unit 8 - ART (Arte)
        unit8_readings = [
            {
                "title": "El Poder de la Música en Nuestras Vidas",
                "content": """Music is a universal language. No matter where you come from, music makes you feel emotions. It can make you happy, sad, energetic, or calm. Scientists have discovered that music affects our brains in powerful ways. When we listen to music we like, our brains release dopamine, which is the happiness chemical. Music therapy is now used in hospitals to help patients recover faster. It reduces stress and pain. Many students study better with music in the background. Classical music, especially, helps people focus. But music is not just about health. It is about culture and identity. Every country has its own music style. Through music, we learn about other cultures. We understand different ways of living. Musicians tell stories with their instruments. They express feelings that words cannot express. If you have never tried learning an instrument, consider starting today. You don't need to be talented. You just need to enjoy the process. Music is for everyone.""",
                "difficulty": "beginner",
                "instructions": "Extract sentences that explain why music is important for our health and emotions.",
                "order": 1
            },
            {
                "title": "Arte Moderno y su Significado",
                "content": """Modern art is confusing for many people. You look at a painting that looks like random colors or strange shapes, and you wonder: Is this really art? The answer is yes. Modern art is not about making things look realistic. It is about expressing ideas and emotions. An artist might paint something ugly or disturbing to make us think about a problem in society. Abstract art doesn't show real objects. Instead, it shows feelings. A blue painting might represent sadness or calm. Red might represent anger or passion. When you look at modern art, you don't need to understand the artist's exact message. You just need to feel something. Your reaction is valid. Modern art challenges us to think differently. It tells us that art can be anything. It breaks the rules of traditional art. Some people hate modern art because it is so different. But this is exactly why it is important. Art should make us uncomfortable sometimes. It should make us question our beliefs. Great artists are those who are brave enough to be different.""",
                "difficulty": "intermediate",
                "instructions": "Explain what modern art is trying to do according to this text. Extract key ideas.",
                "order": 2
            },
            {
                "title": "Las Películas Que Cambian Perspectivas",
                "content": """Movies are more than entertainment. They can change how we see the world. A great film makes you think about important topics. It can make you sympathize with someone you would never meet in real life. When you watch a movie from a different country or culture, you learn about their values and struggles. Cinema is a powerful tool for education. During difficult times, movies give us hope and inspiration. They remind us that we are not alone in our struggles. Some movies tackle serious problems like racism, poverty, or environmental destruction. Watching these films helps us understand these issues better. After watching them, we might want to make a difference. Movies can make you laugh, cry, and think. They unite people across the world. In movie theaters, strangers sit together and share emotions. This is magical. In our digital world, where everyone is isolated, movies remind us that we are all human. We all have fears, dreams, and hopes. If you want to watch a movie that teaches you something new, choose one from a different country or one about a topic you know nothing about. You might discover something wonderful.""",
                "difficulty": "intermediate",
                "instructions": "How can movies change our perspective? Extract 3-4 main ideas from the text.",
                "order": 3
            }
        ]
        
        # Unit 9 - MONEY (Dinero)
        unit9_readings = [
            {
                "title": "Cómo Enseñar a los Niños Sobre el Dinero",
                "content": """Teaching children about money is one of the most important things parents can do. Children who learn about money early develop better financial habits as adults. Start small. Give your children a small allowance and let them decide how to spend it. They will learn from their mistakes. If they spend all their money on candy in one day, they will understand why they don't have money later. This is a valuable lesson. Teach them the difference between needs and wants. They need food and clothes, but they want video games and candy. When children understand this difference, they make better choices. Let them save money for something they really want. This teaches patience and goal-setting. You can also teach them about work. When children see their parents working and earning money, they understand that money doesn't just appear. It is earned. Encourage them to do chores and pay them for it. This shows them the connection between work and money. Most importantly, talk about money without shame. Many parents are embarrassed to discuss money with their children. But this silence creates financial problems later. Children should grow up understanding how money works, how to save, and how to spend responsibly.""",
                "difficulty": "beginner",
                "instructions": "What are the main ways to teach children about money? Extract key advice.",
                "order": 1
            },
            {
                "title": "La Filantropía y Dar sin Esperar Nada",
                "content": """Philanthropy is the act of giving money or time to help others. Rich people often give to charity, but philanthropy is for everyone. You don't need to be wealthy to help others. You can volunteer your time. You can donate a small amount of money. You can share your skills. Giving to others has surprising benefits for yourself. Studies show that people who help others are happier. They feel more connected to their community. They have better mental health. When you see the direct impact of your giving, it feels amazing. Maybe you gave money to build a school in a poor village. Now you see a photo of children studying there. You feel proud. You feel like you made a real difference. Philanthropy also fights inequality. When rich people help poor people, the gap between them becomes smaller. Society becomes more stable and peaceful. But philanthropy has limits. Governments should provide basic services like education and healthcare. Charity alone cannot fix systemic poverty. However, individual acts of kindness are still important. Every dollar, every hour, every skill you donate helps someone. Start small. Find a cause you care about. Maybe it's animals, the environment, or helping homeless people. Then, give what you can. Your contribution matters more than you think.""",
                "difficulty": "intermediate",
                "instructions": "Extract sentences explaining what philanthropy is and why it's important.",
                "order": 2
            },
            {
                "title": "Trabajo Remoto y Nuevas Oportunidades Económicas",
                "content": """The pandemic changed how we work. Before 2020, most people went to an office every day. Now, many work from home. This has created new opportunities. People from small towns can now work for international companies. They don't need to move to a big city to earn good money. A programmer in India can work for a company in the United States and earn a good salary. A freelance designer can take projects from all over the world. Remote work has given people freedom. You can work from anywhere. You choose your schedule. This is life-changing for parents who want to spend time with their children. It's also good for the environment because fewer people drive to work. However, remote work has challenges. It's hard to have work-life balance when your home is also your office. Distractions are everywhere. Also, not all jobs can be remote. A nurse, a teacher, or a mechanic must go somewhere. But for jobs that involve a computer, remote work is now normal. Companies are realizing that productivity doesn't depend on being in an office. As this trend continues, it will create new economic opportunities for people who develop digital skills. If you want economic freedom, learn to work online.""",
                "difficulty": "intermediate",
                "instructions": "What new opportunities has remote work created? Extract main ideas.",
                "order": 3
            }
        ]
        
        # Unit 10 - SCIENCE AND TECHNOLOGY
        unit10_readings = [
            {
                "title": "La Inteligencia Artificial y el Futuro del Trabajo",
                "content": """Artificial Intelligence is developing very quickly. AI can now recognize faces, translate languages, and even write essays. Many people are worried that AI will take their jobs. This fear is partly reasonable. Some jobs will disappear. Factories that employed thousands now use robots. Customer service jobs are being replaced by chatbots. But history shows us that new technology creates new jobs. When cars were invented, people thought horses would disappear and horse workers would suffer. But car manufacturing created millions of jobs. The same will happen with AI. New jobs will be created that we haven't imagined yet. Right now, we need AI trainers, AI ethicists, and people who understand how to work alongside AI. The key is education. If you want job security in the future, learn skills that AI cannot do. AI is good at analyzing data and doing repetitive tasks. But AI cannot create art, understand complex human emotions, or make ethical decisions. It cannot replace human connection and creativity. So learn these skills. Take art classes. Study psychology. Practice communication. Learn to work with technology, not against it. The future belongs to people who understand both technology and humanity.""",
                "difficulty": "intermediate",
                "instructions": "What does the text say about AI and jobs? Extract key points about the future.",
                "order": 1
            },
            {
                "title": "Viajes al Espacio y Aventura Humana",
                "content": """For centuries, humans dreamed of visiting space. It seemed impossible. Then, in 1961, Yuri Gagarin became the first human in space. Twelve years later, humans walked on the moon. This was humanity's greatest achievement. For decades, only governments sent people to space. But now, private companies are making space travel possible for regular people. SpaceX, Blue Origin, and other companies are building rockets that can carry tourists to space. In a few years, anyone with enough money will be able to visit space. This sounds like science fiction, but it's real. Soon, there will be hotels in space. Scientists are researching how to live on Mars. These are not dreams anymore. They are plans. Why is this important? First, exploring space pushes technology forward. Every innovation developed for space has been used on Earth. Second, seeing Earth from space changes people's perspective. Astronauts say that from space, you realize how small and precious our planet is. Our borders disappear. Our conflicts seem small. Maybe humanity needs this perspective. We need to look up at the stars and remember that we are all on one planet together. If you love adventure and want to be part of history, space might be your future.""",
                "difficulty": "intermediate",
                "instructions": "Why is space exploration important according to this text? Extract main reasons.",
                "order": 2
            },
            {
                "title": "Dispositivos Inteligentes en el Hogar",
                "content": """Smart home technology is now affordable. You can buy devices that control your lights, temperature, and security from your phone. Alexa, Google Home, and other smart speakers understand voice commands. You can say "turn on the lights" and it happens. This technology is convenient. But is it safe? These devices are listening to everything you say. They record your conversations to improve their services. Your data is stored on company servers. This raises privacy concerns. Companies know what you like, when you leave home, and when you return. Hackers could potentially access this information. However, smart home technology also has real benefits. Elderly people can use voice commands instead of struggling with buttons. People with disabilities can control their environment. Home security systems using smart cameras can prevent burglaries. Smart thermostats save energy and money. The key is understanding the trade-off. You give up some privacy for convenience. Some people think this is worth it. Others don't. The important thing is to make an informed choice. If you use smart devices, read the privacy policy. Understand what data is collected. Use strong passwords. Be aware of what these devices can and cannot do. Technology is here to improve our lives, not to control us.""",
                "difficulty": "beginner",
                "instructions": "Extract the benefits and concerns about smart home devices mentioned in the text.",
                "order": 3
            }
        ]
        
        # Unit 11 - NATURAL WORLD
        unit11_readings = [
            {
                "title": "La Belleza de los Océanos y la Crisis del Plástico",
                "content": """Oceans cover seventy percent of our planet, yet we know very little about them. The ocean is home to millions of species. Some animals live so deep that scientists have never seen them alive. The ocean is beautiful and mysterious. But the ocean is in crisis. Every year, millions of tons of plastic enter the ocean. Fish eat plastic thinking it is food. Whales and dolphins get tangled in fishing nets. Sea turtles eat plastic bags that look like jellyfish. The plastic never disappears. It breaks into tiny pieces called microplastics. These microplastics enter the food chain. When we eat fish, we might be eating plastic. This affects our health. The problem is clear: we use too much plastic, and we don't dispose of it properly. But what can we do? First, reduce plastic use. Use reusable bags, bottles, and containers. Second, recycle when possible. Third, support policies that limit single-use plastics. Fourth, participate in beach cleanups. If every person picks up just one piece of plastic, imagine how much cleaner our oceans would be. The ocean is not someone else's responsibility. It is ours. We depend on it for oxygen, food, and stability. If we don't protect it now, our future generations will suffer.""",
                "difficulty": "beginner",
                "instructions": "What are the main problems facing our oceans? Extract 3-4 key issues.",
                "order": 1
            },
            {
                "title": "Fotografía de Vida Salvaje: Documentar la Naturaleza",
                "content": """Wildlife photographers travel to the most remote places on Earth. They photograph animals in their natural habitats. They wait for hours in the rain and cold just to capture one perfect moment. Why? Because their photographs tell important stories. A powerful image of a polar bear on melting ice can convince more people about climate change than a hundred scientific papers. A photo of a hunter killing an elephant can start a movement to protect endangered species. Wildlife photography combines art, adventure, and conservation. Great wildlife photographers are patient, brave, and skilled. They understand animal behavior. They know when to take the shot. They respect the animals and the environment. Photographers like National Geographic's legendary wildlife specialists have taught the world about nature through their images. These photographs inspire people to protect wildlife. When you see a beautiful animal and learn that it is endangered, you want to help. This is the power of photography. It creates emotional connection. In our digital world where we spend most of our time indoors, wildlife photography reminds us of the beauty that exists outside. It reminds us why we need to protect nature. If you love animals and nature, consider wildlife photography. You don't need expensive equipment to start. A good camera and passion are enough.""",
                "difficulty": "intermediate",
                "instructions": "Why is wildlife photography important? Extract the main reasons from the text.",
                "order": 2
            },
            {
                "title": "Las Maravillas Naturales del Mundo",
                "content": """Our planet has incredible natural wonders. From the Grand Canyon to Victoria Falls, from the Amazon rainforest to the Great Barrier Reef, nature creates masterpieces. These places are not just beautiful. They are also important for our survival. The Amazon rainforest produces twenty percent of the world's oxygen. It is called the lungs of the planet. The Great Barrier Reef is home to thousands of marine species. It protects coastlines from storms. Wetlands filter water and prevent floods. Forests regulate climate and provide medicines. These natural systems are interconnected. When we damage one part, we affect the whole system. Yet we continue to destroy nature. We cut down forests for agriculture and development. We drain wetlands to build cities. We pollute coral reefs with chemicals and plastic. Every animal and plant we lose is permanent. We cannot bring back a species once it is extinct. The good news is that many people around the world are working to protect these wonders. National parks and protected areas have been created. Reforestation projects are planting millions of trees. People are learning that nature is not something we own. We are part of nature. We depend on it. Protecting natural wonders is not a choice. It is a necessity. Start locally. If you live near a forest or river, learn about it. Visit it. Understand its importance. Then, help protect it.""",
                "difficulty": "intermediate",
                "instructions": "What role do natural wonders play in our survival? Extract key information.",
                "order": 3
            }
        ]
        
        # Unit 12 - CITIES AND COMMUNITIES
        unit12_readings = [
            {
                "title": "Ciudades Sostenibles del Futuro",
                "content": """Cities are growing. Soon, most humans will live in urban areas. Current cities have problems: traffic, pollution, overcrowding, and expensive housing. What will cities look like in the future? Sustainable cities will be different. They will have public transportation so good that nobody needs a car. Imagine buses, trains, and bicycles as the main ways to move. This reduces pollution and traffic. Buildings will be designed to use renewable energy. Solar panels on roofs, wind turbines, and geothermal heating will power homes and offices. Green spaces will be everywhere. Parks, gardens, and trees will improve air quality and people's mental health. Housing will be affordable. Nobody will be homeless. Work will be close to home, so nobody spends hours commuting. People will grow food in urban gardens. Some of these cities already exist in small ways. Copenhagen is known for bicycling. Curitiba in Brazil has excellent public transportation. Singapore is planting millions of trees. But we need more cities to transform. This requires government support and citizen participation. If you live in a city, you can help. Support public transportation. Vote for politicians who care about the environment. Plant trees. Use less energy. Every action counts. Cities should be places where humans and nature thrive together.""",
                "difficulty": "intermediate",
                "instructions": "Describe the characteristics of future sustainable cities. Extract key features.",
                "order": 1
            },
            {
                "title": "Comunidades Locales y Sentido de Pertenencia",
                "content": """In modern society, many people feel isolated. We live in cities full of millions but feel lonely. We know our neighbors, but we don't talk to them. We text our friends but never see them. This is a serious problem. Humans are social beings. We need community. A strong community has many benefits. It improves mental health. It provides support during difficult times. It creates safety. In a tight community, people watch out for each other. Crime is lower because neighbors care about each other. Communities also preserve culture and traditions. Immigrants create communities to maintain their heritage. Local traditions and celebrations bring people together. Young people learn from elders. Culture survives. But how do we build community in the modern world? First, participate in local activities. Go to neighborhood events. Join clubs. Volunteer. Second, know your neighbors. Organize dinners or meetings. Share skills. If you know how to fix something, help your neighbor. If they know how to cook, learn from them. Third, support local businesses. Buy from small shops instead of big chains. This keeps money in the community. Fourth, use social media for community building, not just socializing. Create groups where people share resources and help each other. Strong communities can solve problems that governments cannot solve. Start building community today.""",
                "difficulty": "beginner",
                "instructions": "What are the benefits of strong communities? Extract main ideas.",
                "order": 2
            },
            {
                "title": "Inmigración y Diversidad Cultural",
                "content": """Millions of people immigrate to new countries every year. They leave their homes for better opportunities. They want better education, better jobs, safety, or freedom. Immigration is complicated. For immigrants, it is both exciting and scary. They must learn a new language and new customs. They may face discrimination. They miss their families. But immigrants also bring valuable things to their new countries. They bring new ideas, skills, and perspectives. They work hard. They create businesses. Studies show that immigrants are more likely to start companies than people born in the country. They create jobs for others. Culturally, immigrants make cities more vibrant. Different cuisines, music, art, and traditions make places interesting. Children grow up understanding different ways of life. This creates more tolerant and open-minded societies. However, immigration can create tensions. If people feel that immigrants are taking jobs or resources, resentment grows. This leads to discrimination and violence. Governments must manage immigration well. They must provide support for immigrants but also ensure that the process is fair. Most importantly, citizens must understand that immigration is human. When people immigrate, they are not criminals or invaders. They are humans seeking better lives, just like anyone would do. If you live in a diverse community, embrace it. Learn about different cultures. Support immigrant communities. Diversity makes us stronger.""",
                "difficulty": "intermediate",
                "instructions": "What are the benefits and challenges of immigration? Extract key points.",
                "order": 3
            }
        ]
        
        # Diccionario de lecturas por unidad
        readings_by_unit = {
            7: unit7_readings,
            8: unit8_readings,
            9: unit9_readings,
            10: unit10_readings,
            11: unit11_readings,
            12: unit12_readings
        }
        
        # Agregar lecturas
        for unit_number, readings_list in readings_by_unit.items():
            unit = Unit.query.filter_by(unit_number=unit_number).first()
            if unit:
                for reading_data in readings_list:
                    # Verificar si la lectura ya existe
                    existing = Reading.query.filter_by(
                        unit_id=unit.id,
                        title=reading_data["title"]
                    ).first()
                    
                    if not existing:
                        reading = Reading(
                            unit_id=unit.id,
                            title=reading_data["title"],
                            content=reading_data["content"],
                            difficulty=reading_data["difficulty"],
                            instructions=reading_data["instructions"],
                            order=reading_data["order"]
                        )
                        db.session.add(reading)
                        print(f"✓ Lectura agregada: {reading_data['title']} (Unit {unit_number})")
                    else:
                        print(f"- Lectura ya existe: {reading_data['title']} (Unit {unit_number})")
                        
        db.session.commit()
        
        print("\n" + "=" * 70)
        print("✅ ¡TODAS LAS LECTURAS AGREGADAS EXITOSAMENTE!")
        print("=" * 70)

if __name__ == "__main__":
    add_readings()
