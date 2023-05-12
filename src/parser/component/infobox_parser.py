def parse_infobox_vcard(soup) -> dict:
    """
    Method that will parse a table of class infobox vcard from wikipedia

    :param soup:
    :return: See parse_wiki_table
    """
    tbl = soup.find("table", {"class": "infobox vcard"})
    return parse_wiki_table(tbl)


def parse_infobox_geography_vcard(soup) -> dict:
    """
    Method that will parse a table of class infobox geography vcard from wikipedia

    :param soup:
    :return: See parse_wiki_table
    """
    tbl = soup.find("table", {"class": "infobox geography vcard"})
    return parse_wiki_table(tbl)


def parse_wiki_table(tbl) -> dict:
    """
    Parse a wikipedia infobox table

    :param tbl:
    :return: a dict of property: value
    example: https://en.wikipedia.org/wiki/Louvre
    will return
    {
        "Established": "1793; 228 years ago",
        ...
    }
    """
    if tbl is None:
        return {}
    list_of_table_rows = tbl.findAll("tr")
    info = {}
    for tr in list_of_table_rows:

        th = tr.find("th")
        td = tr.find("td")
        if th is not None and td is not None:
            inner_text = ""
            for elem in td.recursiveChildGenerator():
                if isinstance(elem, str):
                    inner_text += elem.strip()
                elif elem.name == "br":
                    inner_text += "\n"
            info[th.text] = inner_text.replace("\xa0•\xa0", "")
    return info
