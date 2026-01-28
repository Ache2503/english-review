from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Unit, UserProgress, UserStreak

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    """Dashboard principal del usuario"""
    # OPTIMIZACIÓN: Obtener datos sin N+1 queries
    units = Unit.query.order_by(Unit.unit_number).all()
    
    user_progress = current_user.get_progress()
    streak = UserStreak.query.filter_by(user_id=current_user.id).first()
    
    # Obtener progreso por unidad de una sola query
    user_progress_by_unit = {
        up.unit_id: up for up in UserProgress.query.filter_by(
            user_id=current_user.id
        ).all()
    }
    
    # Construir lista sin queries adicionales
    unit_progress_list = []
    for unit in units:
        progress = user_progress_by_unit.get(unit.id)
        
        if not progress:
            progress = UserProgress(user_id=current_user.id, unit_id=unit.id)
            db.session.add(progress)
        
        unit_progress_list.append({
            'unit': unit,
            'progress': progress,
            'grammar_count': unit.grammar_rules.count(),
            'vocabulary_count': unit.vocabulary_categories.count(),
            'topics_count': unit.topics.count()
        })
    
    db.session.commit()
    
    return render_template('dashboard.html',
                           user=current_user,
                           units=unit_progress_list,
                           user_progress=user_progress,
                           streak=streak)


@dashboard_bp.route('/progress')
@login_required
def progress():
    """Ver progreso detallado del usuario"""
    progress_data = current_user.get_progress()
    user_progress = UserProgress.query.filter_by(user_id=current_user.id).all()
    
    return render_template('progress.html',
                           progress_data=progress_data,
                           user_progress=user_progress)
