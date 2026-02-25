import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import KidsTopic, KidsVocabulary

app = create_app()

def seed_more_kids_topics():
    with app.app_context():
        print("Inyectando nuevos temas a la Kids Zone...")

        # ==========================================
        # TEMA 3: NUMBERS (Números)
        # ==========================================
        numbers_topic = KidsTopic.query.filter_by(title="Numbers 1-5").first()
        if not numbers_topic:
            print("Creando: Numbers 1-5...")
            numbers_topic = KidsTopic(
                title="Numbers 1-5",
                description="¡Aprende a contar hasta 5!",
                cover_image="Rocket",
                order=3
            )
            db.session.add(numbers_topic)
            db.session.commit()

            numbers_vocab = [
                KidsVocabulary(topic_id=numbers_topic.id, word_english="One", word_spanish="Uno", image_url="1️⃣", audio_url_en="one.mp3"),
                KidsVocabulary(topic_id=numbers_topic.id, word_english="Two", word_spanish="Dos", image_url="2️⃣", audio_url_en="two.mp3"),
                KidsVocabulary(topic_id=numbers_topic.id, word_english="Three", word_spanish="Tres", image_url="3️⃣", audio_url_en="three.mp3"),
                KidsVocabulary(topic_id=numbers_topic.id, word_english="Four", word_spanish="Cuatro", image_url="4️⃣", audio_url_en="four.mp3"),
                KidsVocabulary(topic_id=numbers_topic.id, word_english="Five", word_spanish="Cinco", image_url="5️⃣", audio_url_en="five.mp3")
            ]
            db.session.add_all(numbers_vocab)

        # ==========================================
        # TEMA 4: FRUITS (Frutas)
        # ==========================================
        fruits_topic = KidsTopic.query.filter_by(title="Yummy Fruits").first()
        if not fruits_topic:
            print("Creando: Yummy Fruits...")
            fruits_topic = KidsTopic(
                title="Yummy Fruits",
                description="¡Frutas deliciosas y saludables!",
                cover_image="Apple",
                order=4
            )
            db.session.add(fruits_topic)
            db.session.commit()

            fruits_vocab = [
                KidsVocabulary(topic_id=fruits_topic.id, word_english="Apple", word_spanish="Manzana", image_url="🍎", audio_url_en="apple.mp3"),
                KidsVocabulary(topic_id=fruits_topic.id, word_english="Banana", word_spanish="Plátano", image_url="🍌", audio_url_en="banana.mp3"),
                KidsVocabulary(topic_id=fruits_topic.id, word_english="Orange", word_spanish="Naranja", image_url="🍊", audio_url_en="orange.mp3"),
                KidsVocabulary(topic_id=fruits_topic.id, word_english="Grapes", word_spanish="Uvas", image_url="🍇", audio_url_en="grapes.mp3"),
                KidsVocabulary(topic_id=fruits_topic.id, word_english="Strawberry", word_spanish="Fresa", image_url="🍓", audio_url_en="strawberry.mp3")
            ]
            db.session.add_all(fruits_vocab)

        # ==========================================
        # TEMA 5: MY FAMILY (Mi Familia)
        # ==========================================
        family_topic = KidsTopic.query.filter_by(title="My Family").first()
        if not family_topic:
            print("Creando: My Family...")
            family_topic = KidsTopic(
                title="My Family",
                description="¿Cómo se dice mamá y papá?",
                cover_image="Family",
                order=5
            )
            db.session.add(family_topic)
            db.session.commit()

            family_vocab = [
                KidsVocabulary(topic_id=family_topic.id, word_english="Mother", word_spanish="Mamá", image_url="👩", audio_url_en="mother.mp3"),
                KidsVocabulary(topic_id=family_topic.id, word_english="Father", word_spanish="Papá", image_url="👨", audio_url_en="father.mp3"),
                KidsVocabulary(topic_id=family_topic.id, word_english="Baby", word_spanish="Bebé", image_url="👶", audio_url_en="baby.mp3"),
                KidsVocabulary(topic_id=family_topic.id, word_english="Grandpa", word_spanish="Abuelo", image_url="👴", audio_url_en="grandpa.mp3"),
                KidsVocabulary(topic_id=family_topic.id, word_english="Grandma", word_spanish="Abuela", image_url="👵", audio_url_en="grandma.mp3")
            ]
            db.session.add_all(family_vocab)

        db.session.commit()
        print("¡Nuevos temas inyectados con éxito! 🎉")

if __name__ == '__main__':
    seed_more_kids_topics()