def parse_wikitable_sortable(soup):
    """
    Method that will parse a table of class wikitable sortable from wikipedia

    :param soup:
    :return: list of wikitable rows
    """
    table = soup.find("table", {"class": "wikitable sortable"})
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        if cols:
            data.append([ele for ele in cols if ele])

    return data


def parse_wikitable_for_assignment(soup):
    """
    Parse the wikitable of the page https://en.wikipedia.org/wiki/List_of_most-visited_museums
    for the assignment

    :param soup:
    :return:
    {
        "museum_wiki_page": STRING,
        "museum_name": STRING,
        "country": STRING,
        "city": STRING,
        "visitors": STRING
    }
    """
    table = soup.find("table", {"class": "wikitable sortable"})
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        if cols:
            link_museum_name = cols[0].find_all("a")
            museum_wiki_page = link_museum_name[0]["href"]
            museum_name = link_museum_name[0]["title"]

            links_country_city = cols[1].find_all("a")
            country = links_country_city[0]["title"]
            city = links_country_city[1]["title"]

            visitors = cols[2].text.strip()

            data.append(
                {
                    "museum_wiki_page": museum_wiki_page,
                    "museum_name": museum_name,
                    "country": country,
                    "city": city,
                    "visitors": visitors
                }
            )

    return data
