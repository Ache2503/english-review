#!/usr/bin/env python
"""
Diagnóstico de rendimiento del proyecto
"""
import time
import sys
sys.path.insert(0, '/home/axel-michael/Documentos/guia_estudio/english-learning-platform')

print("="*70)
print("📊 ANÁLISIS DE RENDIMIENTO DEL PROYECTO")
print("="*70)
print()

# 1. Tamaño del proyecto
print("📈 TAMAÑO DEL PROYECTO:")
print("-" * 70)

import os
import glob

routes_files = glob.glob('/home/axel-michael/Documentos/guia_estudio/english-learning-platform/app/routes/*.py')
print(f"  • Archivos de rutas: {len(routes_files)}")

templates = glob.glob('/home/axel-michael/Documentos/guia_estudio/english-learning-platform/app/templates/**/*.html', recursive=True)
print(f"  • Templates: {len(templates)}")

models_path = '/home/axel-michael/Documentos/guia_estudio/english-learning-platform/app/models.py'
with open(models_path) as f:
    models_lines = len(f.readlines())
print(f"  • Líneas en models.py: {models_lines}")

total_routes_lines = sum(len(open(f).readlines()) for f in routes_files)
print(f"  • Líneas totales en rutas: {total_routes_lines}")

print()

# 2. Tiempo de carga de la app
print("⏱️  TIEMPO DE INICIALIZACIÓN:")
print("-" * 70)

start = time.time()
from app import create_app
import os
app = create_app('development')
total_time = time.time() - start

print(f"  • Tiempo total de create_app(): {total_time:.3f}s")

if total_time > 2:
    print("  ⚠️  ¡LENTO! Más de 2 segundos")
elif total_time > 1:
    print("  ⚠️  Moderado. Más de 1 segundo")
else:
    print("  ✅ Rápido. Menos de 1 segundo")

print()

# 3. Número de modelos
print("📦 MODELOS EN BD:")
print("-" * 70)

from app.extensions import db
with app.app_context():
    # Contar tabla
    tables = db.inspect(db.engine).get_table_names()
    print(f"  • Tablas en BD: {len(tables)}")
    
    # Contar modelos
    from app import models
    model_count = sum(1 for attr in dir(models) if not attr.startswith('_') and attr[0].isupper())
    print(f"  • Modelos definidos: {model_count}")
    
    # Información de tablas
    print(f"\n  Tablas:")
    for table in sorted(tables):
        cols = len(db.inspect(db.engine).get_columns(table))
        print(f"    - {table}: {cols} columnas")

print()

# 4. Blueprints registrados
print("🔌 BLUEPRINTS REGISTRADOS:")
print("-" * 70)

blueprints = app.blueprints
print(f"  • Total: {len(blueprints)} blueprints")
for bp_name in sorted(blueprints.keys()):
    print(f"    - {bp_name}")

print()

# 5. Rutas registradas
print("🛣️  RUTAS REGISTRADAS:")
print("-" * 70)

routes = [rule for rule in app.url_map.iter_rules() if rule.endpoint != 'static']
print(f"  • Total de rutas: {len(routes)}")

# Agrupar por blueprint
from collections import defaultdict
routes_by_bp = defaultdict(list)
for rule in routes:
    bp = rule.endpoint.split('.')[0] if '.' in rule.endpoint else 'main'
    routes_by_bp[bp].append(str(rule))

for bp in sorted(routes_by_bp.keys()):
    print(f"    {bp}: {len(routes_by_bp[bp])} rutas")

print()

# 6. Problemas identificados
print("🔍 ANÁLISIS DE RENDIMIENTO:")
print("-" * 70)

issues = []

if models_lines > 500:
    issues.append(f"⚠️  models.py muy grande ({models_lines} líneas)")

if len(tables) > 30:
    issues.append(f"⚠️  Muchas tablas en BD ({len(tables)})")

if total_time > 1:
    issues.append(f"⚠️  Startup lento ({total_time:.2f}s)")

if len(blueprints) > 8:
    issues.append(f"⚠️  Muchos blueprints ({len(blueprints)})")

if len(routes) > 100:
    issues.append(f"⚠️  Muchas rutas ({len(routes)})")

if issues:
    print("  Problemas encontrados:")
    for issue in issues:
        print(f"    {issue}")
else:
    print("  ✅ No hay problemas significativos de rendimiento")

print()

# 7. Recomendaciones
print("💡 RECOMENDACIONES:")
print("-" * 70)

recommendations = [
    "✓ Usar lazy loading en relaciones de BD",
    "✓ Caché de queries frecuentes",
    "✓ Índices en columnas de búsqueda",
    "✓ Dividir models.py en múltiples archivos",
    "✓ Usar blueprints con lazy loading",
    "✓ Optimizar queries N+1",
    "✓ Usar select distinct cuando sea necesario",
]

for rec in recommendations:
    print(f"  {rec}")

print()
print("="*70)
