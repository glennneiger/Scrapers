"""
index_scraper.py is used to scrape the url of the top 500 apps listed in [opt].
imports:
requests : python inbuilt request library to send a web page request to the server.
bs4:Beautiful soup 4
"""

import requests
import bs4,time
from bs4 import BeautifulSoup
#category[] is list of url to a particular category
category = ['https://play.google.com/store/apps/collection/topselling_new_free','https://play.google.com/store/apps/collection/topselling_new_paid','https://play.google.com/store/apps/category/GAME/collection/topselling_new_free','https://play.google.com/store/apps/category/GAME/collection/topselling_new_paid']
#name[] is used just to add name[i] to diffrentiate files.
name=['topselling_new_free','topselling_new_paid','topselling_new_free_games','topselling_new_paid_games']
def url_scraper(opt):
	#s = "index_topselling_new_free.html" or "index_topselling_new_paid.html"
	#the index file saves page containg apps according to the ranks i.e the listing page.
	s = 'index'+'_'+name[opt-1]+'.html'
	f=open(s,'wb')
	f.close()

	for i in range(0,500,50):
		#open the url of the listing page according to the value of [option].
		r = requests.post(category[opt-1],data = {'start':i,'num':50,'numChildren':0,'ipf':1,'xhr':1,'hl':'en'})
		# print(r.status_code,r.reason)
		f = open(s,'a')
		f.write(r.text.encode('utf-8'))
		time.sleep(2)


	url = []
	f = open(s)
	#parse the index file
	soup = BeautifulSoup(f,'html.parser')
	#the div tags conating the href attribute
	div = soup.find_all('div',class_= "card-content id-track-click id-track-impression")
	for obj in div:
		a=obj.find('a',class_="card-click-target")
		url.append("https://play.google.com"+a['href'])
	return url
