from bs4 import BeautifulSoup
from parser.component import infobox_parser


def parse_museum(html_page):
    """
    Parser for a museum wikipedia page.
    example: https://en.wikipedia.org/wiki/Louvre
    It will take the infobox and extract some of its information

    :param html_page: the raw html of the page we want to parse
    :return: returns an dict
    {
        "established": STRING,
        "location": STRING,
        "type": STRING,
        "director": STRING,
        "curator": STRING,
        "website": STRING
    }
    """
    soup = BeautifulSoup(html_page, 'html.parser')
    museum = infobox_parser.parse_infobox_vcard(soup)

    established = ""
    if museum.get("Established"):
        established = museum.get("Established").split(";")[0]

    return {
        "established": established,
        "location": museum.get("Location"),
        "type": museum.get("Type"),
        "director": museum.get("Director"),
        "curator": museum.get("Curator"),
        "website": museum.get("Website")
    }
