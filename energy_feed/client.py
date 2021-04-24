import json
import pathlib
from typing import List
from typing import Union
from energy_feed.news_feed import NewsFeed

class EnergyFeedClient():

    def news_feed(self) -> NewsFeed:
        """Represents the `NewsFeed` service.

        ### Returns
        ----
        NewsFeed
            The news feed report service.
        """

        return NewsFeed()

    def save_reports(self, reports: List, path: Union[str, pathlib.Path]) -> None:
        """Takes the reports and saves them to the specified path as a JSON file.

        ### Parameters
        ----
        report: List
            The parsed URLs and report info.

        path: Union[str, pathlib.Path]
            Either a string pointing to the path
            or a `Path` object.

        ### Usage
        ----
            >>> scraper = ScraperClient()
            >>> scraper.save_reports(
                reports=[
                    {
                        'date': 'April 1, 2021',
                        'link': 'https://www.eia.gov/todayinenergy/detail.cfm?id=47376',
                        'title': 'State gasoline taxes average about 30 cents per gallon'
                    }
                ],
                path="/data/my_reports.json"
            )
        """

        # Make sure we have a Path object.
        if isinstance(path, pathlib.Path):
            path = path
        elif isinstance(path, str):
            path = pathlib.Path(path)
        else:
            raise ValueError("Path must be a str or a Path object.")

        with open(file=path, mode='w+') as report_file:
            json.dump(obj=reports, fp=report_file, indent=2)
