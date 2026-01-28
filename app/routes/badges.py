from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.models import Badge, User

badges_bp = Blueprint('badges', __name__, url_prefix='/badges')


@badges_bp.route('/my-badges')
@login_required
def my_badges():
    """Ver los badges del usuario actual"""
    user = User.query.get(current_user.id)
    
    # Obtener badges ganados
    earned_badges = user.badges_earned
    earned_ids = [b.id for b in earned_badges]
    
    # Obtener todos los badges para mostrar tanto los ganados como los disponibles
    all_badges = Badge.query.filter_by(is_active=True).order_by(Badge.order).all()
    
    # Separar badges ganados y no ganados
    earned = [b for b in all_badges if b.id in earned_ids]
    not_earned = [b for b in all_badges if b.id not in earned_ids]
    
    return render_template('badges/my_badges.html',
                           earned_badges=earned,
                           not_earned_badges=not_earned,
                           total_earned=len(earned),
                           total_badges=len(all_badges))


@badges_bp.route('/all')
@login_required
def all_badges():
    """Ver todos los badges disponibles"""
    badges = Badge.query.filter_by(is_active=True).order_by(Badge.order).all()
    
    return render_template('badges/all_badges.html',
                           badges=badges)


@badges_bp.route('/progress')
@login_required
def badge_progress():
    """API para obtener progreso de badges (JSON)"""
    user = User.query.get(current_user.id)
    earned_badges = user.badges_earned
    all_badges = Badge.query.filter_by(is_active=True).all()
    
    progress = {
        'earned': len(earned_badges),
        'total': len(all_badges),
        'percentage': (len(earned_badges) / len(all_badges) * 100) if len(all_badges) > 0 else 0,
        'badges': [{'id': b.id, 'name': b.name, 'icon': b.icon} for b in earned_badges]
    }
    
    return jsonify(progress)
