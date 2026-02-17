#!/usr/bin/env python3
"""
=============================================================================
DATABASE MANAGER - Sistema de verificación y actualización de base de datos
=============================================================================
Este script verifica que todas las tablas y columnas requeridas existan.
Si faltan tablas o columnas, las crea automáticamente sin perder datos.

Uso:
    python db_manager.py              # Verificar y actualizar DB
    python db_manager.py --check      # Solo verificar (no modificar)
    python db_manager.py --reset      # Resetear DB (¡PELIGROSO!)
    python db_manager.py --backup     # Crear backup antes de cambios
"""

import sys
import os
import argparse
from datetime import datetime

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import inspect, text
from sqlalchemy.exc import SQLAlchemyError

def get_app():
    """Crear y configurar la aplicación Flask"""
    from app import create_app
    return create_app()


def get_model_tables(app):
    """Obtener todas las tablas definidas en los modelos"""
    with app.app_context():
        from app.extensions import db
        from app import models  # Importar todos los modelos
        
        tables = {}
        for table_name, table in db.metadata.tables.items():
            columns = {}
            for column in table.columns:
                columns[column.name] = {
                    'type': str(column.type),
                    'nullable': column.nullable,
                    'primary_key': column.primary_key,
                    'default': str(column.default) if column.default else None
                }
            tables[table_name] = columns
        return tables


def get_database_tables(app):
    """Obtener tablas actuales de la base de datos"""
    with app.app_context():
        from app.extensions import db
        inspector = inspect(db.engine)
        
        tables = {}
        for table_name in inspector.get_table_names():
            columns = {}
            for column in inspector.get_columns(table_name):
                columns[column['name']] = {
                    'type': str(column['type']),
                    'nullable': column.get('nullable', True)
                }
            tables[table_name] = columns
        return tables


def compare_schemas(model_tables, db_tables):
    """Comparar esquemas y encontrar diferencias"""
    differences = {
        'missing_tables': [],
        'missing_columns': {},
        'extra_tables': [],
        'type_mismatches': {}
    }
    
    # Tablas que faltan en la DB
    for table_name in model_tables:
        if table_name not in db_tables:
            differences['missing_tables'].append(table_name)
        else:
            # Columnas que faltan
            model_cols = model_tables[table_name]
            db_cols = db_tables[table_name]
            
            missing_cols = []
            for col_name in model_cols:
                if col_name not in db_cols:
                    missing_cols.append({
                        'name': col_name,
                        'type': model_cols[col_name]['type'],
                        'nullable': model_cols[col_name]['nullable']
                    })
            
            if missing_cols:
                differences['missing_columns'][table_name] = missing_cols
    
    # Tablas extra en DB (no en modelos)
    for table_name in db_tables:
        if table_name not in model_tables and table_name != 'alembic_version':
            differences['extra_tables'].append(table_name)
    
    return differences


def print_report(differences, model_tables, db_tables):
    """Imprimir reporte de diferencias"""
    print("\n" + "="*70)
    print("📊 REPORTE DE VERIFICACIÓN DE BASE DE DATOS")
    print("="*70)
    
    print(f"\n📋 Tablas en modelos: {len(model_tables)}")
    print(f"📋 Tablas en base de datos: {len(db_tables)}")
    
    if not differences['missing_tables'] and not differences['missing_columns']:
        print("\n✅ La base de datos está sincronizada con los modelos")
        return True
    
    if differences['missing_tables']:
        print(f"\n❌ Tablas faltantes ({len(differences['missing_tables'])}):")
        for table in differences['missing_tables']:
            cols = len(model_tables[table])
            print(f"   • {table} ({cols} columnas)")
    
    if differences['missing_columns']:
        print(f"\n⚠️  Columnas faltantes:")
        for table, columns in differences['missing_columns'].items():
            print(f"   Tabla '{table}':")
            for col in columns:
                nullable = "NULL" if col['nullable'] else "NOT NULL"
                print(f"      • {col['name']} ({col['type']}) {nullable}")
    
    if differences['extra_tables']:
        print(f"\nℹ️  Tablas extra en DB (no en modelos):")
        for table in differences['extra_tables']:
            print(f"   • {table}")
    
    return False


