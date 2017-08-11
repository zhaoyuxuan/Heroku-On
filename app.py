from flask import Flask,render_template,request,redirect,url_for
import requests,os
import hashlib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text
import grequests
import validators
import psycopg2
import sys


app = Flask(__name__)

print("COW", os.environ['DATABASE_URL'])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
urls=["http://urls.yuxuanz.com/"];



class WEBSITE(db.Model):
    __tablename__ = 'WEBSITE'

    url = db.Column("url",db.Text, primary_key=True)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<Name %r>' % self.url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate',methods=["POST"])
def generate():
    link = request.form["input_url"]
    result=validators.url(link, public=False)

    if not result:

        return "not a website"
    else :
        link=link.encode('utf-8')
        hash_object = hashlib.md5(link)
        code=hash_object.hexdigest()
        print(4)
        return code[:5]

@app.route('/loaderio-c3b7a65412078c2e7124069686a0188f/')
def verification():
    return "loaderio-c3b7a65412078c2e7124069686a0188f"

@app.route("/test")
def test():
    output = ""
    all_users = WEBSITE.query.all()
    for i in range(len(all_users)):
        output += all_users[i].url + "\n"

    return output


@app.route('/checkurl', methods=["POST"])
def check():
    store_link=[]
    link = request.form["website_url"]
    try:
        webchecking = requests.get(link,verify=False)
    except:
        print("request failed")
        return "request failed"
    webcode=webchecking.text
    url=request.form["website"]
    if (webcode in link):
        print(1)
        try:
            data=WEBSITE(url)
            db.session.add(data)
            db.session.commit()
            print("it is saved")
        except:
            db.session.rollback()
            print("2")
            all_users = WEBSITE.query.all()
            for i in range(len(all_users)):
                print(all_users[i].url)

        db.session.close()
        return "it is in the website"
    else:
        data=WEBSITE(url)
        db.session.add(data)
        db.session.commit()
        # try:
        #     print("start")
        #     data=WEBSITE(url)
        #     db.session.add(data)
        #     db.session.commit()
        #     print("not already exist")
        #     # all_users = WEBSITE.query.all()
        #     # for i in range(len(all_users)):
        #     #     print(all_users[i].url + "\n")
        #     # print("end")
        # except:
        #     db.session.rollback()
        #     print("all already exist")
        #     all_users = WEBSITE.query.all()
        #     print(all_users[0].url)
        return "it is not in the website"





if __name__ == "__main__":
    app.run(debug=True)
