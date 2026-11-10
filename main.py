import unittest

class TestTaskManager(unittest.TestCase):
    def test_search_contact_name(self):
        # Test searching for a contact by name
        self.assertTrue(search_contact_name("Leandro", "41992020511"))

    def test_add_contact_category(self):
        # Test adding a contact to a category
        self.assertTrue(add_contact_category("Leandro", "41992020511"))

if __name__ == "__main__":
    unittest.main()