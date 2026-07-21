from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Unit, UserProgress, UserStreak, MiniGame
from app.services.unit_unlock import UnitUnlockSystem
from datetime import date
import random

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

GAME_ROUTES = {
    'word_scramble': 'games.word_scramble',
    'hangman': 'games.hangman',
    'memory': 'games.memory_game',
    'fill_gaps': 'games.fill_gaps',
    'quick_quiz': 'games.quick_quiz',
    'reading': 'games.reading_list',
    'speed_typing': 'games.speed_typing'
}

def get_random_daily_challenge():
    """Seleccionar un juego aleatorio para el reto diario"""
    games = MiniGame.query.filter_by(is_active=True).all()
    if not games:
        return None
    
    game = random.choice(games)
    game_url = GAME_ROUTES.get(game.game_type, 'games.game_list')
    return {
        'game': game,
        'url': url_for(game_url) + '?from_daily=true'
    }

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
    
    # Sistema de desbloqueo
    unlock_system = UnitUnlockSystem(current_user.id)
    
    # Construir lista sin queries adicionales
    unit_progress_list = []
    for unit in units:
        progress = user_progress_by_unit.get(unit.id)
        
        if not progress:
            progress = UserProgress(user_id=current_user.id, unit_id=unit.id)
            db.session.add(progress)
        
        is_unlocked = unlock_system.is_unit_unlocked(unit.id)
        
        unit_progress_list.append({
            'unit': unit,
            'progress': progress,
            'is_locked': not is_unlocked,
            'grammar_count': unit.grammar_rules.count(),
            'vocabulary_count': unit.vocabulary_categories.count(),
            'topics_count': unit.topics.count()
        })
    
    db.session.commit()
    
    # Verificar si mostrar el reto diario
    show_daily_challenge = session.pop('show_daily_challenge', False)
    daily_challenge = None
    
    if show_daily_challenge and not current_user.daily_challenge_completed:
        daily_challenge = get_random_daily_challenge()
    
    return render_template('dashboard.html',
                           user=current_user,
                           units=unit_progress_list,
                           user_progress=user_progress,
                           streak=streak,
                           daily_challenge=daily_challenge,
                           show_daily_challenge=show_daily_challenge and daily_challenge is not None)


@dashboard_bp.route('/progress')
@login_required
def progress():
    """Ver progreso detallado del usuario"""
    progress_data = current_user.get_progress()
    user_progress = UserProgress.query.filter_by(user_id=current_user.id).all()
    
    return render_template('progress.html',
                           progress_data=progress_data,
                           user_progress=user_progress)
