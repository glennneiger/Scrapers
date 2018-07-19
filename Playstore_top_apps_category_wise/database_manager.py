import MySQLdb
import sys
import play_store_scraper
name=['topselling_new_free','topselling_new_paid','topselling_new_free_games','topselling_new_paid_games']
def insert2db(fetched , new,opt):
	s=name[opt-1]
	dbhost = "root@127.0.0.1:3306"
	dbuser = "root"
	dbpwd = "1408@Gmail"
	dbdatabase = "advantedge_play_store"
	db = MySQLdb.connect(user='root',password='1408@Gmail')
	a='CREATE DATABASE IF NOT EXISTS advantedge_play_store'
	b='USE advantedge_play_store'
	cur=db.cursor()
	cur.execute(a)
	cur.execute(b)
	
	create = '''CREATE TABLE IF NOT EXISTS '''+s+''' (Rank INT NOT NULL,Url VARCHAR(255) PRIMARY KEY,Name VARCHAR(255) , Genre VARCHAR(255),Developer_name VARCHAR(255),Developer_link VARCHAR(255),Avg_rating DOUBLE,Total_reviews INT,Five_Star_ratings INT,Four_Star_ratings INT,Three_Star_ratings INT,Two_Star_ratings INT,One_Star_ratings INT)'''
	cur.execute(create)
	db.commit()
	
	for app in fetched:
		list = (app.rank,(app.url).encode('ascii',errors='ignore').decode('ascii'),(app.name).encode('ascii',errors='ignore').decode('ascii'),(app.genre).encode('ascii',errors='ignore').decode('ascii'),(app.dev_name).encode('ascii',errors='ignore').decode('ascii'),(app.dev_link).encode('ascii',errors='ignore').decode('ascii'),float(app.star_rating),int(app.num_of_reviews),int(app.num_reviews_per_star[0]),int(app.num_reviews_per_star[1]),int(app.num_reviews_per_star[2]),int(app.num_reviews_per_star[3]),int(app.num_reviews_per_star[4]))
		# print list
		p = 'Select *from '+s+' WHERE Url=%s'
		row_count = cur.execute(p,[(app.url).encode('ascii',errors='ignore').decode('ascii')])
		
		if(row_count==0):
		 	sql = 'INSERT INTO '+s+' (Rank,Url,Name,Genre,Developer_name,Developer_link,Avg_rating,Total_reviews,Five_Star_ratings,Four_Star_ratings,Three_Star_ratings,Two_Star_ratings,One_Star_ratings) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		 	cur.execute(sql,list)
		 	db.commit()
		else:
		 	sql = 'UPDATE '+s+' SET Rank=%s,Url=%s,Name=%s,Genre=%s,Developer_name=%s,Developer_link=%s,Avg_rating=%s,Total_reviews=%s,Five_Star_ratings=%s,Four_Star_ratings=%s,Three_Star_ratings=%s,Two_Star_ratings=%s,One_Star_ratings=%s '+'WHERE Url=%s'
		 	list1 = list + ((app.url).encode('ascii',errors='ignore').decode('ascii'),)
		 	cur.execute(sql,list1)
		 	
		print len((app.url[0:56]).replace('.','_')) 	
		create_app = 'CREATE TABLE IF NOT EXISTS '+(app.url[0:56]).replace('.','_')+' (Time_of_fetch TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,Rank INT NOT NULL,Url VARCHAR(255),Name VARCHAR(255),Genre VARCHAR(255),Developer_name VARCHAR(255),Developer_link VARCHAR(255),Avg_rating DOUBLE,Total_reviews INT,Five_Star_ratings INT,Four_Star_ratings INT,Three_Star_ratings INT,Two_Star_ratings INT,One_Star_ratings INT,FOREIGN KEY (Url) REFERENCES '+s+'(Url))'
		cur.execute(create_app)
		db.commit()
		
		insert_into_app_table = 'INSERT INTO '+(app.url[0:56]).replace('.','_')+' (Rank,Url,Name,Genre,Developer_name,Developer_link,Avg_rating,Total_reviews,Five_Star_ratings,Four_Star_ratings,Three_Star_ratings,Two_Star_ratings,One_Star_ratings) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		cur.execute(insert_into_app_table,list)
		db.commit()
		print list		
		db.commit()
	
# params = ['?' for item in list]
#   sql    = 'INSERT INTO table (Col1, Col2. . .) VALUES (%s);' % ','.join(params)
#   conn.execute(sql, list)