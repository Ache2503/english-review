#!/usr/bin/env python3
"""
=============================================================================
SEED RUNNER - Ejecutor ordenado de todos los seeds
=============================================================================
Este script ejecuta todos los archivos de seed en el orden correcto,
verificando dependencias y evitando duplicados.

Uso:
    python seed_runner.py              # Ejecutar todos los seeds
    python seed_runner.py --dry-run    # Simular sin ejecutar
    python seed_runner.py --only units # Ejecutar solo un seed específico
    python seed_runner.py --skip badges # Saltar un seed específico
    python seed_runner.py --status     # Ver estado de los seeds
"""

import sys
import os
import argparse
import importlib.util
import traceback
from datetime import datetime
from pathlib import Path

# Agregar el directorio raíz al path
ROOT_DIR = Path(__file__).resolve().parent.parent
SEEDS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(SEEDS_DIR))

# ============================================================================
# CONFIGURACIÓN DE SEEDS
# ============================================================================
# Orden de ejecución de seeds (IMPORTANTE: respetar dependencias)

SEED_ORDER = [
    {
        'name': 'units',
        'file': 'seed_db.py',
        'description': 'Unidades base (1-24), gramática, vocabulario, ejercicios de escritura',
        'required': True,
        'dependencies': [],
        'tables': ['units', 'grammar_rules', 'vocabulary_categories', 'vocabulary_items', 'writing_practices']
    },
    {
        'name': 'cefr_units',
        'file': 'seed_cefr_units.py',
        'description': 'Unidades adicionales por nivel CEFR (25-72)',
        'required': True,
        'dependencies': [],
        'tables': ['units', 'grammar_rules', 'vocabulary_categories']
    },
    {
        'name': 'vocabulary',
        'file': 'seed_vocabulary.py',
        'description': 'Vocabulario detallado para todas las categorías',
        'required': True,
        'dependencies': ['cefr_units'],
        'tables': ['vocabulary_items', 'flashcards']
    },
    {
        'name': 'extended',
        'file': 'seed_db_extended.py',
        'description': 'Contenido extendido para las primeras 12 unidades',
        'required': False,
        'dependencies': ['cefr_units'],
        'tables': ['unit_extras']
    },
    {
        'name': 'readings',
        'file': 'seed_all_readings.py',
        'description': 'Lecturas de comprensión por unidad',
        'required': True,
        'dependencies': ['cefr_units'],
        'tables': ['readings']
    },
    {
        'name': 'sentence_exercises',
        'file': 'seed_sentence_exercises.py',
        'description': 'Ejercicios de construcción de oraciones',
        'required': True,
        'dependencies': ['cefr_units'],
        'tables': ['sentence_exercises']
    },
    {
        'name': 'verbs',
        'file': 'seed_verbs.py',
        'description': 'Tabla de verbos con conjugaciones',
        'required': True,
        'dependencies': [],
        'tables': ['verbs']
    },
    {
        'name': 'badges',
        'file': 'seed_badges.py',
        'description': 'Badges y logros del sistema',
        'required': True,
        'dependencies': [],
        'tables': ['badges']
    },
    {
        'name': 'master',
        'file': 'seed_master.py',
        'description': 'Quizzes, mensajes motivacionales, explicaciones',
        'required': True,
        'dependencies': ['cefr_units'],
        'tables': ['quizzes', 'quiz_questions', 'quiz_options', 'motivational_messages', 'unit_explanations']
    },
    {
        'name': 'unit_challenges',
        'file': 'seed_unit_challenges.py',
        'description': 'Desafíos de desbloqueo de unidades',
        'required': False,
        'dependencies': ['cefr_units'],
        'tables': ['unit_challenges', 'challenge_questions']
    },
    {
        'name': 'explanations',
        'file': 'seed_explanations.py',
        'description': 'Explicaciones detalladas adicionales',
        'required': False,
        'dependencies': ['cefr_units'],
        'tables': ['unit_explanations', 'topic_explanations']
    },
    {
        'name': 'phrasal_verbs',
        'file': 'seed_phrasal_verbs.py',
        'description': 'Phrasal verbs organizados por nivel CEFR',
        'required': False,
        'dependencies': [],
        'tables': ['phrasal_verbs']
    },
    {
        'name': 'idioms',
        'file': 'seed_idioms.py',
        'description': 'Expresiones idiomáticas con traducciones',
        'required': False,
        'dependencies': [],
        'tables': ['idioms']
    },
    {
        'name': 'conversations',
        'file': 'seed_conversations.py',
        'description': 'Conversaciones para práctica oral',
        'required': False,
        'dependencies': [],
        'tables': ['conversations', 'conversation_lines']
    },
    {
        'name': 'additional_readings',
        'file': 'seed_additional_readings.py',
        'description': 'Lecturas adicionales por nivel',
        'required': False,
        'dependencies': ['cefr_units'],
        'tables': ['readings']
    },
    {
        'name': 'conversations_interactive',
        'file': 'seed_conversations_interactive.py',
        'description': 'Conversaciones interactivas (diálogos con expected/options)',
        'required': True,
        'dependencies': [],
        'tables': ['conversations', 'conversation_lines']
    },
    {
        'name': 'customer_moods',
        'file': 'seed_customer_moods.py',
        'description': 'Estados de ánimo del cliente para el simulador roleplay',
        'required': True,
        'dependencies': [],
        'tables': ['customer_moods']
    },
    {
        'name': 'study_content',
        'file': 'seed_study_content.py',
        'description': 'Contenido de temas de estudio intensivo (migrado desde hardcoded)',
        'required': True,
        'dependencies': [],
        'tables': ['study_topic_contents']
    },
    {
        'name': 'grammar_topics',
        'file': 'seed_grammar_topics.py',
        'description': 'Contenido de temas gramaticales de referencia (migrado desde hardcoded)',
        'required': True,
        'dependencies': [],
        'tables': ['grammar_topic_contents']
    },
    {
        'name': 'writing_content',
        'file': 'seed_writing_content.py',
        'description': 'Patrones de errores y tips de escritura (migrado desde hardcoded)',
        'required': True,
        'dependencies': [],
        'tables': ['writing_error_patterns', 'writing_tip_contents']
    },
    {
        'name': 'remaining_content',
        'file': 'seed_remaining_content.py',
        'description': 'Patrones de oraciones, sinónimos, tips de errores, logros (migrado desde hardcoded)',
        'required': True,
        'dependencies': [],
        'tables': ['sentence_pattern_contents', 'concept_synonyms', 'error_tip_contents', 'achievement_milestones']
    },
]


