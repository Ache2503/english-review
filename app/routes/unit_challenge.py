"""
Rutas para el sistema de desafíos de unidades
=============================================
Maneja el desbloqueo progresivo de unidades.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from datetime import datetime
from app.extensions import db
from app.models import (
    Unit, UserProgress, UnitChallenge, ChallengeQuestion, 
    UserChallengeAttempt
)
from app.services.unit_unlock import UnitUnlockSystem

unit_challenge_bp = Blueprint('unit_challenge', __name__, url_prefix='/challenge')


@unit_challenge_bp.route('/units')
@login_required
def units_overview():
    """Vista general de todas las unidades con su estado de desbloqueo"""
    unlock_system = UnitUnlockSystem(current_user.id)
    units_status = unlock_system.get_all_units_status()
    
    return render_template('challenge/units_overview.html',
                           units_status=units_status)


@unit_challenge_bp.route('/unit/<int:unit_id>/requirements')
@login_required
def unit_requirements(unit_id):
    """Ver requisitos para desbloquear la siguiente unidad"""
    unlock_system = UnitUnlockSystem(current_user.id)
    
    if not unlock_system.is_unit_unlocked(unit_id):
        flash('Esta unidad aún no está desbloqueada.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    requirements = unlock_system.get_unit_requirements(unit_id)
    can_challenge, message = unlock_system.can_attempt_challenge(unit_id)
    challenge = unlock_system.get_challenge_for_unit(unit_id)
    
    return render_template('challenge/unit_requirements.html',
                           requirements=requirements,
                           can_challenge=can_challenge,
                           challenge_message=message,
                           challenge=challenge)


@unit_challenge_bp.route('/unit/<int:unit_id>/mark-complete/<section>')
@login_required
def mark_section_complete(unit_id, section):
    """Marcar una sección como completada"""
    if section not in ['grammar', 'vocabulary', 'exercises']:
        flash('Sección no válida.', 'error')
        return redirect(url_for('unit_challenge.unit_requirements', unit_id=unit_id))
    
    unlock_system = UnitUnlockSystem(current_user.id)
    
    if not unlock_system.is_unit_unlocked(unit_id):
        flash('Esta unidad no está desbloqueada.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    unlock_system.mark_section_complete(unit_id, section)
    
    section_names = {
        'grammar': 'Gramática',
        'vocabulary': 'Vocabulario',
        'exercises': 'Ejercicios'
    }
    
    flash(f'¡{section_names[section]} completado! 🎉', 'success')
    return redirect(url_for('unit_challenge.unit_requirements', unit_id=unit_id))


@unit_challenge_bp.route('/unit/<int:unit_id>/start')
@login_required
def start_challenge(unit_id):
    """Iniciar el desafío de una unidad"""
    unlock_system = UnitUnlockSystem(current_user.id)
    
    # Verificar si puede tomar el desafío
    can_attempt, message = unlock_system.can_attempt_challenge(unit_id)
    if not can_attempt:
        flash(message, 'warning')
        return redirect(url_for('unit_challenge.unit_requirements', unit_id=unit_id))
    
    # Obtener el desafío
    challenge = unlock_system.get_challenge_for_unit(unit_id)
    if not challenge:
        flash('No hay desafío disponible para esta unidad.', 'error')
        return redirect(url_for('unit_challenge.unit_requirements', unit_id=unit_id))
    
    # Iniciar intento
    attempt = unlock_system.start_challenge_attempt(challenge.id)
    
    # Guardar en sesión
    session['current_challenge_attempt'] = attempt.id
    session['challenge_start_time'] = datetime.utcnow().isoformat()
    
    # Obtener preguntas
    questions = ChallengeQuestion.query.filter_by(
        challenge_id=challenge.id
    ).order_by(ChallengeQuestion.order).all()
    
    unit = Unit.query.get(unit_id)
    
    return render_template('challenge/take_challenge.html',
                           unit=unit,
                           challenge=challenge,
                           questions=questions,
                           attempt_id=attempt.id)


@unit_challenge_bp.route('/submit/<int:attempt_id>', methods=['POST'])
@login_required
def submit_challenge(attempt_id):
    """Enviar respuestas del desafío"""
    unlock_system = UnitUnlockSystem(current_user.id)
    
    # Recopilar respuestas
    answers = {}
    for key, value in request.form.items():
        if key.startswith('question_'):
            question_id = key.replace('question_', '')
            answers[question_id] = value
    
    # Procesar respuestas
    result, error = unlock_system.submit_challenge(attempt_id, answers)
    
    if error:
        flash(error, 'error')
        return redirect(url_for('unit_challenge.units_overview'))
    
    # Limpiar sesión
    session.pop('current_challenge_attempt', None)
    session.pop('challenge_start_time', None)
    
    # Obtener información del intento
    attempt = UserChallengeAttempt.query.get(attempt_id)
    unit = Unit.query.get(attempt.challenge.unit_id)
    
    return render_template('challenge/challenge_result.html',
                           unit=unit,
                           result=result,
                           passed=result['passed'])


@unit_challenge_bp.route('/api/check-unlock/<int:unit_id>')
@login_required
def api_check_unlock(unit_id):
    """API para verificar si una unidad está desbloqueada"""
    unlock_system = UnitUnlockSystem(current_user.id)
    
    is_unlocked = unlock_system.is_unit_unlocked(unit_id)
    progress = unlock_system.get_user_progress(unit_id)
    
    return jsonify({
        'unlocked': is_unlocked,
        'progress': {
            'grammar_completed': progress.grammar_completed,
            'vocabulary_completed': progress.vocabulary_completed,
            'exercises_completed': progress.exercises_completed,
            'challenge_passed': progress.challenge_passed,
            'progress_percentage': progress.progress_percentage
        }
    })


@unit_challenge_bp.route('/history')
@login_required
def challenge_history():
    """Ver historial de intentos de desafíos"""
    attempts = UserChallengeAttempt.query.filter_by(
        user_id=current_user.id
    ).order_by(UserChallengeAttempt.started_at.desc()).all()
    
    return render_template('challenge/history.html',
                           attempts=attempts)
