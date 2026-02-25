"""
Sistema de Simulación Roleplay Avanzado
=======================================
Maneja la lógica del simulador con branching, dificultades y moods de clientes.
"""

from datetime import datetime
from app.extensions import db
from app.models import (
    ThematicScenario, SimulationStep, SimulationOption, 
    SimulationAttempt, UserScenarioProgress, CustomerMood
)


class RoleplaySimulator:
    """Motor del simulador de roleplay con branching"""
    
    PASSING_SCORE = 70.0
    
    # Moods del cliente
    MOOD_SCORES = {
        'happy': 100,
        'neutral': 75,
        'annoyed': 50,
        'angry': 25
    }
    
    # Cambios de mood según la respuesta
    MOOD_IMPACT = {
        'correct': +15,      # Respuesta correcta mejora el mood
        'partial': +5,       # Respuesta parcial
        'incorrect': -20,     # Respuesta incorrecta baja el mood
        'very_bad': -35      # Respuesta muy mala
    }
    
    def __init__(self, user_id, scenario_id, difficulty='normal'):
        self.user_id = user_id
        self.scenario_id = scenario_id
        self.difficulty = difficulty
        self.attempt = None
        self.current_step = None
        self.current_mood = 'neutral'
        self.mood_score = 75
    
    def start_attempt(self):
        """Iniciar un nuevo intento de simulación"""
        # Obtener primer paso
        first_step = SimulationStep.query.filter_by(
            scenario_id=self.scenario_id
        ).order_by(SimulationStep.step_order).first()
        
        if not first_step:
            return None, "No hay pasos configurados para este escenario"
        
        # Ajustar dificultad
        initial_mood = self._get_initial_mood()
        self.current_mood = initial_mood
        self.mood_score = self.MOOD_SCORES.get(initial_mood, 75)
        
        # Crear intento
        self.attempt = SimulationAttempt(
            user_id=self.user_id,
            scenario_id=self.scenario_id,
            difficulty_level=self.difficulty,
            initial_mood=initial_mood,
            mood_score=self.mood_score,
            answers_log=[]
        )
        db.session.add(self.attempt)
        db.session.commit()
        
        self.current_step = first_step
        return self._get_step_data(first_step), None
    
    def _get_initial_mood(self):
        """Determinar el mood inicial según la dificultad"""
        if self.difficulty == 'easy':
            return 'happy'
        elif self.difficulty == 'difficult':
            return 'annoyed'
        return 'neutral'
    
    def get_step(self, step_id):
        """Obtener un paso específico"""
        step = SimulationStep.query.get(step_id)
        if not step:
            return None
        
        self.current_step = step
        return self._get_step_data(step)
    
    def get_next_step(self, current_step_id):
        """Obtener el siguiente paso en orden"""
        current = SimulationStep.query.get(current_step_id)
        if not current:
            return None
        
        next_step = SimulationStep.query.filter_by(
            scenario_id=self.scenario_id,
            step_order=current.step_order + 1
        ).first()
        
        if next_step:
            self.current_step = next_step
            return self._get_step_data(next_step)
        
        return None
    
    def _get_step_data(self, step):
        """Obtener datos del paso para la UI"""
        options = SimulationOption.query.filter_by(
            step_id=step.id
        ).order_by(SimulationOption.order).all()
        
        # En dificultad difícil, mostrar menos opciones
        display_options = options
        if self.difficulty == 'difficult':
            # Ocultar la respuesta correcta entre opciones similares
            display_options = [o for o in options if not o.is_correct][:3]
            if not display_options:
                display_options = options[:3]
        
        return {
            'step_id': step.id,
            'order': step.step_order,
            'message': step.customer_message,
            'mood': self.current_mood,
            'mood_score': self.mood_score,
            'context': step.situation_context,
            'audio_url': step.audio_url,
            'image_url': step.image_url,
            'time_limit': step.time_limit_seconds,
            'points': step.points_value,
            'is_final': step.is_final_step,
            'options': [
                {
                    'id': opt.id,
                    'text': opt.option_text,
                    'order': opt.order
                }
                for opt in display_options
            ]
        }
    
    def submit_answer(self, step_id, option_id, time_taken=None):
        """Procesar la respuesta del usuario"""
        # Convertir a integers si vienen como strings
        try:
            step_id = int(step_id)
            option_id = int(option_id)
        except (ValueError, TypeError):
            return None, "ID de paso o opción inválido"
        
        step = SimulationStep.query.get(step_id)
        option = SimulationOption.query.get(option_id)
        
        if not step:
            return None, f"Paso no encontrado: {step_id}"
        
        if not option:
            return None, f"Opción no encontrada: {option_id}"
        
        # Evaluar respuesta
        is_correct = option.is_correct
        points = option.points_earned if is_correct else 0
        
        # Calcular correctness_score
        correctness = option.correctness_score
        
        # Actualizar mood
        if is_correct:
            mood_change = self.MOOD_IMPACT['correct']
        elif correctness > 0.5:
            mood_change = self.MOOD_IMPACT['partial']
        elif correctness > 0.3:
            mood_change = self.MOOD_IMPACT['incorrect']
        else:
            mood_change = self.MOOD_IMPACT['very_bad']
        
        # En difícil, el impacto es mayor
        if self.difficulty == 'difficult':
            mood_change = int(mood_change * 1.5)
        
        self.mood_score = max(0, min(100, self.mood_score + mood_change))
        self.current_mood = self._get_mood_from_score(self.mood_score)
        
        # Actualizar attempt
        if self.attempt:
            self.attempt.total_points += points
            self.attempt.steps_completed += 1
            
            if is_correct:
                self.attempt.correct_answers += 1
            else:
                self.attempt.incorrect_answers += 1
            
            # Agregar al log
            answer_log = {
                'step_id': step_id,
                'option_id': option_id,
                'is_correct': is_correct,
                'correctness': correctness,
                'points': points,
                'mood_before': self.current_mood,
                'mood_after': self.current_mood,
                'time_taken': time_taken,
                'timestamp': datetime.utcnow().isoformat()
            }
            # Convertir a lista mutable
            current_log = list(self.attempt.answers_log) if self.attempt.answers_log else []
            current_log.append(answer_log)
            self.attempt.answers_log = current_log
        
        # Determinar feedback
        feedback = {
            'is_correct': is_correct,
            'correctness': correctness,
            'points_earned': points,
            'total_points': self.attempt.total_points if self.attempt else points,
            'mood': self.current_mood,
            'mood_score': self.mood_score,
            'feedback': option.feedback_correct if is_correct else option.feedback_incorrect,
            'mood_change': mood_change
        }
        
        # Determinar siguiente paso (branching)
        # Primero obtenemos el siguiente paso como objeto, luego lo convertimos a datos
        if is_correct and option.next_step_if_chosen:
            next_step_obj = SimulationStep.query.get(option.next_step_if_chosen)
        else:
            # Si falló, intentar siguiente paso o finalizar
            if step.is_final_step:
                next_step_obj = None
            else:
                # Obtener el siguiente step por orden
                next_step_obj = SimulationStep.query.filter_by(
                    scenario_id=self.scenario_id,
                    step_order=step.step_order + 1
                ).first()
        
        db.session.commit()
        
        # Convertir el objeto step a datos para la UI
        next_step_data = None
        if next_step_obj:
            self.current_step = next_step_obj
            next_step_data = self._get_step_data(next_step_obj)
        
        return {
            'feedback': feedback,
            'next_step': next_step_data,
            'is_complete': next_step_obj is None
        }, None
    
    def _get_mood_from_score(self, score):
        """Obtener mood desde la puntuación"""
        if score >= 90:
            return 'happy'
        elif score >= 60:
            return 'neutral'
        elif score >= 35:
            return 'annoyed'
        return 'angry'
    
    def complete_attempt(self):
        """Finalizar el intento y calcular puntuación"""
        if not self.attempt:
            return None
        
        # Obtener max points
        max_points = SimulationStep.query.filter_by(
            scenario_id=self.scenario_id
        ).with_entities(
            db.func.sum(SimulationStep.points_value)
        ).scalar() or 1
        
        self.attempt.max_points = max_points
        self.attempt.score_percentage = (self.attempt.total_points / max_points * 100) if max_points > 0 else 0
        self.attempt.final_mood = self.current_mood
        self.attempt.mood_score = self.mood_score
        self.attempt.completed_at = datetime.utcnow()
        
        # Determinar si pasó
        self.attempt.passed = self.attempt.score_percentage >= self.PASSING_SCORE
        
        # Actualizar progreso del usuario
        self._update_user_progress()
        
        db.session.commit()
        
        return {
            'total_points': self.attempt.total_points,
            'max_points': max_points,
            'score_percentage': round(self.attempt.score_percentage, 1),
            'passed': self.attempt.passed,
            'correct_answers': self.attempt.correct_answers,
            'incorrect_answers': self.attempt.incorrect_answers,
            'final_mood': self.current_mood,
            'mood_score': self.mood_score,
            'steps_completed': self.attempt.steps_completed
        }
    
    def _update_user_progress(self):
        """Actualizar el progreso del usuario en el escenario"""
        progress = UserScenarioProgress.query.filter_by(
            user_id=self.user_id,
            scenario_id=self.scenario_id
        ).first()
        
        if not progress:
            progress = UserScenarioProgress(
                user_id=self.user_id,
                scenario_id=self.scenario_id
            )
            db.session.add(progress)
        
        if self.attempt.passed:
            progress.simulation_score = max(
                progress.simulation_score or 0,
                self.attempt.score_percentage
            )
            progress.is_completed = True
            progress.completed_at = datetime.utcnow()
        
        db.session.commit()
    
    def get_current_state(self):
        """Obtener el estado actual de la simulación"""
        if not self.attempt:
            return None
        
        return {
            'attempt_id': self.attempt.id,
            'steps_completed': self.attempt.steps_completed,
            'total_points': self.attempt.total_points,
            'current_mood': self.current_mood,
            'mood_score': self.mood_score,
            'difficulty': self.difficulty
        }


