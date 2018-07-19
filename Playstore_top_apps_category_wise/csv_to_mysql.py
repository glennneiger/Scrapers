import MySQLdb
import sys

create_table = '''CREATE TABLE IF NOT EXISTS scraped_output (name VARCHAR(255) PRIMARY KEY, genre VARCHAR(255),Developer_name VARCHAR(255),Developer_link VARCHAR(255),Avg_rating DOUBLE,Total_reviews INT,Five_Star_ratings INT,Four_Star_ratings INT,Three_Star_ratings INT,Two_Star_ratings INT,One_Star_ratings INT,)'''
dbhost = "root@127.0.0.1:3306"
dbuser = "root"
dbpwd = "1408@Gmail"
dbdatabase = "advantedge_play_store"
db = MySQLdb.connect(user='root',password='1408@Gmail')
a='USE advantedge_play_store'
sql = 'INSERT INTO scraped_output (name,genre,dev_name,dev_link,avg_rating,five_star,four_star,three_start,two_star,one_star) VALUES ("vaibhav","Sharma","abc","efg",5.0,1,2,3,4,5)'
cur=db.cursor()
cur.execute(a)
print cur.execute(sql)
db.commit()