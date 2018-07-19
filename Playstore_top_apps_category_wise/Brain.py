"""
Brain.py is the controlling unit of the Play Store Scraper project.The modules used by url and their usage is listed below:
1.play_store_scraper : Library to scrape the page of the app.
2.inout : The I/O moudule to read/write from/into a CSV.
3.index_scraper : Scrapes the URL of top 500 listing in the category [option].
4.time : (optional) inbuilt python module to measure runtime.
"""

import play_store_scraper
import inout
import index_scraper
import time
import database_manager
opt = input('Choose the category you want to scrap:\n1.Top New Free Android Apps\n2.Top New Paid Android Apps\n3.Top New Free Games\n4.Top New Paid Games\n')
# opt=1
url = index_scraper.url_scraper(opt) #Call to the method with the selected option as pass by value.The return type is a list of url.The i-th url i.e url[i] references to page of the application ranked i in the list.  
# print 'url_fetched',len(url) 
# for i in url:
# 	print i
# for i in url:
# 	print i,count
# 	count = count+1
# start = time.time()
fetched = play_store_scraper.scrape(url) #The scrape() method scrapes the data for each url listed in url[].The return type of the method is a list fetched[],of objects of class App(refer to module play_store_scraper). 
new = 1 #first write
database_manager.insert2db(fetched,new,opt);
# for app in fetched:
# 	# print 'new',new
# 	 inout.write_scrapped_output(app,new,opt) #writes each scraped object to csvfile.The newflag determines whether it's the first write to file or not.
# 	 new = 0 #once first write is complete new flag is set to zero
# 	 print app

# print time.time()-start



