#!/usr/bin/env python
"""
Test script para validar el sistema de retroalimentación por tema
"""
import sys
import os
from pathlib import Path

# Add project to path
proj_dir = Path(__file__).parent
sys.path.insert(0, str(proj_dir))

from app import create_app
from app.extensions import db
from app.models import Unit, GrammarRule
from app.services.feedback import analyze_text

# Test cases per unit
TEST_CASES = {
    7: {
        "good": "I used to sleep late every day when I was younger, but now I wake up early. I go to school to study English and improve my skills every morning. The book that I am currently reading is very interesting and helpful for my learning journey and personal growth.",
        "bad": "I sleep late. I going school.",
        "expected_topics": ["used to", "articles"]
    },
    8: {
        "good": "I bought myself a new book. If I have time, I will go to the museum to see art.",
        "bad": "I bought me book. I go museum.",
        "expected_topics": ["reflexive pronouns", "infinitive of purpose", "first conditional"]
    },
    9: {
        "good": "If I had money, I would travel. Spending time with family is important. People who help others are kind.",
        "bad": "If I have money, I travel. Spend time is good.",
        "expected_topics": ["second conditional", "gerunds", "adjective clauses"]
    },
    10: {
        "good": "This phone is faster than my old one. It's the most expensive device. We need to update it.",
        "bad": "This phone fast than old. It expensive device.",
        "expected_topics": ["comparatives", "superlatives", "need to"]
    },
    11: {
        "good": "Plastic is found everywhere. It is important to protect nature. I looked somewhere for help.",
        "bad": "Plastic found. Important protect nature.",
        "expected_topics": ["passive voice", "adjective + infinitive", "where words"]
    },
    12: {
        "good": "She said that we should recycle. The news had already started when I arrived.",
        "bad": "She say we recycle. News start when I arrive.",
        "expected_topics": ["reported speech", "past perfect", "should"]
    }
}


def run_tests():
    """Execute all feedback tests"""
    app = create_app('development')
    
    with app.app_context():
        print("=" * 70)
        print("PRUEBAS DEL SISTEMA DE RETROALIMENTACIÓN POR TEMA")
        print("=" * 70)
        print()
        
        total_tests = 0
        passed_tests = 0
        
        for unit_num in sorted(TEST_CASES.keys()):
            print(f"\n{'─' * 70}")
            unit = Unit.query.filter_by(unit_number=unit_num).first()
            
            if not unit:
                print(f"❌ Unit {unit_num}: NO ENCONTRADA")
                continue
            
            print(f"📚 Unit {unit_num}: {unit.title}")
            print(f"{'─' * 70}")
            
            # Get grammar topics for this unit
            grammar_titles = [gr.topic for gr in GrammarRule.query.filter_by(
                unit_id=unit.id
            ).order_by(GrammarRule.order).all()]
            
            print(f"Temas de gramática: {', '.join(grammar_titles)}")
            print()
            
            test_data = TEST_CASES[unit_num]
            
            # Test 1: Good text
            print("✅ Prueba 1: Texto con buen uso de gramática")
            total_tests += 1
            result_good = analyze_text(test_data["good"], unit_num, grammar_titles)
            print(f"   Texto: {test_data['good'][:60]}...")
            print(f"   Score: {result_good['score']}/100")
            print(f"   Mensajes ({len(result_good['messages'])}):")
            for msg in result_good['messages'][:3]:
                print(f"      • {msg}")
            if result_good['score'] >= 60:
                print("   ✓ PASS: Score >= 60")
                passed_tests += 1
            else:
                print("   ✗ FAIL: Score < 60")
            print()
            
            # Test 2: Bad text
            print("⚠️  Prueba 2: Texto con errores")
            total_tests += 1
            result_bad = analyze_text(test_data["bad"], unit_num, grammar_titles)
            print(f"   Texto: {test_data['bad']}")
            print(f"   Score: {result_bad['score']}/100")
            print(f"   Mensajes ({len(result_bad['messages'])}):")
            for msg in result_bad['messages'][:3]:
                print(f"      • {msg}")
            if result_bad['score'] < result_good['score']:
                print("   ✓ PASS: Score menor que texto bueno")
                passed_tests += 1
            else:
                print("   ✗ FAIL: Score no refleja errores")
            print()
            
            # Test 3: Topic filtering
            print("🔍 Prueba 3: Filtrado por tema")
            total_tests += 1
            result_no_filter = analyze_text(test_data["good"], unit_num, None)
            result_filtered = analyze_text(test_data["good"], unit_num, grammar_titles)
            
            print(f"   Sin filtro: {len(result_no_filter['messages'])} mensajes")
            print(f"   Con filtro: {len(result_filtered['messages'])} mensajes")
            
            # Check that filtering happens (messages might differ)
            if len(result_filtered['messages']) > 0:
                print("   ✓ PASS: Analizador genera mensajes por tema")
                passed_tests += 1
            else:
                print("   ✗ FAIL: No se generaron mensajes")
            print()
        
        # Summary
        print("\n" + "=" * 70)
        print("RESUMEN DE PRUEBAS")
        print("=" * 70)
        print(f"Total de pruebas: {total_tests}")
        print(f"Pruebas exitosas: {passed_tests}")
        print(f"Pruebas fallidas: {total_tests - passed_tests}")
        print(f"Tasa de éxito: {(passed_tests/total_tests*100):.1f}%")
        
        if passed_tests == total_tests:
            print("\n✅ ¡TODAS LAS PRUEBAS PASARON!")
            return 0
        else:
            print(f"\n⚠️  {total_tests - passed_tests} prueba(s) fallaron")
            return 1


if __name__ == '__main__':
    sys.exit(run_tests())
