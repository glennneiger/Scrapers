"""
index_scraper.py is used to scrape the url of the top 500 apps listed in [opt].
imports:
requests : python inbuilt request library to send a web page request to the server.
bs4:Beautiful soup 4
"""

import requests
import bs4, time
from bs4 import BeautifulSoup

# category[] is list of url to a particular category
category = ['https://www.airbnb.com/s/New-York--NY?guests=2&checkin=09%2F09%2F2018&checkout=09%2F15%2F2018&search_by_map=true&sw_lng=-74.15053101169235&sw_lat=40.28249032559194&ne_lng=-73.15077515231735&ne_lat=41.132524449471795&zoom=10&ss_id=fc6429hj&ss_preload=true&source=bb&s_tag=PGDH1Zuz',
            'https://play.google.com/store/apps/collection/topselling_new_paid',
            'https://play.google.com/store/apps/category/GAME/collection/topselling_new_free',
            'https://play.google.com/store/apps/category/GAME/collection/topselling_new_paid']
# name[] is used just to add name[i] to diffrentiate files.
name = ['topselling_new_free', 'topselling_new_paid', 'topselling_new_free_games', 'topselling_new_paid_games']


def url_scraper(opt):
    # s = "index_topselling_new_free.html" or "index_topselling_new_paid.html"
    # the index file saves page containg apps according to the ranks i.e the listing page.
    s = 'index' + '_' + '.html'
    f = open(s, 'wb')
    f.close()

    for i in range(0,50, 2):
        # open the url of the listing page according to the value of [option].
        r = requests.post(str(category[opt - 1]),
                          data={'start': i, 'num': 50, 'numChildren': 0, 'ipf': 1, 'xhr': 1, 'hl': 'en'})
        # print(r.status_code,r.reason)
        f = open(s, 'a')
        f.write(str(r.text.encode('utf-8')))
        time.sleep(2)

    url = []
    f = open(s)
    # parse the index file
    soup = BeautifulSoup(f, 'html.parser')
    # the div tags conating the href attribute
    div = soup.find_all('div', class_="card-content id-track-click id-track-impression")
    for obj in div:
        a = obj.find('a', class_="card-click-target")
        url.append("https://play.google.com" + a['href'])
    return url
