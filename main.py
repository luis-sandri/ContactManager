import unittest

class TestTaskManager(unittest.TestCase):
    def test_search_contact_name(self):
        # Test searching for a contact by name
        self.assertTrue(search_contact_name("Leandro", "41992020511"))

    def test_block_contact_number(self):
        # Test blocking a contact number
        self.assertTrue(block_contact_number("Leandro", "41992020511"))

if __name__ == "__main__":
    unittest.main()