def get_app():
    """Crear y configurar la aplicación Flask"""
    from app import create_app
    return create_app()


def check_table_count(app, table_name):
    """Verificar cantidad de registros en una tabla"""
    with app.app_context():
        from app.extensions import db
        from sqlalchemy import text
        
        try:
            result = db.session.execute(text(f'SELECT COUNT(*) FROM {table_name}'))
            count = result.scalar()
            return count
        except Exception:
            return 0


def check_seed_status(app, seed_config):
    """Verificar si un seed ya fue ejecutado"""
    tables = seed_config.get('tables', [])
    if not tables:
        return 'unknown', 0
    
    total_records = 0
    for table in tables:
        count = check_table_count(app, table)
        total_records += count
    
    if total_records > 0:
        return 'seeded', total_records
    else:
        return 'empty', 0


def run_seed_file(seed_file, dry_run=False):
    """Ejecutar un archivo de seed y reportar errores sin detener el resto."""
    seed_path = Path(seed_file)
    if not seed_path.is_absolute():
        seed_path = SEEDS_DIR / seed_path
    seed_path = seed_path.resolve()
    if not seed_path.exists():
        return False, f"Archivo no encontrado: {seed_file}"

    if dry_run:
        return True, "Simulación - no ejecutado"

    try:
        spec = importlib.util.spec_from_file_location("seed_module", seed_path)
        if spec is None or spec.loader is None:
            return False, f"No se pudo cargar el módulo desde {seed_file}"

        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)

        if hasattr(module, 'main') and callable(module.main):
            module.main()
        elif hasattr(module, 'seed_database') and callable(module.seed_database):
            module.seed_database(clean=False)
        elif hasattr(module, 'seed_units') and callable(module.seed_units):
            module.seed_units()
        elif hasattr(module, 'add_badges') and callable(module.add_badges):
            module.add_badges()
        elif hasattr(module, 'add_readings') and callable(module.add_readings):
            module.add_readings()
        elif hasattr(module, 'add_sentence_exercises') and callable(module.add_sentence_exercises):
            module.add_sentence_exercises()
        elif hasattr(module, 'seed_vocabulary') and callable(module.seed_vocabulary):
            module.seed_vocabulary()
        elif hasattr(module, 'seed_quizzes') and callable(module.seed_quizzes):
            module.seed_quizzes()
        elif hasattr(module, 'seed_motivational_messages') and callable(module.seed_motivational_messages):
            module.seed_motivational_messages()
        elif hasattr(module, 'seed_unit_explanations') and callable(module.seed_unit_explanations):
            module.seed_unit_explanations()
        elif hasattr(module, 'seed_phrasal_verbs') and callable(module.seed_phrasal_verbs):
            module.seed_phrasal_verbs()
        elif hasattr(module, 'seed_idioms') and callable(module.seed_idioms):
            module.seed_idioms()
        elif hasattr(module, 'seed_conversations') and callable(module.seed_conversations):
            module.seed_conversations()
        elif hasattr(module, 'seed_additional_readings') and callable(module.seed_additional_readings):
            module.seed_additional_readings()
        elif hasattr(module, 'seed_study_content') and callable(module.seed_study_content):
            module.seed_study_content()
        elif hasattr(module, 'seed_grammar_topics') and callable(module.seed_grammar_topics):
            module.seed_grammar_topics()
        elif hasattr(module, 'seed_writing_content') and callable(module.seed_writing_content):
            module.seed_writing_content()
        elif hasattr(module, 'seed_sentence_patterns') and callable(module.seed_sentence_patterns):
            module.seed_sentence_patterns()
        elif hasattr(module, 'seed_error_patterns') and callable(module.seed_error_patterns):
            module.seed_error_patterns()
        elif hasattr(module, 'seed_tip_contents') and callable(module.seed_tip_contents):
            module.seed_tip_contents()
        elif hasattr(module, 'seed_achievement_milestones') and callable(module.seed_achievement_milestones):
            module.seed_achievement_milestones()
        elif hasattr(module, 'seed_database_extended') and callable(module.seed_database_extended):
            module.seed_database_extended()
        else:
            return False, f"No se encontró una función ejecutable para {seed_file}"

        return True, "Ejecutado correctamente"
    except Exception as e:
        return False, f"Error: {str(e)}\n{traceback.format_exc()}"


