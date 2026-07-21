import pytest
from datetime import date, timedelta
from unittest.mock import patch


# =============================================
# SRS (Spaced Repetition System) Tests
# =============================================

def test_srs_easy_review_increases_interval(db):
    from app.services.srs import calculate_next_review
    interval, ease, reps = calculate_next_review(quality=5, repetitions=0, ease_factor=2.5, interval=1)
    assert reps == 1
    assert interval == 1

    interval, ease, reps = calculate_next_review(quality=5, repetitions=1, ease_factor=ease, interval=interval)
    assert reps == 2
    assert interval == 6

    prev_interval = interval
    interval, ease, reps = calculate_next_review(quality=5, repetitions=2, ease_factor=ease, interval=interval)
    assert reps == 3
    assert interval > prev_interval


def test_srs_poor_review_resets(db):
    from app.services.srs import calculate_next_review
    interval, ease, reps = calculate_next_review(quality=5, repetitions=5, ease_factor=2.5, interval=20)
    assert reps == 6

    interval, ease, reps = calculate_next_review(quality=1, repetitions=reps, ease_factor=ease, interval=interval)
    assert reps == 0
    assert interval == 1


def test_srs_ease_factor_minimum(db):
    from app.services.srs import calculate_next_review
    ease = 2.5
    for _ in range(20):
        _, ease, _ = calculate_next_review(quality=0, repetitions=0, ease_factor=ease, interval=1)
    assert ease >= 1.3


def test_srs_quality_from_response_correct_fast(db):
    from app.services.srs import quality_from_response
    assert quality_from_response(True, response_time_seconds=2) == 5


def test_srs_quality_from_response_correct_medium(db):
    from app.services.srs import quality_from_response
    assert quality_from_response(True, response_time_seconds=5) == 4


def test_srs_quality_from_response_correct_slow(db):
    from app.services.srs import quality_from_response
    assert quality_from_response(True, response_time_seconds=10) == 3


def test_srs_quality_from_response_incorrect(db):
    from app.services.srs import quality_from_response
    assert quality_from_response(False) == 1


def test_srs_quality_from_response_no_time(db):
    from app.services.srs import quality_from_response
    assert quality_from_response(True, response_time_seconds=None) == 4


def test_srs_get_next_review_date(db):
    from app.services.srs import get_next_review_date
    from datetime import datetime
    result = get_next_review_date(7)
    expected = datetime.utcnow().date() + timedelta(days=7)
    assert result.date() == expected


def test_srs_review_flashcard_first_time(db):
    from app.models import User, Flashcard, Unit
    from app.services.srs import review_flashcard_srs

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Test')
    db.session.add_all([user, unit])
    db.session.flush()

    card = Flashcard(unit_id=unit.id, front='hello', back='hola')
    db.session.add(card)
    db.session.commit()

    result = review_flashcard_srs(user.id, card.id, quality=5)

    assert result['is_correct'] is True
    assert result['repetitions'] == 1
    assert result['interval'] == 1


def test_srs_review_flashcard_progressive(db):
    from app.models import User, Flashcard, Unit
    from app.services.srs import review_flashcard_srs

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Test')
    db.session.add_all([user, unit])
    db.session.flush()

    card = Flashcard(unit_id=unit.id, front='hello', back='hola')
    db.session.add(card)
    db.session.commit()

    review_flashcard_srs(user.id, card.id, quality=5)
    review_flashcard_srs(user.id, card.id, quality=5)
    result = review_flashcard_srs(user.id, card.id, quality=4)

    assert result['repetitions'] == 3
    assert result['is_correct'] is True


def test_srs_review_flashcard_fail_resets(db):
    from app.models import User, Flashcard, Unit
    from app.services.srs import review_flashcard_srs

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Test')
    db.session.add_all([user, unit])
    db.session.flush()

    card = Flashcard(unit_id=unit.id, front='hello', back='hola')
    db.session.add(card)
    db.session.commit()

    review_flashcard_srs(user.id, card.id, quality=5)
    review_flashcard_srs(user.id, card.id, quality=5)
    result = review_flashcard_srs(user.id, card.id, quality=1)

    assert result['repetitions'] == 0
    assert result['is_correct'] is False


def test_srs_user_flashcard_srs_model_properties(db):
    from app.models import UserFlashcardSRS
    from datetime import datetime

    srs = UserFlashcardSRS(
        user_id=1, flashcard_id=1,
        total_reviews=10, correct_reviews=8,
        repetitions=4
    )
    assert srs.retention_rate == 80.0
    assert srs.status == 'learned'

    srs.repetitions = 0
    assert srs.status == 'new'

    srs.repetitions = 2
    assert srs.status == 'learning'

    srs.repetitions = 7
    assert srs.status == 'mastered'


def test_srs_user_flashcard_srs_zero_reviews(db):
    from app.models import UserFlashcardSRS

    srs = UserFlashcardSRS(
        user_id=1, flashcard_id=1,
        total_reviews=0, correct_reviews=0
    )
    assert srs.retention_rate == 0


# =============================================
# Streak Tracking Tests
# =============================================

def test_streak_creates_new(db):
    from app.models import User
    from app.services.streaks import update_user_streak

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    streak = update_user_streak(user.id)

    assert streak.current_streak == 1
    assert streak.longest_streak == 1
    assert streak.last_activity_date == date.today()


def test_streak_same_day_no_change(db):
    from app.models import User
    from app.services.streaks import update_user_streak

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    streak1 = update_user_streak(user.id)
    streak2 = update_user_streak(user.id)

    assert streak1.id == streak2.id
    assert streak2.current_streak == 1


def test_streak_consecutive_days(db):
    from app.models import User, UserStreak
    from app.services.streaks import update_user_streak

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    yesterday = date.today() - timedelta(days=1)
    streak = UserStreak(
        user_id=user.id,
        current_streak=3,
        longest_streak=3,
        last_activity_date=yesterday
    )
    db.session.add(streak)
    db.session.commit()

    updated = update_user_streak(user.id)

    assert updated.current_streak == 4
    assert updated.longest_streak == 4
    assert updated.last_activity_date == date.today()


def test_streak_broken_resets_to_one(db):
    from app.models import User, UserStreak
    from app.services.streaks import update_user_streak

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    three_days_ago = date.today() - timedelta(days=3)
    streak = UserStreak(
        user_id=user.id,
        current_streak=10,
        longest_streak=10,
        last_activity_date=three_days_ago
    )
    db.session.add(streak)
    db.session.commit()

    updated = update_user_streak(user.id)

    assert updated.current_streak == 1
    assert updated.longest_streak == 10


def test_streak_longest_preserved(db):
    from app.models import User, UserStreak
    from app.services.streaks import update_user_streak

    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    yesterday = date.today() - timedelta(days=1)
    streak = UserStreak(
        user_id=user.id,
        current_streak=1,
        longest_streak=15,
        last_activity_date=yesterday
    )
    db.session.add(streak)
    db.session.commit()

    updated = update_user_streak(user.id)

    assert updated.current_streak == 2
    assert updated.longest_streak == 15
