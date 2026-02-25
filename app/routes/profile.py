"""
Rutas para Perfil de Usuario
============================
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')


@profile_bp.route('/')
@login_required
def view():
    """Ver perfil del usuario"""
    from app.models import UserProgress, UserStreak, Badge, Certificate, Bookmark
    
    # Estadísticas
    total_progress = UserProgress.query.filter_by(user_id=current_user.id).count()
    streak = UserStreak.query.filter_by(user_id=current_user.id).first()
    badges_count = len(current_user.badges_earned)
    certificates_count = Certificate.query.filter_by(user_id=current_user.id).count()
    bookmarks_count = Bookmark.query.filter_by(user_id=current_user.id).count()
    
    # Última actividad
    from app.models import UserActivity
    recent_activities = UserActivity.query.filter_by(
        user_id=current_user.id
    ).order_by(UserActivity.created_at.desc()).limit(10).all()
    
    return render_template('profile/view.html',
                           streak=streak,
                           badges_count=badges_count,
                           certificates_count=certificates_count,
                           bookmarks_count=bookmarks_count,
                           recent_activities=recent_activities)


@profile_bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    """Editar perfil del usuario"""
    if request.method == 'POST':
        # Actualizar campos
        current_user.full_name = request.form.get('full_name', '').strip()
        current_user.bio = request.form.get('bio', '').strip()
        current_user.country = request.form.get('country', '').strip()
        current_user.preferred_language = request.form.get('preferred_language', 'es')
        current_user.timezone = request.form.get('timezone', 'America/Mexico_City')
        current_user.notification_email = 'notification_email' in request.form
        current_user.notification_daily = 'notification_daily' in request.form
        current_user.daily_goal_minutes = int(request.form.get('daily_goal_minutes', 15))
        current_user.show_progress = 'show_progress' in request.form
        
        # Avatar URL
        avatar_url = request.form.get('avatar_url', '').strip()
        if avatar_url:
            current_user.avatar_url = avatar_url
        
        db.session.commit()
        flash('Perfil actualizado correctamente', 'success')
        return redirect(url_for('profile.view'))
    
    return render_template('profile/edit.html')


@profile_bp.route('/avatar', methods=['POST'])
@login_required
def update_avatar():
    """Actualizar avatar via AJAX"""
    data = request.get_json()
    
    if not data or not data.get('avatar_url'):
        return jsonify({'success': False, 'error': 'URL requerida'}), 400
    
    current_user.avatar_url = data['avatar_url']
    db.session.commit()
    
    return jsonify({'success': True, 'avatar_url': current_user.avatar_url})


@profile_bp.route('/preferences', methods=['GET', 'POST'])
@login_required
def preferences():
    """Preferencias del usuario"""
    if request.method == 'POST':
        current_user.preferred_language = request.form.get('preferred_language', 'es')
        current_user.timezone = request.form.get('timezone', 'America/Mexico_City')
        current_user.daily_goal_minutes = int(request.form.get('daily_goal_minutes', 15))
        current_user.notification_email = 'notification_email' in request.form
        current_user.notification_daily = 'notification_daily' in request.form
        
        db.session.commit()
        flash('Preferencias guardadas', 'success')
        return redirect(url_for('profile.preferences'))
    
    return render_template('profile/preferences.html')


@profile_bp.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """Configuración de cuenta (email, contraseña)"""
    if request.method == 'POST':
        # Cambiar email
        new_email = request.form.get('email', '').strip()
        if new_email and new_email != current_user.email:
            from app.models import User
            existing = User.query.filter_by(email=new_email).first()
            if existing:
                flash('Ese email ya está en uso', 'danger')
            else:
                current_user.email = new_email
                flash('Email actualizado', 'success')
        
        # Cambiar contraseña
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if current_password and new_password:
            from werkzeug.security import check_password_hash
            if not check_password_hash(current_user.password_hash, current_password):
                flash('Contraseña actual incorrecta', 'danger')
            elif new_password != confirm_password:
                flash('Las contraseñas no coinciden', 'danger')
            elif len(new_password) < 6:
                flash('La contraseña debe tener al menos 6 caracteres', 'danger')
            else:
                from werkzeug.security import generate_password_hash
                current_user.password_hash = generate_password_hash(new_password)
                flash('Contraseña actualizada', 'success')
        
        db.session.commit()
        return redirect(url_for('profile.account'))
    
    return render_template('profile/account.html')


@profile_bp.route('/onboarding')
@login_required
def onboarding():
    """Tour de onboarding para nuevos usuarios"""
    if current_user.onboarding_completed:
        return redirect(url_for('dashboard.index'))
    
    # Marcar como completado
    current_user.onboarding_completed = True
    db.session.commit()
    
    return render_template('profile/onboarding.html')


@profile_bp.route('/complete-onboarding', methods=['POST'])
@login_required
def complete_onboarding():
    """Completar onboarding"""
    current_user.onboarding_completed = True
    db.session.commit()
    return jsonify({'success': True})
