import pytest
from second_part.src import AccessWebsite
from src import CacheDecorator

def test_access_website():
    website = AccessWebsite()
    website.login(username="admin", password="admin")
    assert website.access_website() == "Success"
    website2 = AccessWebsite()
    website2.login(username="test", password="test")
    with pytest.raises(Exception):
        website2.access_website()




import unittest
class TestCacheDecorator(unittest.TestCase):
    def test_cache_decorator(self):
        @CacheDecorator()
        def add(a, b):
            return a + b

        self.assertEqual(add(1, 2), 3)  # Test cached result for (1, 2)
        self.assertTrue(1 in add.cache)  # Check if (1, 2) is in cache

    def test_different_arguments(self):
        @CacheDecorator()
        def add(a, b):
            return a + b

        self.assertEqual(add(1, 2), 3)  # Test cached result for (1, 2)
        self.assertFalse(2 in add.cache)  # Check if (2, 3) is not in cache

    def test_mutable_arguments(self):
        @CacheDecorator()
        def add_list(lst):
            return sum(lst)

        list1 = [1, 2, 3]
        list2 = [1, 2, 3]

        self.assertEqual(add_list(list1), 6)  # Test cached result for list1
        self.assertTrue(list1 in add_list.cache)  # Check if list1 is in cache
        self.assertEqual(add_list(list2), 6)  # Test cached result for list2
        self.assertTrue(list2 in add_list.cache)  # Check if list2 is in cache


if __name__ == '__main__':
    unittest.main()
