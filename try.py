import psycopg2
import sys
import validators

print(validators.url("https://validators.readthedocs.io/en/latest/", public=False))



conn = psycopg2.connect(host="ec2-23-21-220-32.compute-1.amazonaws.com",database="dbct8eg95erdn7", user="piijiioaookene", password="819660e4205df62db5c480c00ab4f1590161aa21c7b546bea6544b92aa2fc2b7")
cur = conn.cursor()
cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cur.fetchall():
    print(table)
cur.execute("SELECT url FROM website")
db_version = cur.fetchall()
print(db_version)

cur.close()