def print_status(app):
    """Imprimir estado de todos los seeds"""
    print("\n" + "="*80)
    print("📊 ESTADO DE SEEDS")
    print("="*80)
    print(f"{'Seed':<20} {'Archivo':<30} {'Estado':<10} {'Registros':<10}")
    print("-"*80)
    
    total_records = 0
    for seed in SEED_ORDER:
        status, count = check_seed_status(app, seed)
        total_records += count
        
        status_icon = "✅" if status == 'seeded' else "⚪" if status == 'empty' else "❓"
        req = "*" if seed['required'] else ""
        
        print(f"{seed['name']:<20} {seed['file']:<30} {status_icon} {status:<7} {count:>8}")
    
    print("-"*80)
    print(f"{'TOTAL':<50} {'':<10} {total_records:>8}")
    print("\n* = Requerido")


def run_all_seeds(app, dry_run=False, only=None, skip=None):
    """Ejecutar todos los seeds en orden con manejo de errores y sin reincluir datos ya existentes."""
    print("\n" + "="*80)
    print("🌱 SEED RUNNER - English Learning Platform")
    print("="*80)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if dry_run:
        print("🔍 MODO DRY-RUN - Solo simulación, no se ejecutará nada")
    
    seeds_to_run = []
    skipped = []
    
    # Filtrar seeds
    for seed in SEED_ORDER:
        if only and seed['name'] != only:
            skipped.append(f"{seed['name']} (filtrado)")
            continue
        if skip and seed['name'] == skip:
            skipped.append(f"{seed['name']} (saltado)")
            continue

        seed_path = Path(seed['file'])
        if not seed_path.is_absolute():
            seed_path = SEEDS_DIR / seed_path
        seed_path = seed_path.resolve()
        if not seed_path.exists():
            skipped.append(f"{seed['name']} (archivo no existe)")
            continue

        seeds_to_run.append((seed, seed_path))
    
    if skipped:
        print(f"\n⏭️  Seeds saltados: {', '.join(skipped)}")
    
    print(f"\n📦 Seeds a ejecutar: {len(seeds_to_run)}")
    
    # Verificar dependencias
    executed = set()
    results = []
    
    for seed, seed_path in seeds_to_run:
        print(f"\n{'─'*60}")
        print(f"▶️  {seed['name'].upper()}")
        print(f"   📄 Archivo: {seed['file']}")
        print(f"   📝 {seed['description']}")
        
        # Verificar dependencias
        missing_deps = [dep for dep in seed['dependencies'] if dep not in executed]
        if missing_deps and not only:
            # Verificar si ya está en la DB
            has_data = False
            for dep in missing_deps:
                dep_seed = next((s for s in SEED_ORDER if s['name'] == dep), None)
                if dep_seed:
                    status, count = check_seed_status(app, dep_seed)
                    if status == 'seeded':
                        has_data = True
                        break
            
            if not has_data:
                print(f"   ⚠️  Dependencias faltantes: {', '.join(missing_deps)}")
                results.append((seed['name'], False, "Dependencias faltantes"))
                continue
        
        # Verificar estado actual
        status, count = check_seed_status(app, seed)
        if status == 'seeded' and count > 0:
            print(f"   ℹ️  Ya tiene {count} registros")
            if not only and not dry_run:
                print(f"   ⏭️  Se omite la ejecución para evitar duplicados")
                executed.add(seed['name'])
                results.append((seed['name'], True, f"Saltado (ya tiene {count} registros)"))
                continue
        
        # Ejecutar
        print(f"   🔄 Ejecutando...")
        success, message = run_seed_file(str(seed_path), dry_run)
        
        if success:
            print(f"   ✅ {message}")
            executed.add(seed['name'])
            
            # Verificar nuevos registros
            if not dry_run:
                new_status, new_count = check_seed_status(app, seed)
                print(f"   📊 Registros ahora: {new_count}")
        else:
            print(f"   ❌ {message}")
        
        results.append((seed['name'], success, message))
    
    # Resumen
    print("\n" + "="*80)
    print("📊 RESUMEN DE EJECUCIÓN")
    print("="*80)
    
    success_count = sum(1 for _, success, _ in results if success)
    fail_count = len(results) - success_count
    
    for name, success, message in results:
        icon = "✅" if success else "❌"
        print(f"   {icon} {name}: {message[:50]}")
    
    print(f"\n✅ Exitosos: {success_count}")
    print(f"❌ Fallidos: {fail_count}")
    
    return fail_count == 0


