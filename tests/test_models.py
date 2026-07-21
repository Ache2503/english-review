import pytest
from datetime import date, timedelta


def test_user_creation(db):
    from app.models import User
    user = User(username='testuser', email='test@test.com')
    user.set_password('pass123')
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert user.username == 'testuser'
    assert user.email == 'test@test.com'
    assert user.is_admin is False
    assert user.password_hash != 'pass123'


def test_user_check_password(db):
    from app.models import User
    user = User(username='testuser', email='test@test.com')
    user.set_password('secret')
    db.session.add(user)
    db.session.commit()

    assert user.check_password('secret') is True
    assert user.check_password('wrong') is False


def test_user_age_with_dob(db):
    from app.models import User
    today = date.today()
    user = User(
        username='testuser',
        email='test@test.com',
        date_of_birth=date(today.year - 25, today.month, today.day)
    )
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    assert user.age == 25


def test_user_age_without_dob(db):
    from app.models import User
    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    db.session.add(user)
    db.session.commit()

    assert user.age == 15


def test_unit_creation(db):
    from app.models import Unit
    unit = Unit(unit_number=1, title='Greetings', description='Basic greetings')
    db.session.add(unit)
    db.session.commit()

    assert unit.id is not None
    assert unit.unit_number == 1
    assert unit.title == 'Greetings'


def test_unit_topics_relationship(db):
    from app.models import Unit, Topic
    unit = Unit(unit_number=1, title='Greetings')
    db.session.add(unit)
    db.session.flush()

    topic = Topic(unit_id=unit.id, title='Hello and Goodbye', order=1)
    db.session.add(topic)
    db.session.commit()

    assert unit.topics.count() == 1
    assert unit.topics.first().title == 'Hello and Goodbye'


def test_unit_grammar_rules_relationship(db):
    from app.models import Unit, GrammarRule
    unit = Unit(unit_number=2, title='Verbs')
    db.session.add(unit)
    db.session.flush()

    rule = GrammarRule(
        unit_id=unit.id,
        topic='Present Simple',
        rule='Subject + verb (s/es for he/she/it)'
    )
    db.session.add(rule)
    db.session.commit()

    assert unit.grammar_rules.count() == 1
    assert unit.grammar_rules.first().topic == 'Present Simple'


def test_quiz_creation(db):
    from app.models import Unit, Quiz, QuizQuestion, QuizOption
    unit = Unit(unit_number=3, title='Past Tense')
    db.session.add(unit)
    db.session.flush()

    quiz = Quiz(unit_id=unit.id, title='Past Tense Quiz')
    db.session.add(quiz)
    db.session.flush()

    question = QuizQuestion(quiz_id=quiz.id, prompt='What is the past of "go"?')
    db.session.add(question)
    db.session.flush()

    opt1 = QuizOption(question_id=question.id, text='went', is_correct=True)
    opt2 = QuizOption(question_id=question.id, text='goed', is_correct=False)
    db.session.add_all([opt1, opt2])
    db.session.commit()

    assert quiz.id is not None
    assert quiz.questions.count() == 1
    q = quiz.questions.first()
    assert q.options.count() == 2
    assert q.options.filter_by(is_correct=True).first().text == 'went'


def test_flashcard_creation(db):
    from app.models import Unit, Flashcard
    unit = Unit(unit_number=4, title='Vocabulary')
    db.session.add(unit)
    db.session.flush()

    card = Flashcard(unit_id=unit.id, front='apple', back='manzana', example='I eat an apple.')
    db.session.add(card)
    db.session.commit()

    assert card.id is not None
    assert card.front == 'apple'
    assert card.back == 'manzana'
    assert card.is_active is True


def test_user_progress_creation(db):
    from app.models import User, Unit, UserProgress
    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Greetings')
    db.session.add_all([user, unit])
    db.session.flush()

    progress = UserProgress(user_id=user.id, unit_id=unit.id)
    db.session.add(progress)
    db.session.commit()

    assert progress.id is not None
    assert progress.completed is False
    assert progress.progress_percentage == 0.0


def test_user_progress_unique_constraint(db):
    from app.models import User, Unit, UserProgress
    from sqlalchemy.exc import IntegrityError
    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Greetings')
    db.session.add_all([user, unit])
    db.session.flush()

    p1 = UserProgress(user_id=user.id, unit_id=unit.id)
    db.session.add(p1)
    db.session.commit()

    p2 = UserProgress(user_id=user.id, unit_id=unit.id)
    db.session.add(p2)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()


def test_bookmark_creation(db):
    from app.models import User, Bookmark, Unit, GrammarRule
    user = User(username='testuser', email='test@test.com')
    user.set_password('pass')
    unit = Unit(unit_number=1, title='Greetings')
    db.session.add_all([user, unit])
    db.session.flush()

    rule = GrammarRule(
        unit_id=unit.id,
        topic='Articles',
        rule='Use "a" before consonant sounds, "an" before vowel sounds'
    )
    db.session.add(rule)
    db.session.flush()

    bookmark = Bookmark(
        user_id=user.id,
        bookmark_type='grammar',
        grammar_id=rule.id,
        english_text='Use "an" before vowel sounds',
        spanish_translation='Usar "an" antes de sonidos de vocal'
    )
    db.session.add(bookmark)
    db.session.commit()

    assert bookmark.id is not None
    assert bookmark.grammar_id == rule.id
    assert bookmark.user_id == user.id
