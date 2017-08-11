from flask import Flask,render_template,request,redirect,url_for
import requests,os
import hashlib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text







app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class WEBSITE(db.Model):
    __tablename__ = 'WEBSITE'

    url = db.Column(Text, primary_key=True)

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
    try:
        webchecking = requests.get(link,verify=False)

    except:
        print(3)
        return "not a website"
    if webchecking.status_code != 200:

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



@app.route('/checkurl', methods=["POST"])
def check():
    link = request.form["website_url"]
    try:
        webchecking = requests.get(link,verify=False)
    except:
        print("request failed")
    webcode=webchecking.text
    url=request.form["website"]
    if (webcode in link):
        print(1)
        data=WEBSITE(url)
        db.session.add(data)
        db.session.commit()

        print(all_users)
        return "it is in the website"
    else:
        data=WEBSITE(url)
        try:
            db.session.add(data)
            db.session.commit()
        except:
            print("all already exist")
            all_users = WEBSITE.query.all()
            print(all_users.url)



        return "it is not in the website"





if __name__ == "__main__":
    app.run(debug=True)
