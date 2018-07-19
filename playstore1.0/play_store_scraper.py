"""Play Store Scrapper.
This module scrapes a Google Play Store page of a particular App,provided the URL to the page.It scrapes the page for the attributes: 1.Name of the app 2.Genre of the App 3.Name of the developer 4.Link to the developer 5.Raiting of the app 6.NUmber of reviews App has recieved 7.Number of raitings for each star

Example:
	Name of the App: Sniper Arena: PvP Army Shooter
	Genre of the App: Action
	Name of the developer: Nordcurrent
	Link to the developer page: https://play.google.com/store/apps/dev?id=6790926766572360607
	Rating of the app: Rated 4.4 stars out of five stars
	Number of reviews app have: 201,594
	Number of raitings for each star:
		1 star "15574"
		2 star "3775"
		3 star "12775"
		4 star "31781"
		5 star "137689"
Libraries:
	This module is built using python development libraries Beautiful soup and urllib2.The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world basic and digest authentication, redirections, cookies.

	urllib2.urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]])
	Open the URL url, which can be either a string or a Request object.

	Beautiful Soup is a Python library for pulling data out of HTML and XML files. It provide idiomatic ways of navigating, searching, and modifying the parse tree. 
Class:
	The class App bundles the scraped data to instance.
	The class diagram for the following:
		---------------------------|
		|	        App            |
		|--------------------------|
		|      +name:String        |
		|      +genre:String       |
		|     +dev_name:String     |
		|     +dev_link:String     |
		|   +num_of_reviews:String |
		|    +star_raiting:String  |
		|+num_of_reviews_per_star  |
		|                 :list    |
		|--------------------------|
		|   +app_details()         |
		|  +developer_details()    |   
		|   +app_rating()          |
		|  +reviews_per_star()     |
		|--------------------------|

"""

import pyautogui
from bs4 import BeautifulSoup
import csv
from csv import reader
import requests
import sys
import re

class App:
	def rank(self,rank):
		self.rank = rank
	def url(self,u):
		self.url = u
	def app_details(self,name,genre):
		self.name = name
		self.genre = genre
	
	def developer_details(self,dev_link,dev_name):
		self.dev_name = dev_name
		self.dev_link = dev_link
	
	def app_rating(self,star_rating,num_of_reviews):
		self.num_of_reviews = num_of_reviews
		self.star_rating = star_rating
	
	def reviews_per_star(self,num_reviews_per_star):
		self.num_reviews_per_star = num_reviews_per_star
	
	"""def __str__(self):
		print("Url of the app:",self.url)
		print("Name of the App:",self.name)
		print("Genre of the App:",self.genre)
		print("Name of the developer:",self.dev_name)
		print("Link to the developer page:",self.dev_link)
		print("Rating of the app:",self.star_rating)
		print("Number of reviews app have:",self.num_of_reviews)
		print("Number of raitings for each star:")
		index=1
		for i in self.num_reviews_per_star:
			print ("\t",index,"star",i)
			index+=1
			"""
			
		return "------------------"


def scrape(url):
	fetched=[]
	count = 1
	for i in url:
		# print (i.split('id=',1)[1])
		try:
			page = requests.get(i)
			page=page.text
			soup = BeautifulSoup(page,'html.parser')

			#instance of class App
			app=App()
			u=i.split('id=',1)
			app.url(u[1])
			#Block = tag or div used to define an attribute
			#finding the name block 
			name_block = soup.find('div',attrs={'class':'sIskre'})
			#finding the tag containing name attribute in name block.
			name = name_block.find('h1',attrs={'class':'AHFaub'})
			name = name.text.strip()
			name = name.encode('ascii',errors='ignore')
			#finding the developer block containg developer's url, developer's name and app genre 
			developer = name_block.find('div',class_ = 'i4sPve') # find method returns the complete tag having class="xyz"
			genre = developer.find("a",itemprop="genre")
			#finding nested tag containing hyperlink to developer page and developer name
			link_block = developer.find("a")
			dev_link = link_block["href"]
			dev_name = link_block.text
			
			rating_tag = soup.find('div',class_='dNLKff') # the first div tag contains the rating of the app 
			#try and except statements are used as some new apps don't have a raiting or review yet
			try:
				star_rating = rating_tag.find('div',class_='pf5lIe')
				star_rating = star_rating.find('div')
				star_rating = star_rating['aria-label']
				star_rating = float(star_rating[6:9])
			except:
				star_rating = 0

			#finding the rating block
			try:
				rating = soup.find_all('div',class_="W4P4ne")
				rating = rating[1]

				#Block containg total number of reviews
				num_of_reviews_block = rating.find("span",class_="EymY4b")
				num_of_reviews = num_of_reviews_block.find_all("span")
				num_of_reviews = num_of_reviews[1]
				num_of_reviews = num_of_reviews.text
				num_of_reviews = int(num_of_reviews.replace(',',''))
				#print (num_of_reviews)
				
				# print ("Number of ratings: "+num_of_reviews.text)

				# finding the table containg detailed raiting
				detailed_rating = soup.find('div',class_="VEF2C")
				#the table contains multiple div tags.One for each star raiting
				div = detailed_rating.find_all('div')
				#print ("Number of ratings for each star:")
				num_reviews_per_star = []
				for obj in div:
					b = obj.find_all("span")
					num_reviews_per_star.insert(0,int(str(int(b[1]['title'].replace(',','')))))
			except:
				num_of_reviews = 0
				num_reviews_per_star = [0,0,0,0,0]

			app.app_details(name,genre.text)	# strip() is used to remove starting and trailing
			app.developer_details(dev_link,dev_name)
			app.app_rating(star_rating,num_of_reviews)
			app.reviews_per_star(num_reviews_per_star)
			app.rank(count)
			print(count)
			print(app)
			fetched.append(app)
		except AttributeError as e:
		 	# print (count)
			# count=count+1
			# print('URL SKIPPED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			# print(e)
			continue
		count = count+1
	return fetched
