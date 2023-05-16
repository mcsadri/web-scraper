import parse as parse
import requests
from bs4 import BeautifulSoup
import parse


url = "https://en.wikipedia.org/wiki/Star_Trek"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

italics_results = soup.find_all(title="Wikipedia:Citation needed")

for element in italics_results:
    date = parse.search("({})", element.span)
