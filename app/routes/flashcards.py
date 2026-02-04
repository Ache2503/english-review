from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Flashcard, UserFlashcardReview, UserFlashcardSRS, Unit
from app.services.streaks import update_user_streak
from app.services.srs import (
    get_due_flashcards, get_srs_stats, review_flashcard_srs,
    quality_from_response, calculate_next_review
)
from datetime import datetime

flashcards_bp = Blueprint('flashcards', __name__, url_prefix='/flashcards')


@flashcards_bp.route('/unit/<int:unit_id>')
@login_required
def unit_flashcards(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    flashcards = Flashcard.query.filter_by(unit_id=unit_id, is_active=True).order_by(Flashcard.order).all()

    total = len(flashcards)
    reviewed = UserFlashcardReview.query.filter_by(user_id=current_user.id).join(Flashcard).filter(
        Flashcard.unit_id == unit_id
    ).count()
    
    # Estadísticas SRS
    srs_stats = get_srs_stats(current_user.id, unit_id)

    return render_template('flashcards/unit_flashcards.html',
                           unit=unit,
                           flashcards=flashcards,
                           total=total,
                           reviewed=reviewed,
                           srs_stats=srs_stats)


@flashcards_bp.route('/srs')
@login_required
def srs_overview():
    """Vista general del sistema de Repetición Espaciada"""
    stats = get_srs_stats(current_user.id)
    units = Unit.query.order_by(Unit.unit_number).all()
    
    # Estadísticas por unidad
    unit_stats = []
    for unit in units:
        unit_srs = get_srs_stats(current_user.id, unit.id)
        unit_stats.append({
            'unit': unit,
            'stats': unit_srs
        })
    
    return render_template('flashcards/srs_overview.html',
                           stats=stats,
                           unit_stats=unit_stats)


@flashcards_bp.route('/srs/study')
@flashcards_bp.route('/srs/study/<int:unit_id>')
@login_required
def srs_study(unit_id=None):
    """Modo de estudio SRS - tarjetas pendientes de repaso"""
    due_cards = get_due_flashcards(current_user.id, unit_id, limit=20)
    
    if not due_cards:
        flash('¡Felicidades! No tienes tarjetas pendientes de repaso.', 'success')
        if unit_id:
            return redirect(url_for('flashcards.unit_flashcards', unit_id=unit_id))
        return redirect(url_for('flashcards.srs_overview'))
    
    unit = None
    if unit_id:
        unit = Unit.query.get(unit_id)
    
    stats = get_srs_stats(current_user.id, unit_id)
    
    return render_template('flashcards/srs_study.html',
                           due_cards=due_cards,
                           unit=unit,
                           stats=stats,
                           total_due=len(due_cards))


@flashcards_bp.route('/srs/review/<int:flashcard_id>', methods=['POST'])
@login_required
def srs_review(flashcard_id):
    """Procesa una revisión con sistema SRS"""
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    
    # Obtener calificación del formulario (0-5) o convertir de respuesta simple
    quality = request.form.get('quality', type=int)
    
    if quality is None:
        # Compatibilidad con sistema anterior
        result = request.form.get('result', '').strip().lower()
        if result == 'perfect':
            quality = 5
        elif result == 'known':
            quality = 4
        elif result == 'hard':
            quality = 3
        elif result == 'forgot':
            quality = 1
        else:
            quality = 2
    
    # Procesar revisión con SRS
    srs_result = review_flashcard_srs(current_user.id, flashcard_id, quality)
    update_user_streak(current_user.id)
    
    # Mensajes según resultado
    if quality >= 4:
        flash(f'¡Excelente! Próximo repaso en {srs_result["interval"]} días.', 'success')
    elif quality == 3:
        flash(f'Bien. Próximo repaso en {srs_result["interval"]} días.', 'info')
    else:
        flash('Repasaremos esta tarjeta pronto.', 'warning')
    
    # Si es AJAX, retornar JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'success': True,
            'next_review': srs_result['next_review_date'].strftime('%Y-%m-%d'),
            'interval': srs_result['interval']
        })
    
    # Redireccionar al estudio
    unit_id = request.form.get('unit_id', type=int)
    if unit_id:
        return redirect(url_for('flashcards.srs_study', unit_id=unit_id))
    return redirect(url_for('flashcards.srs_study'))


@flashcards_bp.route('/review/<int:flashcard_id>', methods=['POST'])
@login_required
def review_flashcard(flashcard_id):
    """Revisión simple de flashcard (compatibilidad con sistema anterior)"""
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    result = request.form.get('result', '').strip().lower()

    is_correct = result == 'known'
    
    # Convertir a calidad SRS
    quality = 4 if is_correct else 1
    
    # Usar sistema SRS
    srs_result = review_flashcard_srs(current_user.id, flashcard_id, quality)
    update_user_streak(current_user.id)

    if is_correct:
        flash(f'¡Bien! Próximo repaso en {srs_result["interval"]} días.', 'success')
    else:
        flash('Marcada para repaso pronto.', 'warning')

    return redirect(url_for('flashcards.unit_flashcards', unit_id=flashcard.unit_id))


@flashcards_bp.route('/api/srs/stats')
@login_required
def api_srs_stats():
    """API para obtener estadísticas SRS"""
    unit_id = request.args.get('unit_id', type=int)
    stats = get_srs_stats(current_user.id, unit_id)
    return jsonify(stats)
