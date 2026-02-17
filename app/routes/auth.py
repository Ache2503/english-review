from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models import User, MiniGame
from datetime import datetime, date
import random

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def send_welcome_email_if_enabled(user):
    """Enviar email de bienvenida si está habilitado"""
    try:
        if current_app.config.get('MAIL_ENABLED'):
            from app.services.email_service import send_welcome_email
            send_welcome_email(user)
            return True
    except Exception as e:
        current_app.logger.error(f"Error enviando email de bienvenida: {e}")
    return False

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registro de nuevos usuarios"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name', '').strip()
        
        # Validaciones
        if not username or len(username) < 3:
            flash('El usuario debe tener al menos 3 caracteres.', 'danger')
            return redirect(url_for('auth.register'))
        
        if not email or '@' not in email:
            flash('Por favor ingresa un email válido.', 'danger')
            return redirect(url_for('auth.register'))
        
        if password != confirm_password or len(password) < 6:
            flash('Las contraseñas no coinciden o son muy cortas (mín. 6 caracteres).', 'danger')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(username=username).first():
            flash('Este usuario ya existe.', 'warning')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Este email ya está registrado.', 'warning')
            return redirect(url_for('auth.register'))
        
        # Crear usuario
        user = User(
            username=username,
            email=email,
            full_name=full_name or username
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Enviar email de bienvenida
        send_welcome_email_if_enabled(user)
        
        flash('¡Registro exitoso! Por favor inicia sesión.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login de usuarios"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=request.form.get('remember') == 'on')
            
            today = date.today()
            show_daily_challenge = False
            
            # Verificar si es el primer login del día
            if user.last_login_date != today:
                # Nuevo día - resetear el flag de reto diario
                user.daily_challenge_completed = False
                user.last_login_date = today
                db.session.commit()
                
                # Mostrar reto diario solo si no lo ha completado hoy
                show_daily_challenge = True
            
            # Guardar en sesión para usar después del redirect
            from flask import session
            session['show_daily_challenge'] = show_daily_challenge
            
            next_page = request.args.get('next')
            if not next_page or not url_has_allowed_host_and_scheme(next_page):
                next_page = url_for('dashboard.index')
            return redirect(next_page)
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    
    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout de usuario"""
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('main.index'))


def url_has_allowed_host_and_scheme(url):
    """Validar que la URL sea segura para redirect"""
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return not parsed.netloc or parsed.netloc == request.host