def create_default_admin(app):
    """Crear usuario administrador por defecto"""
    with app.app_context():
        from app.extensions import db
        from app.models import User
        
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("\n👤 Creando usuario administrador...")
            admin = User(
                username='admin',
                email='admin@example.com',
                full_name='Administrador',
                is_admin=True,
                is_active=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("   ✅ Usuario admin creado (password: admin123)")
        else:
            print("\n👤 Usuario admin ya existe")


def main():
    parser = argparse.ArgumentParser(
        description='Ejecutor de seeds para English Learning Platform',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python seed_runner.py              # Ejecutar todos los seeds
  python seed_runner.py --dry-run    # Simular sin ejecutar
  python seed_runner.py --status     # Ver estado actual
  python seed_runner.py --only units # Ejecutar solo un seed
  python seed_runner.py --skip master # Saltar un seed
  python seed_runner.py --force      # No preguntar confirmación
        """
    )
    
    parser.add_argument('--dry-run', action='store_true',
                        help='Simular ejecución sin hacer cambios')
    parser.add_argument('--status', action='store_true',
                        help='Mostrar estado de los seeds')
    parser.add_argument('--only', type=str,
                        help='Ejecutar solo un seed específico')
    parser.add_argument('--skip', type=str,
                        help='Saltar un seed específico')
    parser.add_argument('--force', action='store_true',
                        help='No preguntar confirmaciones')
    parser.add_argument('--create-admin', action='store_true',
                        help='Crear usuario administrador')
    
    args = parser.parse_args()
    
    # Crear app
    app = get_app()
    
    # Solo mostrar estado
    if args.status:
        print_status(app)
        return 0
    
    # Crear admin
    if args.create_admin:
        create_default_admin(app)
        return 0
    
    # Ejecutar seeds
    success = run_all_seeds(
        app,
        dry_run=args.dry_run,
        only=args.only,
        skip=args.skip
    )
    
    # Crear admin si no existe
    if success and not args.dry_run:
        create_default_admin(app)
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
