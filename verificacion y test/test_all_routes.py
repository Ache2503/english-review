#!/usr/bin/env python
"""
Script para verificar que todas las rutas funcionan correctamente.
"""

import os
import sys
import time

os.chdir('/home/axel-michael/Documentos/guia_estudio/english-learning-platform')
sys.path.insert(0, '/home/axel-michael/Documentos/guia_estudio/english-learning-platform')

from flask import Flask
from config import config
from app import create_app
from app.extensions import db
from app.models import User, Unit, Topic, Reading, WritingPractice

app = create_app('development')

print("=" * 80)
print("🔍 VERIFICACIÓN DE TODAS LAS RUTAS DEL SISTEMA")
print("=" * 80)
print()

with app.app_context():
    # Obtener cliente de prueba
    client = app.test_client()
    
    # Crear usuario de prueba si no existe
    test_user = User.query.filter_by(email='test@example.com').first()
    if not test_user:
        test_user = User(
            username='testuser',
            email='test@example.com',
            password_hash='hashed_password'
        )
        db.session.add(test_user)
        db.session.commit()
    
    # Obtener IDs de entidades para pruebas
    unit_id = Unit.query.first().id if Unit.query.first() else 1
    topic_id = Topic.query.first().id if Topic.query.first() else 1
    reading_id = Reading.query.first().id if Reading.query.first() else 1
    
    routes_to_test = [
        # Rutas públicas
        ("GET", "/", "Página principal", True),
        ("GET", "/about", "Acerca de", True),
        
        # Auth
        ("GET", "/auth/login", "Página de login", True),
        ("GET", "/auth/register", "Página de registro", True),
        
        # Units
        (f"GET", f"/units/{unit_id}", "Ver unidad", False),
        (f"GET", f"/units/{unit_id}/grammar", "Ver gramática de unidad", False),
        (f"GET", f"/units/{unit_id}/vocabulary", "Ver vocabulario de unidad", False),
        
        # Readings
        ("GET", f"/reading/unit/1", "Ver lecturas de unidad", False),
        ("GET", f"/reading/{reading_id}", "Ver lectura específica", False),
        
        # Dashboard
        ("GET", "/dashboard/", "Dashboard", False),
        ("GET", "/dashboard/progress", "Progreso del usuario", False),
        
        # Explanations
        ("GET", f"/explanations/unit/{unit_id}", "Explicación de unidad", False),
        ("GET", f"/explanations/topic/{topic_id}", "Explicación de tema", False),
        
        # Practice
        ("GET", f"/practice/writing/{unit_id}", "Práctica de escritura", False),
        ("GET", f"/practice/sentence-exercises/{unit_id}", "Ejercicios de oraciones", False),
        
        # Quiz
        ("GET", f"/quiz/unit/{unit_id}", "Quiz de unidad", False),
        
        # Flashcards
        ("GET", f"/flashcards/unit/{unit_id}", "Flashcards de unidad", False),
        
        # Badges
        ("GET", "/badges/my-badges", "Mis insignias", False),
        ("GET", "/badges/all", "Todas las insignias", False),
        
        # Error Logs
        ("GET", "/errors/my-errors", "Ver mis errores", False),
        
        # Error handling
        ("GET", "/nonexistent", "Página no existente (404)", True),
    ]
    
    results = {
        'success': [],
        'redirect': [],
        'client_error': [],
        'server_error': [],
        'unknown': []
    }
    
    print("Probando rutas...")
    print("-" * 80)
    
    for method, route, description, public in routes_to_test:
        try:
            if method == "GET":
                response = client.get(route, follow_redirects=False)
            
            status = response.status_code
            
            # Clasificar respuestas
            if status in [200, 201]:
                results['success'].append((route, description, status))
                symbol = "✅"
            elif status in [301, 302, 303, 307, 308]:
                results['redirect'].append((route, description, status))
                symbol = "➡️"
            elif status in [400, 401, 403, 404]:
                # 401 y 403 son esperados si no estás autenticado
                if not public and status in [401, 403]:
                    results['success'].append((route, description, status))
                    symbol = "✅"
                else:
                    results['client_error'].append((route, description, status))
                    symbol = "⚠️"
            elif status >= 500:
                results['server_error'].append((route, description, status))
                symbol = "❌"
            else:
                results['unknown'].append((route, description, status))
                symbol = "❓"
            
            print(f"{symbol} {method:6} {route:40} [{status}] {description}")
            
        except Exception as e:
            results['server_error'].append((route, description, str(e)))
            print(f"❌ {method:6} {route:40} [ERROR] {description} - {str(e)[:30]}")
    
    print()
    print("=" * 80)
    print("📊 RESUMEN DE RESULTADOS")
    print("=" * 80)
    print()
    
    total = len(routes_to_test)
    success = len(results['success'])
    redirect = len(results['redirect'])
    client_err = len(results['client_error'])
    server_err = len(results['server_error'])
    unknown = len(results['unknown'])
    
    print(f"✅ Exitosas (200-201):          {success:3d} / {total}")
    print(f"➡️  Redirecciones (30x):        {redirect:3d} / {total}")
    print(f"⚠️  Errores de cliente (4xx):    {client_err:3d} / {total}")
    print(f"❌ Errores de servidor (5xx):   {server_err:3d} / {total}")
    print(f"❓ Otros:                       {unknown:3d} / {total}")
    print()
    
    # Porcentaje de éxito
    ok_count = success + redirect
    success_rate = (ok_count / total * 100) if total > 0 else 0
    
    print(f"📈 Tasa de éxito: {success_rate:.1f}%")
    print()
    
    if server_err > 0:
        print("❌ ERRORES DE SERVIDOR ENCONTRADOS:")
        print("-" * 80)
        for route, desc, status in results['server_error']:
            print(f"  • {route:40} - {desc}")
        print()
    
    if client_err > 0:
        print("⚠️  ERRORES DE CLIENTE (revisar si es esperado):")
        print("-" * 80)
        for route, desc, status in results['client_error']:
            print(f"  • {route:40} [{status}] - {desc}")
        print()
    
    # Conclusión
    print("=" * 80)
    if success_rate >= 90:
        print("✅ SISTEMA EN BUEN ESTADO - La mayoría de rutas funcionan correctamente")
    elif success_rate >= 70:
        print("⚠️  SISTEMA CON PEQUEÑOS PROBLEMAS - Revisar errores de cliente")
    else:
        print("❌ SISTEMA CON PROBLEMAS - Hay errores de servidor que revisar")
    
    print("=" * 80)
