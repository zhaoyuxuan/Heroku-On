import os
import psycopg2
import urllib.parse
import grequests

urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
#conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor=conn.cursor()
cursor.execute("SELECT url FROM WEBSITE;")
urls=cursor.fetchall()
print(urls)

def activate_website():
    rs = (grequests.get(each[0]) for each in urls)
    grequests.map(rs)
    print("doing it")


activate_website()
