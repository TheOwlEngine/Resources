# ----------------
# Required Library
# ----------------

import json
import requests

from bs4 import BeautifulSoup

# --------------------
# Getting The Web Page
# --------------------

web_url  = 'https://www.worldwildlife.org/species/orangutan'
web_page = requests.get(web_url)
web_text = web_page.content

# -------------------
# Parsing Web Content
# -------------------

soup = BeautifulSoup(web_text, 'html.parser')

animal_banner     = soup.select_one('[data-picture] img')
animal_excerpt    = soup.select_one('#overview p')
animal_overview   = soup.select('.section-pop p')
animal_statistics = soup.select('.list-stats li')

# -------------------
# Defining Dictionary
# -------------------

result = {
    'main_image': '',
    'excerpt'   : '',
    'detail'    : '',
    'statistics': {},
}

# -----------------------------
# Saving Result into Dictionary
# -----------------------------

result['main_image'] = animal_banner['src']

result['excerpt'] = animal_excerpt.text

for detail in animal_overview:
    result['detail'] += detail.text

for stat in animal_statistics:
    category = stat.find('strong').text.strip()
    information = stat.find('div').text.strip()

    result['statistics'][category] = information

# ----------------
# Print the Result
# ----------------

print(json.dumps(result, indent=4))