from flask import Flask
from flask_caching import Cache
from config import config
from app.extensions import db, login_manager, init_app
from app.models import User
from dotenv import load_dotenv

# OPTIMIZACIÓN: Inicializar caché
cache = Cache(config={
    'CACHE_TYPE': 'simple',  # SimpleCache (en memoria)
    'CACHE_DEFAULT_TIMEOUT': 3600  # 1 hora por defecto
})

def create_app(config_name='development'):
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Cargar variables de entorno
    load_dotenv()
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Inicializar caché
    cache.init_app(app)
    
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
