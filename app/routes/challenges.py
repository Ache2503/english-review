"""
Rutas para Daily Challenge, Leaderboard y sistema de puntos
"""
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    DailyChallenge, UserDailyChallenge, UserPoints, PointsTransaction,
    UserStreak, User
)
from datetime import datetime, date, timedelta
from sqlalchemy import func

challenges_bp = Blueprint('challenges', __name__, url_prefix='/challenges')


# ==========================================
# DAILY CHALLENGE
# ==========================================

@challenges_bp.route('/daily')
@login_required
def daily_challenge():
    """Página del reto diario"""
    today = date.today()
    
    # Obtener el reto de hoy
    challenge = DailyChallenge.query.filter_by(challenge_date=today).first()
    
    # Verificar si el usuario ya completó el reto
    completed = None
    if challenge:
        completed = UserDailyChallenge.query.filter_by(
            user_id=current_user.id,
            challenge_id=challenge.id
        ).first()
    
    # Obtener racha del usuario
    streak = UserStreak.query.filter_by(user_id=current_user.id).first()
    current_streak = streak.current_streak if streak else 0
    
    # Historial de retos recientes
    recent_completions = UserDailyChallenge.query.filter_by(
        user_id=current_user.id
    ).order_by(UserDailyChallenge.completed_at.desc()).limit(7).all()
    
    return render_template(
        'challenges/daily.html',
        challenge=challenge,
        completed=completed,
        current_streak=current_streak,
        recent_completions=recent_completions
    )


@challenges_bp.route('/daily/submit', methods=['POST'])
@login_required
def submit_daily_challenge():
    """Enviar respuestas del reto diario"""
    data = request.get_json()
    challenge_id = data.get('challenge_id')
    answers = data.get('answers', [])
    time_taken = data.get('time_taken', 0)
    
    challenge = DailyChallenge.query.get_or_404(challenge_id)
    
    # Verificar que no haya completado ya
    existing = UserDailyChallenge.query.filter_by(
        user_id=current_user.id,
        challenge_id=challenge_id
    ).first()
    
    if existing:
        return jsonify({'error': 'Ya completaste este reto'}), 400
    
    # Calcular puntuación
    questions = challenge.questions
    correct = 0
    results = []
    
    for i, answer in enumerate(answers):
        if i < len(questions):
            is_correct = answer.lower().strip() == questions[i].get('correct_answer', '').lower().strip()
            if is_correct:
                correct += 1
            results.append({
                'question': questions[i].get('question'),
                'user_answer': answer,
                'correct_answer': questions[i].get('correct_answer'),
                'is_correct': is_correct
            })
    
    score = (correct / len(questions) * 100) if questions else 0
    
    # Calcular puntos
    points_earned = int(challenge.points_reward * (score / 100))
    
    # Bonus por racha
    streak = UserStreak.query.filter_by(user_id=current_user.id).first()
    streak_bonus = 0
    if streak and streak.current_streak >= 3:
        streak_bonus = challenge.bonus_streak_points * min(streak.current_streak // 3, 5)
        points_earned += streak_bonus
    
    # Guardar resultado
    user_challenge = UserDailyChallenge(
        user_id=current_user.id,
        challenge_id=challenge_id,
        score=score,
        points_earned=points_earned,
        answers=results,
        time_taken_seconds=time_taken
    )
    db.session.add(user_challenge)
    
    # Actualizar puntos
    add_points(current_user.id, points_earned, 'daily_challenge', f'Reto diario: {challenge.title}')
    
    # Actualizar racha
    update_streak(current_user.id)
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'score': score,
        'correct': correct,
        'total': len(questions),
        'points_earned': points_earned,
        'streak_bonus': streak_bonus,
        'results': results
    })


# ==========================================
# LEADERBOARD
# ==========================================

