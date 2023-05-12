from bs4 import BeautifulSoup
from parser.component import wikitable_parser

MUSEUM_NAME = 0
MUSEUM_CITY = 1
MUSEUM_VISITORS = 2


def parse_list_of_most_visited_museums(html_page):
    """
    This parser will parse https://en.wikipedia.org/wiki/List_of_most-visited_museums
    and return a list of dict with the museum name, it's city and how many visitors it had.

    :param html_page: the raw html of the page we want to parse

    :return: list of dict
    {
        "museum": STRING,
        "museum_wiki_page": STRING,
        "city": STRING,
        "country": STRING,
        "visitors": INT
    }
    """
    soup = BeautifulSoup(html_page, 'html.parser')
    wikitable = wikitable_parser.parse_wikitable_for_assignment(soup)
    data = []
    for d in wikitable:
        data.append({"museum": d["museum_name"],
                     "museum_wiki_page": d["museum_wiki_page"],
                     "city": d["city"],
                     "country": d["country"],
                     # In the wikitable they use , to delimit their numbers. Remove it to have a proper number
                     "visitors": int(d["visitors"].replace(",", ""))})
    return data
