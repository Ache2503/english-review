#!/usr/bin/env python3
"""
Script para verificar los estilos dark mode en grammar/topic.html
"""

import re

def check_dark_mode_styles():
    """Verifica que los estilos dark mode estén correctamente aplicados"""
    
    with open('/home/axel-michael/Documentos/guia_estudio/english-learning-platform/app/templates/grammar/topic.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues_found = []
    
    # Buscar elementos problemáticos
    checks = {
        'topic-header with color variable': (r'\.topic-header\s*{[^}]*color:\s*var\(--text-main\)', 'topic-header tiene color variable'),
        'grammar-table th with var(--bg-body)': (r'\.grammar-table\s+th\s*{[^}]*background:\s*var\(--bg-body\)', 'grammar-table th usa CSS variable'),
        'note-box color in dark mode': (r'@media.*prefers-color-scheme:\s*dark.*\.note-box\s*{[^}]*color:\s*[#\w]+', 'note-box tiene color en dark mode'),
        'comparison boxes in dark mode': (r'@media.*prefers-color-scheme:\s*dark.*\.comparison-', 'comparison boxes tienen estilos dark mode'),
        'vocab-chip dark mode': (r'@media.*prefers-color-scheme:\s*dark.*\.vocab-chip\s*{[^}]*color:\s*', 'vocab-chip tiene estilos dark mode'),
        'highlight-cell dark mode': (r'@media.*prefers-color-scheme:\s*dark.*\.highlight-cell\s*{[^}]*background:', 'highlight-cell tiene dark mode'),
        'Dark mode media query present': (r'@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)', '@media prefers-color-scheme: dark presente'),
    }
    
    results = []
    for check_name, (pattern, description) in checks.items():
        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
            results.append(f"✅ {description}")
        else:
            results.append(f"❌ {check_name} - NO ENCONTRADO")
            issues_found.append(check_name)
    
    print("=" * 60)
    print("VERIFICACIÓN DE ESTILOS DARK MODE - grammar/topic.html")
    print("=" * 60)
    
    for result in results:
        print(result)
    
    print("\n" + "=" * 60)
    
    # Verificar hardcoded colors que deben estar en dark mode
    hardcoded_check = []
    
    # Buscar colores hardcodeados en el archivo
    light_colors = ['#f8f9fa', '#e9ecef', '#fffbeb', '#e8f4fd', '#e3f2fd', '#bbdefb', '#e8f5e9', '#c8e6c9']
    
    print("\nVERIFICACIÓN DE COLORES HARDCODEADOS:")
    print("-" * 60)
    
    # Contar ocurrencias
    for color in light_colors:
        count = content.count(color)
        if count > 0:
            # Buscar si está en dark mode section
            dark_mode_section = re.search(r'@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\).*', content, re.DOTALL)
            if dark_mode_section:
                dark_content = dark_mode_section.group(0)
                in_dark = color in dark_content
                status = "✅ (tiene override en dark mode)" if in_dark else "⚠️ (NO tiene override en dark mode)"
            else:
                status = "❌ (no hay sección dark mode)"
            print(f"{color}: {count} ocurrencias - {status}")
    
    print("\n" + "=" * 60)
    
    if not issues_found:
        print("\n✅ RESULTADO: Todos los estilos dark mode están presentes!")
    else:
        print(f"\n❌ RESULTADO: Se encontraron {len(issues_found)} problemas")
    
    print("=" * 60)
    
    return len(issues_found) == 0

if __name__ == '__main__':
    success = check_dark_mode_styles()
    exit(0 if success else 1)
