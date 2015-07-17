import unittest


class OtherTest(unittest.TestCase):
    """A test that you can make fail
    """

    def test_three(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)

    def test_four(self):
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)  # fails
