"""
Rutas para Progress Reports - Reportes detallados de progreso
"""
from flask import Blueprint, render_template, request, jsonify, Response
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    User, UserProgress, UserPoints, UserStreak, UserDailyChallenge,
    UserExamAttempt, UserDrillResult, UserGameScore, UserQuizSubmission,
    UserWritingSubmission, UserFlashcardSRS, ErrorLog, Unit, Badge, user_badges
)
from datetime import datetime, timedelta
from sqlalchemy import func
import json

reports_bp = Blueprint('reports', __name__, url_prefix='/reports')


@reports_bp.route('/')
@login_required
def dashboard():
    """Dashboard principal de reportes"""
    # Estadísticas generales
    stats = get_user_stats(current_user.id)
    
    # Actividad reciente (últimos 30 días)
    activity = get_activity_chart_data(current_user.id, 30)
    
    # Progreso por área
    area_progress = get_area_progress(current_user.id)
    
    # Puntos por categoría
    points_breakdown = get_points_breakdown(current_user.id)
    
    return render_template(
        'reports/dashboard.html',
        stats=stats,
        activity=activity,
        area_progress=area_progress,
        points_breakdown=points_breakdown
    )


@reports_bp.route('/detailed')
@login_required
def detailed_report():
    """Reporte detallado completo"""
    period = request.args.get('period', '30')  # días
    days = int(period)
    
    since = datetime.utcnow() - timedelta(days=days)
    
    # Estadísticas del período
    stats = get_period_stats(current_user.id, since)
    
    # Desglose por actividad
    activities = get_activity_breakdown(current_user.id, since)
    
    # Errores más frecuentes
    errors = get_top_errors(current_user.id, since)
    
    # Progreso en unidades
    unit_progress = get_unit_progress(current_user.id)
    
    # Comparación con período anterior
    prev_since = since - timedelta(days=days)
    prev_stats = get_period_stats(current_user.id, prev_since, since)
    comparison = compare_stats(stats, prev_stats)
    
    return render_template(
        'reports/detailed.html',
        stats=stats,
        activities=activities,
        errors=errors,
        unit_progress=unit_progress,
        comparison=comparison,
        period=period
    )


@reports_bp.route('/export')
@login_required
def export_report():
    """Exportar reporte en JSON"""
    period = request.args.get('period', '30')
    days = int(period)
    since = datetime.utcnow() - timedelta(days=days)
    
    report = {
        'user': {
            'username': current_user.username,
            'email': current_user.email,
            'member_since': current_user.created_at.isoformat() if current_user.created_at else None
        },
        'generated_at': datetime.utcnow().isoformat(),
        'period_days': days,
        'stats': get_user_stats(current_user.id),
        'period_stats': get_period_stats(current_user.id, since),
        'area_progress': get_area_progress(current_user.id),
        'unit_progress': get_unit_progress(current_user.id),
        'top_errors': get_top_errors(current_user.id, since),
        'activity_breakdown': get_activity_breakdown(current_user.id, since)
    }
    
    return Response(
        json.dumps(report, indent=2, default=str),
        mimetype='application/json',
        headers={'Content-Disposition': f'attachment;filename=report_{current_user.username}_{datetime.now().strftime("%Y%m%d")}.json'}
    )


@reports_bp.route('/achievements')
@login_required
def achievements():
    """Ver logros y badges"""
    # Badges obtenidos
    earned_badges = db.session.query(Badge, user_badges.c.earned_at).join(
        user_badges, Badge.id == user_badges.c.badge_id
    ).filter(user_badges.c.user_id == current_user.id).all()
    
    # Todos los badges
    all_badges = Badge.query.all()
    earned_ids = [b[0].id for b in earned_badges]
    
    # Organizar por tipo
    badges_by_type = {}
    for badge in all_badges:
        if badge.badge_type not in badges_by_type:
            badges_by_type[badge.badge_type] = []
        badges_by_type[badge.badge_type].append({
            'badge': badge,
            'earned': badge.id in earned_ids,
            'earned_at': next((b[1] for b in earned_badges if b[0].id == badge.id), None)
        })
    
    # Próximos logros (basado en progreso)
    next_achievements = get_next_achievements(current_user.id)
    
    return render_template(
        'reports/achievements.html',
        badges_by_type=badges_by_type,
        earned_count=len(earned_badges),
        total_count=len(all_badges),
        next_achievements=next_achievements
    )


