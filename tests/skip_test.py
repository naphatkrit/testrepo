import unittest


class SkippedTest(unittest.TestCase):
    """A test that gets skipped
    """

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")
