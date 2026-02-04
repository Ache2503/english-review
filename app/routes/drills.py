"""
Rutas para Grammar Drills y Error Tracker
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    GrammarDrill, UserDrillResult, UserErrorPattern, ErrorLog, Unit
)
from datetime import datetime, timedelta
from sqlalchemy import func
from app.routes.challenges import add_points

drills_bp = Blueprint('drills', __name__, url_prefix='/drills')


# ==========================================
# GRAMMAR DRILLS
# ==========================================

@drills_bp.route('/')
@login_required
def drill_list():
    """Lista de ejercicios intensivos disponibles"""
    level = request.args.get('level', None)
    topic = request.args.get('topic', None)
    
    query = GrammarDrill.query.filter_by(is_active=True)
    
    if level:
        query = query.filter_by(level=level)
    if topic:
        query = query.filter(GrammarDrill.grammar_topic.ilike(f'%{topic}%'))
    
    drills = query.order_by(GrammarDrill.level, GrammarDrill.grammar_topic).all()
    
    # Agrupar por nivel
    drills_by_level = {}
    for drill in drills:
        if drill.level not in drills_by_level:
            drills_by_level[drill.level] = []
        drills_by_level[drill.level].append(drill)
    
    # Estadísticas del usuario
    user_stats = {}
    for drill in drills:
        best = UserDrillResult.query.filter_by(
            user_id=current_user.id,
            drill_id=drill.id
        ).order_by(UserDrillResult.score.desc()).first()
        
        attempts = UserDrillResult.query.filter_by(
            user_id=current_user.id,
            drill_id=drill.id
        ).count()
        
        user_stats[drill.id] = {
            'best_score': best.score if best else None,
            'passed': best.passed if best else False,
            'attempts': attempts
        }
    
    # Obtener niveles y tópicos disponibles
    levels = db.session.query(GrammarDrill.level).distinct().all()
    topics = db.session.query(GrammarDrill.grammar_topic).distinct().all()
    
    return render_template(
        'drills/list.html',
        drills_by_level=drills_by_level,
        user_stats=user_stats,
        levels=[l[0] for l in levels],
        topics=[t[0] for t in topics],
        current_level=level,
        current_topic=topic
    )


@drills_bp.route('/<int:drill_id>')
@login_required
def take_drill(drill_id):
    """Tomar un drill"""
    drill = GrammarDrill.query.get_or_404(drill_id)
    
    return render_template(
        'drills/take.html',
        drill=drill
    )


@drills_bp.route('/<int:drill_id>/submit', methods=['POST'])
@login_required
def submit_drill(drill_id):
    """Enviar respuestas de drill"""
    drill = GrammarDrill.query.get_or_404(drill_id)
    data = request.get_json()
    
    answers = data.get('answers', [])
    time_taken = data.get('time_taken', 0)
    
    # Calcular puntuación
    questions = drill.questions or []
    correct = 0
    results = []
    errors = []
    
    for i, answer in enumerate(answers):
        if i < len(questions):
            question = questions[i]
            correct_answer = question.get('correct_answer', '')
            
            # Verificar respuesta
            is_correct = False
            if isinstance(correct_answer, list):
                is_correct = answer.lower().strip() in [a.lower().strip() for a in correct_answer]
            else:
                is_correct = answer.lower().strip() == correct_answer.lower().strip()
            
            if is_correct:
                correct += 1
            else:
                # Registrar error
                errors.append({
                    'question': question.get('question', ''),
                    'user_answer': answer,
                    'correct_answer': correct_answer,
                    'grammar_topic': drill.grammar_topic
                })
            
            results.append({
                'question': question.get('question', ''),
                'user_answer': answer,
                'correct_answer': correct_answer,
                'is_correct': is_correct,
                'explanation': question.get('explanation', '')
            })
    
    score = (correct / len(questions) * 100) if questions else 0
    passed = score >= drill.passing_score
    
    # Guardar resultado
    result = UserDrillResult(
        user_id=current_user.id,
        drill_id=drill_id,
        score=score,
        correct_answers=correct,
        total_questions=len(questions),
        time_taken_seconds=time_taken,
        passed=passed,
        answers=results
    )
    db.session.add(result)
    
    # Registrar errores
    for error in errors:
        log_error(
            current_user.id,
            'drill',
            error['grammar_topic'],
            f"Respuesta incorrecta: '{error['user_answer']}' en vez de '{error['correct_answer']}'",
            error['question']
        )
    
    # Dar puntos
    points = int(score / 10) + (20 if passed else 0)
    if time_taken < drill.time_limit_seconds * 0.5:
        points += 10  # Bonus por velocidad
    
    add_points(current_user.id, points, 'drill', f'Drill: {drill.title}')
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'score': score,
        'passed': passed,
        'correct': correct,
        'total': len(questions),
        'time_taken': time_taken,
        'points_earned': points,
        'results': results
    })


# ==========================================
# ERROR TRACKER
# ==========================================

@drills_bp.route('/errors')
@login_required
def error_tracker():
    """Ver análisis de errores del usuario"""
    # Patrones de error más frecuentes
    error_patterns = UserErrorPattern.query.filter_by(
        user_id=current_user.id
    ).order_by(UserErrorPattern.error_count.desc()).limit(10).all()
    
    # Errores por categoría
    error_by_category = db.session.query(
        UserErrorPattern.error_category,
        func.sum(UserErrorPattern.error_count)
    ).filter_by(user_id=current_user.id)\
     .group_by(UserErrorPattern.error_category).all()
    
    # Errores recientes
    recent_errors = ErrorLog.query.filter_by(
        user_id=current_user.id
    ).order_by(ErrorLog.created_at.desc()).limit(20).all()
    
    # Progreso (errores por semana)
    week_ago = datetime.utcnow() - timedelta(days=7)
    errors_this_week = ErrorLog.query.filter(
        ErrorLog.user_id == current_user.id,
        ErrorLog.created_at >= week_ago
    ).count()
    
    two_weeks_ago = datetime.utcnow() - timedelta(days=14)
    errors_last_week = ErrorLog.query.filter(
        ErrorLog.user_id == current_user.id,
        ErrorLog.created_at >= two_weeks_ago,
        ErrorLog.created_at < week_ago
    ).count()
    
    improvement = None
    if errors_last_week > 0:
        improvement = round((1 - errors_this_week / errors_last_week) * 100, 1)
    
    return render_template(
        'drills/errors.html',
        error_patterns=error_patterns,
        error_by_category=dict(error_by_category),
        recent_errors=recent_errors,
        errors_this_week=errors_this_week,
        errors_last_week=errors_last_week,
        improvement=improvement
    )


@drills_bp.route('/errors/suggestions')
@login_required
def error_suggestions():
    """Obtener sugerencias basadas en errores"""
    # Top 3 categorías con más errores
    top_errors = UserErrorPattern.query.filter_by(
        user_id=current_user.id
    ).order_by(UserErrorPattern.error_count.desc()).limit(3).all()
    
    suggestions = []
    for error in top_errors:
        suggestion = {
            'error_type': error.error_type,
            'error_category': error.error_category,
            'count': error.error_count,
            'tips': get_error_tips(error.error_category, error.error_type),
            'recommended_drills': get_recommended_drills(error.error_type)
        }
        suggestions.append(suggestion)
    
    return jsonify({'suggestions': suggestions})


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def log_error(user_id, source, error_type, message, context=None):
    """Registrar un error del usuario"""
    # Crear log
    error_log = ErrorLog(
        user_id=user_id,
        source=source,
        message=message,
        context=context,
        rule=error_type
    )
    db.session.add(error_log)
    
    # Actualizar patrón
    pattern = UserErrorPattern.query.filter_by(
        user_id=user_id,
        error_category=source,
        error_type=error_type
    ).first()
    
    if pattern:
        pattern.error_count += 1
        pattern.last_occurrence = datetime.utcnow()
        if pattern.examples:
            examples = pattern.examples
            examples.append({'message': message, 'context': context})
            pattern.examples = examples[-10:]  # Mantener últimos 10
        else:
            pattern.examples = [{'message': message, 'context': context}]
    else:
        pattern = UserErrorPattern(
            user_id=user_id,
            error_category=source,
            error_type=error_type,
            examples=[{'message': message, 'context': context}]
        )
        db.session.add(pattern)


def get_error_tips(category, error_type):
    """Obtener consejos para un tipo de error"""
    tips = {
        'grammar': {
            'verb_tenses': [
                'Practica identificar el tiempo verbal en oraciones',
                'Crea tarjetas con las conjugaciones irregulares',
                'Lee textos y subraya los verbos'
            ],
            'articles': [
                'Recuerda: "a" antes de consonante, "an" antes de vocal',
                'Los nombres propios no llevan artículo',
                'Usa "the" para cosas específicas'
            ],
            'prepositions': [
                'Las preposiciones de tiempo: in (meses/años), on (días), at (hora)',
                'Memoriza las combinaciones verbo + preposición',
                'Practica con ejercicios de fill-in-the-blank'
            ]
        },
        'vocabulary': {
            'spelling': [
                'Lee en voz alta mientras escribes',
                'Usa la técnica de "look, cover, write, check"',
                'Agrupa palabras con patrones similares'
            ],
            'word_choice': [
                'Usa un diccionario de sinónimos',
                'Aprende palabras en contexto, no aisladas',
                'Practica con ejercicios de matching'
            ]
        }
    }
    
    return tips.get(category, {}).get(error_type, [
        'Practica regularmente',
        'Revisa tus errores anteriores',
        'Pide feedback en tus escritos'
    ])


def get_recommended_drills(error_type):
    """Obtener drills recomendados para un tipo de error"""
    drills = GrammarDrill.query.filter(
        GrammarDrill.grammar_topic.ilike(f'%{error_type}%'),
        GrammarDrill.is_active == True
    ).limit(3).all()
    
    return [{
        'id': d.id,
        'title': d.title,
        'level': d.level
    } for d in drills]
