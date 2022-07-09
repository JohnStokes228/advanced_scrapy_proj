"""
More basic, less shit? higher maintenance, more maintainable? what is truth, what is lies, what is this shit????

I'm going to scrape a live site called cinch this time mostly because im feeling cheeky. Originally I'd intended to
scrape the 'quotes to scrape' site as it has some JS elements that would've made it more interesting but unfortunately
the entire site is easily accessible via API which would make any kind of actual scrapy use invalid really.

TODO:
    - consider using the sitemap? -> can we use this to further filter our results?
    - add ability to alter results of api further
    - consider logging
    - save the output data to DB somewhere
    - tidy up some (most) of the code
    - build the cmd interface for the spider
"""
import time
import random

from scrapy import Spider
from scrapy.utils.httpobj import urlparse
from typing import Optional, List, Annotated
from annotated_types import Gt

from spider_try_2.string_cleaning import StrTransformer
from spider_try_2.api_request import CinchRequester
from spider_try_2.data_model import VehicleListing


class CinchShelfSpider(Spider):

    def __init__(
        self,
        name: str,
        start_urls: List[str],
        manual_run: bool,
        allowed_domains: Optional[List[str]] = None,
        start_page: Annotated[int, Gt(0)] = 1,
        end_page: int = 10
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        allowed_domains : As with start urls, a comma separated list of allowed domains, to avoid over crawling.
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        start_page : Page to start scraping.
        end_page : Page to finish the scrape on.
        """
        super(CinchShelfSpider, self).__init__(name=name,
                                               start_urls=start_urls,
                                               allowed_domains=allowed_domains)  # do we need allowed domains at all?
        self.manual_run = manual_run  # this needs using in like the logger or someshit
        self.start_page = start_page
        self.end_page = end_page
        self.requester = CinchRequester(
            url="https://search.api.cinch.co.uk/vehicles?pageNumber=",
            headers={'authority': 'search.api.cinch.co.uk'},
        )

    def start_requests(self):
        for url in self.start_urls:
            for i in range(self.start_page, self.end_page):  # is there a nicer way to create this request swarm?
                yield Request(url=url, callback=self.parse, meta={'page_no': str(i)})

    def parse(self, response, **kwargs):
        time.sleep(random.randint(0, 3) + random.random())  # throttle requests
        response = self.requester.make_request(endpoint_spec=response.meta.page_no)
        response = {key: value for key, value in response.items() if key != 'facets'}  # uggo blech

        for vehicle in response['vehicleListings']:  # what if it doesn't exist?
            vehicle['pageNumber'] = response['pageNumber']  # what if this doesn't exist too
            vehicle['spiderName'] = self.name
            vehicle['manualRun'] = self.manual_run  # these three lines ^^ should be automated somewhere.
            vehicle = VehicleListing(**vehicle)  # should probs do something to save raw, incase doesn't fit the model?
            print(vehicle)  # save it to db somewhere.


if __name__ == "__main__":
    spider_name = StrTransformer.clean_str('Johno boii!! ')
    spider_start_urls = StrTransformer.str_to_list('https://www.realfakewebsites.com, wwww.lies.com')
    spider_manual_run = StrTransformer.str_to_boolean('True')

    spider_allowed_domains = ['https://www.amazing_site-yeah_baby.com/clothes/hats/longest-of-all-hats']
    if not spider_allowed_domains:
        spider_allowed_domains: List[str] = list(filter(None, [urlparse(url).netloc for url in spider_start_urls]))
    # refactor ^^ into command line argument module later

    test = CinchShelfSpider(
        name=spider_name,
        start_urls=spider_start_urls,
        manual_run=spider_manual_run,
        allowed_domains=spider_allowed_domains
    )
    print(test.name)
    print(test.start_urls)
    print(test.allowed_domains)
    print(test.manual_run)