@reports_bp.route('/weekly-summary')
@login_required
def weekly_summary():
    """Resumen semanal"""
    week_ago = datetime.utcnow() - timedelta(days=7)
    
    summary = {
        'challenges_completed': UserDailyChallenge.query.filter(
            UserDailyChallenge.user_id == current_user.id,
            UserDailyChallenge.completed_at >= week_ago
        ).count(),
        
        'quizzes_taken': UserQuizSubmission.query.filter(
            UserQuizSubmission.user_id == current_user.id,
            UserQuizSubmission.submitted_at >= week_ago
        ).count(),
        
        'drills_completed': UserDrillResult.query.filter(
            UserDrillResult.user_id == current_user.id,
            UserDrillResult.completed_at >= week_ago
        ).count(),
        
        'games_played': UserGameScore.query.filter(
            UserGameScore.user_id == current_user.id,
            UserGameScore.played_at >= week_ago
        ).count(),
        
        'writings_submitted': UserWritingSubmission.query.filter(
            UserWritingSubmission.user_id == current_user.id,
            UserWritingSubmission.submitted_at >= week_ago
        ).count(),
        
        'flashcards_reviewed': db.session.query(func.count(UserFlashcardSRS.id)).filter(
            UserFlashcardSRS.user_id == current_user.id,
            UserFlashcardSRS.last_reviewed_at >= week_ago
        ).scalar() or 0,
        
        'errors_made': ErrorLog.query.filter(
            ErrorLog.user_id == current_user.id,
            ErrorLog.created_at >= week_ago
        ).count()
    }
    
    # Calcular puntos ganados esta semana
    user_points = UserPoints.query.filter_by(user_id=current_user.id).first()
    summary['points_earned'] = user_points.weekly_points if user_points else 0
    
    # Racha actual
    streak = UserStreak.query.filter_by(user_id=current_user.id).first()
    summary['current_streak'] = streak.current_streak if streak else 0
    
    # Día más activo
    daily_activity = db.session.query(
        func.date(ErrorLog.created_at),
        func.count(ErrorLog.id)
    ).filter(
        ErrorLog.user_id == current_user.id,
        ErrorLog.created_at >= week_ago
    ).group_by(func.date(ErrorLog.created_at)).all()
    
    if daily_activity:
        most_active = max(daily_activity, key=lambda x: x[1])
        summary['most_active_day'] = most_active[0]
    else:
        summary['most_active_day'] = None
    
    return render_template(
        'reports/weekly_summary.html',
        summary=summary
    )


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_user_stats(user_id):
    """Obtener estadísticas generales del usuario"""
    user_points = UserPoints.query.filter_by(user_id=user_id).first()
    streak = UserStreak.query.filter_by(user_id=user_id).first()
    
    total_units = Unit.query.count()
    completed_units = UserProgress.query.filter_by(
        user_id=user_id,
        completed=True
    ).count()
    
    return {
        'total_points': user_points.total_points if user_points else 0,
        'level': user_points.level if user_points else 1,
        'current_streak': streak.current_streak if streak else 0,
        'longest_streak': streak.longest_streak if streak else 0,
        'units_completed': completed_units,
        'total_units': total_units,
        'completion_percentage': round(completed_units / total_units * 100, 1) if total_units else 0
    }


def get_period_stats(user_id, since, until=None):
    """Estadísticas de un período específico"""
    if until is None:
        until = datetime.utcnow()
    
    return {
        'challenges': UserDailyChallenge.query.filter(
            UserDailyChallenge.user_id == user_id,
            UserDailyChallenge.completed_at >= since,
            UserDailyChallenge.completed_at < until
        ).count(),
        
        'quizzes': UserQuizSubmission.query.filter(
            UserQuizSubmission.user_id == user_id,
            UserQuizSubmission.submitted_at >= since,
            UserQuizSubmission.submitted_at < until
        ).count(),
        
        'drills': UserDrillResult.query.filter(
            UserDrillResult.user_id == user_id,
            UserDrillResult.completed_at >= since,
            UserDrillResult.completed_at < until
        ).count(),
        
        'games': UserGameScore.query.filter(
            UserGameScore.user_id == user_id,
            UserGameScore.played_at >= since,
            UserGameScore.played_at < until
        ).count(),
        
        'avg_quiz_score': db.session.query(func.avg(UserQuizSubmission.score)).filter(
            UserQuizSubmission.user_id == user_id,
            UserQuizSubmission.submitted_at >= since,
            UserQuizSubmission.submitted_at < until
        ).scalar() or 0,
        
        'avg_drill_score': db.session.query(func.avg(UserDrillResult.score)).filter(
            UserDrillResult.user_id == user_id,
            UserDrillResult.completed_at >= since,
            UserDrillResult.completed_at < until
        ).scalar() or 0
    }


