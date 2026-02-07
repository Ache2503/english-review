"""
Rutas para el Sistema de Estudio Intensivo
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.services.study_content import get_all_topics, get_topic, check_exercise_answer

study_bp = Blueprint('study', __name__, url_prefix='/study')


@study_bp.route('/')
@login_required
def study_home():
    """Página principal con todos los temas de estudio."""
    topics = get_all_topics()
    return render_template('study/index.html', topics=topics)


@study_bp.route('/topic/<topic_id>')
@login_required
def study_topic(topic_id):
    """Página de un tema específico con todo el contenido."""
    topic = get_topic(topic_id)
    if not topic:
        return render_template('errors/404.html'), 404
    
    all_topics = get_all_topics()
    current_index = next((i for i, t in enumerate(all_topics) if t['id'] == topic_id), 0)
    
    prev_topic = all_topics[current_index - 1] if current_index > 0 else None
    next_topic = all_topics[current_index + 1] if current_index < len(all_topics) - 1 else None
    
    return render_template('study/topic.html', 
                         topic=topic, 
                         topic_id=topic_id,
                         prev_topic=prev_topic,
                         next_topic=next_topic)


@study_bp.route('/api/check-answer', methods=['POST'])
@login_required
def check_answer():
    """API para verificar respuestas de ejercicios y guardar progreso."""
    data = request.get_json()
    
    topic_id = data.get('topic_id')
    exercise_index = data.get('exercise_index', 0)
    question_index = data.get('question_index', 0)
    user_answer = data.get('answer', '')
    
    # Pasar user_id para guardar progreso
    result = check_exercise_answer(
        topic_id, 
        exercise_index, 
        question_index, 
        user_answer,
        user_id=current_user.id
    )
    
    return jsonify(result)


@study_bp.route('/api/topic-stats/<topic_id>')
@login_required
def topic_stats(topic_id):
    """API para obtener estadísticas de un tema."""
    from app.models import StudyProgress
    
    stats = StudyProgress.query.filter_by(
        user_id=current_user.id,
        topic_id=topic_id
    ).first()
    
    if not stats:
        return jsonify({
            'success': True,
            'exercises_attempted': 0,
            'exercises_correct': 0,
            'success_rate': 0,
            'is_completed': False,
            'started_at': None,
            'completed_at': None
        })
    
    return jsonify({
        'success': True,
        'exercises_attempted': stats.exercises_attempted,
        'exercises_correct': stats.exercises_correct,
        'success_rate': stats.success_rate,
        'is_completed': stats.is_completed,
        'started_at': stats.started_at.isoformat() if stats.started_at else None,
        'completed_at': stats.completed_at.isoformat() if stats.completed_at else None
    })


@study_bp.route('/quick-reference/<topic_id>')
@login_required
def quick_reference(topic_id):
    """Vista de referencia rápida para un tema."""
    topic = get_topic(topic_id)
    if not topic:
        return render_template('errors/404.html'), 404
    
    return render_template('study/quick_reference.html', 
                         topic=topic, 
                         topic_id=topic_id)
