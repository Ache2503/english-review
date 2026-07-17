import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from app import create_app
from app.extensions import db
from app.models import User, Unit
from app.services.unit_unlock import UnitUnlockSystem


class UnitUnlockLevelsTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_first_unit_is_unlocked_and_level_is_detected(self):
        user = User(username='tester', email='tester@example.com')
        user.set_password('secret')
        db.session.add(user)

        unit7 = Unit(unit_number=7, title='MIND (La Mente)', description='Unit 7')
        unit8 = Unit(unit_number=8, title='ART (Arte)', description='Unit 8')
        db.session.add_all([unit7, unit8])
        db.session.commit()

        unlock_system = UnitUnlockSystem(user.id)
        statuses = unlock_system.get_all_units_status()

        self.assertEqual(len(statuses), 2)
        self.assertTrue(statuses[0]['unlocked'])
        self.assertEqual(statuses[0]['level'], 'A1')
        self.assertEqual(statuses[1]['level'], 'A1')


if __name__ == '__main__':
    unittest.main()
