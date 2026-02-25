import sys
import os
# Agregar el directorio raíz al path para poder importar la app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import (
    ThematicScenario, ScenarioVocabulary, ScenarioPhrase, ScenarioSimulation,
    KidsTopic, KidsVocabulary, User, ChildProfile
)

app = create_app()

def seeds_new_features():
    with app.app_context():
        print("Iniciando la inyección de datos para Escenarios y Zona Infantil...")

        # ---------------------------------------------------------
        # 1. CREAR ESCENARIO: EN EL RESTAURANTE (ADULTOS)
        # ---------------------------------------------------------
        print("Creando escenario: En el Restaurante...")
        restaurant_scenario = ThematicScenario.query.filter_by(title="At the Restaurant").first()
        if not restaurant_scenario:
            restaurant_scenario = ThematicScenario(
                title="At the Restaurant",
                category="Food & Dining",
                description="Aprende a pedir comida, entender el menú y pagar la cuenta como un nativo.",
                difficulty="beginner",
                icon_or_image="fas fa-utensils", # Usando un icono de FontAwesome por ahora
                is_premium=True,
                price_points=150
            )
            db.session.add(restaurant_scenario)
            db.session.commit() # Hacemos commit para obtener el ID

            # -- Vocabulario del Restaurante --
            vocab = [
                ScenarioVocabulary(scenario_id=restaurant_scenario.id, word="Menu", translation="Menú", part_of_speech="noun", example_usage="Could I see the menu, please?"),
                ScenarioVocabulary(scenario_id=restaurant_scenario.id, word="Waiter", translation="Mesero", part_of_speech="noun", example_usage="The waiter will take your order soon."),
                ScenarioVocabulary(scenario_id=restaurant_scenario.id, word="Bill", translation="Cuenta", part_of_speech="noun", example_usage="Can we have the bill, please?"),
                ScenarioVocabulary(scenario_id=restaurant_scenario.id, word="Tip", translation="Propina", part_of_speech="noun", example_usage="Is the tip included?"),
                ScenarioVocabulary(scenario_id=restaurant_scenario.id, word="To order", translation="Ordenar / Pedir", part_of_speech="verb", example_usage="Are you ready to order?")
            ]
            db.session.add_all(vocab)

            # -- Frases Clave --
            phrases = [
                ScenarioPhrase(scenario_id=restaurant_scenario.id, role="Waiter", phrase_type="question", english_text="Are you ready to order?", spanish_translation="¿Están listos para ordenar?", order=1),
                ScenarioPhrase(scenario_id=restaurant_scenario.id, role="Customer", phrase_type="answer", english_text="Yes, I'll have the chicken, please.", spanish_translation="Sí, pediré el pollo, por favor.", order=2),
                ScenarioPhrase(scenario_id=restaurant_scenario.id, role="Customer", phrase_type="question", english_text="Could we get the bill, please?", spanish_translation="¿Nos trae la cuenta, por favor?", order=3)
            ]
            db.session.add_all(phrases)

            # -- Simulador (Roleplay) --
            simulations = [
                ScenarioSimulation(
                    scenario_id=restaurant_scenario.id,
                    order=1,
                    prompt_text="El mesero se acerca a tu mesa y te dice: 'Good evening! Are you ready to order?' ¿Qué respondes?",
                    options=[
                        {"text": "Yes, where is the bathroom?", "is_correct": False},
                        {"text": "Yes, I would like the steak, please.", "is_correct": True},
                        {"text": "No, I am sleeping.", "is_correct": False}
                    ],
                    correct_option_index=1,
                    explanation_on_error="En este momento debes pedir tu comida. 'I would like...' es la forma más educada de hacerlo."
                )
            ]
            db.session.add_all(simulations)

        # ---------------------------------------------------------
        # 2. CREAR TEMA INFANTIL: COLORES MÁGICOS (KIDS ZONE)
        # ---------------------------------------------------------
        print("Creando tema infantil: Colores Mágicos...")
        colors_topic = KidsTopic.query.filter_by(title="Magic Colors").first()
        if not colors_topic:
            colors_topic = KidsTopic(
                title="Magic Colors",
                description="¡Aprende los colores del arcoíris!",
                cover_image="/static/img/kids/colors_cover.png", # Imágenes placeholder
                order=1
            )
            db.session.add(colors_topic)
            db.session.commit()

            # -- Vocabulario Infantil (Muy visual y auditivo) --
            kids_vocab = [
                KidsVocabulary(topic_id=colors_topic.id, word_english="Red", word_spanish="Rojo", image_url="/static/img/kids/red_apple.png", audio_url_en="/static/audio/kids/red.mp3"),
                KidsVocabulary(topic_id=colors_topic.id, word_english="Blue", word_spanish="Azul", image_url="/static/img/kids/blue_sky.png", audio_url_en="/static/audio/kids/blue.mp3"),
                KidsVocabulary(topic_id=colors_topic.id, word_english="Yellow", word_spanish="Amarillo", image_url="/static/img/kids/yellow_sun.png", audio_url_en="/static/audio/kids/yellow.mp3")
            ]
            db.session.add_all(kids_vocab)

        # ---------------------------------------------------------
        # 3. DAR ACCESO AL PRIMER USUARIO (Para que puedas probar)
        # ---------------------------------------------------------
        first_user = User.query.first()
        if first_user:
            print(f"Configurando cuenta de prueba para el usuario: {first_user.username}")
            # Hacerlo premium para que pueda ver todo
            first_user.subscription_type = 'premium_all_access'
            
            # Buscamos si ya tiene un perfil de niño creado usando una consulta directa
            child_count = ChildProfile.query.filter_by(parent_id=first_user.id).count()
            
            if child_count == 0:
                child = ChildProfile(parent_id=first_user.id, name="Pequeño Genio", age=6, avatar_url="/static/img/kids/avatars/lion.png")
                db.session.add(child)
            
        db.session.commit()
        print("¡Datos inyectados con éxito!")

if __name__ == '__main__':
    # Corregido: Sin la 's' extra
    seeds_new_features()