#!/usr/bin/env python
"""
Master test runner - executes all test suites
"""
import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"\n{'='*70}")
    print(f"🧪 {description}")
    print(f"{'='*70}\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            capture_output=False
        )
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    """Run all test suites"""
    # Set environment
    os.environ['DATABASE_URL'] = 'postgresql:///english_learning'
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    venv_python = '/home/axel-michael/Documentos/guia_estudio/.venv/bin/python'
    
    print("=" * 70)
    print("🚀 EJECUTANDO TODAS LAS PRUEBAS")
    print("=" * 70)
    
    results = {}
    
    # Test 1: Feedback System
    results['Feedback System'] = run_command(
        f'export DATABASE_URL=postgresql:///english_learning && {venv_python} {test_dir}/test_feedback_system.py',
        'PRUEBAS DEL SISTEMA DE RETROALIMENTACIÓN'
    )
    
    # Test 2: Integration Tests
    results['Integration Tests'] = run_command(
        f'export DATABASE_URL=postgresql:///english_learning && {venv_python} {test_dir}/test_integration.py',
        'PRUEBAS DE INTEGRACIÓN'
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 RESUMEN GENERAL")
    print("=" * 70)
    
    for suite_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{suite_name}: {status}")
    
    total = len(results)
    passed_count = sum(1 for p in results.values() if p)
    
    print(f"\nSuites exitosas: {passed_count}/{total}")
    print(f"Tasa global: {(passed_count/total*100):.1f}%")
    
    if passed_count == total:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON!")
        return 0
    else:
        print(f"\n⚠️  {total - passed_count} suite(s) fallaron")
        return 1


if __name__ == '__main__':
    sys.exit(main())
