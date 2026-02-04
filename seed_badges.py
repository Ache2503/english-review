#!/usr/bin/env python3
"""
Script para agregar badges/logros al sistema.
Ejecutar: python seed_badges.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Badge

def add_badges():
    """Agrega badges al sistema."""
    
    app = create_app()
    with app.app_context():
        print("=" * 70)
        print("AGREGANDO BADGES AL SISTEMA")
        print("=" * 70)
        
        badges_data = [
            {
                "name": "Primer Paso",
                "description": "Completar tu primera unidad",
                "icon": "🚀",
                "color": "primary",
                "badge_type": "completion",
                "criteria": "Completar Unit 1",
                "order": 1
            },
            {
                "name": "Explorador",
                "description": "Completar 3 unidades",
                "icon": "🗺️",
                "color": "info",
                "badge_type": "completion",
                "criteria": "Completar 3 unidades",
                "order": 2
            },
            {
                "name": "Viajero Experimentado",
                "description": "Completar todas las 6 unidades",
                "icon": "✈️",
                "color": "success",
                "badge_type": "completion",
                "criteria": "Completar todas las unidades",
                "order": 3
            },
            {
                "name": "Lector Ávido",
                "description": "Completar 5 lecturas",
                "icon": "📚",
                "color": "success",
                "badge_type": "reading",
                "criteria": "Completar 5 lecturas",
                "order": 4
            },
            {
                "name": "Maestro de Lecturas",
                "description": "Completar todas las lecturas",
                "icon": "📖",
                "color": "primary",
                "badge_type": "reading",
                "criteria": "Completar todas las lecturas",
                "order": 5
            },
            {
                "name": "Escritor Principiante",
                "description": "Completar 10 ejercicios de escritura",
                "icon": "✍️",
                "color": "warning",
                "badge_type": "writing",
                "criteria": "10 ejercicios de escritura",
                "order": 6
            },
            {
                "name": "Escritor Confiado",
                "description": "Completar 25 ejercicios de escritura",
                "icon": "📝",
                "color": "primary",
                "badge_type": "writing",
                "criteria": "25 ejercicios de escritura",
                "order": 7
            },
            {
                "name": "Novelista",
                "description": "Completar 50 ejercicios de escritura",
                "icon": "📕",
                "color": "success",
                "badge_type": "writing",
                "criteria": "50 ejercicios de escritura",
                "order": 8
            },
            {
                "name": "Quiz Master",
                "description": "Completar todos los quizzes",
                "icon": "🎯",
                "color": "danger",
                "badge_type": "quiz",
                "criteria": "Completar todos los quizzes",
                "order": 9
            },
            {
                "name": "Perfeccionista",
                "description": "Obtener 100% en un quiz",
                "icon": "⭐",
                "color": "warning",
                "badge_type": "perfect",
                "criteria": "Puntuación perfecta en quiz",
                "order": 10
            },
            {
                "name": "Genio Académico",
                "description": "Obtener 100% en 3 quizzes",
                "icon": "🧠",
                "color": "primary",
                "badge_type": "perfect",
                "criteria": "3 puntuaciones perfectas",
                "order": 11
            },
            {
                "name": "Racha de Fuego",
                "description": "Estudiar 7 días consecutivos",
                "icon": "🔥",
                "color": "danger",
                "badge_type": "streak",
                "criteria": "7 días consecutivos",
                "order": 12
            },
            {
                "name": "En la Zona",
                "description": "Estudiar 14 días consecutivos",
                "icon": "⚡",
                "color": "warning",
                "badge_type": "streak",
                "criteria": "14 días consecutivos",
                "order": 13
            },
            {
                "name": "Máquina de Aprendizaje",
                "description": "Estudiar 30 días consecutivos",
                "icon": "🤖",
                "color": "primary",
                "badge_type": "streak",
                "criteria": "30 días consecutivos",
                "order": 14
            },
            {
                "name": "Gramático Experto",
                "description": "Dominar todas las reglas de gramática",
                "icon": "📋",
                "color": "success",
                "badge_type": "grammar",
                "criteria": "Completar todas las lecciones de gramática",
                "order": 15
            },
            {
                "name": "Genio del Vocabulario",
                "description": "Aprender 100+ palabras nuevas",
                "icon": "💎",
                "color": "primary",
                "badge_type": "vocabulary",
                "criteria": "100+ palabras en vocabulario",
                "order": 16
            },
            {
                "name": "Campeón de Oraciones",
                "description": "Practicar 50 oraciones",
                "icon": "🏆",
                "color": "warning",
                "badge_type": "sentence",
                "criteria": "50 ejercicios de oraciones",
                "order": 17
            },
            {
                "name": "Estudiante Dedicado",
                "description": "Completar todas las secciones",
                "icon": "👨‍🎓",
                "color": "success",
                "badge_type": "completion",
                "criteria": "Todas las secciones completadas",
                "order": 18
            },
        ]
        
        for badge_data in badges_data:
            # Verificar si el badge ya existe
            existing = Badge.query.filter_by(name=badge_data["name"]).first()
            
            if not existing:
                badge = Badge(
                    name=badge_data["name"],
                    description=badge_data["description"],
                    icon=badge_data["icon"],
                    color=badge_data["color"],
                    badge_type=badge_data["badge_type"],
                    criteria=badge_data.get("criteria")
                )
                db.session.add(badge)
                print(f"✓ Badge agregado: {badge_data['name']} ({badge_data['icon']})")
            else:
                print(f"- Badge ya existe: {badge_data['name']}")
                
        db.session.commit()
        
        print("\n" + "=" * 70)
        print("✅ ¡BADGES AGREGADOS EXITOSAMENTE!")
        print("=" * 70)

if __name__ == "__main__":
    add_badges()
