from app import hello
from app import test
import unittest

class TestApp(unittest.TestCase):
    def test_hello(self):
        expected = "Hello World!"
        self.assertEqual(expected, hello())

    def test_test(self):
        expected = "Test"
        self.assertEqual(expected, test())

if __name__ == "__main__":
    unittest.main()
