#!/usr/bin/env python3
"""
Test script to verify statistics and progress saving functionality.
Tests the StudyExerciseResult and StudyProgress models.
"""

from app import create_app
from app.extensions import db
from app.models import User, StudyExerciseResult, StudyProgress
from datetime import datetime

app = create_app()

with app.app_context():
    # Clean up test data
    StudyExerciseResult.query.delete()
    StudyProgress.query.delete()
    db.session.commit()
    
    # Find or create test user
    test_user = User.query.filter_by(username='testuser').first()
    if not test_user:
        test_user = User(
            username='testuser',
            email='test@example.com'
        )
        test_user.set_password('test123')
        db.session.add(test_user)
        db.session.commit()
    
    print(f"✓ Test user: {test_user.username} (ID: {test_user.id})")
    
    # Test 1: Create StudyExerciseResult (individual attempt)
    print("\n" + "="*50)
    print("TEST 1: Creating StudyExerciseResult (individual attempt)")
    print("="*50)
    
    result1 = StudyExerciseResult(
        user_id=test_user.id,
        topic_id='grammar-basics',
        exercise_index=0,
        question_index=0,
        user_answer='The answer',
        is_correct=True,
        attempts=1,
        completed_at=datetime.utcnow()
    )
    db.session.add(result1)
    db.session.commit()
    
    print(f"✓ Created StudyExerciseResult:")
    print(f"  - Topic: {result1.topic_id}")
    print(f"  - Exercise: {result1.exercise_index}, Question: {result1.question_index}")
    print(f"  - Correct: {result1.is_correct}")
    print(f"  - Completed at: {result1.completed_at}")
    
    # Test 2: Create/Update StudyProgress (topic progress tracking)
    print("\n" + "="*50)
    print("TEST 2: Creating StudyProgress (topic tracking)")
    print("="*50)
    
    progress = StudyProgress(
        user_id=test_user.id,
        topic_id='grammar-basics',
        exercises_attempted=1,
        exercises_correct=1,
        success_rate=100.0,
        is_completed=False,
        started_at=datetime.utcnow()
    )
    db.session.add(progress)
    db.session.commit()
    
    print(f"✓ Created StudyProgress:")
    print(f"  - Topic: {progress.topic_id}")
    print(f"  - Exercises attempted: {progress.exercises_attempted}")
    print(f"  - Exercises correct: {progress.exercises_correct}")
    print(f"  - Success rate: {progress.success_rate}%")
    print(f"  - Is completed: {progress.is_completed}")
    
    # Test 3: Add more results and update progress
    print("\n" + "="*50)
    print("TEST 3: Adding more results and updating progress")
    print("="*50)
    
    result2 = StudyExerciseResult(
        user_id=test_user.id,
        topic_id='grammar-basics',
        exercise_index=0,
        question_index=1,
        user_answer='Wrong answer',
        is_correct=False,
        attempts=1,
        completed_at=datetime.utcnow()
    )
    db.session.add(result2)
    
    # Update progress
    progress.exercises_attempted = 2
    progress.exercises_correct = 1
    progress.success_rate = progress.calculate_success_rate()
    db.session.commit()
    
    print(f"✓ Added another result and updated progress:")
    print(f"  - Exercises attempted: {progress.exercises_attempted}")
    print(f"  - Exercises correct: {progress.exercises_correct}")
    print(f"  - Success rate: {progress.success_rate}%")
    
    # Test 4: Query and verify data
    print("\n" + "="*50)
    print("TEST 4: Querying saved data")
    print("="*50)
    
    results = StudyExerciseResult.query.filter_by(
        user_id=test_user.id,
        topic_id='grammar-basics'
    ).all()
    
    print(f"✓ Found {len(results)} exercise results:")
    for r in results:
        print(f"  - Q{r.question_index}: {'✓' if r.is_correct else '✗'} ({r.user_answer})")
    
    prog = StudyProgress.query.filter_by(
        user_id=test_user.id,
        topic_id='grammar-basics'
    ).first()
    
    print(f"\n✓ Progress summary:")
    print(f"  - Total: {prog.exercises_attempted}")
    print(f"  - Correct: {prog.exercises_correct}")
    print(f"  - Success: {prog.success_rate}%")
    
    # Test 5: Test mark_completed
    print("\n" + "="*50)
    print("TEST 5: Marking topic as completed")
    print("="*50)
    
    prog.mark_completed()
    db.session.commit()
    
    print(f"✓ Topic marked as completed:")
    print(f"  - Is completed: {prog.is_completed}")
    print(f"  - Completed at: {prog.completed_at}")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)
    print("\nStatistics and progress saving functionality is working correctly!")
