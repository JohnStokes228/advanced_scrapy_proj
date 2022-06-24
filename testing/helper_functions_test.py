import unittest
from spiders.helper_functions import reraise


class TestHelperFunctions(unittest.TestCase):
    @staticmethod
    def useless():
        try:
            raise Exception
        except Exception as e:
            reraise(e, 'twiddly twoo')

    def test_reraise(self):
        with self.assertRaises(Exception) as context:
            self.useless()
        self.assertTrue('twiddly twoo' in str(context.exception))


if __name__ == "__main__":
    unittest.main()
