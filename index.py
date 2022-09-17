from datetime import datetime
import random
from flask import render_template, request, session, redirect, url_for
from jisho_api.kanji import Kanji
from flask import Flask
import CONFIG
# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = CONFIG.SECRET_KEY
# Views
@app.route('/')
def home():
    # Put every line of kanji_list.txt into a list
    with open('kanji_list.txt', 'r',encoding="utf-8") as f:
        kanji_list = f.readlines()
    # Remove the newline character from each line
    kanji_list = [kanji.strip() for kanji in kanji_list]
    # Get a random kanji from the list
    random.seed(datetime.now().date())
    kanji = random.choice(kanji_list)

    year = datetime.now().year
    date = datetime.now().strftime("%b %d")

    return render_template("index.html", kanji=kanji, date=date, year=year)

@app.route('/kanjidata/<kanji>')
def kanji_data(kanji):
    kanji_data = Kanji.request(kanji)

    # Put all data into a dictionary
    data = {
        'kanji': kanji_data.data.kanji,
        'meanings': kanji_data.data.main_meanings,
        'onyomi': kanji_data.data.main_readings.on,
        'kunyomi': kanji_data.data.main_readings.kun,
    }
    return data

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_post', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username == CONFIG.loginInfo['username'] and password == CONFIG.loginInfo['password']:
        session['logged_in'] = True
        return {'response':200, 'message':'Login successful', 'redirect' : url_for('settings')}
    else:
        return {'response':400, 'message':'Incorrect username or password'}

@app.route('/settings')
def settings():
    if session.get('logged_in'):
        return render_template("settings.html")
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