def apply_changes(app, differences):
    """Aplicar cambios a la base de datos"""
    with app.app_context():
        from app.extensions import db
        
        print("\n" + "="*70)
        print("🔧 APLICANDO CAMBIOS")
        print("="*70)
        
        changes_made = 0
        
        # Crear tablas faltantes
        if differences['missing_tables']:
            print(f"\n📦 Creando {len(differences['missing_tables'])} tablas faltantes...")
            try:
                # Crear solo las tablas que faltan
                db.create_all()
                for table in differences['missing_tables']:
                    print(f"   ✅ Tabla '{table}' creada")
                    changes_made += 1
            except SQLAlchemyError as e:
                print(f"   ❌ Error creando tablas: {e}")
                return False
        
        # Agregar columnas faltantes
        if differences['missing_columns']:
            print(f"\n📝 Agregando columnas faltantes...")
            for table_name, columns in differences['missing_columns'].items():
                for col in columns:
                    try:
                        # Determinar tipo de dato SQL
                        sql_type = convert_to_sql_type(col['type'])
                        nullable = "NULL" if col['nullable'] else "NOT NULL DEFAULT ''"
                        
                        # Para columnas NOT NULL, usar un default apropiado
                        if not col['nullable']:
                            if 'INTEGER' in sql_type.upper():
                                nullable = "NOT NULL DEFAULT 0"
                            elif 'BOOLEAN' in sql_type.upper():
                                nullable = "NOT NULL DEFAULT FALSE"
                            elif 'FLOAT' in sql_type.upper() or 'DOUBLE' in sql_type.upper():
                                nullable = "NOT NULL DEFAULT 0.0"
                            elif 'DATETIME' in sql_type.upper() or 'TIMESTAMP' in sql_type.upper():
                                nullable = "NULL"  # Permitir NULL para datetime
                            else:
                                nullable = "NOT NULL DEFAULT ''"
                        
                        sql = f'ALTER TABLE {table_name} ADD COLUMN "{col["name"]}" {sql_type} {nullable}'
                        db.session.execute(text(sql))
                        db.session.commit()
                        print(f"   ✅ Columna '{col['name']}' agregada a '{table_name}'")
                        changes_made += 1
                    except SQLAlchemyError as e:
                        db.session.rollback()
                        if "already exists" in str(e).lower() or "duplicate" in str(e).lower():
                            print(f"   ℹ️  Columna '{col['name']}' ya existe en '{table_name}'")
                        else:
                            print(f"   ⚠️  Error agregando '{col['name']}' a '{table_name}': {e}")
        
        print(f"\n✅ {changes_made} cambios aplicados exitosamente")
        return True


def convert_to_sql_type(sqlalchemy_type):
    """Convertir tipo SQLAlchemy a SQL estándar"""
    type_str = str(sqlalchemy_type).upper()
    
    # Mapeo de tipos
    type_map = {
        'VARCHAR': 'VARCHAR(255)',
        'STRING': 'VARCHAR(255)',
        'TEXT': 'TEXT',
        'INTEGER': 'INTEGER',
        'BIGINT': 'BIGINT',
        'SMALLINT': 'SMALLINT',
        'FLOAT': 'FLOAT',
        'DOUBLE': 'DOUBLE PRECISION',
        'BOOLEAN': 'BOOLEAN',
        'DATETIME': 'TIMESTAMP',
        'DATE': 'DATE',
        'TIME': 'TIME',
        'JSON': 'JSON',
        'JSONB': 'JSONB'
    }
    
    # Buscar coincidencia
    for key, value in type_map.items():
        if key in type_str:
            # Si ya tiene longitud especificada, usarla
            if '(' in type_str and ')' in type_str:
                return type_str
            return value
    
    # Default
    return type_str if type_str else 'VARCHAR(255)'


def create_backup(app):
    """Crear backup de la base de datos"""
    with app.app_context():
        from app.extensions import db
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_before_migration_{timestamp}.sql"
        
        # Obtener URL de la base de datos
        db_url = str(db.engine.url)
        
        if 'postgresql' in db_url:
            # Extraer credenciales para pg_dump
            from urllib.parse import urlparse
            parsed = urlparse(db_url)
            
            os.environ['PGPASSWORD'] = parsed.password or ''
            cmd = f'pg_dump -h {parsed.hostname or "localhost"} -U {parsed.username} -d {parsed.path.strip("/")} -f {backup_file}'
            
            result = os.system(cmd)
            if result == 0:
                print(f"✅ Backup creado: {backup_file}")
                return True
            else:
                print(f"⚠️  No se pudo crear backup automático")
                return False
        else:
            print("ℹ️  Backup automático solo disponible para PostgreSQL")
            return False


