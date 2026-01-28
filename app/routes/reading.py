"""
Rutas para el sistema de lectura con extracción de oraciones y retroalimentación
"""
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from app import db, cache
from app.models import Unit, Reading, UserReadingSubmission, MotivationalMessage
from app.services.feedback import analyze_reading_sentences
from app.services.streaks import update_user_streak
import json

reading_bp = Blueprint('reading', __name__, url_prefix='/reading')


@reading_bp.route('/unit/<int:unit_number>')
@login_required
@cache.cached(timeout=3600, query_string=True)  # OPTIMIZACIÓN: Caché 1 hora
def unit_readings(unit_number):
    """Ver todas las lecturas de una unidad"""
    unit = Unit.query.filter_by(unit_number=unit_number).first_or_404()
    readings = Reading.query.filter_by(unit_id=unit.id).order_by(Reading.order).all()
    messages = MotivationalMessage.query.filter(
        (MotivationalMessage.unit_id == unit.id) | 
        (MotivationalMessage.unit_id == None)
    ).filter_by(is_active=True).all()
    
    return render_template('reading/list.html', 
                         unit=unit, 
                         readings=readings,
                         messages=messages)


@reading_bp.route('/<int:reading_id>')
@login_required
@cache.cached(timeout=3600)  # OPTIMIZACIÓN: Caché 1 hora
def view_reading(reading_id):
    """Ver una lectura específica"""
    reading = Reading.query.get_or_404(reading_id)
    unit = reading.unit
    
    # Obtener mensajes motivacionales
    messages = MotivationalMessage.query.filter(
        (MotivationalMessage.unit_id == unit.id) | 
        (MotivationalMessage.unit_id == None)
    ).filter_by(is_active=True).all()
    
    # Obtener intentos anteriores del usuario
    previous_submissions = UserReadingSubmission.query.filter_by(
        user_id=current_user.id,
        reading_id=reading_id
    ).order_by(UserReadingSubmission.submitted_at.desc()).all()
    
    return render_template('reading/view.html', 
                         reading=reading,
                         unit=unit,
                         messages=messages,
                         previous_submissions=previous_submissions)


@reading_bp.route('/<int:reading_id>/submit', methods=['POST'])
@login_required
def submit_reading(reading_id):
    """Procesar las oraciones extraídas por el usuario"""
    reading = Reading.query.get_or_404(reading_id)
    
    data = request.get_json()
    extracted_sentences = data.get('sentences', [])
    
    if not extracted_sentences:
        return jsonify({'error': 'No sentences provided'}), 400
    
    # Analizar las oraciones extraídas
    feedback_result = analyze_reading_sentences(
        sentences=extracted_sentences,
        reading_text=reading.content,
        unit_number=reading.unit.unit_number
    )
    
    # Guardar el intento
    submission = UserReadingSubmission(
        user_id=current_user.id,
        reading_id=reading_id,
        extracted_sentences=json.dumps(extracted_sentences),
        feedback=json.dumps(feedback_result['messages']),
        score=feedback_result['score']
    )
    db.session.add(submission)
    db.session.commit()

    update_user_streak(current_user.id)
    
    return jsonify({
        'success': True,
        'score': feedback_result['score'],
        'messages': feedback_result['messages'],
        'submission_id': submission.id
    })


@reading_bp.route('/history/<int:reading_id>')
@login_required
def reading_history(reading_id):
    """Ver historial de intentos en una lectura"""
    reading = Reading.query.get_or_404(reading_id)
    
    # Verificar que el usuario tenga acceso
    if reading.unit.id != current_user.id:
        # Verificar que sea su lectura
        pass
    
    submissions = UserReadingSubmission.query.filter_by(
        user_id=current_user.id,
        reading_id=reading_id
    ).order_by(UserReadingSubmission.submitted_at.desc()).all()
    
    return render_template('reading/history.html',
                         reading=reading,
                         submissions=submissions)


@reading_bp.route('/submission/<int:submission_id>')
@login_required
def view_submission(submission_id):
    """Ver detalles de un intento específico"""
    submission = UserReadingSubmission.query.get_or_404(submission_id)
    
    # Verificar que sea del usuario actual
    if submission.user_id != current_user.id:
        flash('No tienes acceso a este intento', 'danger')
        return redirect(url_for('reading.unit_readings', 
                              unit_number=submission.reading.unit.unit_number))
    
    reading = submission.reading
    extracted_sentences = json.loads(submission.extracted_sentences)
    feedback = json.loads(submission.feedback) if submission.feedback else []
    
    return render_template('reading/submission_detail.html',
                         submission=submission,
                         reading=reading,
                         extracted_sentences=extracted_sentences,
                         feedback=feedback)
