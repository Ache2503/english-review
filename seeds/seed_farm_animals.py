import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import KidsTopic, KidsVocabulary

app = create_app()

def seed_farm_animals():
    with app.app_context():
        print("Creando tema: Animales de la Granja...")

        # 1. Crear el Tema
        farm_topic = KidsTopic.query.filter_by(title="Farm Animals").first()
        if not farm_topic:
            farm_topic = KidsTopic(
                title="Farm Animals",
                description="¡Conoce a los animalitos que viven en la granja!",
                cover_image="cow", # Lo usaremos como referencia de icono
                order=2
            )
            db.session.add(farm_topic)
            db.session.commit()

            # 2. Crear el Vocabulario (Usaremos Emojis en el campo de la imagen temporalmente)
            animals = [
                KidsVocabulary(topic_id=farm_topic.id, word_english="Cow", word_spanish="Vaca", image_url="🐄", audio_url_en="cow.mp3"),
                KidsVocabulary(topic_id=farm_topic.id, word_english="Pig", word_spanish="Cerdo", image_url="🐖", audio_url_en="pig.mp3"),
                KidsVocabulary(topic_id=farm_topic.id, word_english="Horse", word_spanish="Caballo", image_url="🐎", audio_url_en="horse.mp3"),
                KidsVocabulary(topic_id=farm_topic.id, word_english="Chicken", word_spanish="Gallina", image_url="🐔", audio_url_en="chicken.mp3"),
                KidsVocabulary(topic_id=farm_topic.id, word_english="Sheep", word_spanish="Oveja", image_url="🐑", audio_url_en="sheep.mp3")
            ]
            db.session.add_all(animals)
            db.session.commit()
            print("¡Animales de la granja añadidos con éxito! 🐄🐖🐎")
        else:
            print("El tema 'Farm Animals' ya existe.")

if __name__ == '__main__':
    seed_farm_animals()