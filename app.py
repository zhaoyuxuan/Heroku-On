from flask import Flask,render_template,request,redirect,url_for, jsonify
import requests,os
import hashlib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text
import grequests
import validators
import psycopg2
import sys,json


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ucopmphmoaavjo:0c8f53188864f3d286d4839a205975b0bf7dc5fd07202590e47ce4a01aa8978d@ec2-107-20-250-195.compute-1.amazonaws.com:5432/d18irpdh4tn89i"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class WEBSITE(db.Model):
    __tablename__ = 'WEBSITE'

    url = db.Column("url",db.Text, primary_key=True)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<Name %r>' % self.url
db.create_all()

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
        return code[:5]

@app.route('/04122')
def verification():
    return "04122"

@app.route("/test", methods=["POST"])
def test():
    websites = []
    all_users = WEBSITE.query.all()
    for i in range(len(all_users)):
        websites.append(all_users[i].url)
    rs = (grequests.get(u) for u in websites)
    grequests.map(rs)

    return "1"


@app.route('/checkurl', methods=["POST"])
def check():
    store_link=[]
    link = request.form["website_url"]

    try:
        webchecking = requests.get(link,verify=False)
    except:
        return "it is not in the website"
    webcode=webchecking.text
    url=request.form["website"]
    if (webcode in link):
        try:
            data=WEBSITE(url)
            db.session.add(data)
            db.session.commit()
            all_users = WEBSITE.query.all()
        except:
            db.session.rollback()
            all_users = WEBSITE.query.all()

        db.session.close()
        return "it is in the website"
    else:
        return "it is not in the website"


if __name__ == "__main__":
    app.run()