@challenges_bp.route('/leaderboard')
@login_required
def leaderboard():
    """Tabla de clasificación"""
    period = request.args.get('period', 'total')  # total, weekly, monthly
    
    # Query base
    query = db.session.query(
        User.id,
        User.username,
        User.full_name,
        UserPoints.total_points,
        UserPoints.weekly_points,
        UserPoints.monthly_points,
        UserPoints.level,
        UserStreak.current_streak,
        UserStreak.longest_streak
    ).outerjoin(UserPoints, User.id == UserPoints.user_id)\
     .outerjoin(UserStreak, User.id == UserStreak.user_id)
    
    # Ordenar según período
    if period == 'weekly':
        query = query.order_by(UserPoints.weekly_points.desc().nullslast())
    elif period == 'monthly':
        query = query.order_by(UserPoints.monthly_points.desc().nullslast())
    else:
        query = query.order_by(UserPoints.total_points.desc().nullslast())
    
    top_users = query.limit(50).all()
    
    # Posición del usuario actual
    user_points = UserPoints.query.filter_by(user_id=current_user.id).first()
    user_rank = None
    if user_points:
        if period == 'weekly':
            user_rank = UserPoints.query.filter(
                UserPoints.weekly_points > user_points.weekly_points
            ).count() + 1
        elif period == 'monthly':
            user_rank = UserPoints.query.filter(
                UserPoints.monthly_points > user_points.monthly_points
            ).count() + 1
        else:
            user_rank = UserPoints.query.filter(
                UserPoints.total_points > user_points.total_points
            ).count() + 1
    
    return render_template(
        'challenges/leaderboard.html',
        top_users=top_users,
        period=period,
        user_points=user_points,
        user_rank=user_rank
    )


# ==========================================
# PUNTOS
# ==========================================

@challenges_bp.route('/points')
@login_required
def my_points():
    """Ver mis puntos y transacciones"""
    user_points = UserPoints.query.filter_by(user_id=current_user.id).first()
    
    if not user_points:
        user_points = UserPoints(user_id=current_user.id)
        db.session.add(user_points)
        db.session.commit()
    
    # Historial reciente
    transactions = PointsTransaction.query.filter_by(
        user_id=current_user.id
    ).order_by(PointsTransaction.created_at.desc()).limit(20).all()
    
    # Estadísticas
    stats = {
        'total_challenges': UserDailyChallenge.query.filter_by(user_id=current_user.id).count(),
        'total_transactions': PointsTransaction.query.filter_by(user_id=current_user.id).count(),
        'this_week': db.session.query(func.sum(PointsTransaction.points)).filter(
            PointsTransaction.user_id == current_user.id,
            PointsTransaction.created_at >= datetime.now() - timedelta(days=7)
        ).scalar() or 0
    }
    
    return render_template(
        'challenges/points.html',
        user_points=user_points,
        transactions=transactions,
        stats=stats
    )


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def add_points(user_id, points, source, description=None):
    """Agregar puntos a un usuario"""
    user_points = UserPoints.query.filter_by(user_id=user_id).first()
    
    if not user_points:
        user_points = UserPoints(user_id=user_id)
        db.session.add(user_points)
    
    user_points.total_points += points
    user_points.weekly_points += points
    user_points.monthly_points += points
    user_points.experience += points
    user_points.last_points_update = datetime.utcnow()
    
    # Calcular nivel (cada 500 puntos)
    user_points.level = (user_points.experience // 500) + 1
    
    # Registrar transacción
    transaction = PointsTransaction(
        user_id=user_id,
        points=points,
        source=source,
        description=description
    )
    db.session.add(transaction)


def update_streak(user_id):
    """Actualizar racha del usuario"""
    streak = UserStreak.query.filter_by(user_id=user_id).first()
    today = date.today()
    
    if not streak:
        streak = UserStreak(user_id=user_id, current_streak=1, longest_streak=1, last_activity_date=today)
        db.session.add(streak)
    else:
        if streak.last_activity_date == today:
            return  # Ya actualizó hoy
        elif streak.last_activity_date == today - timedelta(days=1):
            streak.current_streak += 1
            if streak.current_streak > streak.longest_streak:
                streak.longest_streak = streak.current_streak
        else:
            streak.current_streak = 1
        
        streak.last_activity_date = today
