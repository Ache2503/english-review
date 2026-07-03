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
    
    Contiene las configuraciones por defecto o comunes a todos los entornos.
    """
    # Clave secreta para proteger formularios y sesiones contra CSRF.
    # Es crucial que esta clave sea segura y no se exponga públicamente.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    
    # URI de la base de datos. Lee desde una variable de entorno o usa una local.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql:///english_learning'
    
    # Desactiva el sistema de eventos de Flask-SQLAlchemy, que no es necesario y consume recursos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Duración de la sesión de usuario antes de que expire.
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # --- Configuraciones de Cookies de Sesión ---
    # Asegura que las cookies solo se envíen a través de HTTPS en producción.
    SESSION_COOKIE_SECURE = False  # Cambiar a True en producción con HTTPS
    # Previene que el JavaScript del lado del cliente acceda a las cookies de sesión.
    SESSION_COOKIE_HTTPONLY = True
    # Mitiga el riesgo de ataques CSRF. 'Lax' es un buen equilibrio entre seguridad y usabilidad.
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
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
