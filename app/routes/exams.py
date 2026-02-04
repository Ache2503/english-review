"""
Rutas para Exam Simulator - Simulador de exámenes TOEFL, IELTS, Cambridge
"""
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models import ExamSimulator, ExamSection, UserExamAttempt
from datetime import datetime
from app.routes.challenges import add_points

exams_bp = Blueprint('exams', __name__, url_prefix='/exams')


@exams_bp.route('/')
@login_required
def exam_list():
    """Lista de exámenes disponibles"""
    exams = ExamSimulator.query.filter_by(is_active=True).all()
    
    # Agrupar por tipo
    exam_types = {}
    for exam in exams:
        if exam.exam_type not in exam_types:
            exam_types[exam.exam_type] = []
        exam_types[exam.exam_type].append(exam)
    
    # Historial del usuario
    user_attempts = UserExamAttempt.query.filter_by(
        user_id=current_user.id
    ).order_by(UserExamAttempt.completed_at.desc()).limit(10).all()
    
    # Mejores puntuaciones
    best_scores = {}
    for attempt in UserExamAttempt.query.filter_by(user_id=current_user.id).all():
        if attempt.exam_id not in best_scores:
            best_scores[attempt.exam_id] = attempt.percentage
        else:
            best_scores[attempt.exam_id] = max(best_scores[attempt.exam_id], attempt.percentage or 0)
    
    return render_template(
        'exams/list.html',
        exam_types=exam_types,
        user_attempts=user_attempts,
        best_scores=best_scores
    )


@exams_bp.route('/<int:exam_id>')
@login_required
def exam_detail(exam_id):
    """Detalles del examen antes de iniciar"""
    exam = ExamSimulator.query.get_or_404(exam_id)
    sections = ExamSection.query.filter_by(exam_id=exam_id).order_by(ExamSection.order).all()
    
    # Intentos previos
    attempts = UserExamAttempt.query.filter_by(
        user_id=current_user.id,
        exam_id=exam_id
    ).order_by(UserExamAttempt.completed_at.desc()).limit(5).all()
    
    return render_template(
        'exams/detail.html',
        exam=exam,
        sections=sections,
        attempts=attempts
    )


@exams_bp.route('/<int:exam_id>/start')
@login_required
def start_exam(exam_id):
    """Iniciar un examen"""
    exam = ExamSimulator.query.get_or_404(exam_id)
    sections = ExamSection.query.filter_by(exam_id=exam_id).order_by(ExamSection.order).all()
    
    return render_template(
        'exams/take.html',
        exam=exam,
        sections=sections
    )


@exams_bp.route('/<int:exam_id>/submit', methods=['POST'])
@login_required
def submit_exam(exam_id):
    """Enviar respuestas del examen"""
    exam = ExamSimulator.query.get_or_404(exam_id)
    sections = ExamSection.query.filter_by(exam_id=exam_id).all()
    
    data = request.get_json()
    answers = data.get('answers', {})
    time_taken = data.get('time_taken', 0)
    
    # Calcular puntuación por sección
    section_scores = {}
    total_correct = 0
    total_questions = 0
    all_results = {}
    
    for section in sections:
        section_answers = answers.get(str(section.id), {})
        section_correct = 0
        section_questions = section.questions or []
        section_results = []
        
        for i, question in enumerate(section_questions):
            user_answer = section_answers.get(str(i), '')
            correct_answer = question.get('correct_answer', '')
            
            # Comparar respuestas (case insensitive)
            is_correct = False
            if isinstance(correct_answer, list):
                is_correct = user_answer.lower().strip() in [a.lower().strip() for a in correct_answer]
            else:
                is_correct = user_answer.lower().strip() == correct_answer.lower().strip()
            
            if is_correct:
                section_correct += 1
                total_correct += 1
            
            total_questions += 1
            
            section_results.append({
                'question': question.get('question', ''),
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': is_correct,
                'explanation': question.get('explanation', '')
            })
        
        section_score = (section_correct / len(section_questions) * 100) if section_questions else 0
        section_scores[section.section_type] = {
            'score': section_score,
            'correct': section_correct,
            'total': len(section_questions)
        }
        all_results[section.section_type] = section_results
    
    # Puntuación total
    total_percentage = (total_correct / total_questions * 100) if total_questions else 0
    passed = total_percentage >= exam.passing_score
    
    # Guardar intento
    attempt = UserExamAttempt(
        user_id=current_user.id,
        exam_id=exam_id,
        section_scores=section_scores,
        total_score=total_correct,
        percentage=total_percentage,
        passed=passed,
        time_taken_minutes=time_taken // 60,
        answers=all_results,
        completed_at=datetime.utcnow()
    )
    db.session.add(attempt)
    
    # Dar puntos
    points = int(total_percentage) + (50 if passed else 0)
    add_points(current_user.id, points, 'exam', f'Examen {exam.exam_type}: {exam.title}')
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'attempt_id': attempt.id,
        'percentage': total_percentage,
        'passed': passed,
        'section_scores': section_scores,
        'total_correct': total_correct,
        'total_questions': total_questions,
        'points_earned': points
    })


@exams_bp.route('/attempt/<int:attempt_id>')
@login_required
def view_attempt(attempt_id):
    """Ver resultados de un intento"""
    attempt = UserExamAttempt.query.get_or_404(attempt_id)
    
    # Verificar que es del usuario actual
    if attempt.user_id != current_user.id:
        flash('No tienes permiso para ver este intento', 'error')
        return redirect(url_for('exams.exam_list'))
    
    exam = ExamSimulator.query.get(attempt.exam_id)
    
    return render_template(
        'exams/result.html',
        attempt=attempt,
        exam=exam
    )
