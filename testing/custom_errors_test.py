import unittest
from spiders.custom_errors import (
    reraise,
    InvalidURLError,
    InvalidPriceError,
)


class TestCustomErrors(unittest.TestCase):
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

    def test_invalid_url_error(self):
        with self.assertRaises(Exception) as context:
            raise InvalidURLError(url='not a url', scrape_id='crap id')
        self.assertTrue("'not a url'" in str(context.exception))

    def test_invalid_price_error(self):
        with self.assertRaises(Exception) as context:
            raise InvalidPriceError('ssdddjkdfjk')
        self.assertTrue("'ssdddjkdfjk'" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
