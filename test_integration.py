#!/usr/bin/env python
"""
Integration tests for practice routes with feedback system
"""
import sys
import os
from pathlib import Path

proj_dir = Path(__file__).parent
sys.path.insert(0, str(proj_dir))

from app import create_app, db
from app.models import User, Unit, WritingPractice, UserWritingSubmission, UserSentencePractice
import json


def test_api_analyze():
    """Test the API analyze endpoint"""
    app = create_app('development')
    app.config['TESTING'] = True
    
    with app.app_context():
        with app.test_client() as client:
            # Create test user
            user = User.query.filter_by(username='testuser').first()
            if not user:
                user = User(username='testuser', email='test@example.com', full_name='Test User')
                user.set_password('test123')
                db.session.add(user)
                db.session.commit()
            
            # Login
            response = client.post('/auth/login', data={
                'username': 'testuser',
                'password': 'test123'
            }, follow_redirects=True)
            
            print("=" * 70)
            print("PRUEBA DE INTEGRACIÓN - API ANALYZE")
            print("=" * 70)
            
            # Test API analyze
            test_cases = [
                {
                    "unit": 8,
                    "text": "I bought myself a new book. If I have time, I will go to the museum.",
                    "expected_min_score": 50
                },
                {
                    "unit": 10,
                    "text": "This laptop is faster than my phone. It's the most powerful device I own.",
                    "expected_min_score": 50
                }
            ]
            
            passed = 0
            total = len(test_cases)
            
            for idx, test in enumerate(test_cases, 1):
                print(f"\n📝 Test Case {idx}: Unit {test['unit']}")
                print(f"   Texto: {test['text'][:60]}...")
                
                response = client.post('/practice/api/analyze',
                    data=json.dumps({
                        'text': test['text'],
                        'unit_number': test['unit']
                    }),
                    content_type='application/json'
                )
                
                if response.status_code == 200:
                    data = response.get_json()
                    if data.get('ok'):
                        score = data.get('score', 0)
                        messages = data.get('messages', [])
                        print(f"   ✓ Status: 200 OK")
                        print(f"   Score: {score}/100")
                        print(f"   Mensajes: {len(messages)}")
                        
                        if score >= test['expected_min_score'] and len(messages) > 0:
                            print(f"   ✅ PASS")
                            passed += 1
                        else:
                            print(f"   ❌ FAIL: Score o mensajes insuficientes")
                    else:
                        print(f"   ❌ FAIL: Response not OK")
                else:
                    print(f"   ❌ FAIL: Status {response.status_code}")
            
            print(f"\n{'=' * 70}")
            print(f"Resultado: {passed}/{total} pruebas exitosas")
            
            return passed == total


def test_writing_submission():
    """Test writing practice submission with feedback"""
    app = create_app('development')
    app.config['TESTING'] = True
    
    with app.app_context():
        with app.test_client() as client:
            # Login
            user = User.query.filter_by(username='testuser').first()
            client.post('/auth/login', data={
                'username': 'testuser',
                'password': 'test123'
            })
            
            print("\n" + "=" * 70)
            print("PRUEBA DE INTEGRACIÓN - WRITING SUBMISSION")
            print("=" * 70)
            
            # Get a writing practice
            practice = WritingPractice.query.first()
            if not practice:
                print("❌ No writing practices found")
                return False
            
            print(f"\n📝 Writing Practice: {practice.title}")
            
            # Submit writing
            test_text = "I used to think that happiness was impossible to find, but now I realize that simple things bring joy. Going to the park with friends makes me happy. The sunset we watched yesterday was beautiful."
            
            response = client.post(f'/practice/writing/{practice.id}',
                data={'text': test_text},
                follow_redirects=False
            )
            
            if response.status_code == 302:  # Redirect after success
                print("✓ Submission successful (redirect)")
                
                # Check database for submission
                submission = UserWritingSubmission.query.filter_by(
                    user_id=user.id,
                    practice_id=practice.id
                ).order_by(UserWritingSubmission.submitted_at.desc()).first()
                
                if submission:
                    print(f"✓ Submission found in DB")
                    print(f"  Score: {submission.score}")
                    print(f"  Feedback length: {len(submission.feedback) if submission.feedback else 0} chars")
                    
                    if submission.score is not None and submission.feedback:
                        print("✅ PASS: Feedback generated")
                        return True
                    else:
                        print("❌ FAIL: No feedback generated")
                        return False
                else:
                    print("❌ FAIL: Submission not found in DB")
                    return False
            else:
                print(f"❌ FAIL: Unexpected status {response.status_code}")
                return False


def test_sentence_practice():
    """Test sentence practice with feedback"""
    app = create_app('development')
    app.config['TESTING'] = True
    
    with app.app_context():
        with app.test_client() as client:
            # Login
            user = User.query.filter_by(username='testuser').first()
            client.post('/auth/login', data={
                'username': 'testuser',
                'password': 'test123'
            })
            
            print("\n" + "=" * 70)
            print("PRUEBA DE INTEGRACIÓN - SENTENCE PRACTICE")
            print("=" * 70)
            
            # Get a unit
            unit = Unit.query.filter_by(unit_number=9).first()
            if not unit:
                print("❌ Unit 9 not found")
                return False
            
            print(f"\n📝 Unit: {unit.title}")
            
            # Submit sentence
            test_sentence = "If I had more time, I would volunteer at the animal shelter."
            
            response = client.post(f'/practice/sentence/{unit.id}',
                data={'sentence': test_sentence},
                follow_redirects=False
            )
            
            if response.status_code == 302:
                print("✓ Sentence submission successful")
                
                # Check database
                sentence_practice = UserSentencePractice.query.filter_by(
                    user_id=user.id,
                    unit_id=unit.id
                ).order_by(UserSentencePractice.created_at.desc()).first()
                
                if sentence_practice:
                    print(f"✓ Sentence found in DB")
                    print(f"  Score: {sentence_practice.score}")
                    print(f"  Feedback: {sentence_practice.feedback[:80] if sentence_practice.feedback else 'None'}...")
                    
                    if sentence_practice.score is not None and sentence_practice.feedback:
                        print("✅ PASS: Feedback generated")
                        return True
                    else:
                        print("❌ FAIL: No feedback")
                        return False
                else:
                    print("❌ FAIL: Sentence not saved")
                    return False
            else:
                print(f"❌ FAIL: Status {response.status_code}")
                return False


def run_integration_tests():
    """Run all integration tests"""
    print("\n" + "=" * 70)
    print("PRUEBAS DE INTEGRACIÓN - SISTEMA COMPLETO")
    print("=" * 70)
    
    results = {
        'API Analyze': test_api_analyze(),
        'Writing Submission': test_writing_submission(),
        'Sentence Practice': test_sentence_practice()
    }
    
    print("\n" + "=" * 70)
    print("RESUMEN DE INTEGRACIÓN")
    print("=" * 70)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed_count = sum(1 for p in results.values() if p)
    
    print(f"\nTotal: {passed_count}/{total} pruebas exitosas")
    print(f"Tasa de éxito: {(passed_count/total*100):.1f}%")
    
    if passed_count == total:
        print("\n✅ ¡TODAS LAS PRUEBAS DE INTEGRACIÓN PASARON!")
        return 0
    else:
        print(f"\n⚠️  {total - passed_count} prueba(s) fallaron")
        return 1


if __name__ == '__main__':
    sys.exit(run_integration_tests())
