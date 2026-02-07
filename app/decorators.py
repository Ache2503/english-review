"""
Decoradores de seguridad para la aplicación
"""

from functools import wraps
from flask import redirect, url_for, abort, request, session
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
            # Usar IP como identificador
            identifier = request.remote_addr
            key = f"rate_limit:{f.__name__}:{identifier}"
            
            # Verificar intentos en la sesión o cache
            if key in session:
                attempts, timestamp = session[key]
                elapsed = (datetime.utcnow() - timestamp).total_seconds()
                
                # Si la ventana ha pasado, resetear
                if elapsed > window_seconds:
                    session[key] = [0, datetime.utcnow()]
                else:
                    if attempts >= max_attempts:
                        abort(429)  # Too Many Requests
                    
                    # Incrementar intentos
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

