import unittest, json
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_example(self):
        with open("test.json") as test_json:
            convert = json.load(test_json)
        answer = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
        }
        self.assertEqual(flatten(convert), answer)

    def test_more(self):
        with open("2json.json") as test_json:
            convert = json.load(test_json)
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
        with open("empty.json") as test_json:
            convert = json.load(test_json)
        answer = {}
        self.assertEqual(flatten(convert), answer)

    def test_one_single_key(self):
        with open("single.json") as test_json:
            convert = json.load(test_json)
        answer = {
            "c.d": 3,
            "c.e": "test"
        }
        self.assertEqual(flatten(convert), answer)

if __name__ == '__main__':
    unittest.main()