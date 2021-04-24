# https://www.eia.gov/petroleum/gasdiesel/includes/gas_diesel_rss.xml

import requests
from enum import Enum
from typing import List
from typing import Union
from energy_feed.parser import EnergyReportParser


class NewsFeed():

    def __init__(self) -> None:
        """Initializes the `NewsFeed` service."""
        
        self._parser = EnergyReportParser()
        self.base_url = 'https://www.eia.gov/todayinenergy/archive.php?my='
    
    def today_in_energy(self, month: Union[str, Enum], year: int) -> List:
        """Short, timely articles with graphics on energy facts, issues,
        and trends.

        ### Parameters
        ----
        month: Union[str, Enum]
            The month you want to query.

        year: int
            The year you want to query.

        ### Returns
        ----
        List
            A list of `Article` resources.
        """        
        
        # Deal with enums.
        if isinstance(month, Enum):
            month = month.value

        month_id = month + str(year)
        response = requests.get(url=self.base_url + month_id)

        if response.ok:
            return self._parser.parse_rss_update(
                content=response.text
            )
        else:
            raise requests.HTTPError()
