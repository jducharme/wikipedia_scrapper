import qwikidata
import qwikidata.sparql


def get_city_population(city, country):
    """
    https://stackoverflow.com/questions/42335273/python-getting-the-population-of-a-city-given-its-name
    :param city:
    :param country:
    :return: The population value as an int
    """
    query = """
    SELECT ?city ?cityLabel ?country ?countryLabel ?population
    WHERE
    {
      ?city rdfs:label "%s"@en.
      ?city wdt:P1082 ?population.
      ?city wdt:P17 ?country.
      ?city rdfs:label ?cityLabel.
      ?country rdfs:label ?countryLabel.
      FILTER(CONTAINS(?countryLabel, "%s")).
    }
    """ % (city, country)

    res = qwikidata.sparql.return_sparql_query_results(query)
    out = res['results']['bindings'][0]
    return int(out["population"]["value"])
