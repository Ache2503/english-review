import re
from flask import Flask
from markupsafe import Markup
from flask_caching import Cache
from config import config
from app.extensions import db, login_manager, init_app
from app.models import User
from dotenv import load_dotenv
from app.routes.conversation import conversation_bp


def markdown_to_html(text):
    """Convierte **texto** a <strong>texto</strong> y otros formatos markdown básicos"""
    if not text:
        return ''
    # Convertir **texto** a <strong>texto</strong>
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', str(text))
    # Convertir *texto* a <em>texto</em>
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Convertir saltos de línea
    text = text.replace('\n', '<br>')
    return Markup(text)
# OPTIMIZACIÓN: Inicializar caché
cache = Cache(config={
    'CACHE_TYPE': 'simple',  # SimpleCache (en memoria)
    'CACHE_DEFAULT_TIMEOUT': 3600  # 1 hora por defecto
})

def create_app(config_name='development'):
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Cargar variables de entorno PRIMERO
    load_dotenv(override=True)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Cargar configuraciones adicionales desde variables de entorno
    # para Flask-Mail
    import os
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL', 'False').lower() == 'true'
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER') or os.environ.get('MAIL_USERNAME')
    app.config['MAIL_ENABLED'] = os.environ.get('MAIL_ENABLED', 'False').lower() == 'true'
    
    # Inicializar caché
    cache.init_app(app)
    
    # Registrar filtros personalizados de Jinja2
    app.jinja_env.filters['md'] = markdown_to_html
    app.jinja_env.filters['markdown'] = markdown_to_html
    
    # Inicializar extensiones
    init_app(app)
    
    # Registrar callback para login_manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Crear tablas de base de datos
    with app.app_context():
        db.create_all()
    
    # Registrar blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.units import units_bp
    from app.routes.practice import practice_bp
    from app.routes.quiz import quiz_bp
    from app.routes.reading import reading_bp
    from app.routes.badges import badges_bp
    from app.routes.flashcards import flashcards_bp
    from app.routes.errors import errors_bp
    from app.routes.explanations import explanations_bp
    from app.routes.conversation import conversation_bp
    from app.routes.grammar import grammar_bp
    from app.routes.stats import stats_bp
    from app.routes.study import study_bp
    from app.routes.challenges import challenges_bp
    from app.routes.exams import exams_bp
    from app.routes.games import games_bp
    from app.routes.drills import drills_bp
    from app.routes.idioms import idioms_bp
    from app.routes.reports import reports_bp
    from app.routes.review import review_bp
    from app.routes.writing import writing_bp
    from app.routes.unit_challenge import unit_challenge_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(units_bp)
    app.register_blueprint(practice_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(reading_bp)
    app.register_blueprint(badges_bp)
    app.register_blueprint(flashcards_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(explanations_bp)
    app.register_blueprint(conversation_bp)
    app.register_blueprint(grammar_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(study_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(exams_bp)
    app.register_blueprint(games_bp)
    app.register_blueprint(drills_bp)
    app.register_blueprint(idioms_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(writing_bp)
    app.register_blueprint(unit_challenge_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {
            'error': 'No encontrado',
            'message': 'La página que buscas no existe'
        }, 404
    
    @app.errorhandler(500)
    def server_error(error):
        db.session.rollback()
        return {
            'error': 'Error del servidor',
            'message': 'Algo salió mal en nuestro servidor'
        }, 500
    
    return app
