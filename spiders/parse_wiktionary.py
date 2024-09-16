import os
import urllib.parse
import json
from output2 import URL

output_folder = 'outputparsed'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

diacritics_map = {
    'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't',
    'Ă': 'A', 'Â': 'A', 'Î': 'I', 'Ș': 'S', 'Ț': 'T'
}

def replace_diacritics(text):
    for diacritic, replacement in diacritics_map.items():
        text = text.replace(diacritic, replacement)
    return text

def extract_last_word(url):
    parsed_url = urllib.parse.unquote(url)
    last_word = os.path.basename(parsed_url)
    last_word = replace_diacritics(last_word)
    if len(last_word) == 5:
        return last_word
    return None

last_words = [extract_last_word(url) for url in URL if extract_last_word(url) is not None]

output_file = os.path.join(output_folder, '5letterwords.json')
with open(output_file, 'w') as file:
    for word in last_words:
        file.write(f"('{word}'),\n")

print(f"5-letter words have been written to {output_file}")
