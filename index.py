from datetime import datetime
import random
from flask import render_template
from jisho_api.kanji import Kanji
from flask import Flask
# Create app
app = Flask(__name__)

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