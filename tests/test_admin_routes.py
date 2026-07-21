import pytest
from app.models import Unit


class TestAdminDashboard:
    def test_dashboard_loads(self, admin_client):
        resp = admin_client.get('/admin/')
        assert resp.status_code == 200
        assert b'Dashboard' in resp.data


class TestAdminUnits:
    def test_unit_create_form_loads(self, admin_client):
        resp = admin_client.get('/admin/units/new')
        assert resp.status_code == 200
        assert b'Nueva Unidad' in resp.data

    def test_unit_create_post(self, admin_client, db):
        resp = admin_client.post('/admin/units/new', data={
            'unit_number': '1',
            'title': 'Test Unit',
            'description': 'A test unit',
        })
        assert resp.status_code == 302
        assert Unit.query.count() == 1
        unit = Unit.query.first()
        assert unit.title == 'Test Unit'
        assert unit.unit_number == 1

    def test_unit_edit(self, admin_client, db):
        unit = Unit(unit_number=1, title='Original Title')
        db.session.add(unit)
        db.session.commit()

        resp = admin_client.get(f'/admin/units/{unit.id}/edit')
        assert resp.status_code == 200
        assert b'Original Title' in resp.data

    def test_unit_edit_post(self, admin_client, db):
        unit = Unit(unit_number=1, title='Old Title')
        db.session.add(unit)
        db.session.commit()

        resp = admin_client.post(f'/admin/units/{unit.id}/edit', data={
            'unit_number': '1',
            'title': 'New Title',
        })
        assert resp.status_code == 302
        db.session.refresh(unit)
        assert unit.title == 'New Title'

    def test_unit_delete(self, admin_client, db):
        unit = Unit(unit_number=1, title='To Delete')
        db.session.add(unit)
        db.session.commit()
        assert Unit.query.count() == 1

        resp = admin_client.post(f'/admin/units/{unit.id}/delete')
        assert resp.status_code == 302
        assert Unit.query.count() == 0


class TestAdminUsers:
    def test_user_create_form_loads(self, admin_client):
        resp = admin_client.get('/admin/users/new')
        assert resp.status_code == 200


class TestAdminAccessControl:
    def test_non_admin_redirected(self, client):
        resp = client.get('/admin/')
        assert resp.status_code == 302
        assert '/auth/login' in resp.headers['Location']

    def test_unauthenticated_redirected(self, client):
        resp = client.get('/admin/units')
        assert resp.status_code == 302
        assert '/auth/login' in resp.headers['Location']
