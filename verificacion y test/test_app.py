"""Test Flask Application for Admin Dashboard - PostgreSQL Version"""
import os
import sys
from flask import Flask
from flask_login import LoginManager

# Asegurar que el módulo admin_dashboard esté disponible
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar db PRIMERO del módulo admin_dashboard
from admin_dashboard.models import db
from admin_dashboard import init_admin_dashboard

app = Flask(__name__)

# Configuración - Usar PostgreSQL del proyecto
db_uri = os.environ.get('DATABASE_URL') or 'postgresql:///english_learning'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'test-secret-key-12345'

# Inicializar extensions con la misma instancia
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Importar AdminUser después
from admin_dashboard.models import AdminUser

if __name__ == '__main__':
    # Inicializar admin dashboard
    init_admin_dashboard(app, db)
    
    # Crear tablas dentro del contexto
    with app.app_context():
        db.create_all()
        print("✅ Tablas de BD creadas")
        
        # Crear usuario admin
        admin = AdminUser.query.filter_by(username='admin').first()
        if not admin:
            admin = AdminUser(
                username='admin',
                email='admin@example.com',
                role='admin',
                is_active=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print(f"✅ Admin creado: {admin.username}")
        else:
            print(f"ℹ️  Admin ya existe: {admin.username}")
        
        print(f"\n✅ CONFIGURACIÓN COMPLETADA")
        print(f"Base de datos: {db_uri.split('@')[-1] if '@' in db_uri else 'english_learning'}")
        print(f"Usuarios admin:")
        for user in AdminUser.query.all():
            print(f"  - {user.username} ({user.email})")


