import requests
from bs4 import BeautifulSoup
import json

def scrape_page(url):
    print(f"Scraping {url}")
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
                hrefs.append(f"https://ro.wiktionary.org{a_tag['href']}")

    next_page_link = soup.find('a', title='Categorie:Română', href=True)
    if next_page_link and 'mw-pages' in next_page_link['href']:
        next_page_url = f"https://ro.wiktionary.org{next_page_link['href']}"
        return hrefs, next_page_url

    return hrefs, None

start_url = 'https://ro.wiktionary.org/wiki/Categorie:Rom%C3%A2n%C4%83'

all_hrefs = []

current_url = start_url
while current_url:
    hrefs, next_url = scrape_page(current_url)
    all_hrefs.extend(hrefs)
    current_url = next_url

with open('discovery.json', 'w') as file:
    json.dump(all_hrefs, file, indent=4)

print("discovery.json")
