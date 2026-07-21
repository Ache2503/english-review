import pytest
from app import create_app
from app.extensions import db as _db


@pytest.fixture(scope='session')
def app():
    """Create application for testing."""
    app = create_app('testing')
    return app


@pytest.fixture(scope='function')
def db(app):
    """Create database tables for each test, drop after."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.rollback()
        _db.drop_all()


@pytest.fixture(scope='function')
def client(app, db):
    """Test client with fresh database."""
    return app.test_client()


@pytest.fixture(scope='function')
def runner(app, db):
    """Test CLI runner with fresh database."""
    return app.test_cli_runner()


@pytest.fixture
def logged_in_client(client, db):
    """Client logged in as a regular user."""
    from app.models import User
    user = User(username='testuser', email='test@test.com', is_admin=False)
    user.set_password('test123')
    db.session.add(user)
    db.session.commit()
    
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'test123'
    }, follow_redirects=True)
    return client


@pytest.fixture
def admin_client(client, db):
    """Client logged in as admin."""
    from app.models import User
    admin = User(username='admin', email='admin@test.com', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    
    client.post('/auth/login', data={
        'username': 'admin',
        'password': 'admin123'
    }, follow_redirects=True)
    return client