def create_sample_scenario(scenario_id):
    """Crear datos de ejemplo para un escenario"""
    scenario = ThematicScenario.query.get(scenario_id)
    if not scenario:
        return None
    
    # Primero eliminar las opciones y luego los pasos (respetando foreign keys)
    steps = SimulationStep.query.filter_by(scenario_id=scenario_id).all()
    for step in steps:
        SimulationOption.query.filter_by(step_id=step.id).delete()
    SimulationStep.query.filter_by(scenario_id=scenario_id).delete()
    db.session.commit()
    
    # Datos de ejemplo para escenario de restaurante
    steps_data = [
        {
            'order': 1,
            'message': "Good evening! I don't have a reservation. Do you have a table available?",
            'mood': 'neutral',
            'context': 'El cliente llega al restaurante sin reservación',
            'time_limit': 30,
            'points': 10,
            'options': [
                {'text': "Yes, of course! How many people in your party?", 'correct': True, 'points': 10, 'correctness': 1.0, 'feedback_c': "Perfect! Very professional and welcoming.", 'feedback_i': None},
                {'text': "I'll check if we have space. Please wait.", 'correct': True, 'points': 7, 'correctness': 0.7, 'feedback_c': "Good, but try to be more welcoming.", 'feedback_i': None},
                {'text': "Wait a moment please.", 'correct': False, 'points': 3, 'correctness': 0.3, 'feedback_c': None, 'feedback_i': "That's a bit cold. Try being warmer and more welcoming."},
                {'text': "We're full. Come back later.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Never turn away a customer like this!"},
                {'text': "Do you have a reservation name?", 'correct': False, 'points': 2, 'correctness': 0.2, 'feedback_c': None, 'feedback_i': "The customer said they don't have a reservation."}
            ]
        },
        {
            'order': 2,
            'message': "There are two of us. And can we sit near the window?",
            'mood': 'neutral',
            'context': 'El cliente tiene preferencias de asientos',
            'time_limit': 25,
            'points': 10,
            'options': [
                {'text': "I'll check if it's available. Please follow me.", 'correct': True, 'points': 10, 'correctness': 1.0, 'feedback_c': "Excellent service! You addressed their request.", 'feedback_i': None},
                {'text': "We have a table by the window. Right this way!", 'correct': True, 'points': 10, 'correctness': 1.0, 'feedback_c': "Perfect! Proactive service.", 'feedback_i': None},
                {'text': "All tables are the same. Sit anywhere.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Show some flexibility and willingness to help."},
                {'text': "Yes, but it's a 30-minute wait for the window.", 'correct': True, 'points': 6, 'correctness': 0.6, 'feedback_c': "Honest, but offer an alternative nicely.", 'feedback_i': None},
                {'text': "The window tables are reserved. You'll need to sit inside.", 'correct': False, 'points': 2, 'correctness': 0.2, 'feedback_c': None, 'feedback_i': "Try to find a solution, not just say no."}
            ]
        },
        {
            'order': 3,
            'message': "I'd like to see the menu, please. What's your chef's special today?",
            'mood': 'neutral',
            'context': 'El cliente quiere ver el menú y recomendaciones',
            'time_limit': 30,
            'points': 10,
            'options': [
                {'text': "Here's the menu. Our special today is grilled salmon with seasonal vegetables.", 'correct': True, 'points': 10, 'correctness': 1.0, 'feedback_c': "Perfect! Helpful, informative, and detailed.", 'feedback_i': None},
                {'text': "Here's your menu. Everything is delicious!", 'correct': True, 'points': 7, 'correctness': 0.7, 'feedback_c': "Good, but could be more specific about recommendations.", 'feedback_i': None},
                {'text': "The menu is on the table.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Be more proactive in helping and making recommendations."},
                {'text': "Our special is the steak, but I'm not sure about today's.", 'correct': False, 'points': 2, 'correctness': 0.2, 'feedback_c': None, 'feedback_i': "Don't show uncertainty. Know your menu!"},
                {'text': "Everything is good. Just pick something.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Show enthusiasm and make suggestions!"}
            ]
        },
        {
            'order': 4,
            'message': "Excuse me, I ordered the salmon, but I asked for it well-done, not medium-rare. I'm in a hurry.",
            'mood': 'annoyed',
            'context': 'El cliente tiene una queja sobre su orden y está apurado',
            'time_limit': 25,
            'points': 15,
            'options': [
                {'text': "I'm so sorry! I'll have the chef prepare a new one right away. It will be quick!", 'correct': True, 'points': 15, 'correctness': 1.0, 'feedback_c': "Excellent recovery! You acknowledged the urgency and took action.", 'feedback_i': None},
                {'text': "I apologize for the mistake. Let me take care of this immediately.", 'correct': True, 'points': 12, 'correctness': 0.8, 'feedback_c': "Good apology and action, but mention the urgency.", 'feedback_i': None},
                {'text': "That's how it's cooked. We can't change it.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Never argue with a customer. Always apologize first!"},
                {'text': "Let me check with the kitchen.", 'correct': True, 'points': 8, 'correctness': 0.6, 'feedback_c': "Good approach, but be more apologetic and urgent.", 'feedback_i': None},
                {'text': "I'll give you a discount on your next visit.", 'correct': False, 'points': 3, 'correctness': 0.3, 'feedback_c': None, 'feedback_i': "Don't offer compensation without addressing the immediate problem."}
            ]
        },
        {
            'order': 5,
            'message': "Can we have the check, please? And do you accept credit cards?",
            'mood': 'neutral',
            'context': 'El cliente quiere pagar',
            'time_limit': 20,
            'points': 10,
            'options': [
                {'text': "Yes, we accept all major credit cards. Here's the bill. Thank you for dining with us!", 'correct': True, 'points': 10, 'correctness': 1.0, 'feedback_c': "Perfect ending! Professional, warm, and complete.", 'feedback_i': None},
                {'text': "Of course! Here's your bill. We accept Visa, Mastercard, and Amex.", 'correct': True, 'points': 9, 'correctness': 0.9, 'feedback_c': "Very good! You listed the specific cards accepted.", 'feedback_i': None},
                {'text': "Cash only.", 'correct': False, 'points': 3, 'correctness': 0.3, 'feedback_c': None, 'feedback_i': "Mention payment options earlier in the service."},
                {'text': "Wait, I'll calculate it.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Be more prepared and efficient. Have the bill ready."},
                {'text': "The total is $45.50. Would you like to pay now?", 'correct': True, 'points': 7, 'correctness': 0.7, 'feedback_c': "Good, but also mention payment methods.", 'feedback_i': None}
            ]
        },
        {
            'order': 6,
            'message': "This dessert is amazing! What's it called?",
            'mood': 'happy',
            'context': 'El cliente está disfrutando y quiere más información',
            'time_limit': 25,
            'points': 8,
            'options': [
                {'text': "It's our signature chocolate lava cake with vanilla ice cream!", 'correct': True, 'points': 8, 'correctness': 1.0, 'feedback_c': "Perfect! Detailed and enthusiastic.", 'feedback_i': None},
                {'text': "It's the chocolate cake. Would you like another one?", 'correct': True, 'points': 6, 'correctness': 0.7, 'feedback_c': "Good, but could be more descriptive.", 'feedback_i': None},
                {'text': "I can check with the kitchen.", 'correct': False, 'points': 2, 'correctness': 0.2, 'feedback_c': None, 'feedback_i': "You should know your desserts!"},
                {'text': "Thanks! It's popular.", 'correct': True, 'points': 5, 'correctness': 0.5, 'feedback_c': "Good, but add more details about the dessert.", 'feedback_i': None}
            ]
        },
        {
            'order': 7,
            'message': "I'm allergic to nuts. Is there anything I should avoid?",
            'mood': 'neutral',
            'context': 'El cliente tiene una alergia alimentaria',
            'time_limit': 30,
            'points': 12,
            'options': [
                {'text': "I'll check with our chef to give you safe options. Please wait a moment.", 'correct': True, 'points': 12, 'correctness': 1.0, 'feedback_c': "Excellent! You took it seriously and took action.", 'feedback_i': None},
                {'text': "Many of our desserts have nuts. Let me show you the ones that are safe.", 'correct': True, 'points': 10, 'correctness': 0.9, 'feedback_c': "Great! You showed knowledge and helped immediately.", 'feedback_i': None},
                {'text': "I think the salad should be fine.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "Never guess about allergies! Always check with the kitchen."},
                {'text': "We don't use nuts in our kitchen.", 'correct': False, 'points': 3, 'correctness': 0.3, 'feedback_c': None, 'feedback_i': "Don't make assumptions. Verify with the chef."},
                {'text': "Don't worry, I'll make sure your food is safe.", 'correct': True, 'points': 8, 'correctness': 0.7, 'feedback_c': "Good reassurance, but also check the menu for them.", 'feedback_i': None}
            ]
        },
        {
            'order': 8,
            'message': "Can we have the check? We're in a big hurry for a movie.",
            'mood': 'annoyed',
            'context': 'El cliente tiene prisa',
            'time_limit': 15,
            'points': 12,
            'options': [
                {'text': "Of course! I'll bring it right away.", 'correct': True, 'points': 12, 'correctness': 1.0, 'feedback_c': "Perfect! Quick and responsive.", 'feedback_i': None},
                {'text': "I'll process your payment immediately.", 'correct': True, 'points': 10, 'correctness': 0.9, 'feedback_c': "Great! You understood the urgency.", 'feedback_i': None},
                {'text': "I'll need to calculate it first.", 'correct': False, 'points': 2, 'correctness': 0.2, 'feedback_c': None, 'feedback_i': "The bill should always be ready when asked."},
                {'text': "The server will be with you shortly.", 'correct': False, 'points': 0, 'correctness': 0.0, 'feedback_c': None, 'feedback_i': "They need it NOW, not shortly!"},
                {'text': "Would you like to pay separately or together?", 'correct': True, 'points': 6, 'correctness': 0.6, 'feedback_c': "Good question, but be faster about it.", 'feedback_i': None}
            ]
        }
    ]
    
    # Crear los pasos
    for step_data in steps_data:
        step = SimulationStep(
            scenario_id=scenario_id,
            step_order=step_data['order'],
            customer_message=step_data['message'],
            customer_mood=step_data['mood'],
            situation_context=step_data.get('context'),
            time_limit_seconds=step_data['time_limit'],
            points_value=step_data['points'],
            is_final_step=step_data['order'] == len(steps_data)
        )
        db.session.add(step)
        db.session.flush()
        
        # Crear opciones
        for i, opt_data in enumerate(step_data['options']):
            option = SimulationOption(
                step_id=step.id,
                option_text=opt_data['text'],
                is_correct=opt_data['correct'],
                correctness_score=opt_data.get('correctness', 1.0 if opt_data['correct'] else 0.0),
                points_earned=opt_data['points'],
                feedback_correct=opt_data.get('feedback_c'),
                feedback_incorrect=opt_data.get('feedback_i'),
                order=i
            )
            db.session.add(option)
    
    db.session.commit()
    return True


def populate_all_scenarios():
    """Poblar la base de datos con todos los escenarios y datos de simulación"""
    from app.models import ThematicScenario
    
    # Escenarios a crear
    scenarios_data = [
        {
            'title': 'At the Restaurant',
            'category': 'Food & Dining',
            'description': 'Practice English at a restaurant: greeting, taking orders, handling complaints, and payment.',
            'difficulty': 'beginner',
            'icon_or_image': 'fas fa-utensils'
        },
        {
            'title': 'Hotel Reception',
            'category': 'Hospitality',
            'description': 'Check-in, check-out, room service, and handling guest requests at a hotel.',
            'difficulty': 'intermediate',
            'icon_or_image': 'fas fa-hotel'
        },
        {
            'title': 'Coffee Shop',
            'category': 'Food & Dining',
            'description': 'Taking drink orders, customizing orders, and handling payments at a cafe.',
            'difficulty': 'beginner',
            'icon_or_image': 'fas fa-coffee'
        },
        {
            'title': 'Customer Service',
            'category': 'Business',
            'description': 'Handling customer complaints, returns, and providing information over the phone.',
            'difficulty': 'advanced',
            'icon_or_image': 'fas fa-headset'
        }
    ]
    
    created = []
    for sc in scenarios_data:
        # Verificar si ya existe
        existing = ThematicScenario.query.filter_by(title=sc['title']).first()
        if existing:
            # Regenerar datos de simulación
            create_sample_scenario(existing.id)
            created.append(existing)
            continue
            
        scenario = ThematicScenario(
            title=sc['title'],
            category=sc['category'],
            description=sc['description'],
            difficulty=sc['difficulty'],
            icon_or_image=sc['icon_or_image'],
            is_premium=False  # Gratis para demo
        )
        db.session.add(scenario)
        db.session.flush()
        
        # Crear datos de simulación
        create_sample_scenario(scenario.id)
        created.append(scenario)
    
    db.session.commit()
    return created
