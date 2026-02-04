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
    """API para verificar respuestas de ejercicios."""
    data = request.get_json()
    
    topic_id = data.get('topic_id')
    exercise_index = data.get('exercise_index', 0)
    question_index = data.get('question_index', 0)
    user_answer = data.get('answer', '')
    
    result = check_exercise_answer(topic_id, exercise_index, question_index, user_answer)
    return jsonify(result)


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
