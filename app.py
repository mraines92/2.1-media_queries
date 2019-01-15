

import csv

from flask import Flask
from flask import request
# import requests

app = Flask(__name__)


@app.route("/")
def index():
    # Etsy: https://api.etsy.com/v2/listings/active.js?api_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicycle&includes=Images,Shop&sort_on=score

    response = requests.get('https://api.etsy.com/v2/listings/active.js?api_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicycle&includes=Images,Shop&sort_on=score')
    data = response.json()

    bike_photos = data['results']

    planet_html = []

    for planet in planets:
        planet_html.append('<li>{} :: {}</li>'.format(planet['name'], planet['climate']))

    planet_html = ''.join(planet_html)

    # Get html and render to screen
    index_file = open('index.html', 'r')
    index_html = index_file.read()
    index_html = index_html.replace('{{planet_list}}', planet_html)
    index_file.close()

    return index_html

