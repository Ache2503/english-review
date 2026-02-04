"""
Rutas para el Sistema de Repaso Avanzado.

Este módulo proporciona endpoints para:
- Iniciar sesiones de repaso
- Procesar respuestas de repaso
- Ver estadísticas de repaso
- Obtener recomendaciones de estudio
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import login_required, current_user
from datetime import datetime

from app.services.review_system import (
    AdvancedReviewSystem, 
    get_review_session, 
    get_user_review_stats,
    get_study_recommendations,
    ReviewItemType
)
from app.extensions import db

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.route('/')
@review_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard principal del sistema de repaso."""
    system = AdvancedReviewSystem(current_user.id)
    
    stats = system.get_statistics()
    weak_areas = system.get_weak_areas()
    recommendations = system.get_recommendations()
    
    return render_template('review/dashboard.html',
                          stats=stats,
                          weak_areas=weak_areas,
                          recommendations=recommendations)


@review_bp.route('/start', methods=['GET', 'POST'])
@login_required
def start_session():
    """Inicia una nueva sesión de repaso."""
    if request.method == 'POST':
        # Configurar sesión según preferencias del usuario
        item_count = int(request.form.get('item_count', 20))
        focus_types = request.form.getlist('focus_types')
        focus_unit = request.form.get('focus_unit')
        include_new = request.form.get('include_new', 'true') == 'true'
        
        # Convertir tipos de string a enum
        type_enums = []
        for t in focus_types:
            try:
                type_enums.append(ReviewItemType(t))
            except ValueError:
                pass
        
        # Generar sesión
        system = AdvancedReviewSystem(current_user.id)
        review_session = system.generate_session(
            item_count=item_count,
            focus_types=type_enums if type_enums else None,
            focus_unit=int(focus_unit) if focus_unit else None,
            include_new=include_new
        )
        
        if not review_session.items:
            flash('No hay elementos para repasar en este momento. ¡Buen trabajo!', 'info')
            return redirect(url_for('review.dashboard'))
        
        # Guardar sesión en session
        session['review_session'] = {
            'session_id': review_session.session_id,
            'items': [
                {
                    'item_type': item.item_type.value,
                    'item_id': item.item_id,
                    'question': item.question,
                    'answer': item.answer,
                    'hints': item.hints,
                    'difficulty': item.difficulty.value,
                    'mastery_level': item.mastery_level,
                }
                for item in review_session.items
            ],
            'current_index': 0,
            'correct_count': 0,
            'wrong_count': 0,
            'started_at': datetime.utcnow().isoformat(),
            'focus_areas': review_session.focus_areas
        }
        
        return redirect(url_for('review.practice'))
    
    # GET: Mostrar configuración de sesión
    from app.models import Unit
    units = Unit.query.order_by(Unit.unit_number).all()
    
    # Obtener estadísticas para mostrar qué repasar
    system = AdvancedReviewSystem(current_user.id)
    stats = system.get_statistics()
    
    return render_template('review/start_session.html',
                          units=units,
                          stats=stats)


@review_bp.route('/practice')
@login_required
def practice():
    """Página principal de práctica de repaso."""
    review_data = session.get('review_session')
    
    if not review_data or not review_data.get('items'):
        flash('No hay sesión de repaso activa.', 'warning')
        return redirect(url_for('review.dashboard'))
    
    current_index = review_data.get('current_index', 0)
    items = review_data.get('items', [])
    
    if current_index >= len(items):
        return redirect(url_for('review.results'))
    
    current_item = items[current_index]
    
    return render_template('review/practice.html',
                          item=current_item,
                          current_index=current_index + 1,
                          total_items=len(items),
                          correct_count=review_data.get('correct_count', 0),
                          wrong_count=review_data.get('wrong_count', 0),
                          focus_areas=review_data.get('focus_areas', []))


@review_bp.route('/submit', methods=['POST'])
@login_required
def submit_answer():
    """Procesa una respuesta de repaso."""
    review_data = session.get('review_session')
    
    if not review_data:
        return jsonify({'error': 'No hay sesión activa'}), 400
    
    current_index = review_data.get('current_index', 0)
    items = review_data.get('items', [])
    
    if current_index >= len(items):
        return jsonify({'error': 'Sesión completada'}), 400
    
    current_item = items[current_index]
    user_answer = request.json.get('answer', '').strip().lower()
    correct_answer = current_item['answer'].lower()
    
    # Verificar respuesta (comparación flexible)
    is_correct = (
        user_answer == correct_answer or
        user_answer in [h.lower() for h in current_item.get('hints', [])]
    )
    
    # También verificar similitud
    from difflib import SequenceMatcher
    similarity = SequenceMatcher(None, user_answer, correct_answer).ratio()
    if similarity >= 0.85:
        is_correct = True
    
    # Registrar en el sistema de repaso
    system = AdvancedReviewSystem(current_user.id)
    
    from app.services.review_system import ReviewItem, ReviewItemType, Difficulty
    item = ReviewItem(
        item_type=ReviewItemType(current_item['item_type']),
        item_id=current_item['item_id'],
        question=current_item['question'],
        answer=current_item['answer'],
        hints=current_item.get('hints', []),
        difficulty=Difficulty(current_item.get('difficulty', 2)),
        last_reviewed=None,
        times_correct=0,
        times_wrong=0,
        mastery_level=current_item.get('mastery_level', 0),
        priority=0
    )
    
    result = system.record_review(item, is_correct)
    
    # Actualizar sesión
    if is_correct:
        review_data['correct_count'] = review_data.get('correct_count', 0) + 1
    else:
        review_data['wrong_count'] = review_data.get('wrong_count', 0) + 1
    
    review_data['current_index'] = current_index + 1
    session['review_session'] = review_data
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': current_item['answer'],
        'new_mastery': result.get('new_mastery', 0),
        'next_review_days': result.get('next_review_days', 1),
        'has_next': (current_index + 1) < len(items),
        'progress': {
            'current': current_index + 1,
            'total': len(items),
            'correct': review_data['correct_count'],
            'wrong': review_data['wrong_count']
        }
    })


