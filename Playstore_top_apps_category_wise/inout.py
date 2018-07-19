"""
The inout.py module is the input output module used to store th write the scrapeddata to csv and read from csv.
refer to the module index_scraper first.
"""
#category[] is list of url to a particular category
category = ['https://play.google.com/store/apps/collection/topselling_new_free','https://play.google.com/store/apps/collection/topselling_new_paid','https://play.google.com/store/apps/category/GAME/collection/topselling_new_free','https://play.google.com/store/apps/category/GAME/collection/topselling_new_paid']
# name[] is used just to add name[i] to diffrentiate files.
name=['topselling_new_free','topselling_new_paid','topselling_new_free_games','topselling_new_paid_games']

def read_URL_input(path):
	csv_file = open(path,'r')
	csv_file_reader =csv.reader(csv_file)
	for row in csv_file_reader:
		#print str(row[0])
		main(str(row[0]).encode('utf-8'))
#method having attributes: obj of class App,new flag,option choosen by user.
def write_scrapped_output(app,new,opt):
	s = 'scrapped_output_'+name[opt-1]+'.csv'
	if(new==1):
		csv_file = open(s,"w")
		csv_file.close()
	csv_file = open(s,'a')
	output_list = [app.name,app.genre,app.dev_name,app.dev_link,app.star_rating,app.num_of_reviews]
	for i in app.num_reviews_per_star:
		output_list.append(str(i).encode('utf-8'))
	# print output_list
	csv_file.write((",".join(output_list)+"\n").encode('utf-8'))