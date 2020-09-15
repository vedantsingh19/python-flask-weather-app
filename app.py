from flask import Flask, render_template, request
import requests
import json
from datetime import datetime
from utility_method import prime_number_utility
from constants import API_KEY
app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/weatherapp',methods=['POST'])
def extracting_weather_data_by_cityname():
    if request.method == 'POST':
        current_date_time = datetime.now()

        if prime_number_utility(current_date_time.day):

            city_name = request.form.get('City')
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + API_KEY + "&q=" + city_name

            response = requests.get(complete_url)
            data = json.loads(response.text)

            return data
        else:
            return 'Date is not prime so no date'


if __name__ == '__main__':
    app.run()