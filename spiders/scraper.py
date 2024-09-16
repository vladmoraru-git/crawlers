import requests
from bs4 import BeautifulSoup
import json

url = 'https://ro.wiktionary.org/w/index.php?title=Categorie:Rom%C3%A2n%C4%83&pageuntil=zarzavat#mw-pages'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

category_group = soup.find_all('div', class_='mw-category-group')

hrefs = []

for group in category_group:
    lis = group.find_all('li')
    for li in lis:
        a_tag = li.find('a', href=True)
        if a_tag:
            hrefs.append(f"{a_tag['title']}")

with open('output.json', 'w') as file:
    json.dump(hrefs, file, indent=4)

print("Links have been written to 'links.json'")
