import unittest


class GenericTest(unittest.TestCase):
    """A test that you can make fail
    """

    def test_one(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)
