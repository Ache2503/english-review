#!/usr/bin/env python3
"""
Script maestro para agregar todos los nuevos juegos a la base de datos
Ejecuta todas las migraciones y seeders
"""

import sys
import os
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db

# Importar seeders
from seed_quick_quiz import seed_quick_quiz
from seed_reading_comprehension import seed_reading_comprehension
from seed_speed_typing import seed_speed_typing

def main():
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("🎮 MIGRANDO BASE DE DATOS - NUEVOS JUEGOS")
        print("=" * 60)
        
        try:
            # 1. Crear todas las tablas
            print("\n📊 Creando tablas en la base de datos...")
            db.create_all()
            print("✅ Tablas creadas exitosamente")
            
            # 2. Ejecutar seeders
            print("\n" + "=" * 60)
            print("🌱 EJECUTANDO SEEDERS")
            print("=" * 60)
            
            print("\n1️⃣  Seeding Quick Quiz...")
            seed_quick_quiz()
            
            print("\n2️⃣  Seeding Reading Comprehension...")
            seed_reading_comprehension()
            
            print("\n3️⃣  Seeding Speed Typing...")
            seed_speed_typing()
            
            print("\n" + "=" * 60)
            print("✅ MIGRACIONES Y SEEDERS COMPLETADOS")
            print("=" * 60)
            
            # Estadísticas finales
            from app.models import QuickQuiz, ReadingComprehension, SpeedTyping
            
            print("\n📈 ESTADÍSTICAS FINALES:")
            print(f"   - Quick Quiz Questions: {QuickQuiz.query.count()}")
            print(f"   - Reading Comprehensions: {ReadingComprehension.query.count()}")
            print(f"   - Speed Typing Phrases: {SpeedTyping.query.count()}")
            
            print("\n✨ ¡Sistema listo para usar!")
            
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}")
            print("\nTraceback:")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    main()
