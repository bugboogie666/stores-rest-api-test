from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTestIntegration(BaseTest):

    def test_create_store_items_empty(self):
        store = StoreModel('lahudky')

        self.assertListEqual(store.items.all(), [], 'store items length not 0')

    def test_crud(self):
        with self.app_context():
            store = StoreModel('lahudky')

            self.assertIsNone(StoreModel.find_by_name('lahudky'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('lahudky'), 'store has not found in DB')

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('lahudky'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('lahudky')
            item = ItemModel('chlebicek', 20, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'chlebicek')

    def test_json_store_with_item(self):
        expected = {'name': 'lahudky',
                    'items': [{'name': 'chlebicek', 'price': 20}]}
        with self.app_context():
            store = StoreModel('lahudky')
            item = ItemModel('chlebicek', 20, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertDictEqual(store.json(), expected)






