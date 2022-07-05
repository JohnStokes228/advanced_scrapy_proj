"""
More basic, less shit? higher maintenance, more maintainable? what is truth, what is lies, what is this shit????

Try to maintain the positives of attempt 1 but address the shortfalls of the design. I think the major issues
were:
        - objects doing too much
        - too many class attributes got confusing
        - the init method got way out of hand
        - the saving method was utter shit
        - I got bored before I implemented the logger so probs see to that

good bits were:
        - tbh the crawler utility was pretty slick
        - i liked custom objects for cleaning that was nice
        - validator
        - scraper only existing to scrape shit
        - i wrote at least 2 unit tests which was chill i guess. more than 0 at least...
"""
from scrapy import Spider
from scrapy.utils.httpobj import urlparse
from typing import Optional, List

from spider_try_2.string_cleaning import StrTransformer


class QuotesToScrapeShelfSpider(Spider):
    def __init__(
            self,
            name: str,
            start_urls: str,
            allowed_domains: Optional[str] = None,
            manual_run: str = 'True',
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        allowed_domains : As with start urls, a comma separated list of allowed domains, to avoid over crawling.
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        """
        self.name = StrTransformer.clean_str(name)
        self.start_urls = StrTransformer.str_to_list(start_urls)

        if allowed_domains:
            self.allowed_domains = StrTransformer.str_to_list(start_urls)
        else:  # fill it with all provided domains if user doesn't want only a subset
            self.allowed_domains: List[str] = list(filter(None, [urlparse(url).netloc for url in self.start_urls]))

        self.manual_run = StrTransformer.str_to_boolean(manual_run)

        super(QuotesToScrapeShelfSpider, self).__init__(name=self.name,
                                                        start_urls=self.start_urls,
                                                        allowed_domains=self.allowed_domains)

    def start_requests(self):
        pass  # please give me data

    def parse(self, response, **kwargs):
        pass  # i said please oh please oh please


if __name__ == "__main__":
    test = QuotesToScrapeShelfSpider(name='Johno boii!! ', start_urls='https://www.realfakewebsites.com, wwww.lies.com')
    print(test.name)
    print(test.start_urls)
    print(test.allowed_domains)
    print(test.manual_run)