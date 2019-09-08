from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel


class UserTestUnit(UnitBaseTest):

    def test_create_user(self):
        user = UserModel('testuser', 'testpasswd')

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpasswd')
