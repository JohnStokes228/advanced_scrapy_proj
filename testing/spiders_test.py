import unittest
from spiders.spiders import BooksToScrapeSpider


class TestBooksToScrape(unittest.TestCase):
    def test_name_translation(self):
        testcase = BooksToScrapeSpider(name='wow, very fantastic body!!', start_urls='dfs')
        self.assertEqual(testcase.name, 'wow_very_fantastic_body')

    def test_start_urls_negative_case(self):
        testcase = BooksToScrapeSpider(name='5', start_urls='adas,ada')
        with self.assertRaises(TypeError):
            testcase.start_urls = 12321

    def test_start_urls_positive_case(self):
        testcase = BooksToScrapeSpider(name='5', start_urls='adas,ada')
        self.assertEqual(testcase.start_urls, ['adas', 'ada'])


if __name__ == '__main__':
    unittest.main()
