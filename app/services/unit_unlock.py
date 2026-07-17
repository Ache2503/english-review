"""
Sistema de Desbloqueo de Unidades
=================================
Maneja la lógica de progresión y desbloqueo de unidades.
Para desbloquear la siguiente unidad, el usuario debe:
1. Completar la gramática de la unidad actual
2. Completar el vocabulario
3. Completar los ejercicios
4. Pasar el desafío final con al menos 70%
"""

from datetime import datetime, timedelta
from app.extensions import db
from app.models import (
    Unit, UserProgress, UnitChallenge, ChallengeQuestion, 
    UserChallengeAttempt, GrammarRule, VocabularyCategory
)


LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


def get_unit_level(unit_number):
    """Inferir el nivel CEFR a partir del número de unidad."""
    if unit_number <= 12:
        return 'A1'
    if unit_number <= 24:
        return 'A2'
    if unit_number <= 36:
        return 'B1'
    if unit_number <= 48:
        return 'B2'
    if unit_number <= 60:
        return 'C1'
    return 'C2'


class UnitUnlockSystem:
    """Sistema para manejar el desbloqueo de unidades"""
    
    PASSING_SCORE = 70.0  # Porcentaje mínimo para pasar
    MAX_DAILY_ATTEMPTS = 3  # Intentos máximos por día
    
    def __init__(self, user_id):
        self.user_id = user_id
    
    def get_user_progress(self, unit_id):
        """Obtener o crear progreso del usuario para una unidad"""
        progress = UserProgress.query.filter_by(
            user_id=self.user_id,
            unit_id=unit_id
        ).first()
        
        if not progress:
            progress = UserProgress(
                user_id=self.user_id,
                unit_id=unit_id,
                unlocked=self._is_first_unit(unit_id)
            )
            db.session.add(progress)
            db.session.commit()
        
        return progress
    
    def _is_first_unit(self, unit_id):
        """Verificar si es la primera unidad (siempre desbloqueada)"""
        unit = Unit.query.get(unit_id)
        if unit:
            return unit.unit_number == 1
        return False
    
    def is_unit_unlocked(self, unit_id):
        """Verificar si una unidad está desbloqueada para el usuario"""
        unit = Unit.query.get(unit_id)
        if not unit:
            return False
        
        # La primera unidad siempre está desbloqueada
        if unit.unit_number == 1:
            return True

        # Si no existe progreso previo del usuario, desbloquear la siguiente unidad para una experiencia más fluida
        prev_unit = Unit.query.filter_by(unit_number=unit.unit_number - 1).first()
        if prev_unit:
            prev_progress = UserProgress.query.filter_by(
                user_id=self.user_id,
                unit_id=prev_unit.id
            ).first()
            if not prev_progress:
                return True
        
        # Verificar si el usuario completó la unidad anterior
        prev_unit = Unit.query.filter_by(unit_number=unit.unit_number - 1).first()
        if prev_unit:
            prev_progress = UserProgress.query.filter_by(
                user_id=self.user_id,
                unit_id=prev_unit.id
            ).first()
            
            if prev_progress and prev_progress.challenge_passed:
                return True
        
        return False
    
    def get_all_units_status(self):
        """Obtener el estado de todas las unidades para el usuario"""
        units = Unit.query.order_by(Unit.unit_number).all()
        units_status = []
        
        for unit in units:
            progress = self.get_user_progress(unit.id)
            is_unlocked = self.is_unit_unlocked(unit.id)
            
            # Actualizar el estado de desbloqueo
            if is_unlocked and not progress.unlocked:
                progress.unlocked = True
                db.session.commit()
            
            units_status.append({
                'unit': unit,
                'progress': progress,
                'unlocked': is_unlocked,
                'can_take_challenge': progress.can_take_challenge() if is_unlocked else False,
                'challenge_passed': progress.challenge_passed,
                'progress_percentage': self._calculate_progress_percentage(progress),
                'level': get_unit_level(unit.unit_number)
            })
        
        return units_status
    
    def _calculate_progress_percentage(self, progress):
        """Calcular el porcentaje de progreso real"""
        completed_steps = 0
        total_steps = 4  # grammar, vocabulary, exercises, challenge
        
        if progress.grammar_completed:
            completed_steps += 1
        if progress.vocabulary_completed:
            completed_steps += 1
        if progress.exercises_completed:
            completed_steps += 1
        if progress.challenge_passed:
            completed_steps += 1
        
        return (completed_steps / total_steps) * 100
    
    def mark_section_complete(self, unit_id, section):
        """Marcar una sección como completada"""
        progress = self.get_user_progress(unit_id)
        
        if section == 'grammar':
            progress.grammar_completed = True
        elif section == 'vocabulary':
            progress.vocabulary_completed = True
        elif section == 'exercises':
            progress.exercises_completed = True
        
        progress.progress_percentage = self._calculate_progress_percentage(progress)
        db.session.commit()
        
        return progress
    
    def can_attempt_challenge(self, unit_id):
        """Verificar si el usuario puede intentar el desafío"""
        progress = self.get_user_progress(unit_id)
        
        # Debe completar todas las secciones primero
        if not progress.can_take_challenge():
            return False, "Debes completar gramática, vocabulario y ejercicios primero"
        
        # Verificar intentos del día
        today = datetime.utcnow().date()
        today_attempts = UserChallengeAttempt.query.filter(
            UserChallengeAttempt.user_id == self.user_id,
            UserChallengeAttempt.started_at >= datetime.combine(today, datetime.min.time())
        ).join(UnitChallenge).filter(
            UnitChallenge.unit_id == unit_id
        ).count()
        
        if today_attempts >= self.MAX_DAILY_ATTEMPTS:
            return False, f"Has alcanzado el límite de {self.MAX_DAILY_ATTEMPTS} intentos por hoy. Intenta mañana."
        
        return True, f"Tienes {self.MAX_DAILY_ATTEMPTS - today_attempts} intentos restantes hoy"
    
    def get_challenge_for_unit(self, unit_id):
        """Obtener el desafío de una unidad"""
        challenge = UnitChallenge.query.filter_by(
            unit_id=unit_id,
            is_active=True
        ).first()
        
        return challenge
    
    def start_challenge_attempt(self, challenge_id):
        """Iniciar un intento de desafío"""
        attempt = UserChallengeAttempt(
            user_id=self.user_id,
            challenge_id=challenge_id,
            started_at=datetime.utcnow()
        )
        db.session.add(attempt)
        db.session.commit()
        
        return attempt
    
    def submit_challenge(self, attempt_id, answers):
        """Enviar respuestas del desafío y calcular puntuación"""
        attempt = UserChallengeAttempt.query.get(attempt_id)
        if not attempt or attempt.user_id != self.user_id:
            return None, "Intento no válido"
        
        challenge = attempt.challenge
        questions = ChallengeQuestion.query.filter_by(
            challenge_id=challenge.id
        ).order_by(ChallengeQuestion.order).all()
        
        total_points = sum(q.points for q in questions)
        earned_points = 0
        results = []
        
        for question in questions:
            user_answer = answers.get(str(question.id), '').strip().lower()
            correct_answer = question.correct_answer.strip().lower()
            
            # Verificar respuesta (con algo de flexibilidad)
            is_correct = self._check_answer(user_answer, correct_answer, question.question_type)
            
            if is_correct:
                earned_points += question.points
            
            results.append({
                'question_id': question.id,
                'question_text': question.question_text,
                'user_answer': answers.get(str(question.id), ''),
                'correct_answer': question.correct_answer,
                'is_correct': is_correct,
                'explanation': question.explanation,
                'points': question.points if is_correct else 0
            })
        
        # Calcular puntuación final
        score = (earned_points / total_points) * 100 if total_points > 0 else 0
        passed = score >= self.PASSING_SCORE
        
        # Actualizar intento
        attempt.completed_at = datetime.utcnow()
        attempt.score = score
        attempt.passed = passed
        attempt.answers = answers
        attempt.time_taken = int((attempt.completed_at - attempt.started_at).total_seconds())
        
        # Si pasó, actualizar progreso
        if passed:
            progress = self.get_user_progress(challenge.unit_id)
            progress.challenge_passed = True
            progress.challenge_score = max(progress.challenge_score, score)
            progress.completed = True
            progress.completed_at = datetime.utcnow()
            progress.progress_percentage = 100.0
        
        # Incrementar intentos
        progress = self.get_user_progress(challenge.unit_id)
        progress.challenge_attempts += 1
        
        db.session.commit()
        
        return {
            'score': score,
            'passed': passed,
            'earned_points': earned_points,
            'total_points': total_points,
            'results': results,
            'time_taken': attempt.time_taken
        }, None
    
    def _check_answer(self, user_answer, correct_answer, question_type):
        """Verificar si la respuesta es correcta con flexibilidad"""
        if question_type == 'multiple_choice':
            return user_answer == correct_answer
        
        # Para otros tipos, ser más flexible
        # Eliminar puntuación y espacios extra
        user_clean = ''.join(c for c in user_answer if c.isalnum() or c.isspace()).strip()
        correct_clean = ''.join(c for c in correct_answer if c.isalnum() or c.isspace()).strip()
        
        # Verificar igualdad exacta
        if user_clean == correct_clean:
            return True
        
        # Verificar si es una respuesta aceptable (puede haber múltiples correctas separadas por |)
        if '|' in correct_answer:
            acceptable = [a.strip().lower() for a in correct_answer.split('|')]
            return user_answer in acceptable
        
        return False
    
    def get_unit_requirements(self, unit_id):
        """Obtener los requisitos para desbloquear una unidad"""
        unit = Unit.query.get(unit_id)
        progress = self.get_user_progress(unit_id)
        
        # Contar elementos de la unidad
        grammar_count = GrammarRule.query.filter_by(unit_id=unit_id).count()
        vocab_count = VocabularyCategory.query.filter_by(unit_id=unit_id).count()
        
        return {
            'unit': unit,
            'grammar': {
                'total': grammar_count,
                'completed': progress.grammar_completed,
                'required': True
            },
            'vocabulary': {
                'total': vocab_count,
                'completed': progress.vocabulary_completed,
                'required': True
            },
            'exercises': {
                'completed': progress.exercises_completed,
                'required': True
            },
            'challenge': {
                'completed': progress.challenge_passed,
                'score': progress.challenge_score,
                'attempts': progress.challenge_attempts,
                'required': True,
                'can_attempt': progress.can_take_challenge()
            }
        }
