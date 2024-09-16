import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
import time
import os


def scrape_page(url):
    print(f"Scraping {url}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    hrefs = []
    category_groups = soup.find_all('div', class_='mw-category-group')
    for group in category_groups:
        lis = group.find_all('li')
        for li in lis:
            a_tag = li.find('a', href=True)
            if a_tag:
                hrefs.append(f"https://ro.wiktionary.org{a_tag['href']}")

    mw_pages = soup.find('div', id='mw-pages')
    next_page_url = None
    if mw_pages:
        next_page_link = mw_pages.find('a', string='pagina următoare', href=True)
        if next_page_link:
            next_page_url = urllib.parse.urljoin(url, next_page_link['href'])

    return hrefs, next_page_url


def append_to_json(file_path, data):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.extend(item for item in data if item not in existing_data)
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)


def main(start_url, file_path):
    all_hrefs = set()
    current_url = start_url

    open(file_path, 'w').close()

    while current_url:
        hrefs, next_page_url = scrape_page(current_url)
        new_hrefs = set(hrefs) - all_hrefs
        all_hrefs.update(new_hrefs)
        append_to_json(file_path, new_hrefs)
        current_url = next_page_url
        time.sleep(1)

    print(f"Links have been written to '{file_path}'")


start_url = 'https://ro.wiktionary.org/wiki/Categorie:Rom%C3%A2n%C4%83'
file_path = 'output.json'
main(start_url, file_path)
