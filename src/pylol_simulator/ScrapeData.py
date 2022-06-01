import re

import requests
from bs4 import BeautifulSoup


def scrape_url_for_items_from_wiki(url):
    # Source: https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    lines = soup.prettify().split("\n")
    out = False
    items = []
    for i in range(len(lines)):
        line = lines[i]
        if "<ul>" in line and not out:
            out = True
            continue
        if "</ul>" in line and out:
            break
        if out:
            if "<img alt=" in line:
                pattern = re.compile("alt=\"[^\"]*")
                pngs = pattern.findall(line.strip())
                if len(pngs) == 0:
                    continue
                png = re.sub("item", "", re.sub("\"", "", re.sub("\\.png", "", pngs[0].split("=")[1]))).strip()
                items.append(png)
    return items


def scrape_mythic_items_from_wiki():
    # https://leagueoflegends.fandom.com/wiki/Mythic_item
    return scrape_url_for_items_from_wiki("https://leagueoflegends.fandom.com/wiki/Mythic_item")


def scrape_legendary_items_from_wiki():
    # https://leagueoflegends.fandom.com/wiki/Legendary_item
    return scrape_url_for_items_from_wiki("https://leagueoflegends.fandom.com/wiki/Legendary_item")
