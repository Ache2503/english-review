"""
Módulo de Configuración de la Aplicación.

Este archivo define las configuraciones para la aplicación Flask, utilizando un sistema
basado en clases para gestionar diferentes entornos como desarrollo, pruebas y producción.

Las configuraciones sensibles o específicas del entorno se cargan desde variables de
entorno para mayor seguridad y portabilidad.
"""
import os
from datetime import timedelta

class Config:
    """
    Configuración base de la que heredan todas las demás.
    """
    # Clave secreta para proteger formularios y sesiones contra CSRF.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    
    # --- INICIO DEL PARCHE PARA RENDER ---
    db_url = os.environ.get('DATABASE_URL')
    if db_url and db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = db_url or 'postgresql:///english_learning'
    # --- FIN DEL PARCHE ---
    
    # Desactiva el sistema de eventos de Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Duración de la sesión de usuario antes de que expire.
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # --- Configuraciones de Cookies de Sesión ---
    SESSION_COOKIE_SECURE = False  # Cambiar a True en producción con HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # --- Configuración de Flask-Mail para el envío de correos ---
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # El remitente por defecto si no se especifica uno.
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or os.environ.get('MAIL_USERNAME')
    # Permite habilitar o deshabilitar globalmente el envío de correos.
    MAIL_ENABLED = os.environ.get('MAIL_ENABLED', 'False').lower() == 'true'

class DevelopmentConfig(Config):
    """Configuración para el entorno de desarrollo."""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Configuración para el entorno de pruebas (testing)."""
    TESTING = True
    # Usa una base de datos en memoria para que las pruebas sean rápidas y aisladas.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Configuración para el entorno de producción."""
    DEBUG = False
    TESTING = False
    # En producción, las cookies de sesión deben ser seguras.
    SESSION_COOKIE_SECURE = True

# Diccionario que mapea nombres de entornos a sus respectivas clases de configuración.
# Facilita la carga de la configuración correcta al iniciar la aplicación.
config = { # type: ignore
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