def reset_database(app):
    """Resetear completamente la base de datos (¡PELIGROSO!)"""
    confirm = input("\n⚠️  ¿Estás SEGURO de que quieres ELIMINAR TODOS LOS DATOS? (escribe 'SI ELIMINAR'): ")
    if confirm != 'SI ELIMINAR':
        print("Operación cancelada")
        return False
    
    with app.app_context():
        from app.extensions import db
        
        print("\n🗑️  Eliminando todas las tablas...")
        db.drop_all()
        print("📦 Creando todas las tablas...")
        db.create_all()
        print("✅ Base de datos reseteada")
        return True


def verify_indexes(app):
    """Verificar y crear índices importantes"""
    with app.app_context():
        from app.extensions import db
        
        print("\n📇 Verificando índices...")
        
        # Índices importantes que deberían existir
        important_indexes = [
            ('users', 'username'),
            ('users', 'email'),
            ('units', 'unit_number'),
            ('grammar_rules', 'unit_id'),
            ('vocabulary_items', 'category_id'),
            ('flashcards', 'unit_id'),
            ('quizzes', 'unit_id'),
            ('readings', 'unit_id'),
            ('user_progress', 'user_id'),
            ('user_progress', 'unit_id'),
        ]
        
        inspector = inspect(db.engine)
        
        for table, column in important_indexes:
            try:
                indexes = inspector.get_indexes(table)
                index_columns = [idx['column_names'] for idx in indexes]
                flat_columns = [col for cols in index_columns for col in cols]
                
                if column not in flat_columns:
                    # Crear índice
                    index_name = f"idx_{table}_{column}"
                    sql = f'CREATE INDEX IF NOT EXISTS {index_name} ON {table} ({column})'
                    db.session.execute(text(sql))
                    db.session.commit()
                    print(f"   ✅ Índice creado: {index_name}")
            except Exception as e:
                pass  # Tabla puede no existir aún


def main():
    parser = argparse.ArgumentParser(
        description='Gestor de base de datos para English Learning Platform',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python db_manager.py              # Verificar y actualizar automáticamente
  python db_manager.py --check      # Solo verificar (sin modificar)
  python db_manager.py --backup     # Crear backup antes de actualizar
  python db_manager.py --reset      # Resetear toda la DB (¡PELIGROSO!)
        """
    )
    
    parser.add_argument('--check', action='store_true', 
                        help='Solo verificar sin hacer cambios')
    parser.add_argument('--reset', action='store_true', 
                        help='Resetear completamente la base de datos (¡ELIMINA DATOS!)')
    parser.add_argument('--backup', action='store_true', 
                        help='Crear backup antes de hacer cambios')
    parser.add_argument('--verbose', '-v', action='store_true', 
                        help='Mostrar información detallada')
    
    args = parser.parse_args()
    
    print("\n" + "="*70)
    print("🗄️  DATABASE MANAGER - English Learning Platform")
    print("="*70)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Crear app
    app = get_app()
    
    # Reset mode
    if args.reset:
        return 0 if reset_database(app) else 1
    
    # Obtener esquemas
    print("\n🔍 Analizando esquemas...")
    
    try:
        model_tables = get_model_tables(app)
        print(f"   📋 Modelos cargados: {len(model_tables)} tablas")
    except Exception as e:
        print(f"   ❌ Error cargando modelos: {e}")
        return 1
    
    try:
        db_tables = get_database_tables(app)
        print(f"   📋 Tablas en DB: {len(db_tables)} tablas")
    except Exception as e:
        print(f"   ❌ Error conectando a DB: {e}")
        print("\n💡 Tip: Verifica que PostgreSQL esté corriendo y las credenciales en .env sean correctas")
        return 1
    
    # Comparar
    differences = compare_schemas(model_tables, db_tables)
    is_synced = print_report(differences, model_tables, db_tables)
    
    # Solo verificar
    if args.check:
        if is_synced:
            print("\n✅ Verificación completada - Sin cambios necesarios")
            return 0
        else:
            print("\n⚠️  Se encontraron diferencias - Ejecuta sin --check para aplicar cambios")
            return 1
    
    # Aplicar cambios si hay diferencias
    if not is_synced:
        # Backup opcional
        if args.backup:
            create_backup(app)
        
        # Aplicar
        if apply_changes(app, differences):
            verify_indexes(app)
            print("\n✅ Base de datos actualizada correctamente")
            return 0
        else:
            print("\n❌ Hubo errores durante la actualización")
            return 1
    
    # Verificar índices aunque esté sincronizado
    verify_indexes(app)
    
    print("\n✅ Verificación completada")
    return 0


if __name__ == '__main__':
    sys.exit(main())
