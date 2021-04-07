from bs4 import Tag
from bs4 import BeautifulSoup
from typing import List


class EnergyReportParser():

    def __init__(self) -> None:
        pass

    def parse_rss_update(self, content: str) -> List:
        """Parses the RSS Articles Feed.

        ### Parameters
        ----
        content : str
            The HTML content as string.

        ### Returns
        ----
        List
            A list of article resources.
        """

        article_list = []

        # Parse the content.
        soup = BeautifulSoup(markup=content, features='html.parser')
        desc = soup.find(name='div', attrs={'class': 'white_box green_top'})

        # Find all the articles.
        articles = desc.find_all(name='h2')

        for article in articles:

            # Parse the content.
            a_tag: Tag = article.find('a', href=True)
            article_link = 'https://www.eia.gov/todayinenergy/' + a_tag['href']
            article_title = a_tag.text.strip()
            article_date = a_tag.find_previous(name='span').text

            article_record = {
                'link': article_link,
                'title': article_title,
                'date': article_date
            }

            article_list.append(article_record)

        return article_list
