#!/usr/bin/env python3
"""
Script de Verificación de Tema Automático
Verifica que todos los archivos necesarios estén presentes y sean válidos
"""

import os
import re
from pathlib import Path

def check_file_exists(file_path, description):
    """Verifica si un archivo existe"""
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"✅ {description}")
        print(f"   📁 {file_path} ({size} bytes)")
        return True
    else:
        print(f"❌ {description}")
        print(f"   ❗ Archivo no encontrado: {file_path}")
        return False

def check_file_contains(file_path, pattern, description):
    """Verifica si un archivo contiene un patrón específico"""
    if not os.path.exists(file_path):
        print(f"❌ {description} - Archivo no existe")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if re.search(pattern, content, re.IGNORECASE):
                print(f"✅ {description}")
                return True
            else:
                print(f"❌ {description} - Patrón no encontrado")
                return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False

def main():
    print("=" * 80)
    print("🌓 VERIFICADOR DE TEMA AUTOMÁTICO")
    print("=" * 80)
    print()

    base_path = Path(__file__).parent

    # Lista de verificaciones
    checks = []

    print("📋 VERIFICANDO ARCHIVOS NECESARIOS...")
    print("-" * 80)

    # 1. Verificar theme-detector.js
    checks.append(check_file_exists(
        base_path / "app" / "static" / "js" / "theme-detector.js",
        "Script de detección de tema"
    ))
    print()

    # 2. Verificar base.html tiene las nuevas variables CSS
    checks.append(check_file_contains(
        base_path / "app" / "templates" / "base.html",
        r"--text-primary:\s*#f0f4f8",
        "Variables CSS mejoradas en base.html"
    ))
    print()

    # 3. Verificar dark mode en base.html
    checks.append(check_file_contains(
        base_path / "app" / "templates" / "base.html",
        r"@media\s*\(prefers-color-scheme:\s*dark\)",
        "Media query para dark mode en base.html"
    ))
    print()

    # 4. Verificar script incluido en base.html
    checks.append(check_file_contains(
        base_path / "app" / "templates" / "base.html",
        r"theme-detector\.js",
        "Script theme-detector.js incluido en base.html"
    ))
    print()

    # 5. Verificar stats/dashboard.html mejorado
    checks.append(check_file_contains(
        base_path / "app" / "templates" / "stats" / "dashboard.html",
        r"prefers-color-scheme.*dark",
        "Mejoras de dark mode en stats/dashboard.html"
    ))
    print()

    # 6. Verificar conversation_detail.html mejorado
    checks.append(check_file_contains(
        base_path / "app" / "templates" / "conversation_detail.html",
        r"var\(--bg-card\)",
        "Variables CSS en conversation_detail.html"
    ))
    print()

    # 7. Verificar guía de tema
    checks.append(check_file_exists(
        base_path / "TEMA_AUTOMATICO_GUIDE.md",
        "Guía de tema automático"
    ))
    print()

    # Resumen
    print("=" * 80)
    print("📊 RESUMEN DE VERIFICACIÓN")
    print("=" * 80)
    total = len(checks)
    passed = sum(checks)
    failed = total - passed

    print(f"✅ Verificaciones exitosas: {passed}/{total}")
    print(f"❌ Verificaciones fallidas:  {failed}/{total}")
    print()

    if failed == 0:
        print("🎉 ¡EXCELENTE! Todos los archivos están en su lugar.")
        print()
        print("Próximos pasos:")
        print("1. Ejecuta tu servidor Flask: python run.py")
        print("2. Abre tu navegador")
        print("3. Cambia tu tema del sistema a oscuro")
        print("4. Recarga la página (F5)")
        print("5. ¡Deberías ver el tema oscuro automáticamente!")
        print()
        print("Para probar en Chrome:")
        print("  • F12 → Ctrl+Shift+P (Cmd+Shift+P en Mac)")
        print("  • Busca: 'Emulate CSS media feature prefers-color-scheme'")
        print("  • Selecciona 'dark'")
        print()
    else:
        print(f"⚠️  Hay {failed} verificación(es) que fallaron.")
        print("Por favor, revisa los errores arriba.")
        print()

    # Información adicional
    print("=" * 80)
    print("ℹ️  INFORMACIÓN DEL SISTEMA")
    print("=" * 80)
    print()
    print("Funciones públicas disponibles en el navegador:")
    print("  • window.setTheme('dark')     - Cambiar a tema oscuro")
    print("  • window.setTheme('light')    - Cambiar a tema claro")
    print("  • window.getTheme()           - Obtener tema actual")
    print("  • window.resetTheme()         - Usar tema del sistema")
    print()
    print("Evento personalizado:")
    print("  • document.addEventListener('themechange', handler)")
    print()

    # Verificar colores en el código
    print("=" * 80)
    print("🎨 PALETA DE COLORES (Dark Mode)")
    print("=" * 80)
    print()
    print("Fondos:")
    print("  • #0a0e27 - Fondo principal (casi negro)")
    print("  • #141829 - Fondo de tarjetas")
    print("  • #1a2332 - Fondo de inputs")
    print("  • #1a2f4f - Fondo de headers (gradiente)")
    print()
    print("Textos:")
    print("  • #f0f4f8 - Texto principal (blanco brillante)")
    print("  • #e0e8f0 - Texto normal")
    print("  • #a8b8cc - Texto débil/muted")
    print()
    print("Bordes:")
    print("  • #2a3f5f - Bordes visibles")
    print()
    print("Colores de Estado:")
    print("  • #3b82f6 - Azul (primario)")
    print("  • #22c55e - Verde (éxito)")
    print("  • #ef4444 - Rojo (peligro)")
    print("  • #fbbf24 - Amarillo (alerta)")
    print()

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit(main())
