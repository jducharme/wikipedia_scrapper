from parser.most_visited_museum_parser import parse_list_of_most_visited_museums
from parser.museum_parser import parse_museum
from commons.wikidata import get_city_population
from commons.bigqueury_saver import save_museum

import json
import requests

most_viewed_museums_response = requests.get(
    url="https://en.wikipedia.org/w/api.php?action=parse&prop=text&page=List_of_most-visited_museums&format=json")
html_page = json.loads(most_viewed_museums_response.content)["parse"]["text"]["*"]
most_viewed_museums = parse_list_of_most_visited_museums(html_page)

# Create a cache mechanism to not call twice the wikidata api
cities = {}

for museum in most_viewed_museums:
    museum_url = f"https://en.wikipedia.org{museum.get('museum_wiki_page')}"
    parsed_museum = parse_museum(requests.get(url=museum_url).content)

    if museum["city"] in cities:
        city_population = cities[museum["city"]]
    else:
        city_population = get_city_population(museum["city"], museum["country"])
        cities[museum["city"]] = city_population

    museum["city_population"] = city_population
    museum["type"] = parsed_museum.get("type")
    museum["director"] = parsed_museum.get("director")
    museum["curator"] = parsed_museum.get("curator")
    museum["website"] = parsed_museum.get("website")

# keep the file creation
with open("data.json", "w") as file:
    for m in most_viewed_museums:
        file.write(json.dumps(m) + "\n")
save_museum(most_viewed_museums)