def get_activity_chart_data(user_id, days):
    """Datos para gráfica de actividad"""
    data = []
    for i in range(days, -1, -1):
        date = datetime.utcnow().date() - timedelta(days=i)
        
        # Contar actividades del día
        count = ErrorLog.query.filter(
            ErrorLog.user_id == user_id,
            func.date(ErrorLog.created_at) == date
        ).count()
        
        data.append({
            'date': date.isoformat(),
            'activity': count
        })
    
    return data


def get_area_progress(user_id):
    """Progreso por área de estudio"""
    areas = {
        'grammar': {
            'total': UserDrillResult.query.filter_by(user_id=user_id).count(),
            'avg_score': db.session.query(func.avg(UserDrillResult.score)).filter_by(user_id=user_id).scalar() or 0
        },
        'vocabulary': {
            'total': UserFlashcardSRS.query.filter_by(user_id=user_id).count(),
            'mastered': UserFlashcardSRS.query.filter_by(user_id=user_id).filter(
                UserFlashcardSRS.repetitions >= 6
            ).count()
        },
        'quizzes': {
            'total': UserQuizSubmission.query.filter_by(user_id=user_id).count(),
            'avg_score': db.session.query(func.avg(UserQuizSubmission.score)).filter_by(user_id=user_id).scalar() or 0
        },
        'games': {
            'total': UserGameScore.query.filter_by(user_id=user_id).count(),
            'best': db.session.query(func.max(UserGameScore.score)).filter_by(user_id=user_id).scalar() or 0
        },
        'writing': {
            'total': UserWritingSubmission.query.filter_by(user_id=user_id).count(),
            'avg_score': db.session.query(func.avg(UserWritingSubmission.score)).filter_by(user_id=user_id).scalar() or 0
        }
    }
    
    return areas


def get_points_breakdown(user_id):
    """Desglose de puntos por fuente"""
    from app.models import PointsTransaction
    
    breakdown = db.session.query(
        PointsTransaction.source,
        func.sum(PointsTransaction.points)
    ).filter_by(user_id=user_id).group_by(PointsTransaction.source).all()
    
    return dict(breakdown)


def get_activity_breakdown(user_id, since):
    """Desglose de actividades"""
    return {
        'daily_challenges': UserDailyChallenge.query.filter(
            UserDailyChallenge.user_id == user_id,
            UserDailyChallenge.completed_at >= since
        ).all(),
        'drills': UserDrillResult.query.filter(
            UserDrillResult.user_id == user_id,
            UserDrillResult.completed_at >= since
        ).order_by(UserDrillResult.completed_at.desc()).limit(10).all(),
        'games': UserGameScore.query.filter(
            UserGameScore.user_id == user_id,
            UserGameScore.played_at >= since
        ).order_by(UserGameScore.played_at.desc()).limit(10).all()
    }


def get_top_errors(user_id, since):
    """Errores más frecuentes"""
    from app.models import UserErrorPattern
    
    return UserErrorPattern.query.filter_by(
        user_id=user_id
    ).order_by(UserErrorPattern.error_count.desc()).limit(5).all()


def get_unit_progress(user_id):
    """Progreso por unidad"""
    progress = UserProgress.query.filter_by(user_id=user_id).all()
    
    units = []
    for p in progress:
        unit = Unit.query.get(p.unit_id)
        if unit:
            units.append({
                'unit_number': unit.unit_number,
                'title': unit.title,
                'completed': p.completed,
                'percentage': p.progress_percentage
            })
    
    return sorted(units, key=lambda x: x['unit_number'])


def compare_stats(current, previous):
    """Comparar estadísticas entre períodos"""
    comparison = {}
    for key in current:
        if key in previous and previous[key] and current[key]:
            if isinstance(current[key], (int, float)) and isinstance(previous[key], (int, float)):
                if previous[key] > 0:
                    change = ((current[key] - previous[key]) / previous[key]) * 100
                    comparison[key] = round(change, 1)
                else:
                    comparison[key] = 100 if current[key] > 0 else 0
    return comparison


def get_next_achievements(user_id):
    from app.models import AchievementMilestone
    achievements = []
    
    user_points = UserPoints.query.filter_by(user_id=user_id).first()
    points = user_points.total_points if user_points else 0
    
    streak = UserStreak.query.filter_by(user_id=user_id).first()
    current_streak = streak.current_streak if streak else 0
    
    milestones = AchievementMilestone.query.filter_by(is_active=True).all()
    for m in milestones:
        if m.milestone_type == 'points' and points < m.threshold:
            achievements.append({
                'name': m.name,
                'progress': points,
                'goal': m.threshold,
                'percentage': points / m.threshold * 100
            })
        elif m.milestone_type == 'streak' and current_streak < m.threshold:
            achievements.append({
                'name': m.name,
                'progress': current_streak,
                'goal': m.threshold,
                'percentage': current_streak / m.threshold * 100
            })
    
    return achievements
