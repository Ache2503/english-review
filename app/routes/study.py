"""
Rutas para el Sistema de Estudio Intensivo
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models import StudyTopicContent

study_bp = Blueprint('study', __name__, url_prefix='/study')


def get_all_topics():
    topics = StudyTopicContent.query.order_by(StudyTopicContent.id).all()
    return [
        {
            'id': t.slug,
            'title': t.title,
            'icon': t.icon,
            'difficulty': t.difficulty,
            'estimated_time': t.estimated_time,
            'description': t.description
        }
        for t in topics
    ]


def get_topic(topic_id):
    t = StudyTopicContent.query.filter_by(slug=topic_id).first()
    if not t:
        return None
    return {
        'title': t.title,
        'icon': t.icon,
        'difficulty': t.difficulty,
        'estimated_time': t.estimated_time,
        'description': t.description,
        'theory': t.theory,
        'common_mistakes': t.common_mistakes,
        'tips': t.tips,
        'exercises': t.exercises,
    }


def check_exercise_answer(topic_id, exercise_index, question_index, user_answer, user_id=None):
    from app.extensions import db
    from app.models import StudyExerciseResult, StudyProgress
    from datetime import datetime

    t = StudyTopicContent.query.filter_by(slug=topic_id).first()
    if not t:
        return {'correct': False, 'message': 'Tema no encontrado'}

    exercises = t.exercises or []
    if exercise_index >= len(exercises):
        return {'correct': False, 'message': 'Ejercicio no encontrado'}

    exercise = exercises[exercise_index]
    questions = exercise.get('questions', [])
    if question_index >= len(questions):
        return {'correct': False, 'message': 'Pregunta no encontrada'}

    question = questions[question_index]
    correct_answer = question.get('answer', '').lower().strip()
    user_answer = user_answer.lower().strip()

    correct_parts = correct_answer.replace('...', ' ').replace('  ', ' ').split()
    user_parts = user_answer.replace('...', ' ').replace('  ', ' ').split()

    is_correct = correct_answer == user_answer or correct_parts == user_parts

    result = {
        'correct': is_correct,
        'correct_answer': question.get('answer'),
        'explanation': question.get('explanation', question.get('hint', ''))
    }

    if user_id:
        try:
            exercise_result = StudyExerciseResult.query.filter_by(
                user_id=user_id,
                topic_id=topic_id,
                exercise_index=exercise_index,
                question_index=question_index
            ).first()

            if exercise_result:
                exercise_result.attempts += 1
                exercise_result.is_correct = is_correct
                exercise_result.user_answer = user_answer
                exercise_result.completed_at = datetime.utcnow()
            else:
                exercise_result = StudyExerciseResult(
                    user_id=user_id,
                    topic_id=topic_id,
                    exercise_index=exercise_index,
                    question_index=question_index,
                    user_answer=user_answer,
                    is_correct=is_correct
                )
                db.session.add(exercise_result)

            study_progress = StudyProgress.query.filter_by(
                user_id=user_id,
                topic_id=topic_id
            ).first()

            if not study_progress:
                study_progress = StudyProgress(
                    user_id=user_id,
                    topic_id=topic_id,
                    exercises_attempted=1,
                    exercises_correct=1 if is_correct else 0
                )
                db.session.add(study_progress)
            else:
                study_progress.exercises_attempted += 1
                if is_correct:
                    study_progress.exercises_correct += 1
                study_progress.updated_at = datetime.utcnow()

            study_progress.success_rate = study_progress.calculate_success_rate()
            db.session.commit()

            result['stats'] = {
                'exercises_attempted': study_progress.exercises_attempted,
                'exercises_correct': study_progress.exercises_correct,
                'success_rate': study_progress.success_rate
            }
        except Exception:
            db.session.rollback()

    return result


@study_bp.route('/')
@login_required
def study_home():
    topics = get_all_topics()
    return render_template('study/index.html', topics=topics)


@study_bp.route('/topic/<topic_id>')
@login_required
def study_topic(topic_id):
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
    data = request.get_json()

    topic_id = data.get('topic_id')
    exercise_index = data.get('exercise_index', 0)
    question_index = data.get('question_index', 0)
    user_answer = data.get('answer', '')

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
    topic = get_topic(topic_id)
    if not topic:
        return render_template('errors/404.html'), 404

    return render_template('study/quick_reference.html',
                         topic=topic,
                         topic_id=topic_id)
