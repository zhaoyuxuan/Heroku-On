import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor=conn.cursor()
cursor.execute("SELECT url FROM WEBSITE")
urls=cursor.fetchall()

def activate_website():
    rs = (grequests.get(u) for each in urls)
    grequests.map(rs)
    print("doing it")


activate_website()
