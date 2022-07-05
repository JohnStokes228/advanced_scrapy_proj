# advanced_scrapy_proj
playing with some more advanced methods in scrapy.

# stack used:

- scrapy Crawler for crawling
- twisted reactor by default for juggling spiders
- pydantic basemodel for validation
- BS4 for html parsing
- *playwright* for javascript? investigate need for drivers at all
- what for logging?
- what for database? assume some kind of nosql solution but what?

# thoughts on features:

Previously I've produced various web scraping codes of varying degrees of shittiness. I'd like to see how much better I can produce similar software with my current understanding, and also to get a chance to play with some additional packages / features I've seen knocking about online. the main new things I plan to do with this project are:

- Ive seen some ML based extensions for improving pagination and xpathing that id really like to try, assuming they dont have a huge negative impact on runtime.
- a better consideration towards how to keep the code as testable as possible would be an improvement compared to before too
- careful thought to code composition for reusability and readability

# target sites:

the actual web scrapers themselves are of less interest here, im generally much more interested in the surrounding infastrucutre. to that end we'll just be scraping the classic dummy sites:

- https://books.toscrape.com/
- https://quotes.toscrape.com/

And probably some of their more complicated offshoots. Let's see how long it takes to pull it together shall we

# criticism:

- don't like the way im using pydantic at all really, feels like wires are crossed between validation and transformation of inputs.
- in general although i set out thinking pydantic would be a huge improvement i've come away not so convinced its worth its own runtime. there's a fair bit of tip-toeing around its behaviours required to get it working properly and not generally convinced that we wouldn't be better off with a more lightweight, manually designed solution.
- not sure on use of BS4 during the scraping - it's quick to get running and works well but feels like it just adds to the stack without necessarily improving the output.
- the spiders' \_\_init__ method feels overstuffed and somewhat hard to read. possibly would've been better to edit the source code of the crawler to include the act of saving?
- the data saving being on a per item level works in some ways but not convinced it's necessarily the best method, and results in a lot of outputs which presumably slows the code a fair bit.
- some custom objects are half-baked and probably buggy in reality, though I do like the composition with object validation being used to transform and pydantic then preforming the coercion.
- including a pause of up to 3 seconds after every scraped item feels like overkill and substantially slows the scrape down. need to find a reliable way to get per object scraped with minimal requests in order to cut down on downtime.
- current composition doesn't allow for easy reuse of the \_\_init__ logic for the spiders. If this was considered a template that wouldn't be a huge issue but if it were instead considered the basis of a larger project then that would lead to alot of code duplication over time.

to start to address these ive begun work on spiders_try_2 which will hopefully be less shit. maybe by try 5 it'll be at least ok?