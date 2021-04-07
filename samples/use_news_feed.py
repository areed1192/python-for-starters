from pprint import pprint
from energy_feed.enums import Months
from energy_feed.client import EnergyFeedClient

# Initialize the client.
scraper_client = EnergyFeedClient()

# Initialize the `NewsFeed` service.
news_feed_service = scraper_client.news_feed()

# Grab the Articles for the month of April.
pprint(news_feed_service.today_in_energy(month='Apr', year=2021))

# Grab another month but this time use the enums.
pprint(news_feed_service.today_in_energy(month=Months.December, year=2020))
