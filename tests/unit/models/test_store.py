from tests.unit.unit_base_test import UnitBaseTest
from models.store import StoreModel


class StoreTestUnit(UnitBaseTest):

    def test_create_store(self):
        store = StoreModel('musicShop')
        self.assertEqual(store.name, 'musicShop')
