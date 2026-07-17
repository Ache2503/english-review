"""
Decoradores de seguridad para la aplicación
"""
from functools import wraps
from flask import flash, redirect, url_for, abort, request, session
from flask_login import current_user
from app.extensions import db
from datetime import datetime, timedelta
import json


def rate_limit(max_attempts=5, window_seconds=900):
    """
    Decorador para limitar el número de intentos en un período de tiempo.
    Útil para login, cambio de contraseña, etc.
    
    Parámetros:
    - max_attempts: número máximo de intentos
    - window_seconds: ventana de tiempo en segundos (por defecto 15 minutos)
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            identifier = request.remote_addr
            key = f"rate_limit:{f.__name__}:{identifier}"
            
            if key in session:
                attempts, timestamp = session[key]
                elapsed = (datetime.utcnow() - timestamp).total_seconds()
                
                if elapsed > window_seconds:
                    session[key] = [0, datetime.utcnow()]
                else:
                    if attempts >= max_attempts:
                        abort(429)
                    session[key][0] += 1
            else:
                session[key] = [1, datetime.utcnow()]
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator


def json_response(f):
    """
    Decorador para funciones que retornan JSON.
    Captura excepciones y retorna respuestas JSON apropiadas.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'status': 'error'
            }, 500
    
    return decorated_function


def adults_only(f):
    """Bloquea el paso a menores de 15 años"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        
        if current_user.age < 15:
            flash("Esta sección es para mayores de 15 años. ¡Redirigiendo a la Zona Kids!", "info")
            return redirect(url_for('kids.select_profile'))
        
        return f(*args, **kwargs)
    return decorated_function


def require_scenario_access(f):
    """Verifica si el adulto买了 el escenario o es premium"""
    @wraps(f)
    def decorated_function(scenario_id, *args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        
        if current_user.age < 15:
            flash("Esta sección es para mayores de 15 años.", "info")
            return redirect(url_for('kids.select_profile'))
        
        if not current_user.has_access_to_scenario(scenario_id):
            flash("Necesitas desbloquear este escenario para acceder.", "warning")
            return redirect(url_for('scenarios.preview', scenario_id=scenario_id))
        
        return f(scenario_id, *args, **kwargs)
    return decorated_function


def kids_zone_required(f):
    """Decorador para proteger la sección infantil"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        
        valid_subs = ['kids_pass', 'premium_all_access']
        if current_user.subscription_type not in valid_subs and not current_user.is_admin:
            flash("Necesitas el Pase Infantil (Kids Pass) para acceder a esta zona.", "info")
            return redirect(url_for('main.upgrade'))
        
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorador para proteger rutas de administrador"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