@review_bp.route('/results')
@login_required
def results():
    """Muestra los resultados de la sesión de repaso."""
    review_data = session.get('review_session')
    
    if not review_data:
        flash('No hay resultados disponibles.', 'warning')
        return redirect(url_for('review.dashboard'))
    
    total_items = len(review_data.get('items', []))
    correct_count = review_data.get('correct_count', 0)
    wrong_count = review_data.get('wrong_count', 0)
    
    # Calcular estadísticas
    accuracy = round((correct_count / total_items * 100), 1) if total_items > 0 else 0
    
    # Calcular tiempo de sesión
    started_at = review_data.get('started_at')
    if started_at:
        start_time = datetime.fromisoformat(started_at)
        duration = datetime.utcnow() - start_time
        duration_seconds = int(duration.total_seconds())
        duration_minutes = round(duration_seconds / 60, 1)
    else:
        duration_seconds = 0
        duration_minutes = 0
    
    # Guardar sesión en ReviewSessionLog
    from app.models import ReviewSessionLog
    from app.extensions import db
    
    session_log = ReviewSessionLog(
        user_id=current_user.id,
        session_type=review_data.get('session_type', 'mixed'),
        total_items=total_items,
        correct_count=correct_count,
        wrong_count=wrong_count,
        score=accuracy,
        time_spent_seconds=duration_seconds,
        focus_areas=review_data.get('focus_areas', []),
        items_reviewed=[{
            'type': item.get('item_type'),
            'id': item.get('item_id'),
            'question': item.get('question', '')[:100]
        } for item in review_data.get('items', [])[:20]],
        started_at=start_time if started_at else datetime.utcnow(),
        completed_at=datetime.utcnow()
    )
    
    try:
        db.session.add(session_log)
        db.session.commit()
    except Exception:
        db.session.rollback()
    
    results_data = {
        'total_items': total_items,
        'correct_count': correct_count,
        'wrong_count': wrong_count,
        'accuracy': accuracy,
        'duration_minutes': duration_minutes,
        'focus_areas': review_data.get('focus_areas', [])
    }
    
    # Limpiar sesión
    session.pop('review_session', None)
    
    # Obtener nuevas estadísticas
    system = AdvancedReviewSystem(current_user.id)
    stats = system.get_statistics()
    recommendations = system.get_recommendations()
    
    return render_template('review/results.html',
                          results=results_data,
                          stats=stats,
                          recommendations=recommendations)


@review_bp.route('/stats')
@login_required
def stats():
    """API para obtener estadísticas de repaso."""
    system = AdvancedReviewSystem(current_user.id)
    stats = system.get_statistics()
    return jsonify(stats)


@review_bp.route('/weak-areas')
@login_required
def weak_areas():
    """API para obtener áreas débiles."""
    system = AdvancedReviewSystem(current_user.id)
    areas = system.get_weak_areas()
    return jsonify(areas)


@review_bp.route('/recommendations')
@login_required
def recommendations():
    """API para obtener recomendaciones de estudio."""
    system = AdvancedReviewSystem(current_user.id)
    recs = system.get_recommendations()
    return jsonify(recs)


@review_bp.route('/quick-review/<item_type>/<int:item_id>', methods=['POST'])
@login_required
def quick_review(item_type, item_id):
    """Endpoint rápido para registrar una revisión individual."""
    is_correct = request.json.get('is_correct', False)
    
    system = AdvancedReviewSystem(current_user.id)
    
    # Crear item mínimo para registrar
    from app.services.review_system import ReviewItem, ReviewItemType, Difficulty
    
    try:
        review_type = ReviewItemType(item_type)
    except ValueError:
        return jsonify({'error': 'Tipo inválido'}), 400
    
    item = ReviewItem(
        item_type=review_type,
        item_id=item_id,
        question='',
        answer='',
        hints=[],
        difficulty=Difficulty.MEDIUM,
        last_reviewed=None,
        times_correct=0,
        times_wrong=0,
        mastery_level=0,
        priority=0
    )
    
    result = system.record_review(item, is_correct)
    
    return jsonify(result)
