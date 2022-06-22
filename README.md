# advanced_scrapy_proj
playing with some more advanced methods in scrapy.

#TODO:

Previously I've produced various web craping codes of varying degrees of shittiness. I'd like to see how much better I can produce similar software with my current understanding, and also to get a chance to play with some additional packages / features I've seen knocking about online. the main new things I plan to do with this project are:

- avoid use of selenium for interaction with javascript, I'd prefer a more lightweight solution.
- potentially use of item pipelines, or pydantic integration for data validation. look into which ends up better as not convinced on items tbh...
- integration with a database, likely some kind of cloud based NOSQL database i think. If cloud is the direction we go for this, it would be nice to look at what other native tools and patterns we can utilise. 
- deeper logging for monitoring scrapes
- more use of scrapys in built tools rather than building alot of the session settings etc... manually. may not be an improvement but id liek to get more familiar with them
- Ive seen some ML based extensions for improving pagination and xpathing that id really like to try, assuming they dont have a huge negative impact on runtime.
- a better consideration towards how to keep the code as testable as possible would be an improvement compared to before too


the actual web scrapers themselves are of less interest here, im generally much more interested in the surrounding infastrucutre. to that end we'll just be scraping the classic dummy sites:

- https://books.toscrape.com/
- https://quotes.toscrape.com/

And probably some of their more complicated offshoots. Lets see how long it takes to pull it together shall we
