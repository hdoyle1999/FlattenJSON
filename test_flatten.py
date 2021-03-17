import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_example(self):
        convert = {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
            }
        }
        answer = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
        }
        self.assertEqual(flatten(convert), answer)

    def test_more(self):
        convert = {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
            },
            "d": {
                "d": False,
                "e": "Hello World"
            },
            "e": {
                "d": 'c',
                "e": 63.87
            }
        }
        answer = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test",
            "d.d": False,
            "d.e": "Hello World",
            "e.d": 'c',
            "e.e": 63.87
        }
        self.assertEqual(flatten(convert), answer)

    def test_null_JSON(self):
        convert = {}
        answer = {}
        self.assertEqual(flatten(convert), answer)

    def test_one_single_key(self):
        convert = {
            "c": {
                "d": 3,
                "e": "test"
            }
        }
        answer = {
            "c.d": 3,
            "c.e": "test"
        }
        self.assertEqual(flatten(convert), answer)

if __name__ == '__main__':
    unittest.main()