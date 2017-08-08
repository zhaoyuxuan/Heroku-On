from flask import Flask,render_template,request,redirect,url_for
import requests
from random import choice
from string import ascii_lowercase



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate():
    code=''.join(choice(ascii_lowercase) for i in range(12))
    return code
@app.route('/loaderio-c3b7a65412078c2e7124069686a0188f/')
def verification():
    return "loaderio-c3b7a65412078c2e7124069686a0188f"



@app.route('/checkurl', methods=["POST"])
def check():
    link = request.form
    try:
        webchecking = requests.get(link["input_web"],verify=False)


    except:
        return "not a website"

    if webchecking.status_code == 200:
        return "yes"
    else:
        return "no"



if __name__ == "__main__":
    app.run(debug=True)
